// Service Worker — KI verstehen (NIVAO AI)
// v2 — Network-first fuer HTML, Cache-first fuer Assets,
//       Offline-Fallback nur fuer Navigationsanfragen.

const CACHE_NAME = 'ki-verstehen-v2';

// Basispfad automatisch aus SW-Registrierungs-Scope ableiten —
// funktioniert lokal (/sw.js) und auf GitHub Pages (/NIVAO-AI/sw.js).
const SCOPE_PATH = new URL(self.registration.scope).pathname.replace(/\/$/, '');

const SHELL = [
  SCOPE_PATH + '/ki-verstehen.html',
  SCOPE_PATH + '/manifest.json',
  SCOPE_PATH + '/icons/icon-192.png',
  SCOPE_PATH + '/icons/icon-512.png',
  SCOPE_PATH + '/icons/apple-touch-icon.png',
];

// ── Installation: Shell-Dateien vorab cachen ───────────────────────────────
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(SHELL))
      .then(() => self.skipWaiting())
  );
});

// ── Aktivierung: Alte Cache-Versionen bereinigen ───────────────────────────
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(
        keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))
      ))
      .then(() => self.clients.claim())
  );
});

// ── Fetch-Strategie ────────────────────────────────────────────────────────
self.addEventListener('fetch', event => {
  const req = event.request;
  const url = new URL(req.url);

  // Nur Same-Origin-Requests behandeln
  if (url.origin !== self.location.origin) return;

  // ── Navigationsanfragen (HTML): Network-first ──────────────────────────
  // Liefert immer die aktuellste Version; faellt bei Offline auf Cache zurueck.
  if (req.mode === 'navigate') {
    event.respondWith(
      fetch(req)
        .then(response => {
          if (response.ok) {
            const clone = response.clone();
            caches.open(CACHE_NAME).then(cache => cache.put(req, clone));
          }
          return response;
        })
        .catch(() =>
          caches.match(SCOPE_PATH + '/ki-verstehen.html')
        )
    );
    return;
  }

  // ── Statische Assets (Bilder, Icons, Manifest): Cache-first ───────────
  // Aendern sich selten; wird aus Netz nachgeladen falls nicht gecacht.
  // Kein HTML-Fallback bei Fehler — fehlende Icons degradieren still.
  if (req.destination === 'image' ||
      url.pathname.endsWith('.json') ||
      url.pathname.endsWith('.png') ||
      url.pathname.endsWith('.ico')) {
    event.respondWith(
      caches.match(req).then(cached => {
        if (cached) return cached;
        return fetch(req).then(response => {
          if (response.ok) {
            const clone = response.clone();
            caches.open(CACHE_NAME).then(cache => cache.put(req, clone));
          }
          return response;
        });
        // Kein .catch() — fehlende Bilder geben keinen HTML-Fallback
      })
    );
    return;
  }

  // ── Alles andere: Netz mit Cache-Fallback ─────────────────────────────
  event.respondWith(
    fetch(req)
      .then(response => {
        if (response.ok) {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(req, clone));
        }
        return response;
      })
      .catch(() => caches.match(req))
  );
});
