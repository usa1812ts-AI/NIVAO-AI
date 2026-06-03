# Spezifikation: Lern-App „KI verstehen" — Phase 2 (Module 2 & 3)

**Datum:** 2026-06-01
**Status:** Konzept freigegeben, bereit für Umsetzung
**Baut auf:** Phase 1 (`2026-06-01-ki-lern-app-design.md`), Datei `ki-verstehen.html`

---

## 1. Ziel

Die App um die Inhalte aus **Teil 2 und Teil 3** der Wissensbasis erweitern und dafür von einer
flachen Etappen-Liste auf eine **Modul-Struktur** umstellen. Lernlogik (verstehen → verknüpfen →
abprüfen) und NIVAO-Design bleiben unverändert.

## 2. Architektur-Umbau: Modul-Struktur

- Datenmodell wird von einer flachen `etappen`-Liste auf ein **`module`-Array** umgestellt.
  Jedes Modul: `{ id, titel, kurz, etappen:[...], quiz:[...] }`.
- **Module:**
  - **Modul 1 — Grundlagen:** die bestehenden 6 Etappen + bestehendes Quiz (inhaltlich unverändert).
  - **Modul 2 — Wie Modelle arbeiten:** 4 neue Etappen + Quiz (Teil 2).
  - **Modul 3 — Mit Modellen arbeiten:** 5 neue Etappen + Quiz (Teil 3).
- **Views (Router):** `start` (Modulübersicht) · `modul` (Etappen eines Moduls) · `etappe` · `faden` · `netz` · `quiz`.
- **Zustand (`state`):** `view`, `aktuellesModul`, `aktuelleEtappe`, `erledigt` (verschachtelt je Modul/Etappe), `letzteStelle` ({modul, etappe}), `quizErgebnis` (je Modul).
- **Persistenz:** localStorage-Schlüssel auf **`ki-verstehen-v2`** anheben. Phase-1-Häkchen werden dabei einmalig zurückgesetzt (bewusst akzeptiert). `try/catch` wie bisher.
- **„Weiter wo du warst":** merkt sich Modul **und** Etappe; springt direkt dorthin.
- **„Der rote Faden" + „Wissensnetz":** bleiben Synthese-Ansichten von **Modul 1** (aus dessen Modul-Übersicht erreichbar).

## 3. Komponenten / Views

### 3.1 Startseite (Modulübersicht)
- Drei Modul-Karten mit Titel, Kurzbeschreibung, Fortschritt (x/n Etappen erledigt).
- „Weiter wo du warst"-Banner (Modul + Etappe), wenn ein Stand existiert.
- „Fortschritt zurücksetzen" (mit Rückfrage).

### 3.2 Modul-Übersicht
- Etappen des Moduls als Pfad (wie die bisherige Startseite), Fortschrittsbalken.
- Buttons: Abschlussquiz (dieses Moduls); bei Modul 1 zusätzlich „Der rote Faden" + „Wissensnetz".
- Zurück zur Modulübersicht.

### 3.3 Lernseite je Etappe (unverändertes Schema)
Schaubild · Kernsatz · Stichpunkte · Merkbild · Mini-Selbstcheck (1–2 Fragen, Sofort-Feedback) ·
„Verstanden"-Button (hakt ab, geht zur nächsten Etappe; nach der letzten zurück zur Modul-Übersicht).

### 3.4 Abschlussquiz je Modul
Multiple-Choice über die Etappen des Moduls, Auswertung mit Punktzahl + Wiederholungs-Empfehlung,
wiederholbar; Ergebnis je Modul gespeichert.

## 4. Inhalte Modul 2 — Wie Modelle arbeiten (Teil 2)

| # | Thema | Kernidee | Schaubild |
|---|-------|----------|-----------|
| 2.1 | Trainingsphasen | Pretraining → Fine-tuning → RLHF → Constitutional AI | Stufen-Pipeline, Datenmenge nimmt ab |
| 2.2 | Kontextfenster | Arbeitsgedächtnis in Tokens; „lost in the middle"; kein Langzeitgedächtnis | Box mit Tokens, Mitte schwächer, Rest fällt raus |
| 2.3 | Inferenz & Temperature | Temperature steuert Zufälligkeit beim Token-Wählen | zwei Verteilungen: niedrig (spitz) vs. hoch (flach) |
| 2.4 | Halluzinationen & Grenzen | plausibel ≠ wahr; Gegenmaßnahmen | Aussage „✗ falsch" + Gegenmaßnahmen-Liste |

## 5. Inhalte Modul 3 — Mit Modellen arbeiten (Teil 3)

| # | Thema | Kernidee | Schaubild |
|---|-------|----------|-----------|
| 3.1 | Prompt Engineering | Zero-/Few-Shot, Rolle, Kontext, Format | Prompt-Karte mit markierten Bausteinen |
| 3.2 | Chain of Thought & Reasoning | Schritt-für-Schritt verbessert harte Aufgaben | zwei Wege: direkt (✗) vs. schrittweise (✓) |
| 3.3 | RAG | externes Wissen erden, Halluzinationen senken | Pipeline: Frage → Vektor-DB → Treffer → Modell → Antwort |
| 3.4 | Tool Use & MCP | Werkzeuge fürs Modell; MCP = „USB-C für KI" | Modell ruft Werkzeuge über MCP-Stecker |
| 3.5 | Agents & Agentic Coding | Ziel + selbstständige Schleife statt Einzelprompt | Schleife: Ziel → Plan → Aktion → Beobachtung |

## 6. Bewusst außerhalb von Phase 2 (YAGNI)

- Modul 4 (Teil 4 Anbieter-Landschaft + Teil 5 Praxis-Prinzipien) → Phase 3.
- Vertiefungs-Datei (A–K), Karteikarten/Spaced Repetition, Nutzerkonten, Cloud-Sync.

## 7. Erfolgskriterien

- Startseite zeigt 3 Module mit je eigenem Fortschritt.
- Modul 2 (4 Etappen) und Modul 3 (5 Etappen) sind vollständig: Schaubild, Erklärung, Merkbild, Kurz-Check.
- Jedes Modul hat ein funktionierendes Abschlussquiz mit Auswertung.
- „Weiter wo du warst" springt zu Modul + Etappe; Fortschritt überlebt Browser-Neustart.
- Modul 1 inkl. rotem Faden + Wissensnetz funktioniert unverändert.
- NIVAO-Design konsistent; responsive; keine JS-Fehler; iPad-Fallback-Hinweis vorhanden.
