# Design-Spec: Modul 8 „Dateien, Formate & Werkzeuge" + Header-Fix

**Datum:** 2026-06-04  
**Projekt:** KI-Wissensvermittlung / ki-verstehen.html  
**Status:** Approved ✅

---

## 1. Ziel & Kontext

Die Lern-App „KI verstehen" hat aktuell 7 Module. Beim Arbeiten mit Claude Code begegnen dem Nutzer ständig Dateitypen, Formate und Werkzeuge (JSON, Python, Markdown, HTML etc.), die nicht erklärt sind. Modul 8 schließt diese Lücke — aus der Perspektive: „Was ist das und wie begegnet es mir beim Arbeiten mit KI/Claude?"

Zusätzlich wird der NIVAO-Header vergrößert (Logo + Wordmark).

---

## 2. Header-Fix

### Problem
- Logo-Icon (`mark`): 38×38 px — zu klein, kaum sichtbar
- Wordmark (`wordmark`): 25 px Höhe — wirkt wie Fußzeile

### Lösung
- `mark`: **52×52 px**
- `wordmark`: **36 px** Höhe
- Kein weiterer CSS-Eingriff nötig — bestehende Flexbox-Struktur bleibt

---

## 3. Modul 8 — Übersicht

**Name:** Modul 8: Dateien, Formate & Werkzeuge  
**Untertitel auf Startseite:** ASCII, JSON, HTML, Python, Mockup & Co.  
**Perspektive:** KI-first — jeder Begriff wird zuerst aus dem Blickwinkel „was bedeutet das für Claude / Claude Code / LLMs" erklärt  
**Etappen:** 5  
**Karteikarten:** k86–k110 (25 neue Karten)  
**Progress-Counter:** 0/5

---

## 4. Etappen-Struktur

### M8.1 — Wie KI Text liest
**Themen:** ASCII, Unicode/UTF-8, `.txt`, `.md`, `.csv`, `CLAUDE.md`  
**Kernaussage:** LLMs verarbeiten nur Text — alles andere muss konvertiert werden. ASCII ist das Fundament, UTF-8 der heutige Standard. Markdown ist Claudes Muttersprache.  
**Schaubild:** Pyramide — ASCII → Unicode → UTF-8 → Textdatei → CLAUDE.md  
**Vertiefung:** Warum Zeichenkodierungsfehler (U+201D statt U+0022) JS-Code brechen können

### M8.2 — Strukturierte Daten & Kommunikation
**Themen:** JSON, JSON-Struktur, YAML, URL, API-Endpunkt  
**Kernaussage:** Claude „spricht" JSON — bei Tool Use, MCP, API-Calls. YAML für Konfiguration. URLs als Adressen von Ressourcen.  
**Schaubild:** Flussdiagramm — Claude → JSON-Request → API-Endpunkt → JSON-Response → Claude  
**Vertiefung:** JSON-Syntaxregeln & häufige Fehler (fehlende Kommas, falsche Anführungszeichen)

### M8.3 — Code-Dateien
**Themen:** Python `.py`, JavaScript `.js`, Shell-Script `.sh`, Binär vs. Text  
**Kernaussage:** Claude liest, schreibt und erklärt Code-Dateien. Jede Sprache hat ihren Einsatzbereich: Python für Daten/Backend, JS für Web/Node, Shell für Automatisierung.  
**Schaubild:** Vergleichstabelle SVG — Sprache / Dateiendung / Wo läuft es / Claude-Einsatz  
**Vertiefung:** Was passiert wenn Claude Code `node script.js` oder `python3 analyse.py` ausführt

### M8.4 — Web-Formate
**Themen:** HTML, CSS, DOM, JavaScript (Browser), URL im Browser, Mockup/Wireframe  
**Kernaussage:** HTML = Struktur, CSS = Aussehen, JS = Verhalten. Diese App ist eine einzige `.html`-Datei. Ein Mockup entsteht bevor der Code geschrieben wird.  
**Schaubild:** Schichten-Diagramm — HTML (Knochen) + CSS (Haut) + JS (Muskeln) + Browser-Rendering  
**Vertiefung:** Wie Claude eine UI baut: erst Mockup-HTML, dann Logik, dann Feinschliff

### M8.5 — Binär, Bilder & Grenzen von KI
**Themen:** PDF, DOCX/XLSX, PNG/JPG, SVG, `.env`, `package.json`, Binärformat  
**Kernaussage:** Nicht alles ist für LLMs direkt lesbar. Binärformate brauchen Extraktion. Multimodale Modelle können Bilder „sehen". SVG ist der Sonderfall: Vektorgrafik als lesbarer Text.  
**Schaubild:** Radial-Netz — alle Formate gruppiert: Text / Code / Web / Binär / Multimodal  
**Vertiefung:** Sicherheitsrelevante Dateien: `.env`, `CLAUDE.md`, `.gitignore`

---

## 5. Karteikarten k86–k110

Alle Karten: `modul: 7` → `modul: 8` (neues Modul), KI-first formuliert.

| ID | front | Kerninhalt back |
|----|-------|----------------|
| k86 | ASCII | 128 Zeichen als Zahlen 0–127; Fundament aller Textdateien; JSON/Python/Shell basieren darauf |
| k87 | Unicode / UTF-8 | Erweiterung auf alle Sprachen & Symbole; UTF-8 Standard in KI-Tools; Fehler bei gemischten Kodierungen |
| k88 | .txt-Datei | Reiner Text ohne Formatierung; ideal für LLMs; direkt ohne Konvertierung lesbar |
| k89 | Markdown / .md | Textdatei mit einfacher Formatierung; `CLAUDE.md` ist Markdown; Claude liest sie bei jedem Start |
| k90 | CLAUDE.md | Markdown-Datei mit Kontext/Regeln für Claude Code; wird vor jedem Task automatisch geladen |
| k91 | .csv-Datei | Tabellarische Daten als Text; LLMs und Python lesen CSV direkt ohne Excel |
| k92 | JSON | Standardformat für API-Kommunikation; Claude antwortet bei Tool Use immer in JSON |
| k93 | JSON-Struktur | `{"key":"value"}`; Objekte, Arrays, Strings, Zahlen, Boolean; ein Syntaxfehler bricht alles |
| k94 | YAML | Konfigurationssprache mit Einrückung statt `{}`; für MCP-Configs, GitHub Actions, Docker |
| k95 | URL | Adresse einer Web-Ressource; Claude kann URLs via Tools aufrufen, nicht direkt ohne Tool |
| k96 | API-Endpunkt | Spezifische URL für Datenaustausch; jede Claude-Antwort ist ein API-Call an Anthropic |
| k97 | Python-Script (.py) | Python-Codedatei; Claude schreibt/liest `.py`; für Datenanalyse, Automatisierung, Backend |
| k98 | JavaScript-Datei (.js) | Läuft im Browser oder Node.js; diese App enthält JS für die gesamte Logik |
| k99 | Shell-Script (.sh) | Enthält Bash-Befehle; Claude Code führt Shell-Befehle aus; `#!/bin/bash` als Markierung |
| k100 | HTML | Struktur einer Webseite mit Tags; diese Lern-App ist eine einzige `.html`-Datei |
| k101 | CSS | Beschreibt Aussehen (Farben, Abstände, Schriften); in dieser App im `<style>`-Block |
| k102 | DOM | Baumstruktur des HTML im Browser-Speicher; JS manipuliert DOM; Claude nutzt DOM-Abfragen zum Testen |
| k103 | Mockup / Wireframe | Visuelle UI-Skizze vor dem Code; Claude generiert Mockups als HTML/CSS |
| k104 | PDF | Binärformat; LLMs brauchen Textextraktion; Claude mit MCP-Tool kann PDFs analysieren |
| k105 | DOCX / XLSX | Microsoft-Binärformate; müssen zu `.txt`/`.csv` konvertiert werden vor Claude-Verarbeitung |
| k106 | PNG / JPG | Bilddateien; multimodale Modelle (Claude 3+) können Bilder direkt sehen |
| k107 | SVG | Vektorgrafik als XML/Text; Claude kann SVG lesen, schreiben und generieren |
| k108 | Binärformat | Nicht als Text lesbar; LLMs brauchen Extraktion oder multimodale Fähigkeiten |
| k109 | .env-Datei | Enthält API-Keys und Passwörter; wird nie committet; Claude Code warnt vor sensiblen Daten |
| k110 | package.json | Node.js-Konfiguration als JSON; listet Abhängigkeiten; Claude liest sie zum Projektverständnis |

---

## 6. Glossar

Alle 25 Begriffe (k86–k110) werden als Glossareinträge ergänzt und erhalten Inline-Tooltips in den Etappen-Texten.

---

## 7. Technische Umsetzung

### Datei
Alle Änderungen in einer einzigen Datei: `ki-verstehen.html`

### Reihenfolge der Änderungen
1. **CSS:** `.mark` 52×52px, `.wordmark` 36px Höhe
2. **Modul-Array:** Modul 8 Eintrag ergänzen (`id:8`, Etappen-Anzahl: 5)
3. **Etappen-Inhalte:** 5 Template-Strings für M8.1–M8.5 mit Schaubildern
4. **Karteikarten-Array:** k86–k110 anhängen
5. **Glossar-Array:** 25 neue Einträge
6. **Quiz:** Optional — Quizfragen für Modul 8 (falls Zeit)

### Syntaxregeln (gelernt aus k35-Bug)
- Alle JS-String-Delimiter: U+0022 (gerade Anführungszeichen)
- Typografische `"` / `"` nur innerhalb von Strings, nie als Delimiter
- Nach jedem Schritt: `node --check ki-verstehen.html` (via Python-Extraktion)

---

## 8. Nicht im Scope

- Neue Quiz-Fragen für Modul 8 (kann später ergänzt werden)
- Umbenennung bestehender Module
- Änderungen am Fortschritts-Tracking-System
