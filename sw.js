// Service Worker — KI verstehen (NIVAO AI)
// Cacht alle App-Ressourcen für Offline-Nutzung

const CACHE_NAME = 'ki-verstehen-v1';
const BASE = '/NIVAO-AI';

const ASSETS = [
  BASE + '/ki-verstehen.html',
  BASE + '/manifest.json',
  BASE + '/icons/icon-192.png',
  BASE + '/icons/icon-512.png',
  BASE + '/icons/apple-touch-icon.png',
];

// Installation: Alle Assets in den Cache laden
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(ASSETS))
      .then(() => self.skipWaiting())
  );
});

// Aktivierung: Alte Caches löschen
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(
        keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))
      ))
      .then(() => self.clients.claim())
  );
});

// Fetch: Cache-first — bei Netz-Fehler aus Cache liefern
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(cached => {
        if (cached) return cached;
        return fetch(event.request)
          .then(response => {
            // Neue Ressourcen in Cache aufnehmen
            if (response.ok) {
              const clone = response.clone();
              caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
            }
            return response;
          })
          .catch(() => caches.match(BASE + '/ki-verstehen.html'));
      })
  );
});
