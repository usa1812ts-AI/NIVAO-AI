# Lern-App „KI verstehen" — Umsetzungsplan (Phase 1)

> **Hinweis Verifikation:** Dies ist eine einzelne, eigenständige HTML-Datei (kein Build, kein Test-Framework). Statt Unit-Tests wird jede Aufgabe durch **Öffnen im Browser + Sicht-/Klick-Prüfung** verifiziert (Screenshot via Claude-Preview). Das ist hier die angemessene, einfachste Form.

**Goal:** Eine offline lauffähige HTML-Datei `ki-verstehen.html`, die KI-Grundwissen (Teil 1, Kap. 1–6) grafisch vermittelt, pro Etappe abprüft und mit einem Abschlussquiz wiederholt — im NIVAO Corporate Design, mit Fortschritts-Speicherung.

**Architecture:** Single-File-App. Ein `<div id="app">` wird per Vanilla-JS-Router (View-Switch) befüllt. Zustand (aktuelle Etappe, abgehakte Etappen, Quiz-Ergebnis) in `localStorage`. Inhalte als JS-Datenobjekt. Schaubilder als Inline-SVG. Keine externen Abhängigkeiten.

**Tech Stack:** HTML5, CSS3 (CSS-Variablen für NIVAO-Farben), Vanilla JavaScript, Inline-SVG, localStorage, Base64-eingebettete Logo-/Favicon-Assets.

**Quelle Spezifikation:** `docs/superpowers/specs/2026-06-01-ki-lern-app-design.md`
**Quelle Inhalt:** `KI-Wissensbasis.md`, Teil 1, Kapitel 1–6 (+ Glossar/Selbsttest für Quiz)

---

### Task 0: Assets vorbereiten

**Files:** keine (nur Beschaffung von Inhalten für die Einbettung)

- [ ] **Schritt 1:** Pulse-v6-Brand-Mark-SVG lesen: `~/.claude/skills/nivao-corporate-design/assets/logo/01_SVG_Brand_Mark/logo_primary.svg` → Pfad-Daten für Inline-SVG übernehmen.
- [ ] **Schritt 2:** Wortmarke als Base64: `04_Wordmark_Only/wordmark_primary_transparent.png` → `base64` erzeugen (Befehl: `base64 -i <pfad>`), Data-URI vorbereiten.
- [ ] **Schritt 3:** Favicon Base64: `05_Favicon/favicon_32.png` → Data-URI.
- [ ] **Verifikation:** Data-URIs liegen vor (nicht leer), SVG-Pfade extrahiert.

---

### Task 1: Grundgerüst + NIVAO Corporate Design

**Files:** Create `ki-verstehen.html`

- [ ] **Schritt 1:** HTML-Skelett: `<head>` mit `<title>KI verstehen</title>`, `<meta viewport>`, Favicon-Data-URI, `<style>`, `<body><header>…</header><main id="app"></main></body><script>…</script>`.
- [ ] **Schritt 2:** CSS-Variablen im `:root` setzen: `--orange:#D97706; --olive:#2D362E; --graphite:#4B5563; --gray:#9CA3AF; --light:#F3F4F6; --white:#FFFFFF;`. Font-Stack `Arial, 'Liberation Sans', sans-serif`. Basis-Typo (Größen/Weights), max-width-Container, responsive Grundlayout.
- [ ] **Schritt 3:** Header: Inline-SVG-Brand-Mark + Wortmarke-`<img>` (Base64), Orange-Trennlinie darunter. Orange nur als Akzent (≤10–15 % Fläche).
- [ ] **Schritt 4:** JS-Grundgerüst: `const state = loadState()`, `function render()` (View-Switch je `state.view`), `function navigate(view, payload)`, `saveState()`/`loadState()` gegen `localStorage` (Key `ki-verstehen-v1`).
- [ ] **Verifikation:** Datei im Browser öffnen → Header mit Logo + CD-Farben sichtbar, keine Konsolenfehler (Screenshot).

---

### Task 2: Inhalts-Datenmodell (6 Etappen)

**Files:** Modify `ki-verstehen.html` (Script-Block)

- [ ] **Schritt 1:** `const etappen = [...]` mit 6 Objekten anlegen. Pro Etappe: `id, titel, kernsatz, punkte[] (Stichpunkte), merkbild (Analogie-Text), check[] (1–2 Fragen mit Optionen + richtiger Antwort + Erklärung), svgId`.
- [ ] **Schritt 2:** Inhalte aus `KI-Wissensbasis.md` Kap. 1–6 destillieren (kurze Stichpunkte, kein Copy-Paste der Prosa). Für Etappe 5 den Schritt „jedes Token → Embedding-Vektor" explizit aufnehmen.
- [ ] **Schritt 3:** `const quizFragen = [...]` für das Abschlussquiz (Auswahl aus Selbsttest-Katalog, passend zu Kap. 1–6, als Multiple-Choice umformuliert).
- [ ] **Verifikation:** `console.log(etappen.length)` = 6; Daten vollständig (kein leeres Feld).

---

### Task 3: Lernpfad-Startseite + „Weiter wo du warst"

**Files:** Modify `ki-verstehen.html`

- [ ] **Schritt 1:** `renderStart()`: 6 Etappen als Karten/Pfad mit Nummer, Titel, Status (offen/erledigt/aktuell). Fortschrittsbalken (x/6 erledigt).
- [ ] **Schritt 2:** „Weiter wo du warst → Etappe N"-Button oben, sichtbar nur wenn gespeicherter Stand existiert; springt zu `state.letzteEtappe`.
- [ ] **Schritt 3:** Klick auf Karte → `navigate('etappe', {id})`. Button „Zum Abschlussquiz" sichtbar, wenn alle 6 erledigt.
- [ ] **Schritt 4:** „Fortschritt zurücksetzen"-Link (mit `confirm()`-Rückfrage) → leert localStorage, `render()`.
- [ ] **Verifikation:** Browser: Startseite zeigt 6 Karten + Fortschritt; Reset funktioniert; Resume-Button erscheint nach Etappenbesuch (Screenshot).

---

### Task 4: Etappen-Lernseite (Template) + Schaubilder

**Files:** Modify `ki-verstehen.html`

- [ ] **Schritt 1:** `renderEtappe(id)`: einheitlicher Aufbau — Schaubild (SVG) · Kernsatz · Stichpunkte · Merkbild · Mini-Selbstcheck · „Verstanden"-Button · Vor/Zurück + zurück zur Übersicht.
- [ ] **Schritt 2:** `svg(id)`-Funktion mit den 6 Inline-SVG-Schaubildern (je nach Spez. Tabelle Abschnitt 4): 1 verschachtelte Kreise, 2 Wort→Token-Bausteine, 3 Token-Kette, 4 Stellschrauben+aktive Experten, 5 Punkte im Raum (König–Königin), 6 Satz mit hervorgehobenem Bezug. NIVAO-Farben, schlicht.
- [ ] **Schritt 3:** Mini-Selbstcheck: Fragen rendern, Klick auf Option → Sofort-Feedback (richtig/falsch + Erklärung), Farbcodierung dezent.
- [ ] **Schritt 4:** „Verstanden"-Button → `state.erledigt[id]=true`, `state.letzteEtappe=id`, `saveState()`, weiter zur nächsten Etappe (oder zur Synthese nach Etappe 6).
- [ ] **Verifikation:** Browser: jede der 6 Etappen durchklicken → Schaubild sichtbar, Selbstcheck gibt Feedback, „Verstanden" hakt ab und navigiert (Screenshots Etappe 1, 5, 6).

---

### Task 5: Synthese „Der rote Faden"

**Files:** Modify `ki-verstehen.html`

- [ ] **Schritt 1:** `renderRoterFaden()`: horizontale/vertikale Kette als SVG/HTML — Eingabe → Tokens (K2) → Embeddings (K5) → Attention (K6) → Next-Token (K3) → Antwort; Parameter/MoE (K4) als Querbezug, Begriffspyramide (K1) als Rahmen.
- [ ] **Schritt 2:** Kurzer erklärender Satz je Glied; Hinweis-Pfeil Next-Token → Halluzination.
- [ ] **Schritt 3:** Button „Weiter zum Abschlussquiz".
- [ ] **Verifikation:** Browser: Kette vollständig und verständlich (Screenshot).

---

### Task 6: Wissensnetz

**Files:** Modify `ki-verstehen.html`

- [ ] **Schritt 1:** `renderNetz()`: einfache Knoten-Kanten-Darstellung (SVG) der Begriffe mit ihren wichtigsten Beziehungen (z. B. Embeddings→semantische Suche; Next-Token→Halluzination; Transformer→Attention).
- [ ] **Schritt 2:** Aus Startseite/Menü erreichbar.
- [ ] **Verifikation:** Browser: Netz wird ohne Überlappungschaos dargestellt (Screenshot).

---

### Task 7: Abschlussquiz + Auswertung

**Files:** Modify `ki-verstehen.html`

- [ ] **Schritt 1:** `renderQuiz()`: Fragen nacheinander oder als Liste, Multiple-Choice, Antwortauswahl speichern.
- [ ] **Schritt 2:** Auswertung: Punktzahl x/N, Markierung falscher Antworten + richtige Lösung + Erklärung, Empfehlung welche Etappe(n) zu wiederholen.
- [ ] **Schritt 3:** „Quiz wiederholen" + „zurück zur Übersicht"; Ergebnis in `state.quizErgebnis` speichern.
- [ ] **Verifikation:** Browser: Quiz durchspielen → korrekte Auswertung + Wiederholung funktioniert (Screenshot).

---

### Task 8: Feinschliff, Responsive & Endabnahme

**Files:** Modify `ki-verstehen.html`

- [ ] **Schritt 1:** Responsive prüfen (schmales Fenster/Mobil): Karten/Schaubilder brechen sauber um.
- [ ] **Schritt 2:** Konsistenz: Farben/Abstände/Orange-Sparsamkeit gemäß NIVAO; Tonalität der Texte (kurze Sätze).
- [ ] **Schritt 3:** Persistenz-Test: Etappen abhaken, Browser-Tab schließen/neu öffnen → Stand + „Weiter wo du warst" korrekt.
- [ ] **Schritt 4:** Konsolen-Check: keine JS-Fehler.
- [ ] **Verifikation:** Voller Durchlauf Start → 6 Etappen → roter Faden → Quiz; Screenshots Desktop + schmal.

---

## Self-Review (Plan ↔ Spec)

- Spec 2 (Technik/CD/Offline) → Task 0,1 ✓
- Spec 3.1 Startseite + 3.7 Resume → Task 3 ✓
- Spec 3.2 Lernseiten + Selbstcheck → Task 4 ✓
- Spec 3.3 Abschlussquiz → Task 7 ✓
- Spec 3.4 Wissensnetz → Task 6 ✓
- Spec 3.5 Navigation → Task 1,3,4 ✓
- Spec 3.6 Roter Faden → Task 5 ✓
- Spec 4 (6 Etappen + Schaubilder + Verbindungs-Bausteine) → Task 2,4,5 ✓
- Spec 6 Erfolgskriterien → Task 8 (Endabnahme) ✓

Keine Platzhalter offen; Funktions-/State-Namen konsistent (`state.erledigt`, `state.letzteEtappe`, `state.quizErgebnis`, `render*`, `navigate`).
