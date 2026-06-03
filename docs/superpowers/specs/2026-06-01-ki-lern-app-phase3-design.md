# Spezifikation: Lern-App „KI verstehen" — Phase 3 (Modul 4)

**Datum:** 2026-06-01
**Status:** Freigegeben, in Umsetzung
**Baut auf:** Phase 1 & 2, Datei `ki-verstehen.html` (Modul-Struktur vorhanden)

## 1. Ziel
Modul 4 ergänzen — Inhalte aus Teil 4 (Anbieter-Landschaft) und Teil 5 (Praxis-Prinzipien).
Gleiche Architektur, gleiche Lernlogik, gleiches NIVAO-Design. Keine Strukturänderung nötig.

## 2. Umsetzung
- Neues Modul-Objekt `{ id:3, titel:"Anbieter & Praxis", kurz:"…", etappen:etappenMod4, quiz:quizMod4, synthese:false }` ins `module`-Register.
- `schaubild(m,e)`-Dispatcher um `if(m===3) return schaubildMod4(e);` erweitern.
- Keine Änderung an Router, State, Persistenz (skaliert bereits über `module`).

## 3. Modul 4 — 6 Etappen (Teil 4 + 5)
| # | Thema | Schaubild |
|---|-------|-----------|
| 4.1 | Anbieter-Überblick (Claude, GPT, Gemini, offene Modelle) | 2×2-Anbieter-Raster |
| 4.2 | Das richtige Modell wählen | schnell&günstig vs. tief&teuer + Kriterien-Chips |
| 4.3 | Benchmarks & ihre Grenzen | gesättigtes Balken-Diagramm + Kontaminations-Warnung |
| 4.4 | Multimodalität | zentrales Modell + Text/Bild/Audio/Video |
| 4.5 | Sicherheit, Datenschutz & Ethik | Risiko-Kacheln + Grundregel-Banner |
| 4.6 | Praxis-Prinzipien (Capstone) | Merksatz-Checkliste mit Haken |

- Jede Etappe: Schaubild, Kernsatz, Stichpunkte, Merkbild, 1–2 Kurz-Checks.
- Abschlussquiz Modul 4: ~8 Fragen über die Etappen, mit Auswertung + Wiederholungs-Empfehlung.

## 4. Außerhalb (YAGNI)
Vertiefungs-Datei (A–K), Karteikarten/Spaced Repetition, Nutzerkonten, Cloud-Sync.

## 5. Erfolgskriterien
- Startseite zeigt 4 Module mit eigenem Fortschritt.
- Modul 4 vollständig (6 Etappen + Schaubilder + Checks + Quiz).
- Module 1–3 unverändert funktionsfähig (Regression).
- Responsive, keine JS-Fehler.
