# Spezifikation: Baustein B — Karteikarten-Modus

**Datum:** 2026-06-01
**Status:** Umgesetzt & verifiziert
**Baut auf:** Phase 1–3 + Baustein A, Datei `ki-verstehen.html`
**Roadmap:** A ✅ → B (dieser Baustein) ✅ → C (Vertiefungs-Modul) offen

## 1. Ziel
Karteikarten zum Wiederholen der Kernbegriffe, mit Leitner-Spaced-Repetition.

## 2. Umsetzung
- **Einstieg:** Button „🃏 Karteikarten" auf der Startseite → `navigate('karten')`.
- **Stapel-Auswahl** (`renderKartenDecks`): „Alle Module" + 4 Modul-Stapel, je mit `gemeistert/total · fällig`.
- **Lernrunde** (`startRunde`/`renderKartenrunde`): zieht fällige Karten (max. 20/Runde; fällt auf freie Wiederholung zurück, wenn nichts fällig). Karte: Vorderseite Begriff → tippen → Rückseite Definition → „Gewusst ✓" / „Nochmal ✗".
- **Leitner:** je Karte Box 1–5 + Fälligkeits-Runde, gespeichert. „Gewusst" → Box +1, Fälligkeit in 1/2/4/8/16 Runden; „Nochmal" → Box 1, nächste Runde fällig + Wiedervorlage in derselben Runde. Box 5 = gemeistert.
- **Auswertung** (`renderKartenErgebnis`): gewusst/total + Stapel-Lernstand; „Neue Runde" / „Zur Auswahl".
- **Daten:** 45 kuratierte Karten (Begriff → Definition) aus den Glossaren/Kernbegriffen der 4 Module.
- **Zustand:** `state.karten` (Box+Fälligkeit je Karte) und `state.kRunde` (globaler Rundenzähler) in localStorage; abwärtskompatibel über `Object.assign(leererState(), …)`. Reset per `resetKarten`.

## 3. Umgesetzte Korrekturen
- Globale Regel `[hidden]{display:none!important}` — sonst überschrieb `.navrow{display:flex}` das `hidden` der Bewertungsbuttons.
- `kkBewerte` gegen Aufrufe nach Rundenende abgesichert.

## 4. Erfolgskriterien (erfüllt)
- 5 Stapel mit korrekten Zählern; Karte umdrehen zeigt Buttons erst nach dem Flip.
- Leitner: Box steigt/fällt korrekt, „Nochmal"-Karten kommen wieder, Runde endet, Rundenzähler +1.
- Persistenz und Reset funktionieren; bestehende Module/Quiz/Vertiefung unberührt; keine JS-Fehler.
