# Spezifikation: Lern-App „KI verstehen" — Phase 1 (Grundlagen)

**Datum:** 2026-06-01
**Status:** Konzept freigegeben, bereit für Umsetzung

---

## 1. Ziel & Zweck

Eine interaktive Lern-App, die KI-Grundwissen zuerst **grafisch und strukturiert vermittelt**
und das Gelernte anschließend **interaktiv abprüft**. Lernlogik in drei Stufen:

> **verstehen → verknüpfen → abprüfen**

Quelle des Inhalts: `KI-Wissensbasis.md`, Teil 1 (Grundlagen), Kapitel 1–6.
Die Vertiefung (`KI-Wissensbasis-Vertiefung.md`) und die restlichen Teile bleiben späteren Phasen vorbehalten.

## 2. Technische Form

- **Eine einzige, eigenständige HTML-Datei** (`ki-verstehen.html`), per Doppelklick im Browser zu öffnen.
- Reines **HTML + CSS + Vanilla-JavaScript**, Schaubilder als **Inline-SVG**.
- **Keine externen Bibliotheken / kein CDN / keine Internetverbindung nötig** → offline, dauerhaft lauffähig, leicht zu sichern und zu teilen.
- **Lernfortschritt + „Weiter wo du warst"** wird im Browser via `localStorage` gespeichert (siehe 3.6).
- **Responsive**: nutzbar auf Desktop und Mobil.
- **Corporate Design NIVAO** (CD v2.1):
  - Leitfarben: Muted Orange `#D97706` (nur Akzente, max. 10–15 % der Fläche), Technical Olive `#2D362E` (Überschriften, dunkle Flächen).
  - Stützfarben: Graphite Gray `#4B5563` (Fließtext), Medium Gray `#9CA3AF` (Labels), Light Gray `#F3F4F6` (Kartenflächen), Weiß (Hintergrund).
  - Schrift (Single-Font-Mandat): Font-Stack `Arial, 'Liberation Sans', sans-serif`. Hierarchie nur über Größe/Weight/Farbe.
  - Logo: Pulse-v6-Brand-Mark als **Inline-SVG** (aus `logo_primary.svg`) + NIVAO-Wortmarke als **Base64-PNG** (`lockup_primary_transparent.png`) — keine externen Dateien, voll offline. Wortmarke wird NIE als HTML-Text nachgebaut.
  - Favicon aus `05_Favicon/` als Base64 eingebettet.
  - Tonalität: kurze Sätze, klar, bodenständig.

## 3. Struktur & Komponenten

### 3.1 Lernpfad-Startseite (Übersicht)
- Zeigt die 6 Etappen als Pfad-/Kartenansicht.
- Fortschrittsanzeige: erledigte Etappen, aktueller Stand.
- Einstieg in jede Etappe per Klick; Sprung zum Abschlussquiz, wenn alle erledigt.

### 3.2 Lernseite je Etappe (6×, einheitlicher Aufbau)
1. **Schaubild** (Inline-SVG, individuell pro Thema) — das Kernstück.
2. **Kernsatz** — die Essenz in einem Satz.
3. **Erklärung** in Stichpunkten (aus der Prosa der Wissensbasis destilliert).
4. **Merkbild / Analogie** (z. B. Bibliothek für Query/Key/Value).
5. **Mini-Selbstcheck**: 1–2 Fragen mit sofortigem Feedback (richtig/falsch + kurze Erklärung).
6. **„Verstanden"-Button** → Etappe abgehakt, Navigation zur nächsten Etappe.

### 3.3 Abschluss-Gesamtquiz
- Fragen über alle 6 Etappen hinweg (Auswahl/Erweiterung des Selbsttest-Katalogs aus der Wissensbasis).
- Auswertung am Ende: Punktzahl + Hinweis, welche Etappen zur Wiederholung empfohlen sind.
- Wiederholbar.

### 3.4 Wissensnetz (Abschluss-Ansicht)
- Visualisiert die Zusammenhänge zwischen den Begriffen
  (z. B. Next-Token-Prediction → Halluzination → RAG; Embeddings → semantische Suche).

### 3.5 Navigation
- Jederzeit zurück zur Startseite/Übersicht.
- Vor/Zurück zwischen Etappen.

### 3.6 Der rote Faden — Synthese-Ansicht (NEU, schließt die Zusammenhangs-Lücke)
- Eigene Ansicht **nach** den 6 Etappen und **vor** dem Abschlussquiz.
- Zeigt die 6 Konzepte als **eine durchgehende Kette**: *Wie aus deiner Eingabe eine Antwort wird.*
  - Eingabe (Text) → **Tokens** (Kap. 2) → je Token ein **Embedding** (Kap. 5) → **Transformer/Attention** gewichtet Bezüge (Kap. 6) → **Next-Token-Prediction** erzeugt Antwort Token für Token (Kap. 3) → Ausgabe.
  - Eingeordnet: **Parameter/MoE** (Kap. 4) = das „geronnene Wissen", das in jedem Schritt wirkt; **Begriffspyramide** (Kap. 1) = der Rahmen darüber.
- Begründung: Die Quelldateien erklären jedes Konzept einzeln, aber **nie die Kette als Ganzes**. Genau diese Verbindung ist nötig, um die Zusammenhänge zu begreifen. Inhaltlich ist das eine **Synthese vorhandenen Wissens**, keine neue Faktenbehauptung.

### 3.7 „Weiter wo du warst" (Wiedereinstieg)
- Beim Öffnen prüft die App den gespeicherten Stand (`localStorage`).
- Gibt es einen Stand, erscheint oben ein deutlicher Button **„Weiter wo du warst → Etappe N"**, der direkt zur zuletzt offenen Etappe (bzw. zum zuletzt offenen Schritt) springt.
- Gespeichert werden: zuletzt geöffnete Etappe, abgehakte Etappen, Quiz-Ergebnis(se).
- Zusätzlich pro Etappe ein dezenter Hinweis „zuletzt hier" in der Übersicht.
- Reset-Möglichkeit: ein „Fortschritt zurücksetzen"-Link (mit Rückfrage), falls von vorn begonnen werden soll.

## 4. Die 6 Etappen (Inhalt & Schaubild)

| # | Kapitel (Quelle) | Kernidee | Schaubild |
|---|------------------|----------|-----------|
| 1 | Begriffspyramide KI/ML/DL/GenAI | klare Hierarchie von weit zu eng | verschachtelte Kreise/Ebenen |
| 2 | Tokens & Tokenisierung | Modelle denken in Token-Bausteinen, nicht in Wörtern | Wort zerfällt sichtbar in Tokens |
| 3 | Next-Token-Prediction | Kern: nächstes Token vorhersagen, autoregressiv | Kette/Fließband Token→Token |
| 4 | Parameter & Modellgröße (MoE) | Parameter = „geronnenes Wissen"; MoE aktiviert nur Teile | Stellschrauben + aktive Experten |
| 5 | Embeddings & Vektorräume | Bedeutung wird zu Geometrie (Nähe = Ähnlichkeit) | Punkte im Raum, König–Königin |
| 6 | Transformer & Attention | Attention gewichtet relevante Bezüge im Text | Satz mit hervorgehobenen Bezügen |

**Ergänzte Verbindungs-Bausteine (kleine, gezielte Erweiterungen für die Zusammenhänge):**
- In Etappe 5 wird der bisher implizite Schritt **„jedes Token wird in seinen Embedding-Vektor übersetzt"** explizit gemacht — so wird klar, *wie* ein Token überhaupt ins Modell gelangt.
- Die Verbindung **Next-Token-Prediction → Halluzination** (im Quelltext angelegt) wird im Wissensnetz und im roten Faden sichtbar gemacht.
- Diese Ergänzungen synthetisieren vorhandenes Wissen; es werden keine neuen Fakten erfunden.

## 5. Bewusst außerhalb von Phase 1 (YAGNI)

- Vertiefungsinhalte (Datei 2, Kapitel A–K).
- Teile 2–5 der Wissensbasis (Training, Arbeiten mit Modellen, Anbieter, Praxis).
- Karteikarten mit Spaced-Repetition-Algorithmus.
- Nutzerkonten, Cloud-Sync, Mehrsprachigkeit.

→ Diese werden, falls gewünscht, als eigene spätere Phasen ergänzt.

## 6. Erfolgskriterien

- App öffnet sich ohne Setup im Browser und funktioniert offline.
- Alle 6 Etappen sind verständlich erklärt und mit einem passenden Schaubild versehen.
- Pro Etappe funktioniert der Mini-Selbstcheck (1–2 Fragen) mit Feedback.
- Die Synthese-Ansicht „Der rote Faden" zeigt die 6 Konzepte als durchgehende Kette.
- Das Abschlussquiz prüft über alle Etappen und gibt eine Auswertung.
- Fortschritt überlebt das Schließen des Browsers; „Weiter wo du warst" springt zum letzten Stand.
- Optik folgt erkennbar dem NIVAO Corporate Design (Farben, Schrift, Logo).
