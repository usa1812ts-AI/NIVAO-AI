# Glossar + Inline-Tooltips — Implementierungsplan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fachbegriffe im Lerntext als klickbare Tooltips markieren und eine durchsuchbare Glossar-Seite mit allen ~77 Karteikartenbegriffen bereitstellen.

**Architecture:** Alle Änderungen in der einzigen Datei `ki-verstehen.html`. Neue CSS-Klassen im `<style>`-Block. Neue JS-Funktionen im `<script>`-Block. Datenbasis = vorhandenes `karteikarten[]`-Array (kein neuer Datenpflegeaufwand). Neue View `"glossar"` analog zu `"karten"` eingebunden.

**Tech Stack:** Vanilla JS, CSS, Single HTML File — kein Build-Tool, kein Framework, iPad Safari kompatibel.

---

## Datei-Übersicht

| Datei | Änderung |
|---|---|
| `ki-verstehen.html` Zeile 115 | CSS einfügen (vor `</style>`) |
| `ki-verstehen.html` Zeile 1876 | Neue Hilfsfunktionen einfügen (vor `renderStart`) |
| `ki-verstehen.html` Zeile 2237 | `renderGlossar()`, `glossarSuche()`, `glossarSprung()` einfügen (nach `renderKartenDecks`) |
| `ki-verstehen.html` Zeile 1895–1903 | `renderStart()` — Glossar-Button + Layout anpassen |
| `ki-verstehen.html` Zeile 1970–1971 | `renderEtappe()` — `injectTooltips()` aufrufen |
| `ki-verstehen.html` Zeile 2312–2331 | `navigate()` + `render()` — `"glossar"` einbinden |

---

## Task 1: CSS für Tooltips und Glossar-Seite

**Files:**
- Modify: `ki-verstehen.html:115` (vor der Zeile `</style>`)

- [ ] **Schritt 1: CSS einfügen**

Füge direkt vor `</style>` (Zeile 116) folgenden Block ein:

```css
/* ===== Glossar: Inline-Tooltips ===== */
.glossar-term{position:relative;border-bottom:2px dotted var(--orange);cursor:pointer;display:inline}
.glossar-tooltip{display:none;position:absolute;left:0;top:120%;z-index:200;background:#fff;border:1px solid #e5e7eb;border-radius:10px;padding:12px 14px;width:240px;box-shadow:0 4px 16px rgba(0,0,0,.13);font-size:13px;line-height:1.55;color:var(--graphite);font-weight:400;font-style:normal}
.glossar-term.aktiv .glossar-tooltip{display:block}
.gt-link{color:var(--orange);font-weight:700;cursor:pointer;text-decoration:none;display:block;margin-top:8px;font-size:12px}
/* ===== Glossar: Seite ===== */
.gl-suche-wrap{margin-bottom:12px}
.gl-suche{width:100%;border:1.5px solid #e5e7eb;border-radius:8px;padding:10px 12px;font:inherit;font-size:14px;color:var(--graphite);background:#fff}
.gl-suche:focus{outline:none;border-color:var(--orange)}
.gl-buchstaben{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:18px}
.gl-buchstabe{background:var(--light);border:none;border-radius:6px;padding:4px 10px;font:inherit;font-size:12px;font-weight:700;color:var(--olive);cursor:pointer}
.gl-buchstabe:hover{background:var(--orange);color:#fff}
.gl-gruppe{margin-bottom:10px}
.gl-buchstaben-head{font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--gray);padding:6px 0 4px;border-bottom:1px solid var(--light);margin-bottom:6px}
.gl-eintrag{padding:12px 14px;background:#fff;border:1px solid #e5e7eb;border-radius:10px;margin-bottom:8px}
.gl-eintrag-head{display:flex;justify-content:space-between;align-items:baseline;gap:8px;margin-bottom:4px}
.gl-term{font-weight:700;color:var(--olive);font-size:15px}
.gl-modul-badge{font-size:11px;background:#f0fdf4;color:#15803d;padding:2px 8px;border-radius:10px;font-weight:700;white-space:nowrap}
.gl-def{font-size:13px;color:var(--graphite);line-height:1.55}
.gl-karte-link{font-size:12px;margin-top:6px;padding:0;color:var(--orange);display:inline-block}
```

- [ ] **Schritt 2: Syntax prüfen**

```bash
node --check /tmp/ki_check_css.js 2>/dev/null || python3 -c "
import re
with open('ki-verstehen.html') as f: content = f.read()
scripts = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
open('/tmp/ki_extract.js','w').write(scripts[0])
print('JS extrahiert:', len(scripts[0]), 'Zeichen')
" && node --check /tmp/ki_extract.js && echo 'SYNTAX OK'
```

Expected: `SYNTAX OK`

- [ ] **Schritt 3: Im Browser prüfen**

Server starten (falls nicht läuft): `python3 -m http.server 8123` im Projektordner.
Öffne `http://localhost:8123/ki-verstehen.html` — Seite muss wie gewohnt laden (keine Änderung sichtbar, CSS ist noch ohne Verwendung).

- [ ] **Schritt 4: Commit**

```bash
git add ki-verstehen.html
git commit -m "style: add glossar tooltip and glossar-page CSS classes"
```

---

## Task 2: Hilfsfunktionen — escapeRegex, glossarTermMap, toggleTooltip, injectTooltips

**Files:**
- Modify: `ki-verstehen.html:1876` (direkt vor `function renderStart(){`)

- [ ] **Schritt 1: Hilfsfunktionen einfügen**

Füge direkt vor der Zeile `function renderStart(){` (aktuell Zeile 1877) folgenden Block ein:

```javascript
/* ===================== Glossar: Hilfsfunktionen ===================== */
let _glossarAnker = null; // transient: welcher Begriff soll im Glossar hervorgehoben werden

function escHtml(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }
function escRegex(s){ return s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'); }

function glossarTermMap(){
  // Gibt ein Objekt zurück: { "shell": { front:"Shell", back:"...", modul:6 }, ... }
  const map = {};
  karteikarten.forEach(k => { map[k.front.toLowerCase()] = { front:k.front, back:k.back, modul:k.modul }; });
  return map;
}

function toggleTooltip(el){
  const isActive = el.classList.contains('aktiv');
  document.querySelectorAll('.glossar-term.aktiv').forEach(t => t.classList.remove('aktiv'));
  if(!isActive) el.classList.add('aktiv');
}

// Globaler Click-Handler: schließt offene Tooltips
document.addEventListener('click', function(){ document.querySelectorAll('.glossar-term.aktiv').forEach(t => t.classList.remove('aktiv')); });

function injectTooltips(container){
  const map = glossarTermMap();
  // Längste Begriffe zuerst, damit "KI-Agent" vor "KI" gematcht wird
  const terms = Object.values(map).sort((a,b) => b.front.length - a.front.length);
  if(!terms.length) return;

  const SKIP_TAGS = new Set(['H1','H2','H3','H4','BUTTON','SCRIPT','STYLE','INPUT','TEXTAREA','A']);
  const SKIP_CLASSES = ['frage','navrow','abk-box','abk-chip','glossar-term','glossar-tooltip','topnav'];

  function shouldSkip(el){
    if(SKIP_TAGS.has(el.tagName)) return true;
    return SKIP_CLASSES.some(c => el.classList.contains(c));
  }

  // Alle passenden Textknoten sammeln
  const walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT, {
    acceptNode(node){
      let el = node.parentElement;
      while(el && el !== container){
        if(shouldSkip(el)) return NodeFilter.FILTER_REJECT;
        el = el.parentElement;
      }
      return node.textContent.trim() ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP;
    }
  });
  const nodes = [];
  let n;
  while((n = walker.nextNode())) nodes.push(n);

  const used = new Set(); // Jeder Begriff nur beim ersten Vorkommen

  nodes.forEach(textNode => {
    let text = textNode.textContent;
    let changed = false;
    terms.forEach(({ front, back }) => {
      if(used.has(front.toLowerCase())) return;
      const rx = new RegExp('\\b' + escRegex(front) + '\\b', 'i');
      if(!rx.test(text)) return;
      text = text.replace(rx, match => {
        used.add(front.toLowerCase());
        return `<span class="glossar-term" onclick="toggleTooltip(this);event.stopPropagation()"><span class="gt-word">${escHtml(match)}</span><span class="glossar-tooltip"><strong>${escHtml(front)}</strong> — ${escHtml(back)}<a class="gt-link" data-term="${escHtml(front)}" onclick="navigate('glossar',this.dataset.term);event.stopPropagation()">→ Im Glossar nachschlagen</a></span></span>`;
      });
      changed = true;
    });
    if(changed){
      const span = document.createElement('span');
      span.innerHTML = text;
      textNode.parentNode.replaceChild(span, textNode);
    }
  });
}
```

- [ ] **Schritt 2: Syntax prüfen**

```bash
python3 -c "
import re
with open('ki-verstehen.html') as f: content = f.read()
scripts = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
open('/tmp/ki_extract.js','w').write(scripts[0])
" && node --check /tmp/ki_extract.js && echo 'SYNTAX OK'
```

Expected: `SYNTAX OK`

- [ ] **Schritt 3: Commit**

```bash
git add ki-verstehen.html
git commit -m "feat: add glossar helper functions (termMap, injectTooltips, toggleTooltip)"
```

---

## Task 3: renderGlossar(), glossarSuche(), glossarSprung()

**Files:**
- Modify: `ki-verstehen.html` — direkt nach `renderKartenDecks()` (nach der schließenden `}` von `renderKartenDecks`, vor `function startRunde`)

- [ ] **Schritt 1: Drei Funktionen einfügen**

Füge direkt nach der schließenden `}` von `renderKartenDecks()` (aktuell nach Zeile 2237) folgendes ein:

```javascript
/* ===================== Render: Glossar ===================== */
function renderGlossar(){
  // Alphabetisch sortieren
  const sorted = [...karteikarten].sort((a,b) => a.front.localeCompare(b.front,'de'));
  // Nach Anfangsbuchstaben gruppieren
  const groups = {};
  sorted.forEach(k => {
    const letter = k.front[0].toUpperCase();
    if(!groups[letter]) groups[letter] = [];
    groups[letter].push(k);
  });
  const letters = Object.keys(groups).sort();

  const letterButtons = letters.map(l =>
    `<button class="gl-buchstabe" onclick="glossarSprung('${escHtml(l)}')">${escHtml(l)}</button>`
  ).join('');

  const eintraege = letters.map(l => `
    <div class="gl-gruppe" id="gl-gruppe-${l}">
      <div class="gl-buchstaben-head" id="gl-${l}">${l}</div>
      ${groups[l].map(k => `
        <div class="gl-eintrag" data-term="${escHtml(k.front)}">
          <div class="gl-eintrag-head">
            <span class="gl-term">${escHtml(k.front)}</span>
            <span class="gl-modul-badge">Modul ${k.modul+1}</span>
          </div>
          <div class="gl-def">${escHtml(k.back)}</div>
          <button class="btn-ghost gl-karte-link" onclick="navigate('karten')">→ als Karteikarte lernen</button>
        </div>
      `).join('')}
    </div>
  `).join('');

  document.getElementById('app').innerHTML = `
    <div class="topnav"><button class="btn-ghost" onclick="navigate('start')">&#8592; Übersicht</button></div>
    <h1>📖 Glossar</h1>
    <p class="lead">${karteikarten.length} Begriffe aus allen Modulen — Tippe los oder springe per Buchstabe.</p>
    <div class="gl-suche-wrap">
      <input id="gl-suche" class="gl-suche" type="search" placeholder="🔍 Begriff suchen …" oninput="glossarSuche(this.value)" autocomplete="off">
    </div>
    <div class="gl-buchstaben">${letterButtons}</div>
    <div id="gl-liste">${eintraege}</div>`;
  window.scrollTo(0,0);

  // Zum Anker scrollen (wenn aus Tooltip geöffnet)
  if(_glossarAnker){
    const term = _glossarAnker;
    _glossarAnker = null;
    setTimeout(() => {
      const el = document.querySelector(`.gl-eintrag[data-term="${escHtml(term)}"]`);
      if(el) el.scrollIntoView({behavior:'smooth', block:'center'});
    }, 80);
  }
}

function glossarSuche(val){
  const q = val.toLowerCase().trim();
  document.querySelectorAll('.gl-eintrag').forEach(el => {
    const term = (el.querySelector('.gl-term')||{}).textContent||'';
    const def  = (el.querySelector('.gl-def')||{}).textContent||'';
    el.style.display = (!q || term.toLowerCase().includes(q) || def.toLowerCase().includes(q)) ? '' : 'none';
  });
  // Leere Buchstabengruppen ausblenden
  document.querySelectorAll('.gl-gruppe').forEach(g => {
    const visible = [...g.querySelectorAll('.gl-eintrag')].some(e => e.style.display !== 'none');
    g.style.display = visible ? '' : 'none';
  });
}

function glossarSprung(letter){
  const el = document.getElementById('gl-' + letter);
  if(el) el.scrollIntoView({behavior:'smooth', block:'start'});
}
```

- [ ] **Schritt 2: Syntax prüfen**

```bash
python3 -c "
import re
with open('ki-verstehen.html') as f: content = f.read()
scripts = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
open('/tmp/ki_extract.js','w').write(scripts[0])
" && node --check /tmp/ki_extract.js && echo 'SYNTAX OK'
```

Expected: `SYNTAX OK`

- [ ] **Schritt 3: Commit**

```bash
git add ki-verstehen.html
git commit -m "feat: add renderGlossar(), glossarSuche(), glossarSprung()"
```

---

## Task 4: navigate() + render() erweitern + Startseite-Button

**Files:**
- Modify: `ki-verstehen.html` — `navigate()`, `render()`, `renderStart()`

- [ ] **Schritt 1: navigate() — `'glossar'`-Case hinzufügen**

In `navigate()` (Zeile ~2312) nach der Zeile `state.view = view;` den neuen Case einfügen.

Suche diesen Block:
```javascript
function navigate(view, payload){
  state.view = view;
  if(view === "modul"){ state.aktuellesModul = Number(payload); }
```

Ersetze ihn durch:
```javascript
function navigate(view, payload){
  state.view = view;
  if(view === "glossar"){ _glossarAnker = payload || null; }
  else if(view === "modul"){ state.aktuellesModul = Number(payload); }
```

- [ ] **Schritt 2: render() — `renderGlossar()` einbinden**

Suche:
```javascript
  else if(v === "karten") renderKartenDecks();
```

Ersetze durch:
```javascript
  else if(v === "karten") renderKartenDecks();
  else if(v === "glossar") renderGlossar();
```

- [ ] **Schritt 3: renderStart() — Glossar-Button + Layout**

Suche in `renderStart()`:
```javascript
    <div class="abschluss-box">
      <button class="btn btn-primary" onclick="navigate('karten')">🃏 Karteikarten</button>
      <button class="btn-ghost" onclick="resetFortschritt()">Fortschritt zurücksetzen</button>
    </div>`;
```

Ersetze durch:
```javascript
    <div class="abschluss-box">
      <button class="btn btn-primary" onclick="navigate('karten')">🃏 Karteikarten</button>
      <button class="btn btn-secondary" onclick="navigate('glossar')">📖 Glossar</button>
    </div>
    <div style="text-align:center;margin-bottom:18px">
      <button class="btn-ghost" onclick="resetFortschritt()">Fortschritt zurücksetzen</button>
    </div>`;
```

- [ ] **Schritt 4: Syntax prüfen**

```bash
python3 -c "
import re
with open('ki-verstehen.html') as f: content = f.read()
scripts = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
open('/tmp/ki_extract.js','w').write(scripts[0])
" && node --check /tmp/ki_extract.js && echo 'SYNTAX OK'
```

Expected: `SYNTAX OK`

- [ ] **Schritt 5: Im Browser manuell prüfen**

1. Startseite öffnen → Button `📖 Glossar` erscheint neben `🃏 Karteikarten`
2. `📖 Glossar` klicken → Glossar-Seite öffnet sich mit Suchfeld, Buchstabenleiste, Einträgen
3. Suchfeld: `"Shell"` eingeben → nur Shell-Eintrag sichtbar, Rest ausgeblendet
4. Buchstabenknopf `A` klicken → springt zu "Attention", "Agent" etc.
5. `← Übersicht` klicken → zurück zur Startseite

- [ ] **Schritt 6: Commit**

```bash
git add ki-verstehen.html
git commit -m "feat: wire up glossar view — navigate, render, startseite button"
```

---

## Task 5: renderEtappe() — injectTooltips() aufrufen

**Files:**
- Modify: `ki-verstehen.html:1971` (direkt nach `window.scrollTo(0,0)` in `renderEtappe`)

- [ ] **Schritt 1: injectTooltips-Aufruf einfügen**

Suche in `renderEtappe()` (nach `document.getElementById("app").innerHTML = ...`):
```javascript
  window.scrollTo(0,0);
}
function miniAnswer(btn){
```

Ersetze durch:
```javascript
  window.scrollTo(0,0);
  injectTooltips(document.getElementById('app'));
}
function miniAnswer(btn){
```

- [ ] **Schritt 2: Syntax prüfen**

```bash
python3 -c "
import re
with open('ki-verstehen.html') as f: content = f.read()
scripts = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
open('/tmp/ki_extract.js','w').write(scripts[0])
" && node --check /tmp/ki_extract.js && echo 'SYNTAX OK'
```

Expected: `SYNTAX OK`

- [ ] **Schritt 3: End-to-End im Browser prüfen**

1. Modul 7, Etappe 1 öffnen
2. Begriff `Shell` erscheint mit orangener gepunkteter Unterstreichung
3. Antippen → Tooltip öffnet sich: Name + Definition + `→ Im Glossar nachschlagen`
4. Irgendwo anders antippen → Tooltip schließt sich
5. `→ Im Glossar nachschlagen` klicken → Glossar öffnet sich, scrollt zu "Shell"-Eintrag
6. Jeder Begriff erscheint nur einmal pro Etappe unterstrichen (kein Spam)
7. Quiz-Fragen, Überschriften, Buttons haben keine Unterstreichung

- [ ] **Schritt 4: Commit**

```bash
git add ki-verstehen.html
git commit -m "feat: inject glossar tooltips into etappe text after render"
```
