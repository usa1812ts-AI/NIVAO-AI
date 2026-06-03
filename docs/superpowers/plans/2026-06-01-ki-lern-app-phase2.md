# Lern-App „KI verstehen" — Phase 2 Umsetzungsplan (Module 2 & 3)

> **Verifikation:** Eine einzelne HTML-Datei, kein Test-Framework. Verifikation durch **Öffnen im Browser + Sicht-/Klick-Prüfung** (Screenshot/Eval via Claude-Preview).

**Goal:** Die App `ki-verstehen.html` auf eine Modul-Struktur umstellen und um Modul 2 (Teil 2, 4 Etappen) und Modul 3 (Teil 3, 5 Etappen) erweitern — inkl. Schaubilder, Kurz-Checks und Modul-Quizzen.

**Architecture:** Bestehende flache `etappen`-Liste wird zu einem `module`-Array. Modul 1 = bisherige 6 Etappen + Quiz (inhaltlich unverändert). Router bekommt eine neue `modul`-View (Etappenübersicht je Modul). Zustand wird modul-bewusst (`aktuellesModul`, verschachteltes `erledigt`, `letzteStelle`, `quizErgebnis` je Modul); localStorage-Key → `v2`.

**Tech Stack:** HTML5, CSS3 (CSS-Variablen), Vanilla JS, Inline-SVG, localStorage. Keine externen Abhängigkeiten.

**Quelle Spezifikation:** `docs/superpowers/specs/2026-06-01-ki-lern-app-phase2-design.md`
**Quelle Inhalt:** `KI-Wissensbasis.md`, Teil 2 (Abschnitte 7–10) und Teil 3 (Abschnitte 11–15).
**Datei:** `ki-verstehen.html` (vorhanden, Phase 1)

---

### Task 1: Datenmodell auf Module umstellen

**Files:** Modify `ki-verstehen.html` (Script-Block)

- [ ] **Schritt 1:** Bestehendes `etappen`-Array + `quizFragen` in ein Modul-Objekt überführen:
  `const module = [ { id:0, titel:"Grundlagen", kurz:"KI, Tokens, Embeddings, Attention", etappen:[...bisherige 6...], quiz:[...bisherige quizFragen...] }, ... ]`.
  Inhalt der 6 Etappen + des Quiz **unverändert** übernehmen.
- [ ] **Schritt 2:** Modul 2 (`id:1`, titel "Wie Modelle arbeiten") und Modul 3 (`id:2`, titel "Mit Modellen arbeiten") als leere Gerüste mit `etappen:[]`, `quiz:[]` anlegen (Inhalt folgt in Task 5/6).
- [ ] **Schritt 3:** Helfer `function alleEtappen(m){return module[m].etappen;}` und Fortschritt `function modulFortschritt(m){...}` (Anzahl erledigt / gesamt) ergänzen.
- [ ] **Verifikation:** `console.log(module.length)` = 3; `module[0].etappen.length` = 6.

---

### Task 2: Zustand & Persistenz modul-bewusst (v2)

**Files:** Modify `ki-verstehen.html`

- [ ] **Schritt 1:** `STORE_KEY = "ki-verstehen-v2"`. `leererState()` →
  `{ view:"start", aktuellesModul:0, aktuelleEtappe:0, erledigt:{}, letzteStelle:null, quizErgebnis:{} }`.
  `erledigt` ist verschachtelt: `erledigt[modulId] = { etappeId:true }`.
- [ ] **Schritt 2:** Helfer `function istErledigt(m,e){return !!(state.erledigt[m] && state.erledigt[m][e]);}` und
  `function setErledigt(m,e){ if(!state.erledigt[m]) state.erledigt[m]={}; state.erledigt[m][e]=true; }`.
- [ ] **Schritt 3:** `loadState()`/`saveState()` wie bisher mit `try/catch` belassen.
- [ ] **Verifikation:** Im Browser nach Etappenbesuch `localStorage['ki-verstehen-v2']` prüfen (enthält `aktuellesModul`, `letzteStelle`).

---

### Task 3: Router + Start-View (Modulübersicht)

**Files:** Modify `ki-verstehen.html`

- [ ] **Schritt 1:** `navigate(view, payload)` erweitern: bei `view==="modul"` `state.aktuellesModul=Number(payload)`; bei `view==="etappe"` erwartet `payload={m,e}` → `state.aktuellesModul=m; state.aktuelleEtappe=e;`.
- [ ] **Schritt 2:** `render()`-Switch: `start`→`renderStart()`, `modul`→`renderModul()`, `etappe`→`renderEtappe()`, `faden`/`netz`/`quiz` wie gehabt (quiz wird modul-bewusst, Task 7).
- [ ] **Schritt 3:** `renderStart()` neu: Titel + Lead, „Weiter wo du warst"-Banner (aus `state.letzteStelle={m,e}` → Button `navigate('etappe',{m,e})`), 3 Modul-Karten mit Titel/Kurz/Fortschritt (`modulFortschritt`), Klick → `navigate('modul', id)`. „Fortschritt zurücksetzen" (confirm) bleibt.
- [ ] **Verifikation:** Browser: Startseite zeigt 3 Modul-Karten + Fortschritt je Modul; Resume-Banner erscheint nach Etappenbesuch.

---

### Task 4: Modul-View (Etappenübersicht) + angepasste Etappe/„Verstanden"

**Files:** Modify `ki-verstehen.html`

- [ ] **Schritt 1:** `renderModul()`: zeigt Etappen des `state.aktuellesModul` als Pfad (Nummer, Titel, Kurz, Status via `istErledigt`), Fortschrittsbalken, „← Übersicht" (→ `navigate('start')`). Button „Abschlussquiz" (→ `navigate('quiz')`). Nur bei Modul 0 zusätzlich Buttons „Der rote Faden" (`navigate('faden')`) und „Wissensnetz" (`navigate('netz')`).
- [ ] **Schritt 2:** `renderEtappe()` modul-bewusst: liest `e = module[state.aktuellesModul].etappen[state.aktuelleEtappe]`. „← Modul"-Link → `navigate('modul', state.aktuellesModul)`. Setzt `state.letzteStelle={m:state.aktuellesModul,e:state.aktuelleEtappe}` + `saveState()`.
- [ ] **Schritt 3:** `etappeFertig()`: `setErledigt(m,e)`; ist es nicht die letzte Etappe → nächste Etappe; sonst → `navigate('modul', m)` (bei Modul 0 bleibt der rote Faden zusätzlich aus dem Modul erreichbar).
- [ ] **Schritt 4:** `schaubild(m,e)` statt `schaubild(i)` — Schaubilder je Modul/Etappe. Modul-0-Schaubilder unverändert übernehmen.
- [ ] **Verifikation:** Browser: Modul 1 (Grundlagen) komplett durchklickbar wie vorher; roter Faden + Wissensnetz aus Modul-1-Übersicht erreichbar.

---

### Task 5: Inhalte Modul 2 — Wie Modelle arbeiten (4 Etappen)

**Files:** Modify `ki-verstehen.html`

- [ ] **Schritt 1:** `module[1].etappen` mit 4 Objekten füllen (Schema: `titel, kurz, kernsatz, punkte[], merkbild, check[]`), Inhalt aus `KI-Wissensbasis.md` Abschnitte 7–10 destilliert:
  - 2.1 Trainingsphasen · 2.2 Kontextfenster · 2.3 Inferenz & Temperature · 2.4 Halluzinationen & Grenzen.
  Je 1–2 Check-Fragen mit korrekter Option + Erklärung.
- [ ] **Schritt 2:** 4 Inline-SVG-Schaubilder in `schaubild(1,e)` ergänzen:
  - 2.1 Stufen-Pipeline (Pretraining groß → Fine-tuning → RLHF → CAI), 2.2 Kontextfenster-Box (Tokens, Mitte schwächer), 2.3 zwei Verteilungen (niedrig spitz / hoch flach), 2.4 Aussage „✗" + Gegenmaßnahmen.
  NIVAO-Farben, schlicht.
- [ ] **Verifikation:** Browser: alle 4 Etappen von Modul 2 öffnen → Schaubild + Check funktionieren.

---

### Task 6: Inhalte Modul 3 — Mit Modellen arbeiten (5 Etappen)

**Files:** Modify `ki-verstehen.html`

- [ ] **Schritt 1:** `module[2].etappen` mit 5 Objekten füllen, Inhalt aus Abschnitte 11–15:
  - 3.1 Prompt Engineering · 3.2 Chain of Thought & Reasoning · 3.3 RAG · 3.4 Tool Use & MCP · 3.5 Agents & Agentic Coding. Je 1–2 Checks.
- [ ] **Schritt 2:** 5 Inline-SVG-Schaubilder in `schaubild(2,e)`:
  - 3.1 Prompt-Karte mit Bausteinen, 3.2 zwei Wege (direkt ✗ / schrittweise ✓), 3.3 RAG-Pipeline (Frage→Vektor-DB→Treffer→Modell→Antwort), 3.4 Modell + Werkzeuge über MCP-Stecker, 3.5 Agenten-Schleife (Ziel→Plan→Aktion→Beobachtung).
- [ ] **Verifikation:** Browser: alle 5 Etappen von Modul 3 öffnen → Schaubild + Check funktionieren.

---

### Task 7: Modul-Quizze + Auswertung

**Files:** Modify `ki-verstehen.html`

- [ ] **Schritt 1:** `module[1].quiz` (~6 Fragen über Modul 2) und `module[2].quiz` (~8 Fragen über Modul 3) füllen (Format `{f, opt[], korrekt, etappe}`).
- [ ] **Schritt 2:** `renderQuiz()` liest `module[state.aktuellesModul].quiz`. Auswertung: Punktzahl + Wiederholungs-Empfehlung (Etappentitel des jeweiligen Moduls). `state.quizErgebnis[modulId]` speichern. „Quiz wiederholen" + „Zur Modul-Übersicht".
- [ ] **Verifikation:** Browser: Quiz in Modul 2 und Modul 3 durchspielen → korrekte Auswertung + Empfehlung.

---

### Task 8: Feinschliff, Responsive & Endabnahme

**Files:** Modify `ki-verstehen.html`

- [ ] **Schritt 1:** CSS für Modul-Karten (falls nötig) ergänzen; Orange sparsam; Footer-Text ggf. von „(Teil 1)" auf „(Teil 1–3)" anpassen.
- [ ] **Schritt 2:** Responsive prüfen (mobil/Tablet): Karten, Schaubilder, Quiz brechen sauber um.
- [ ] **Schritt 3:** Persistenz-Test: Etappen in Modul 2/3 abhaken, neu laden → Stand + „Weiter wo du warst" korrekt (Modul + Etappe).
- [ ] **Schritt 4:** Regression Modul 1: 6 Etappen, roter Faden, Wissensnetz, Modul-1-Quiz weiterhin ok. Konsolen-Check: keine Fehler.
- [ ] **Verifikation:** Voller Durchlauf Start → Modul 2 (4 Etappen + Quiz) → Modul 3 (5 Etappen + Quiz) → Modul 1 (Regression). Screenshots Desktop + mobil.

---

## Self-Review (Plan ↔ Spec)

- Spec 2 (Modul-Struktur, Router, State v2, Resume, Faden/Netz bei Modul 1) → Task 1,2,3,4 ✓
- Spec 3.1 Startseite (Module) → Task 3 ✓
- Spec 3.2 Modul-Übersicht → Task 4 ✓
- Spec 3.3 Lernseite/„Verstanden" → Task 4 ✓
- Spec 3.4 Modul-Quiz → Task 7 ✓
- Spec 4 (Modul 2, 4 Etappen + Schaubilder) → Task 5 ✓
- Spec 5 (Modul 3, 5 Etappen + Schaubilder) → Task 6 ✓
- Spec 7 Erfolgskriterien → Task 8 ✓

Funktions-/State-Namen konsistent: `module`, `istErledigt(m,e)`, `setErledigt(m,e)`, `modulFortschritt(m)`, `state.aktuellesModul`, `state.letzteStelle={m,e}`, `state.quizErgebnis[modulId]`, `schaubild(m,e)`, `renderStart/renderModul/renderEtappe/renderQuiz`. Keine Platzhalter.
