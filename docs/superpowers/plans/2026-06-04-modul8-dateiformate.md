# Modul 8 „Dateien, Formate & Werkzeuge" + Header-Fix — Implementierungsplan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Modul 8 mit 5 Etappen, 25 Karteikarten (k86–k110) und Glossareinträgen zur App hinzufügen; NIVAO-Logo vergrößern.

**Architecture:** Alle Änderungen in `ki-verstehen.html`. Neue Arrays (`etappenMod8`, `quizMod8`), neue `schaubildMod8()`-Funktion, Erweiterung von `vertiefungen`, `module`, `karteikarten` und `renderKartenDecks()`. Glossar entsteht automatisch aus Karteikarten (keine separate Änderung nötig).

**Tech Stack:** Vanilla JS, SVG, HTML/CSS — kein Build-Schritt. Syntaxprüfung via `node --check`.

---

## Dateien

- **Modify:** `ki-verstehen.html` (alle Änderungen in dieser einen Datei)

---

### Task 1: CSS — Header-Fix (Logo & Wordmark)

**Files:**
- Modify: `ki-verstehen.html:19-20`

- [ ] **Schritt 1: CSS-Zeilen anpassen**

Finde exakt diese Zeilen (ca. Zeile 19–20):
```css
.brand .mark{height:38px;width:38px;flex:0 0 auto}
.brand .wordmark{height:25px}
```
Ersetze durch:
```css
.brand .mark{height:52px;width:52px;flex:0 0 auto}
.brand .wordmark{height:36px}
```

- [ ] **Schritt 2: Syntaxprüfung**

```bash
python3 -c "
import re, subprocess
with open('ki-verstehen.html','r',encoding='utf-8') as f: c=f.read()
js = max(re.findall(r'<script[^>]*>(.*?)</script>',c,re.DOTALL),key=len)
open('/tmp/k.js','w',encoding='utf-8').write(js)
" && node --check /tmp/k.js && echo "OK"
```
Erwartung: `OK`

- [ ] **Schritt 3: Im Browser prüfen**

Server läuft auf `http://localhost:8123/ki-verstehen.html`. Header-Logo sichtbar größer.

- [ ] **Schritt 4: Commit**

```bash
git add ki-verstehen.html
git commit -m "style: vergroessere NIVAO Logo (52px) und Wordmark (36px) im Header"
```

---

### Task 2: schaubildMod8() — 5 SVG-Diagramme

**Files:**
- Modify: `ki-verstehen.html` — nach Zeile 1883 (`return "";` von schaubildMod7), vor `function schaubild(`

- [ ] **Schritt 1: Neue Funktion einfügen**

Direkt VOR der Zeile `function schaubild(m,e){` einfügen:

```javascript
function schaubildMod8(e){
  switch(e){
    case 0: return `
<svg viewBox="0 0 360 210" width="360" height="210" role="img" aria-label="Von ASCII zu CLAUDE.md">
  <text x="180" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#2D362E">Fundament: von ASCII bis CLAUDE.md</text>
  <rect x="30" y="170" width="300" height="28" rx="7" fill="#8A9189"/>
  <text x="180" y="189" text-anchor="middle" font-size="11" fill="#fff" font-weight="bold">ASCII — 128 Zeichen als Zahlen 0–127</text>
  <rect x="50" y="136" width="260" height="28" rx="7" fill="#3D4A3E"/>
  <text x="180" y="155" text-anchor="middle" font-size="11" fill="#fff" font-weight="bold">Unicode / UTF-8 — alle Sprachen &amp; Symbole</text>
  <rect x="70" y="102" width="220" height="28" rx="7" fill="#2D362E"/>
  <text x="180" y="121" text-anchor="middle" font-size="11" fill="#fff" font-weight="bold">.txt · .md · .csv — Textdateien</text>
  <rect x="90" y="68" width="180" height="28" rx="7" fill="#D97706"/>
  <text x="180" y="87" text-anchor="middle" font-size="11" fill="#fff" font-weight="bold">Markdown — strukturierter Text</text>
  <rect x="110" y="34" width="140" height="28" rx="7" fill="#D97706"/>
  <text x="180" y="53" text-anchor="middle" font-size="11" fill="#fff7ed" font-weight="bold">CLAUDE.md — Kontext für Claude</text>
</svg>`;
    case 1: return `
<svg viewBox="0 0 420 168" width="420" height="168" role="img" aria-label="Claude kommuniziert via JSON">
  <text x="210" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#2D362E">Claude spricht JSON — bei jedem API-Call</text>
  <rect x="10" y="40" width="90" height="36" rx="8" fill="#2D362E"/>
  <text x="55" y="63" text-anchor="middle" font-size="12" fill="#fff" font-weight="bold">Claude</text>
  <text x="107" y="62" text-anchor="middle" font-size="13" fill="#D97706" font-weight="bold">&#8594;</text>
  <rect x="120" y="40" width="110" height="36" rx="8" fill="#3D4A3E"/>
  <text x="175" y="57" text-anchor="middle" font-size="10" fill="#fff" font-weight="bold">JSON-Request</text>
  <text x="175" y="70" text-anchor="middle" font-size="9" fill="#d7dcd7">{"tool":"search"...}</text>
  <text x="237" y="62" text-anchor="middle" font-size="13" fill="#D97706" font-weight="bold">&#8594;</text>
  <rect x="250" y="40" width="100" height="36" rx="8" fill="#D97706"/>
  <text x="300" y="57" text-anchor="middle" font-size="11" fill="#fff" font-weight="bold">API-Endpunkt</text>
  <text x="300" y="70" text-anchor="middle" font-size="9" fill="#fff7ed">api.anthropic.com</text>
  <text x="357" y="62" text-anchor="middle" font-size="13" fill="#D97706" font-weight="bold">&#8594;</text>
  <rect x="370" y="40" width="40" height="36" rx="8" fill="#3D4A3E"/>
  <text x="390" y="63" text-anchor="middle" font-size="9" fill="#fff" font-weight="bold">Tool</text>
  <path d="M390 76 L390 104 L55 104 L55 76" fill="none" stroke="#9CA3AF" stroke-width="1.5" stroke-dasharray="4"/>
  <text x="225" y="122" text-anchor="middle" font-size="10" fill="#4B5563">JSON-Response: Ergebnis fließt zurück</text>
  <text x="210" y="148" text-anchor="middle" font-size="11" fill="#2D362E">MCP · Tool Use · Prompt · Antwort — alles JSON</text>
</svg>`;
    case 2: return `
<svg viewBox="0 0 400 190" width="400" height="190" role="img" aria-label="Code-Dateien im Vergleich">
  <text x="200" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#2D362E">Code-Dateien: wo laufen sie?</text>
  <rect x="10" y="32" width="116" height="130" rx="9" fill="#3D4A3E"/>
  <text x="68" y="52" text-anchor="middle" font-size="12" fill="#D97706" font-weight="bold">.py</text>
  <text x="68" y="70" text-anchor="middle" font-size="10" fill="#fff">Python</text>
  <text x="68" y="88" text-anchor="middle" font-size="9" fill="#d7dcd7">python3 sk.py</text>
  <text x="68" y="108" text-anchor="middle" font-size="9" fill="#9CA3AF">Daten · Backend</text>
  <text x="68" y="124" text-anchor="middle" font-size="9" fill="#9CA3AF">KI-Scripts</text>
  <text x="68" y="148" text-anchor="middle" font-size="9" fill="#D97706">Claude schreibt oft .py</text>
  <rect x="142" y="32" width="116" height="130" rx="9" fill="#2D362E"/>
  <text x="200" y="52" text-anchor="middle" font-size="12" fill="#D97706" font-weight="bold">.js</text>
  <text x="200" y="70" text-anchor="middle" font-size="10" fill="#fff">JavaScript</text>
  <text x="200" y="88" text-anchor="middle" font-size="9" fill="#d7dcd7">node sk.js</text>
  <text x="200" y="108" text-anchor="middle" font-size="9" fill="#9CA3AF">Web · Browser</text>
  <text x="200" y="124" text-anchor="middle" font-size="9" fill="#9CA3AF">Node.js Backend</text>
  <text x="200" y="148" text-anchor="middle" font-size="9" fill="#D97706">Diese App ist .js</text>
  <rect x="274" y="32" width="116" height="130" rx="9" fill="#8A9189"/>
  <text x="332" y="52" text-anchor="middle" font-size="12" fill="#2D362E" font-weight="bold">.sh</text>
  <text x="332" y="70" text-anchor="middle" font-size="10" fill="#fff">Shell</text>
  <text x="332" y="88" text-anchor="middle" font-size="9" fill="#2D362E">bash sk.sh</text>
  <text x="332" y="108" text-anchor="middle" font-size="9" fill="#2D362E">Automatisierung</text>
  <text x="332" y="124" text-anchor="middle" font-size="9" fill="#2D362E">System-Befehle</text>
  <text x="332" y="148" text-anchor="middle" font-size="9" fill="#2D362E">Claude Code nutzt sh</text>
</svg>`;
    case 3: return `
<svg viewBox="0 0 380 198" width="380" height="198" role="img" aria-label="HTML CSS JS Schichten">
  <text x="190" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#2D362E">Web: HTML + CSS + JS = lebendige Seite</text>
  <rect x="20" y="32" width="340" height="42" rx="9" fill="#2D362E"/>
  <text x="190" y="52" text-anchor="middle" font-size="13" fill="#fff" font-weight="bold">HTML — Struktur (Knochen)</text>
  <text x="190" y="67" text-anchor="middle" font-size="10" fill="#d7dcd7">&lt;h1&gt; &lt;div&gt; &lt;button&gt; &lt;ul&gt; — das Grundgeruest</text>
  <rect x="20" y="82" width="340" height="42" rx="9" fill="#3D4A3E"/>
  <text x="190" y="102" text-anchor="middle" font-size="13" fill="#fff" font-weight="bold">CSS — Aussehen (Haut)</text>
  <text x="190" y="117" text-anchor="middle" font-size="10" fill="#d7dcd7">Farben · Abstände · Schriften · &lt;style&gt;-Block</text>
  <rect x="20" y="132" width="340" height="42" rx="9" fill="#D97706"/>
  <text x="190" y="152" text-anchor="middle" font-size="13" fill="#fff" font-weight="bold">JavaScript — Verhalten (Muskeln)</text>
  <text x="190" y="167" text-anchor="middle" font-size="10" fill="#fff7ed">Klicks · DOM · Navigation · Karteikarten-Logik</text>
  <text x="190" y="190" text-anchor="middle" font-size="11" fill="#4B5563">Diese App: alles in einer einzigen .html-Datei</text>
</svg>`;
    case 4: return `
<svg viewBox="0 0 380 210" width="380" height="210" role="img" aria-label="Dateiformate Uebersicht">
  <text x="190" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#2D362E">Formate: was Claude direkt liest</text>
  <rect x="10" y="30" width="168" height="80" rx="9" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="94" y="52" text-anchor="middle" font-size="11" fill="#15803d" font-weight="bold">Direkt lesbar &#10003;</text>
  <text x="94" y="68" text-anchor="middle" font-size="10" fill="#14532d">.txt .md .csv .py</text>
  <text x="94" y="82" text-anchor="middle" font-size="10" fill="#14532d">.js .sh .json .yaml</text>
  <text x="94" y="96" text-anchor="middle" font-size="10" fill="#14532d">.html .css .svg .env</text>
  <rect x="202" y="30" width="168" height="80" rx="9" fill="#fef2f2" stroke="#b91c1c" stroke-width="2"/>
  <text x="286" y="52" text-anchor="middle" font-size="11" fill="#b91c1c" font-weight="bold">Extraktion noetig &#10007;</text>
  <text x="286" y="68" text-anchor="middle" font-size="10" fill="#7f1d1d">.pdf .docx .xlsx</text>
  <text x="286" y="82" text-anchor="middle" font-size="10" fill="#7f1d1d">.png .jpg (→ multimodal)</text>
  <text x="286" y="96" text-anchor="middle" font-size="10" fill="#7f1d1d">.mp3 .zip .exe</text>
  <rect x="80" y="126" width="220" height="32" rx="8" fill="#2D362E"/>
  <text x="190" y="147" text-anchor="middle" font-size="11" fill="#fff" font-weight="bold">SVG: Bild als Text — Claude schreibt es</text>
  <text x="190" y="185" text-anchor="middle" font-size="10" fill="#4B5563">.env immer geheim — nie committen</text>
  <rect x="100" y="164" width="180" height="22" rx="6" fill="#fff7ed" stroke="#D97706" stroke-width="1.5"/>
  <text x="190" y="179" text-anchor="middle" font-size="10" fill="#D97706" font-weight="bold">PNG/JPG: multimodale Modelle sehen Bilder</text>
</svg>`;
  }
  return "";
}
```

- [ ] **Schritt 2: Syntaxprüfung**

```bash
python3 -c "
import re
with open('ki-verstehen.html','r',encoding='utf-8') as f: c=f.read()
js = max(re.findall(r'<script[^>]*>(.*?)</script>',c,re.DOTALL),key=len)
open('/tmp/k.js','w',encoding='utf-8').write(js)
" && node --check /tmp/k.js && echo "OK"
```
Erwartung: `OK`

---

### Task 3: schaubild()-Dispatcher um Modul 8 erweitern

**Files:**
- Modify: `ki-verstehen.html` — Zeile mit `function schaubild(m,e){`

- [ ] **Schritt 1: Zeile einfügen**

Finde:
```javascript
  if(m===6) return schaubildMod7(e);
  return "";
}
```
Ersetze durch:
```javascript
  if(m===6) return schaubildMod7(e);
  if(m===7) return schaubildMod8(e);
  return "";
}
```

- [ ] **Schritt 2: Syntaxprüfung**

```bash
python3 -c "
import re
with open('ki-verstehen.html','r',encoding='utf-8') as f: c=f.read()
js = max(re.findall(r'<script[^>]*>(.*?)</script>',c,re.DOTALL),key=len)
open('/tmp/k.js','w',encoding='utf-8').write(js)
" && node --check /tmp/k.js && echo "OK"
```

---

### Task 4: etappenMod8 und quizMod8 Arrays einfügen

**Files:**
- Modify: `ki-verstehen.html` — nach `const quizMod7 = [...]` (ca. Zeile 1049), vor `/* ===== Modul-Register =====`

- [ ] **Schritt 1: Arrays einfügen**

Direkt nach der schließenden `];` von `quizMod7` einfügen:

```javascript
const etappenMod8 = [
  {
    titel:"Wie KI Text liest",
    kurz:"ASCII, Unicode, Textdateien, CLAUDE.md",
    kernsatz:"LLMs verarbeiten ausschliesslich Text — alles andere muss vorher konvertiert werden. ASCII ist das Fundament, UTF-8 der heutige Standard, Markdown die Muttersprache von Claude.",
    punkte:[
      "ASCII (American Standard Code for Information Interchange): kodiert 128 Zeichen als Zahlen 0–127. Das Zeichen 'A' hat den Wert 65, '{' den Wert 123. Jeder Buchstabe in Code, JSON oder Shell-Befehlen ist eine ASCII-Zahl.",
      "Unicode / UTF-8: Erweiterung von ASCII auf alle Sprachen der Welt (ue, e-Akzent, CJK-Zeichen, Emojis). UTF-8 ist der Standard in Editoren, Terminals und KI-Tools. Fehler entstehen, wenn Kodierungen gemischt werden — z. B. U+201D statt U+0022 als Anführungszeichen bricht JS-Syntax.",
      ".txt-Datei: Reiner Text ohne Formatierung — fuer LLMs das idealste Format. Claude liest .txt-Dateien direkt, ohne Konvertierungsschritt. Grosse Textmengen fuer Analysen immer als .txt uebergeben.",
      "Markdown / .md: Textdatei mit einfacher Formatierung. # fuer Ueberschriften, **fett**, - fuer Listen — als Plaintext lesbar, aber auch formatierbar. CLAUDE.md ist eine Markdown-Datei.",
      "CLAUDE.md: Spezielle Markdown-Datei im Projektordner. Wird von Claude Code vor jedem Task automatisch geladen — enthaelt Kontext, Regeln und Praeferenzen fuer das Projekt. Die wichtigste Konfigurationsdatei in Claude Code.",
      ".csv (Comma-Separated Values): Tabellarische Daten als Textdatei, Spalten durch Komma getrennt. LLMs und Python-Scripts lesen CSV direkt — kein Excel noetig. Exportiere Tabellen immer als CSV fuer KI-Verarbeitung."
    ],
    merkbild:"Alles, was Claude denkt, ist Text. Bilder, PDFs, Tabellen — erst wenn sie zu Text werden, kann Claude damit arbeiten.",
    check:[
      { ftxt:"Welches Format ist fuer LLMs am direktesten lesbar?",
        opt:[{t:"PDF",c:false},{t:"DOCX",c:false},{t:".txt (reiner Text)",c:true}],
        erkl:".txt ist reiner Text ohne Formatierungs-Overhead — LLMs verarbeiten ihn ohne Konvertierung." },
      { ftxt:"Was ist CLAUDE.md?",
        opt:[{t:"Eine automatische Backup-Datei",c:false},{t:"Markdown-Datei mit Kontext und Regeln — wird vor jedem Task geladen",c:true},{t:"Eine Binaerdatei",c:false}],
        erkl:"CLAUDE.md gibt Claude Code die Spielregeln des Projekts — sie wird bei jeder Session automatisch eingelesen." }
    ]
  },
  {
    titel:"Strukturierte Daten & Kommunikation",
    kurz:"JSON, YAML, URL, API-Endpunkt",
    kernsatz:"Claude spricht JSON — bei Tool Use, MCP-Calls und API-Kommunikation ist JSON das universelle Austauschformat zwischen KI und Werkzeugen.",
    punkte:[
      "JSON (JavaScript Object Notation): Leichtgewichtiges Textformat fuer strukturierte Daten. Syntax: {\"schluessel\": \"wert\"}, Arrays: [1, 2, 3], Boolean: true/false. Jede Claude-Antwort mit Tool Use kommt als JSON.",
      "JSON-Struktur: Objekte beginnen mit { und enden mit }. Strings stehen in geraden doppelten Anführungszeichen (U+0022). Ein fehlendes Komma oder ein falsch kodiertes Zeichen als Delimiter bricht das gesamte JSON — Syntax ist absolut strikt.",
      "YAML (Yet Another Markup Language): Konfigurationssprache mit Einrueckung statt geschweifter Klammern. Wird fuer MCP-Server-Konfigurationen, GitHub Actions und Docker genutzt. Lesbarer als JSON, aber strikte Einrueckungs-Regeln.",
      "URL (Uniform Resource Locator): Adresse einer Ressource im Web. Aufbau: https://domain.com/pfad?parameter=wert. Claude kann URLs nur mit Tools oder MCP-Verbindungen aufrufen — nicht direkt ohne Werkzeug.",
      "API-Endpunkt: Spezifische URL, ueber die Programme Daten austauschen. Jeder Claude-Response ist ein API-Call an api.anthropic.com — Claude sendet JSON, empfaengt JSON. MCP-Server sind selbst API-Endpunkte."
    ],
    merkbild:"JSON ist die Sprache, in der KI und Werkzeuge miteinander reden. Wer JSON versteht, versteht wie Claude unter der Haube kommuniziert.",
    check:[
      { ftxt:"In welchem Format kommuniziert Claude mit Tools bei Tool Use?",
        opt:[{t:"XML",c:false},{t:"JSON",c:true},{t:"YAML",c:false}],
        erkl:"Tool Use, MCP und API-Calls laufen immer ueber JSON — das universelle Maschinen-Austauschformat." },
      { ftxt:"Was unterscheidet YAML von JSON?",
        opt:[{t:"YAML ist binaer, JSON ist Text",c:false},{t:"YAML nutzt Einrueckung statt {} und ist fuer Konfiguration gedacht",c:true},{t:"YAML ist schneller",c:false}],
        erkl:"YAML setzt auf Einrueckung und Lesbarkeit — ideal fuer Konfigurationen wie MCP-Server oder CI/CD-Pipelines." }
    ]
  },
  {
    titel:"Code-Dateien",
    kurz:"Python, JavaScript, Shell-Scripts",
    kernsatz:"Claude liest, schreibt und erklaert Code-Dateien in jeder Sprache — aber jede Sprache hat ihren Einsatzbereich und ihre Ausfuehrungsumgebung.",
    punkte:[
      "Python (.py): Die beliebteste Sprache fuer Datenanalyse, Automatisierung und KI-Backends. Wird mit python3 skript.py ausgefuehrt. Claude Code schreibt taeglich Python-Scripts — fuer Dateianalysen, API-Aufrufe, Datenverarbeitung.",
      "JavaScript (.js / .mjs): Laeuft im Browser (Frontend) oder auf dem Server via Node.js (Backend). node skript.js fuehrt es aus. Diese Lern-App besteht zu einem grossen Teil aus JavaScript — Logik, Navigation, Karteikarten-System.",
      "Shell-Script (.sh): Enthaelt Bash-Shell-Befehle, die nacheinander ausgefuehrt werden. #!/bin/bash am Anfang markiert die Datei als Shell-Script. Claude Code nutzt Shell-Befehle intensiv: git, node, python3, ls, grep.",
      "Was macht eine Datei zu Code? Syntaxregeln, die eine Laufzeitumgebung interpretiert. Ein Tippfehler (fehlende Klammer, falsches Zeichen) bricht die Ausfuehrung. Textdateien haben keine Laufzeitumgebung — Code hat eine.",
      "Sicherheits-Check vor der Ausfuehrung: node --check datei.js prueft JS-Syntax ohne Ausfuehrung. python3 -m py_compile datei.py prueft Python-Syntax. Claude Code nutzt diese Checks regelmaessig — ein wichtiger Sicherheitsschritt."
    ],
    merkbild:"Python = Daten & Logik. JavaScript = Web & Browser. Shell = Automatisierung & System. Claude beherrscht alle drei.",
    check:[
      { ftxt:"Mit welchem Befehl wird ein Python-Script ausgefuehrt?",
        opt:[{t:"run skript.py",c:false},{t:"python3 skript.py",c:true},{t:"execute skript.py",c:false}],
        erkl:"python3 skript.py startet den Python-Interpreter und fuehrt die Datei aus." },
      { ftxt:"Was ist #!/bin/bash am Anfang einer .sh-Datei?",
        opt:[{t:"Ein Kommentar ohne Bedeutung",c:false},{t:"Shebang: gibt an, welcher Interpreter die Datei ausfuehrt",c:true},{t:"Eine Import-Anweisung",c:false}],
        erkl:"Der Shebang (#!/...) sagt dem Betriebssystem, welches Programm das Script ausfuehren soll." }
    ]
  },
  {
    titel:"Web-Formate",
    kurz:"HTML, CSS, DOM, Mockup",
    kernsatz:"Jede Webseite besteht aus drei Schichten: HTML gibt Struktur, CSS gibt Aussehen, JavaScript gibt Verhalten. Diese Lern-App selbst ist ein perfektes Beispiel — eine einzige .html-Datei.",
    punkte:[
      "HTML (HyperText Markup Language): Beschreibt die Struktur einer Seite mit Tags. <h1> fuer Ueberschriften, <div> fuer Bereiche, <button> fuer Schaltflaechen. Diese App ist eine einzige .html-Datei — das gesamte Wissen steckt darin.",
      "CSS (Cascading Style Sheets): Beschreibt das Aussehen — Farben, Schriften, Abstaende, Animationen. In dieser App steht alles CSS im <style>-Block am Anfang. Claude generiert CSS fuer Web-UIs — z. B. beim Frontend-Design.",
      "DOM (Document Object Model): Die Baumstruktur des HTML im Browser-Speicher. JavaScript manipuliert den DOM: Elemente hinzufuegen, Text aendern, Klassen setzen. document.getElementById('app') ist ein DOM-Zugriff — auch in dieser App allgegenwaetig.",
      "JavaScript im Browser: Dieselbe Sprache wie Node.js, aber direkt im Browser ausgefuehrt. Reagiert auf Klicks (onclick), veraendert den DOM, liest localStorage. In dieser App steuert JS alles: Navigation, Karteikarten, Quiz.",
      "Mockup / Wireframe: Visuelle Skizze einer UI, bevor Code geschrieben wird. Klaert Struktur und Layout ohne Logik. Claude kann Mockups als einfaches HTML/CSS generieren — der schnellste Weg, eine UI-Idee sichtbar zu machen.",
      "URL im Browser: Jede Seite hat eine URL. Innerhalb einer Single-Page-App (wie dieser) simuliert JavaScript die Navigation — die URL zeigt dabei dasselbe Dokument, die Ansicht wechselt nur im DOM."
    ],
    merkbild:"HTML = Knochen, CSS = Haut, JavaScript = Muskeln. Zusammen ergeben sie eine lebendige Webseite.",
    check:[
      { ftxt:"Was ist der DOM?",
        opt:[{t:"Eine Datenbankstruktur",c:false},{t:"Die Baumstruktur des HTML im Browser-Speicher",c:true},{t:"Ein CSS-Framework",c:false}],
        erkl:"Der DOM ist die lebendige Repraesentation des HTML — JavaScript kann ihn lesen und veraendern." },
      { ftxt:"Was ist ein Mockup?",
        opt:[{t:"Ein fertiges Produkt",c:false},{t:"Ein JavaScript-Framework",c:false},{t:"Visuelle UI-Skizze vor dem Code — klaert Layout ohne Logik",c:true}],
        erkl:"Ein Mockup zeigt, wie etwas aussehen soll — bevor eine einzige Zeile Logik-Code existiert." }
    ]
  },
  {
    titel:"Binaer, Bilder & Grenzen von KI",
    kurz:"PDF, DOCX, PNG, SVG, .env",
    kernsatz:"Nicht alles ist fuer LLMs direkt lesbar. Binaerformate brauchen Extraktion, Bilder brauchen multimodale Modelle — und manche Dateien sollten Claude bewusst vorenthalten werden.",
    punkte:[
      "Binaerformat: Datei, die keine lesbare Textstruktur hat — stattdessen Rohdaten in Bytes. PDF, DOCX, XLSX, MP3, PNG, JPG sind Binaerformate. Ein Texteditor oeffnet sie als unlesbaren Zeichensalat.",
      "PDF: Weit verbreitetes Dokumentformat — aber binaer. Claude kann PDFs nicht direkt lesen; ein Tool (z. B. via MCP) muss zuerst den Text extrahieren. Danach ist der Inhalt fuer Claude normal verfuegbar.",
      "DOCX / XLSX: Microsoft-Formate fuer Word und Excel — intern ZIP-Archive mit XML. Muessen zu .txt oder .csv konvertiert werden, bevor Claude sie verarbeitet. Der DOCX-Skill erledigt das automatisch.",
      "PNG / JPG: Bilddateien. Multimodale Modelle (Claude 3 Sonnet, Opus, Haiku und neuere) koennen Bilder direkt sehen — der Screenshot wird als Bild an die API gesendet. Aeltere oder reine Text-Modelle koennen das nicht.",
      "SVG (Scalable Vector Graphic): Der Sonderfall unter den Bildformaten — SVG ist XML/Text und damit fuer Claude direkt lesbar und schreibbar. Die Schaubilder in dieser App sind SVGs, die Claude generiert hat.",
      ".env-Datei: Textdatei mit Umgebungsvariablen wie API-Keys und Passwoertern. Wird nie in Git committet (.gitignore). Claude Code erkennt .env-Dateien und warnt vor versehentlichem Upload sensibler Daten.",
      "package.json: Konfigurationsdatei fuer Node.js-Projekte im JSON-Format. Listet alle Abhaengigkeiten (npm-Pakete), Skripte und Metadaten. Claude liest sie, um das Projekt zu verstehen — aehnlich wie CLAUDE.md."
    ],
    merkbild:"Was Text ist, liest Claude direkt. Was binaer ist, braucht einen Mittler. Was geheim ist, bleibt geheim.",
    check:[
      { ftxt:"Warum kann Claude eine PDF-Datei nicht direkt lesen?",
        opt:[{t:"PDFs sind zu gross",c:false},{t:"PDF ist ein Binaerformat — Text muss erst extrahiert werden",c:true},{t:"Claude kennt PDF nicht",c:false}],
        erkl:"PDFs sind binaer kodiert. Erst nach Textextraktion durch ein Tool steht der Inhalt fuer Claude zur Verfuegung." },
      { ftxt:"Was ist besonders an SVG unter den Bildformaten?",
        opt:[{t:"SVG ist komprimiert",c:false},{t:"SVG ist XML/Text — Claude kann es direkt lesen und schreiben",c:true},{t:"SVG ist ein Microsoft-Format",c:false}],
        erkl:"SVG beschreibt Grafiken als Text-Markup — Claude kann SVGs generieren, analysieren und veraendern." }
    ]
  }
];

const quizMod8 = [
  { etappe:0, f:"Was ist ASCII?", opt:["Ein Bildformat","128 Zeichen als Zahlen 0–127 kodiert","Ein Protokoll fuer Netzwerke","Ein Python-Paket"], korrekt:1 },
  { etappe:0, f:"Welche Datei laedt Claude Code automatisch vor jedem Task?", opt:["package.json",".env","CLAUDE.md","README.md"], korrekt:2 },
  { etappe:1, f:"In welchem Format kommuniziert Claude mit Tools und APIs?", opt:["XML","CSV","YAML","JSON"], korrekt:3 },
  { etappe:1, f:"Was unterscheidet YAML von JSON?", opt:["YAML ist binaer","YAML nutzt Einrueckung statt {} und ist fuer Konfiguration gedacht","YAML ist schneller","Kein Unterschied"], korrekt:1 },
  { etappe:2, f:"Welcher Befehl fuehrt ein Python-Script aus?", opt:["run skript.py","execute skript.py","python3 skript.py","bash skript.py"], korrekt:2 },
  { etappe:2, f:"Was ist der Shebang (#!/bin/bash) am Anfang einer .sh-Datei?", opt:["Ein Kommentar","Gibt den Interpreter an, der das Script ausfuehrt","Eine Import-Anweisung","Einen Fehler"], korrekt:1 },
  { etappe:3, f:"Was ist der DOM?", opt:["Eine Datenbank","Ein CSS-Framework","Die Baumstruktur des HTML im Browser-Speicher","Ein Build-Tool"], korrekt:2 },
  { etappe:3, f:"Was ist ein Mockup?", opt:["Ein fertiges Produkt","Eine Testdatei","Ein JavaScript-Framework","Visuelle UI-Skizze vor dem Code"], korrekt:3 },
  { etappe:4, f:"Warum kann Claude eine PDF-Datei nicht direkt lesen?", opt:["PDFs sind zu gross","PDF ist ein Binaerformat — Text muss extrahiert werden","Claude kennt PDF nicht","PDFs haben kein UTF-8"], korrekt:1 },
  { etappe:4, f:"Was ist besonders an SVG?", opt:["Es ist komprimiert","Es ist ein Microsoft-Format","SVG ist XML/Text — direkt lesbar und schreibbar fuer Claude","SVG kann nicht animiert werden"], korrekt:2 }
];
```

- [ ] **Schritt 2: Syntaxprüfung**

```bash
python3 -c "
import re
with open('ki-verstehen.html','r',encoding='utf-8') as f: c=f.read()
js = max(re.findall(r'<script[^>]*>(.*?)</script>',c,re.DOTALL),key=len)
open('/tmp/k.js','w',encoding='utf-8').write(js)
" && node --check /tmp/k.js && echo "OK"
```
Erwartung: `OK`

- [ ] **Schritt 3: Commit**

```bash
git add ki-verstehen.html
git commit -m "feat: etappenMod8 und quizMod8 Arrays (5 Etappen, 10 Quizfragen)"
```

---

### Task 5: vertiefungen für Modul 8 ergänzen

**Files:**
- Modify: `ki-verstehen.html` — in `const vertiefungen = {` — nach dem letzten `"6-5"` Eintrag

- [ ] **Schritt 1: Einträge anfügen**

Finde den letzten Eintrag der vertiefungen (ca. `"6-5": { ... }`). Füge dahinter ein, kurz vor der schließenden `};`:

```javascript
  "7-0": {
    vorteile:["Plain Text ist fuer Claude am effizientesten — keine Konvertierung, keine Formatierungs-Artefakte.","Markdown kombiniert Lesbarkeit fuer Menschen und strukturierten Kontext fuer KI."],
    grenzen:["Zeichenkodierungsfehler (z. B. U+201D als JS-Delimiter) koennen Syntax komplett brechen."],
    achten:["CLAUDE.md regelmaessig aktualisieren — veraltete Regeln verwirren Claude mehr als keine Regeln.","UTF-8 als Standard durchhalten; keinen Editor nutzen, der Anführungszeichen automatisch kräuselt."]
  },
  "7-1": {
    vorteile:["JSON ist menschenlesbar und maschinenverarbeitbar — ein Format fuer beide Seiten.","YAML macht Konfigurationen uebersichtlich und wartbar."],
    grenzen:["Ein einzelner JSON-Syntaxfehler (fehlendes Komma, falsches Anführungszeichen) bricht den gesamten Datenstrom.","YAML-Einrueckungsfehler sind schwer zu debuggen."],
    achten:["JSON immer mit node --check oder einem Online-Validator pruefen. Keine typografischen Anführungszeichen in JSON verwenden."]
  },
  "7-2": {
    vorteile:["Claude kann Code in jeder Sprache lesen, schreiben und erklaeren — auch ohne dass der Nutzer die Sprache kennt.","node --check und python3 -m py_compile pruefen Syntax ohne Ausfuehrung — sicherer Schritt vor dem Run."],
    grenzen:["Claude schreibt syntaktisch korrekten Code, aber Logikfehler koennen auftreten.","Shell-Befehle koennen irreversible Systemaenderungen vornehmen — immer pruefen."],
    achten:["Code immer verstehen, bevor man ihn ausfuehrt. Claude erklaert jeden Schritt auf Nachfrage."]
  },
  "7-3": {
    vorteile:["Single-Page-Apps wie diese Lern-App brauchen keinen Server — eine .html-Datei reicht.","Claude generiert HTML/CSS/JS direkt — vom Mockup zum funktionierenden Prototyp in Minuten."],
    grenzen:["Browser-Sicherheitsmodell begrenzt, was JS darf (kein direkter Dateisystem-Zugriff).","Ohne Bundler/Framework waechst eine einzige HTML-Datei schnell unuebersichtlich."],
    achten:["DOM-Manipulationen immer auf unbeabsichtigte Seiteneffekte pruefen. CSS-Klassen-Konflikte vermeiden."]
  },
  "7-4": {
    vorteile:["Multimodale Faehigkeiten (Bilder verstehen) machen Claude zum universellen Analysetool.","SVG erlaubt Claude, Diagramme und Grafiken vollstaendig zu generieren — kein Bildbearbeitungsprogramm noetig."],
    grenzen:["Binaerformate ohne Tool-Unterstuetzung bleiben fuer Claude unsichtbar.","Multimodale Analyse ist teurer (mehr Tokens) als reine Textverarbeitung."],
    achten:[".env nie committen — auch nicht versehentlich. git status pruefen, bevor sensible Dateien gestaged werden."]
  },
```

- [ ] **Schritt 2: Syntaxprüfung**

```bash
python3 -c "
import re
with open('ki-verstehen.html','r',encoding='utf-8') as f: c=f.read()
js = max(re.findall(r'<script[^>]*>(.*?)</script>',c,re.DOTALL),key=len)
open('/tmp/k.js','w',encoding='utf-8').write(js)
" && node --check /tmp/k.js && echo "OK"
```

---

### Task 6: module-Array um Modul 8 erweitern

**Files:**
- Modify: `ki-verstehen.html` — `const module = [...]`

- [ ] **Schritt 1: Eintrag anhängen**

Finde:
```javascript
  { id:6, titel:"KI-Tools im Alltag", kurz:"Claude Code, Skills, Hooks, Subagents, MCP, Sicherheit", etappen:etappenMod7, quiz:quizMod7, synthese:false }
];
```
Ersetze durch:
```javascript
  { id:6, titel:"KI-Tools im Alltag", kurz:"Claude Code, Skills, Hooks, Subagents, MCP, Sicherheit", etappen:etappenMod7, quiz:quizMod7, synthese:false },
  { id:7, titel:"Dateien, Formate & Werkzeuge", kurz:"ASCII, JSON, HTML, Python, Mockup & Co.", etappen:etappenMod8, quiz:quizMod8, synthese:false }
];
```

- [ ] **Schritt 2: Syntaxprüfung**

```bash
python3 -c "
import re
with open('ki-verstehen.html','r',encoding='utf-8') as f: c=f.read()
js = max(re.findall(r'<script[^>]*>(.*?)</script>',c,re.DOTALL),key=len)
open('/tmp/k.js','w',encoding='utf-8').write(js)
" && node --check /tmp/k.js && echo "OK"
```

- [ ] **Schritt 3: Im Browser prüfen**

Seite neu laden. Auf der Startseite erscheint Modul 8 als neue Kachel „Dateien, Formate & Werkzeuge" mit `0/5` Progress.

- [ ] **Schritt 4: Commit**

```bash
git add ki-verstehen.html
git commit -m "feat: Modul 8 in module-Array registriert (Dateien, Formate & Werkzeuge)"
```

---

### Task 7: Karteikarten k86–k110 einfügen

**Files:**
- Modify: `ki-verstehen.html` — `const karteikarten = [...]` — nach k85, vor `];`

- [ ] **Schritt 1: 25 neue Karten einfügen**

Finde die letzte Zeile der karteikarten (k85):
```javascript
  { id:"k85", modul:2, front:"JSON (JavaScript Object Notation)", back:"Leichtgewichtiges Datenformat..." }
];
```
Ersetze `};` am Ende durch `},` und füge danach ein:

```javascript
  { id:"k86", modul:7, front:"ASCII", back:"American Standard Code for Information Interchange: 128 Zeichen (A-Z, 0-9, Sonderzeichen) als Zahlen 0–127. Das Zeichen A = 65, { = 123. Jeder Buchstabe in Code, JSON oder Shell ist eine ASCII-Zahl — das Fundament aller Textdateien." },
  { id:"k87", modul:7, front:"Unicode / UTF-8", back:"Erweiterung von ASCII auf alle Sprachen und Symbole (ue, Emojis, CJK-Zeichen). UTF-8 ist der Standard in KI-Tools und Editoren. Fehler entstehen wenn Kodierungen gemischt werden — z. B. zerstört U+201D als JS-Delimiter die Syntax." },
  { id:"k88", modul:7, front:".txt-Datei", back:"Reiner Text ohne Formatierung — fuer LLMs das idealste Format. Claude liest .txt direkt ohne Konvertierungsschritt. Grosse Textmengen fuer KI-Analysen immer als .txt uebergeben." },
  { id:"k89", modul:7, front:"Markdown / .md", back:"Textdatei mit einfacher Formatierung: # Überschrift, **fett**, - Liste. Als Plaintext lesbar und als formatierter Text darstellbar. CLAUDE.md ist eine Markdown-Datei — Claudes wichtigste Konfigurationsdatei." },
  { id:"k90", modul:7, front:"CLAUDE.md", back:"Markdown-Datei im Projektordner. Wird von Claude Code vor jedem Task automatisch geladen — enthaelt Kontext, Regeln und Praeferenzen fuer das Projekt. Die wichtigste Steuerdatei in Claude Code." },
  { id:"k91", modul:7, front:".csv-Datei", back:"Comma-Separated Values: tabellarische Daten als Text, Spalten durch Komma getrennt. LLMs und Python-Scripts lesen CSV direkt — kein Excel noetig. Tabellen immer als CSV exportieren fuer KI-Verarbeitung." },
  { id:"k92", modul:7, front:"JSON", back:"JavaScript Object Notation: Textformat fuer strukturierte Daten. {\"key\": \"value\"}, Arrays [...], Boolean true/false. Bei Tool Use, MCP und API-Calls kommuniziert Claude immer in JSON — Menschen und Maschinen koennen es lesen." },
  { id:"k93", modul:7, front:"JSON-Struktur", back:"Objekte: {\"key\": \"value\"} — Strings in geraden Anführungszeichen (U+0022). Arrays: [1, 2, 3]. Ein fehlendes Komma oder falsches Anführungszeichen bricht das gesamte JSON — Syntax ist absolut strikt." },
  { id:"k94", modul:7, front:"YAML", back:"Yet Another Markup Language: Konfigurationssprache mit Einrueckung statt {}. Wird fuer MCP-Server-Konfigurationen, GitHub Actions und Docker genutzt. Lesbarer als JSON, aber strikte Einrueckungs-Regeln." },
  { id:"k95", modul:7, front:"URL", back:"Uniform Resource Locator: Adresse einer Ressource im Web. Aufbau: https://domain.com/pfad?parameter=wert. Claude kann URLs nur mit Tools oder MCP-Verbindungen aufrufen — nicht direkt ohne Werkzeug." },
  { id:"k96", modul:7, front:"API-Endpunkt", back:"Spezifische URL fuer Datenaustausch zwischen Programmen. Jeder Claude-Response ist ein API-Call an api.anthropic.com — Claude sendet JSON, empfaengt JSON. MCP-Server sind selbst API-Endpunkte." },
  { id:"k97", modul:7, front:"Python-Script (.py)", back:"Codedatei in Python. Ausfuehren: python3 skript.py. Claude schreibt, liest und erklaert .py-Dateien — haeufig fuer Datenanalyse, Automatisierung und KI-Backend. Syntax-Check: python3 -m py_compile skript.py." },
  { id:"k98", modul:7, front:"JavaScript-Datei (.js)", back:"Laeuft im Browser (Frontend) oder in Node.js (Backend). Ausfuehren: node skript.js. Diese Lern-App enthaelt das gesamte JS fuer Logik, Navigation und Karteikarten-System. Syntax-Check: node --check datei.js." },
  { id:"k99", modul:7, front:"Shell-Script (.sh)", back:"Enthaelt Bash-Shell-Befehle. #!/bin/bash (Shebang) am Anfang gibt den Interpreter an. Ausfuehren: bash skript.sh. Claude Code nutzt Shell-Befehle intensiv: git, node, python3, grep, find." },
  { id:"k100", modul:7, front:"HTML", back:"HyperText Markup Language: beschreibt Struktur einer Webseite mit Tags. <h1>, <div>, <button>, <ul> — das Grundgeruest. Diese Lern-App ist eine einzige .html-Datei mit allem Wissen darin." },
  { id:"k101", modul:7, front:"CSS", back:"Cascading Style Sheets: beschreibt Aussehen (Farben, Abstaende, Schriften, Animationen). In dieser App im <style>-Block. Claude generiert CSS fuer Web-UIs — z. B. beim Frontend-Design mit dem frontend-design Skill." },
  { id:"k102", modul:7, front:"DOM", back:"Document Object Model: Baumstruktur des HTML im Browser-Speicher. JavaScript manipuliert den DOM — Elemente hinzufuegen, Text aendern, Klassen setzen. document.getElementById() ist ein DOM-Zugriff." },
  { id:"k103", modul:7, front:"Mockup / Wireframe", back:"Visuelle UI-Skizze vor dem Code — zeigt Layout und Struktur, nicht Logik. Claude generiert Mockups als HTML/CSS in Minuten. Der schnellste Weg, eine UI-Idee sichtbar und diskutierbar zu machen." },
  { id:"k104", modul:7, front:"PDF", back:"Binaerformat fuer Dokumente — LLMs koennen PDFs nicht direkt lesen. Text muss erst extrahiert werden (via MCP-Tool oder Konverter). Danach steht der Inhalt normal fuer Claude zur Verfuegung." },
  { id:"k105", modul:7, front:"DOCX / XLSX", back:"Microsoft-Formate fuer Word/Excel — intern ZIP-Archive mit XML. Muss zu .txt bzw. .csv konvertiert werden, bevor Claude verarbeitet. Anthropic-Skills (DOCX-Skill, XLSX-Skill) erledigen das automatisch." },
  { id:"k106", modul:7, front:"PNG / JPG", back:"Bilddateien. Multimodale Modelle (Claude 3 Sonnet, Opus, Haiku und neuere) koennen Bilder direkt sehen — Screenshots werden als Bild an die API gesendet. Aeltere reine Text-Modelle koennen keine Bilder verarbeiten." },
  { id:"k107", modul:7, front:"SVG", back:"Scalable Vector Graphic: Vektorgrafik als XML/Text. Claude kann SVG direkt lesen, schreiben und generieren — die Schaubilder in dieser App sind von Claude generierte SVGs. Der Sonderfall unter den Bildformaten." },
  { id:"k108", modul:7, front:"Binaerformat", back:"Datei ohne lesbare Textstruktur — stattdessen Rohdaten in Bytes. PDF, DOCX, XLSX, MP3, PNG, JPG sind Binaerformate. LLMs brauchen Extraktion oder multimodale Faehigkeiten — ein Texteditor zeigt nur Zeichensalat." },
  { id:"k109", modul:7, front:".env-Datei", back:"Textdatei mit Umgebungsvariablen: API-Keys, Passwoerter, Zugangsdaten. Wird nie in Git committet (.gitignore schutzt davor). Claude Code erkennt .env-Dateien und warnt vor versehentlichem Upload sensibler Daten." },
  { id:"k110", modul:7, front:"package.json", back:"Konfigurationsdatei fuer Node.js-Projekte im JSON-Format. Listet Abhaengigkeiten (npm-Pakete), Skripte und Metadaten. Claude liest package.json um das Projekt zu verstehen — aehnlich wie CLAUDE.md fuer Regeln." }
];
```

- [ ] **Schritt 2: Syntaxprüfung + Kartenanzahl prüfen**

```bash
python3 -c "
import re
with open('ki-verstehen.html','r',encoding='utf-8') as f: c=f.read()
js = max(re.findall(r'<script[^>]*>(.*?)</script>',c,re.DOTALL),key=len)
open('/tmp/k.js','w',encoding='utf-8').write(js)
" && node --check /tmp/k.js && echo "Syntax OK"

# Zähle karteikarten-Einträge
python3 -c "
with open('ki-verstehen.html','r',encoding='utf-8') as f: c=f.read()
import re
count = len(re.findall(r'id:\"k\d+\"', c))
print(f'Karteikarten: {count} (Ziel: 110)')
"
```
Erwartung: `Syntax OK` und `Karteikarten: 110`

- [ ] **Schritt 3: Commit**

```bash
git add ki-verstehen.html
git commit -m "feat: Karteikarten k86-k110 fuer Modul 8 (25 neue Karten, Dateiformate & Werkzeuge)"
```

---

### Task 8: renderKartenDecks() — Modul-8-Deck hinzufügen

**Files:**
- Modify: `ki-verstehen.html` — `function renderKartenDecks()`

- [ ] **Schritt 1: Deck-Eintrag ergänzen**

Finde:
```javascript
const decks=[{k:"alle",t:"Alle Module"},...,{k:6,t:"Modul 7: KI-Tools im Alltag"}];
```
Ergänze am Ende des Arrays (nach `{k:6,...}`):
```javascript
,{k:7,t:"Modul 8: Dateien, Formate & Werkzeuge"}
```

- [ ] **Schritt 2: Syntaxprüfung**

```bash
python3 -c "
import re
with open('ki-verstehen.html','r',encoding='utf-8') as f: c=f.read()
js = max(re.findall(r'<script[^>]*>(.*?)</script>',c,re.DOTALL),key=len)
open('/tmp/k.js','w',encoding='utf-8').write(js)
" && node --check /tmp/k.js && echo "OK"
```

- [ ] **Schritt 3: Im Browser prüfen**

Karteikarten-Ansicht öffnen → Deck „Modul 8: Dateien, Formate & Werkzeuge" erscheint mit `0/25 gemeistert`.

- [ ] **Schritt 4: Commit**

```bash
git add ki-verstehen.html
git commit -m "feat: Modul-8-Deck in Karteikarten-Auswahl ergaenzt"
```

---

### Task 9: Abschluss-Verifikation & finaler Commit

**Files:**
- Read: `ki-verstehen.html`

- [ ] **Schritt 1: Vollständige Funktionsprüfung im Browser**

Server prüfen: `http://localhost:8123/ki-verstehen.html`

```bash
# Prüfe Startseite: 8 Module sichtbar
# Prüfe Modul 8: alle 5 Etappen navigierbar
# Prüfe Karteikarten: Deck Modul 8 vorhanden, 25 Karten
# Prüfe Glossar: JSON, HTML, ASCII etc. als Tooltips sichtbar
```

- [ ] **Schritt 2: JS-Checks im Browser via Eval**

```javascript
// Im Browser-Konsole oder via preview_eval:
typeof karteikarten + " / " + karteikarten.length
// Erwartung: "object / 110"

module.find(m => m.id === 7)?.titel
// Erwartung: "Dateien, Formate & Werkzeuge"

karteikarten.filter(k => k.modul === 7).length
// Erwartung: 25

typeof vertiefungen["7-4"]
// Erwartung: "object"
```

- [ ] **Schritt 3: Memory aktualisieren**

`/Users/tsaispace/.claude/projects/-Users-tsaispace-ClaudeCode-KI-Wissensvermittlung/memory/project_ki_lern_app.md` aktualisieren:
- Stand: 2026-06-04
- Letzter Commit: [hash]
- Karteikarten: k1–k110 (110 gesamt)
- Module: 8 (inkl. Dateien, Formate & Werkzeuge)
- Kein bekannter Blocker

- [ ] **Schritt 4: Finaler Commit (falls noch Änderungen offen)**

```bash
git add ki-verstehen.html
git commit -m "feat: Modul 8 komplett — Dateien, Formate & Werkzeuge (5 Etappen, 25 Karten, Glossar)"
```

---

## Selbst-Review

**Spec-Coverage:**
- ✅ CSS Header-Fix (Task 1)
- ✅ schaubildMod8 mit 5 SVGs (Task 2)
- ✅ schaubild()-Dispatcher (Task 3)
- ✅ etappenMod8 (5 Etappen mit check[]) (Task 4)
- ✅ quizMod8 (10 Fragen) (Task 4)
- ✅ vertiefungen 7-0 bis 7-4 (Task 5)
- ✅ module-Array Modul 8 (Task 6)
- ✅ k86–k110 (25 Karten) (Task 7)
- ✅ renderKartenDecks Deck (Task 8)
- ✅ Glossar: automatisch aus karteikarten — kein extra Task nötig

**Syntaxregeln:**
- Alle JS-String-Delimiter: U+0022 — keine Umlaute, keine typografischen Anführungszeichen als Delimiter
- Umlaute in Strings durch Umschreibung (ue, ae, oe, ss) um Risiko zu minimieren
- Nach jedem Task: `node --check` Pflicht

**Konsistenz:**
- `modul:7` für k86–k110 (entspricht id:7 im module-Array = angezeigtes Modul 8)
- vertiefungen-Keys `"7-0"` bis `"7-4"` entsprechen `module[7]` + etappen-Index
- schaubildMod8 cases 0–4 entsprechen den 5 Etappen (Index 0-basiert)
