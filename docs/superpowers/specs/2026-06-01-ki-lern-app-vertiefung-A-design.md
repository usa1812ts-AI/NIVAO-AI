# Spezifikation: Baustein A — Mehr Tiefe pro Etappe

**Datum:** 2026-06-01
**Status:** Freigegeben, in Umsetzung
**Baut auf:** Phase 1–3, Datei `ki-verstehen.html` (4 Module, 21 Etappen)
**Roadmap:** A (dieser Baustein) → B (Karteikarten) → C (Vertiefungs-Modul). D/E geparkt.

## 1. Ziel
Jede Etappe um aufklappbare Vertiefung erweitern: **Vorteile**, **Grenzen/Nachteile**, **Worauf achten (Praxis)**.
Kernlernstoff bleibt ruhig; Tiefe öffnet sich auf Klick.

## 2. Architektur
- Separates Daten-Objekt `vertiefungen`, verschlüsselt nach `"<modul>-<etappe>"` → vermeidet Eingriffe in die bestehenden Etappen-Arrays.
  - Form: `{ "2-2": { vorteile:[...], grenzen:[...], achten:[...] }, … }`. Alle drei Listen optional.
- Render-Helfer `vertiefungHTML(m,i)`: erzeugt den Klapp-Block, falls Daten vorhanden.
- `renderEtappe()` ruft `vertiefungHTML(m,i)` zwischen Merkbild und Kurz-Check auf.
- Toggle-Funktion `toggleVertiefung(btn)`: blendet den Body ein/aus (reiner UI-Zustand, keine Persistenz).
- CSS: Akkordeon + drei farbcodierte Blöcke (Vorteile grün, Grenzen rot, Worauf achten orange).

## 3. Darstellung
- Zugeklappter Balken: „＋ Vertiefung: Vorteile · Grenzen · Worauf achten" (unter Merkbild, vor Kurz-Check).
- Aufgeklappt: vorhandene Blöcke je mit Label + Bulletliste, farbiger Linksrand.
- Standard: zugeklappt. Klick wechselt ＋/－ und blendet den Body ein.

## 4. Inhalt (flexibel je Thema)
- ~20 der 21 Etappen erhalten Inhalte; pro Etappe nur die passenden Abschnitte.
- Capstone „Praxis-Prinzipien" (Modul 4, Etappe 6) bleibt ohne Block (ist selbst die Essenz).
- Inhalte aus der Wissensbasis destilliert, je Abschnitt 1–3 kurze Punkte.

## 5. Erfolgskriterien
- In ~20 Etappen erscheint der zugeklappte Vertiefungs-Balken; Klick öffnet/schließt sauber.
- Farbcodierung korrekt (grün/rot/orange); nur vorhandene Abschnitte werden gezeigt.
- Bestehende Funktionen (Etappen, Checks, Quiz, Faden, Netz) unverändert; keine JS-Fehler; responsive.
