# Design-Dokument: Glossar + Inline-Tooltips

**Datum:** 2026-06-03
**Datei:** `ki-verstehen.html`
**Status:** Entwurf — wartet auf Abnahme

---

## Ziel

Lernende sollen unbekannte Fachbegriffe direkt beim Lesen nachschlagen können, ohne das Modul zu verlassen. Zusätzlich gibt es eine dedizierte Glossar-Seite für das kompakte Nachschlagen aller Begriffe.

---

## Entschiedene Designfragen

| Frage | Entscheidung |
|---|---|
| Ansatz | Variante C: Inline-Tooltip im Text + Glossar-Seite |
| Glossar-Navigation | Button auf der Startseite, neben "🃏 Karteikarten" |
| Datenbasis | Vorhandene `karteikarten`-Array (k1–k77) — kein Doppelaufwand |
| Tooltip-Auslöser | Click/Tap (funktioniert auf iPad und Desktop) |

---

## Komponenten

### 1. Datenbasis: `karteikarten` als Glossar-Quelle

Keine neuen Daten nötig. Das bestehende Array (`karteikarten`) wird dual genutzt:
- Wie bisher: Karteikarten-Lernmodus (Leitner-System)
- Neu: Glossar-Nachschlagewerk (alphabetisch sortiert, gefiltert, durchsucht)

Jeder Eintrag liefert:
- `front` → Begriff (Glossar-Stichwort)
- `back` → Definition (Glossar-Erklärung)
- `modul` → Modul-Zuordnung (0-basiert: 0 = Modul 1 … 6 = Modul 7; Anzeige: `modul + 1`)

### 2. Inline-Tooltips im Lerntext

**Wann:** Nach jedem Render einer Etappe (nach `renderEtappe()`) wird der gerenderte Text gescannt.

**Wie:** Eine Funktion `injectTooltips(container)` durchsucht alle Textknoten im Container und ersetzt jeden Treffer, der mit einem Glossar-Begriff übereinstimmt, durch:

```html
<span class="glossar-term" data-term="Shell">Shell
  <span class="glossar-tooltip">
    Befehlszeilen-Umgebung des Betriebssystems.
    <a class="glossar-link">→ Im Glossar</a>
  </span>
</span>
```

**Matching-Regeln:**
- Case-insensitive, Ganz-Wort-Matching (`\bBegriff\b`)
- Begriffe werden **nur im Fließtext** markiert (Punkte, Kernsatz, Merkbild)
- Nicht in: Überschriften, Quiz-Fragen, Quiz-Antworten, bereits markierten `<span>`s
- Jeder Begriff wird **nur beim ersten Vorkommen** pro Etappe markiert (kein Spam)

**Tooltip-Verhalten:**
- Tap/Click auf Begriff → Tooltip öffnet sich
- Tap/Click irgendwo anders → Tooltip schließt sich
- Nur ein Tooltip gleichzeitig offen
- Klick auf "→ Im Glossar" → navigiert zur Glossar-Seite, springt direkt zum Eintrag (`#glossar-Shell`)

### 3. Glossar-Seite (`renderGlossar()`)

Neue Ansicht, erreichbar über den Startseiten-Button. Gleiche Navigation wie Module (← zurück-Button oben links).

**Aufbau der Seite:**
1. **Suchfeld** — Live-Filter beim Tippen, filtert Begriffe nach `front`
2. **Buchstabenleiste** — A–Z Schnellsprung, aktiver Buchstabe hervorgehoben
3. **Einträge** — alphabetisch sortiert, gruppiert nach Anfangsbuchstabe:
   - Begriff (fett)
   - Modul-Badge (z. B. "Modul 1")
   - Definition
   - "→ auch als Karteikarte lernen" (öffnet Karteikarten-Deck des entsprechenden Moduls)
4. **Anker** — jeder Eintrag hat `id="glossar-<Begriff>"` für Deep-Link aus Tooltip

**Startseiten-Button:**
```
[🃏 Karteikarten]  [📖 Glossar]
```
Neben dem bestehenden Karteikarten-Button, gleiche Optik.

---

## Datenfluss

```
karteikarten[]
    │
    ├─→ renderKartenDecks()    (unverändert — Karteikartenmodus)
    │
    └─→ renderGlossar()        (neu — alphabetisch, suchbar)
            │
            └─→ Buchstaben-Gruppen, Einträge mit Modul-Badge

renderEtappe()
    └─→ injectTooltips(container)   (neu — nach dem Rendern)
            └─→ Textknoten scannen
                └─→ Glossar-Treffer → <span class="glossar-term"> wrappen
```

---

## Umfang & Abgrenzung

**In Scope:**
- `injectTooltips()` Funktion
- `renderGlossar()` Funktion
- Startseiten-Button "📖 Glossar"
- CSS für `.glossar-term`, `.glossar-tooltip`, Glossar-Seite
- Buchstaben-Filter + Suchfeld (Live-Filter, kein Server)
- Deep-Link: Tooltip → Glossar-Anker

**Out of Scope (bewusst weggelassen):**
- Neue Glossar-Begriffe hinzufügen (Datenbasis bleibt karteikarten[])
- Tooltips in Quiz-Fragen oder Karteikarten selbst
- Mehrsprachigkeit
- Offline-Speicherung von "zuletzt nachgeschlagen"

---

## Technische Rahmenbedingungen

- Single HTML-Datei, kein Build-Tool, kein Framework
- Vanilla JS, CSS inline im `<style>`-Block
- Keine externen Abhängigkeiten
- Muss auf iPad Safari funktionieren (Touch-Events)
