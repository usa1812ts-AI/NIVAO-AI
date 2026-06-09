# KI & Große Sprachmodelle — Lerninhalt (exportiert aus ki-verstehen.html)

> **Automatisch generiert** | Quelle: `ki-verstehen.html` | Stand: 2026-06-09
> Diese Datei NICHT manuell bearbeiten. Aenderungen gehoeren in `ki-verstehen.html`,
> danach `python3 export_md.py` ausfuehren, um diese Datei neu zu generieren.

**Inhalt:** 8 Module · 43 Etappen · 113 Karteikarten

---

## Lernmodule

### Modul 1: Grundlagen
*KI, Tokens, Embeddings, Attention*

#### 1.1 — Die Begriffspyramide

**Kernsatz:** KI, Machine Learning, Deep Learning und Generative KI stecken ineinander — von weit zu eng.

- Künstliche Intelligenz (KI) = Oberbegriff: jedes System, das Aufgaben löst, die sonst Intelligenz brauchen.
- Machine Learning = Teilmenge der KI: lernt Muster aus Daten statt aus festen Regeln.
- Deep Learning = Teilmenge von ML: nutzt tiefe (vielschichtige) neuronale Netze.
- Generative KI = erzeugt neue Inhalte (Text, Bild, Code, Audio). Große Sprachmodelle gehören hierher.
- Narrow AI vs. AGI: Heutige Sprachmodelle sind spezialisierte KI (Narrow AI) — brillant in Sprache, aber kein allgemeiner Geist (AGI = Artificial General Intelligence).
- Historisch: Vor dem Deep-Learning-Durchbruch dominierte regelbasierte KI (Expertensysteme). ML-Systeme lernen Muster aus Daten statt hart kodierte Regeln zu befolgen — das ist der fundamentale Paradigmenwechsel.

> 🧠 *Jedes Sprachmodell ist Generative KI, ist Deep Learning, ist ML, ist KI — aber nicht jede KI ist ein Sprachmodell.*

#### 1.2 — Tokens & Tokenisierung

**Kernsatz:** Ein Modell liest keine Wörter, sondern Tokens — kleine Textbausteine.

- Token = Textbaustein, meist ein Wortteil. "Maschinenbau" → "Maschinen" + "bau".
- Tokenisierung = der Vorgang, Text in Tokens zu zerlegen.
- Faustregel Englisch: 1 Token ≈ 0,75 Wörter ≈ 4 Zeichen.
- Deutsch ist "teurer": lange zusammengesetzte Wörter zerfallen in mehr Tokens.
- Wichtig: Kontextfenster und Kosten zählen in Tokens — nicht in Wörtern.
- Byte-Pair Encoding (BPE) ist das Standard-Tokenisierungsverfahren: startet mit Einzelzeichen und verschmilzt schrittweise die häufigsten Zeichenpaare — häufige Wörter werden ein Token, seltene zerfallen in viele.

> 🧠 *Denke in Tokens, nicht in Wörtern. Das bestimmt Kosten und Kontext.*

#### 1.3 — Next-Token-Prediction

**Kernsatz:** Im Kern sagt ein Sprachmodell immer nur das wahrscheinlich nächste Token voraus — Schritt für Schritt.

- Das Modell sagt das nächste Token voraus, hängt es an und sagt erneut voraus. Das nennt man "autoregressiv".
- Es "versteht" nicht wie ein Mensch und schlägt keine Faktendatenbank nach.
- Es berechnet Wahrscheinlichkeiten aus den Mustern, die es im Training gesehen hat.
- Folge: Halluzination. Ein flüssiger Satz kann falsch sein — das Modell optimiert auf Plausibilität, nicht auf Wahrheit.
- Das Trainingssignal ist radikal einfach: Vorhersage des nächsten Tokens auf riesigen Textmengen — daraus entstehen trotzdem Übersetzung, Logik und Code als Nebenprodukt.
- Autoregressiv heißt seriell: Das Modell erzeugt Tokens eins nach dem anderen; paralleles Erzeugen mehrerer Tokens gleichzeitig (Speculative Decoding) ist ein aktives Forschungsfeld zur Beschleunigung.

> 🧠 *Im Grunde eine sehr ausgefeilte Vervollständigungsmaschine.*

#### 1.4 — Parameter & Modellgröße

**Kernsatz:** Parameter sind die trainierten Stellschrauben — das "geronnene Wissen" des Modells.

- Parameter (Gewichte) werden im Training millionen- bis milliardenfach justiert.
- "70B" bedeutet 70 Milliarden Parameter.
- Lange galt: mehr Parameter = besser. 2026 stimmt das nur noch eingeschränkt.
- Mixture of Experts (MoE): viele spezialisierte Teilnetze, aber pro Anfrage sind nur wenige aktiv → spart Rechenleistung.
- Training = Gradientenabstieg: Bei jeder falschen Vorhersage wird gemessen, wie stark jeder Parameter zum Fehler beiträgt — dann werden alle Parameter ein kleines Stück korrigiert (Backpropagation).
- Dense vs. Sparse: Klassische Modelle aktivieren alle Parameter pro Token (dense); MoE-Modelle aktivieren nur einen Teil (sparse) — spart Rechenleistung bei gleichwertiger oder besserer Qualität.

> 🧠 *Viele Experten im Haus — aber pro Frage arbeiten nur wenige.*

#### 1.5 — Embeddings & Vektorräume

**Kernsatz:** Bedeutung wird zu Geometrie: Ähnliche Inhalte liegen als Zahlenvektoren nah beieinander.

- Embedding = Übersetzung von Text in eine Zahlenliste (Vektor) in einem hochdimensionalen Raum.
- Jedes Token wird in seinen Embedding-Vektor übersetzt — so gelangt es überhaupt ins Modell.
- Ähnliche Bedeutung → ähnliche Vektoren, die nah beieinander liegen.
- Berühmtes Beispiel: "König" − "Mann" + "Frau" ≈ "Königin".
- Ähnlichkeit misst man oft per Kosinus-Ähnlichkeit (dem Winkel zwischen Vektoren).
- Grundlage für semantische Suche (Suche nach Bedeutung) und für RAG.

> 🧠 *König − Mann + Frau ≈ Königin. Bedeutung wird rechenbar.*

#### 1.6 — Transformer & Attention

**Kernsatz:** Attention gewichtet, welche Wörter im Satz gerade füreinander wichtig sind.

- Fast alle modernen Modelle nutzen die Transformer-Architektur (2017, "Attention Is All You Need").
- Attention (Aufmerksamkeit) gewichtet die relevanten Bezüge im Text.
- Beispiel: "Der Ingenieur prüfte die Komponente, weil sie defekt war" — "sie" bezieht sich auf "Komponente".
- Die Verarbeitung läuft parallel über den ganzen Text → gut auf großen Rechenclustern.
- Das "T" in GPT steht für Transformer (Generative Pre-trained Transformer).
- Multi-Head Attention: Mehrere parallele Aufmerksamkeits-Köpfe beobachten gleichzeitig verschiedene Beziehungsarten (grammatische Bezüge, Thema, Position) — die Ergebnisse werden zusammengeführt.

> 🧠 *"sie" findet sein Bezugswort — Attention richtet den Scheinwerfer auf das Relevante.*

### Modul 2: Wie Modelle arbeiten
*Training, Kontextfenster, Temperature, Halluzinationen*

#### 2.1 — Trainingsphasen

**Kernsatz:** Ein Modell entsteht in Stufen: erst breites Wissen, dann Feinschliff, dann Werte.

- Pretraining: lernt aus riesigen Textmengen das nächste Token vorherzusagen — die teuerste Stufe, baut das Weltwissen auf.
- Fine-tuning: Nachschärfen mit kleineren, gezielten Datensätzen (z. B. Anweisungen folgen, "Instruction Tuning").
- RLHF: Menschen bewerten Antworten; das Modell lernt, hilfreichere, ehrlichere, harmlosere Antworten zu bevorzugen.
- Constitutional AI (Anthropic): Das Modell prüft sich gegen schriftliche Prinzipien (eine "Verfassung") statt nur gegen Einzelurteile.
- Direct Preference Optimization (DPO): alternatives Verfahren zur Praeferenzoptimierung — trainiert direkt auf bevorzugten und abgelehnten Antwortpaaren, ohne separates Belohnungsmodell. Nicht identisch mit RLHF, aber verfolgt aehnliche Ziele einfacher. 2026 Praxisstandard fuer Alignment.
- Wissensstichtag: Das Modell kennt nur Informationen aus seinen Trainingsdaten bis zu einem fixen Datum. Für aktuelles Wissen danach braucht es RAG oder neues Fine-tuning.

> 🧠 *Erst lesen lernen (Pretraining), dann höflich und hilfreich werden (RLHF).*

#### 2.2 — Das Kontextfenster

**Kernsatz:** Das Kontextfenster ist das Arbeitsgedächtnis — alles darin sieht das Modell, der Rest nicht.

- Gemessen in Tokens (Eingabe + Ausgabe zusammen).
- 2026 reichen Spitzenmodelle an ~1 Million Tokens — genug für ganze Dokumentensammlungen.
- Großes Fenster heißt nicht, dass alles gleich gut genutzt wird: die Mitte wird oft schlechter beachtet ("lost in the middle").
- Kein dauerhaftes Gedächtnis: standardmäßig vergisst das Modell nach der Anfrage alles wieder.
- Kosten skalieren mit dem Kontext: sehr lange Eingaben kosten proportional mehr Tokens — Context Caching senkt die Kosten, wenn dieselbe Systembeschreibung oder dasselbe Dokument wiederholt gesendet wird.
- Strategie: Wichtiges an Anfang oder Ende platzieren (nicht in der Mitte vergraben), Irrelevantes heraushalten — eine eigene Disziplin namens Context Engineering.

> 🧠 *Großer Schreibtisch — aber die Mitte gerät leicht aus dem Blick.*

#### 2.3 — Inferenz & Temperature

**Kernsatz:** Temperature regelt, wie konservativ oder kreativ das Modell beim Wählen des nächsten Tokens ist.

- Inferenz = die Nutzung des fertig trainierten Modells (Gegenteil von Training).
- Bei jedem Schritt entsteht eine Wahrscheinlichkeitsverteilung über mögliche nächste Tokens.
- Niedrige Temperature (nahe 0): deterministisch, faktentreu — wählt fast immer das wahrscheinlichste Token.
- Höhere Temperature: vielfältiger und kreativer, aber riskanter (mehr Abwegiges).
- Top-p / Top-k grenzen die Auswahl zusätzlich auf die wahrscheinlichsten Kandidaten ein.
- 2026 ist Inferenz ein erheblicher Kostenfaktor: Anbieter betreiben tausende GPUs; für eigene Deployments gibt es optimierte Frameworks wie vLLM oder llama.cpp, die den Durchsatz vervielfachen.

> 🧠 *Niedrige Temperatur für Fakten, höhere fürs kreative Schreiben.*

#### 2.4 — Halluzinationen & Grenzen

**Kernsatz:** Eine Halluzination ist ein plausibel klingender, aber falscher Output — systembedingt, kein Zufallsfehler.

- Ursachen: plausibelste Fortsetzung statt nachweislich wahrer Inhalt, lueckenhafte Trainingsdaten, fehlende Evidenz fuer seltene Fakten, unklare Prompts — Halluzinationen sind systembedingt und entstehen aus dem Zusammenspiel mehrerer Faktoren, nicht allein aus der Next-Token-Prediction.
- Gegenmaßnahmen: mit Quellen erden (RAG), Werkzeuge zum Nachschlagen (Tool Use), niedrige Temperature, schrittweises Denken.
- Weitere Grenzen: Wissensstichtag (kennt nichts nach dem Training), gelegentliche Fehler bei einfacher Logik/Arithmetik.
- Die Qualität der Antwort hängt stark von der Qualität der Eingabe ab.
- Eingebaute Selbstprüfung: Viele 2025/2026-Modelle mit Extended Thinking hinterfragen eigene Zwischenschritte — das reduziert Halluzinationen, eliminiert sie aber nicht.
- Warnzeichen: Selbstbewusster Ton ist kein Wahrheitsbeweis. Besonders prüfen: sehr spezifische Zahlen, Quellen-Zitate, Datumsangaben — diese immer gegenprüfen.
- → Vertiefung Modul 6: Wie man RAG als vollständige Pipeline mit Chunking, Re-Rankern und Evaluation aufbaut — Etappe ‚RAG als Pipeline'.

> 🧠 *Selbstbewusst vorgetragen heißt nicht wahr — wichtige Fakten gegenprüfen.*

### Modul 3: Mit Modellen arbeiten
*Prompts, Reasoning, RAG, MCP, Agents*

#### 3.1 — Prompt Engineering

**Kernsatz:** Prompt Engineering ist die Kunst, Eingaben so zu formulieren, dass nützliche Antworten herauskommen.

- Zero-Shot: Aufgabe direkt stellen, ohne Beispiele — gut für einfache, klare Aufgaben.
- Few-Shot: ein paar Beispiele mitgeben — das Modell überträgt das Muster, steuert Format und Stil.
- Rolle & Kontext vorgeben ("Du bist ein erfahrener Vertriebsingenieur …") verschiebt die Antwort in die richtige Richtung.
- Struktur vorgeben: Format, Länge, Ton — und ruhig auch Negativbeispiele ("vermeide Fachjargon").
- System-Prompt: Ein separater Rahmen, der Verhalten, Ton und Grenzen für die gesamte Konversation festlegt — typisch für Produktanwendungen und APIs, aber auch in Claude Code per CLAUDE.md.
- Praktische Faustregel: Präzise über vage, Beispiele über keine Beispiele, Schritte über Sprung. Ein guter Prompt kann Qualität vervielfachen — ohne Kosten für Training.
- Vertriebsbeispiel: 'Du bist Experte für Komponentenvertrieb im Maschinenbau. Antworte auf die folgende Kundenanfrage präzise und lösungsorientiert, maximal 5 Sätze: …' — Rolle + Kontext + Format in einem Satz.

> 🧠 *Few-Shot schlägt oft Zero-Shot — Beispiele wirken Wunder.*

#### 3.2 — Chain of Thought & Reasoning

**Kernsatz:** Schritt-für-Schritt-Denken verbessert die Trefferquote bei kniffligen, mehrstufigen Aufgaben.

- Chain of Thought (CoT): das Modell denkt in nachvollziehbaren Zwischenschritten, statt sofort zu antworten ("Lass uns Schritt für Schritt denken").
- Reasoning-Modelle sind gezielt darauf trainiert, vor der Antwort ausführlich intern zu "denken".
- 2026 bieten Anbieter abgestufte Denktiefen an — von niedrig bis sehr hoch.
- Achtung: Mehr Denken kostet mehr Tokens, Zeit und Geld. Für Einfaches reicht ein schnelles Standardmodell.
- Selbstkorrektur: Das Modell kann in Zwischenschritten auf einen Fehler stoßen und ihn korrigieren — ohne CoT hätte der Fehler die ganze Antwort vergiftet.
- Praktischer Tipp: Bei Aufgaben mit Rechenweg, Logik oder mehreren Bedingungen ist CoT sinnvoll. Nicht pauschal fuer alles — besser die passende Denktiefe waehlen und pruefen, ob Zwischenergebnisse nachvollziehbar sind. Fuer einfache Anfragen reicht ein schnelles Modell ohne CoT.
- → Vertiefung Modul 5: Wie Extended Thinking und Test-Time Compute unter der Haube funktionieren — Etappe ‚Reasoning-Mechanik'.

> 🧠 *Schmierzettel im Kopf — erst rechnen, dann antworten.*

#### 3.3 — RAG — Retrieval Augmented Generation

**Kernsatz:** RAG verbindet das Modell mit einer externen Wissensquelle — und senkt Halluzinationen, ohne neu zu trainieren.

- Vorbereitung: Dokumente in Stücke zerlegen ("Chunking"), je Stück ein Embedding, ablegen in einer Vektordatenbank.
- Retrieve: Die Frage wird zum Vektor; die Datenbank sucht per Ähnlichkeit die passendsten Textstücke (oft hybride Suche + Re-Ranker).
- Augment & Generate: Die Treffer kommen mit der Frage als Kontext ins Modell, das daraus die Antwort formuliert.
- Vorteil: Neues Wissen = einfach die Datenbank aktualisieren, kein Neutraining. Liefert zudem nachvollziehbare Quellen.
- Chunking-Strategie ist entscheidend: zu kleine Stücke verlieren Kontext, zu große verwässern die Relevanz — semantisches Chunking (Sinnabschnitte statt fester Länge) liefert bessere Treffer.
- Sicherheit: Vektordatenbanken können ein Angriffsziel sein — aus Embeddings lassen sich teils Rückschlüsse auf Originaldaten ziehen. Zugriff und Verschlüsselung wie bei normalen Datenbanken behandeln.
- Maschinenbau-Anwendung: Ein RAG-System über den Produktkatalog beantwortet Kundenanfragen zu technischen Daten, Alternativen und Verfügbarkeit — ohne manuelle Katalogsuche. Die Datenbank bleibt aktuell, wenn das PDF-Katalog-Update eingespielt wird.
- → Vertiefung Modul 6: Chunking-Strategien, Re-Ranker, Graph-RAG und Pipeline-Evaluation — Etappe ‚RAG als Pipeline'.

> 🧠 *Erst nachschlagen, dann antworten.*

#### 3.4 — Tool Use, Function Calling & MCP

**Kernsatz:** Tool Use gibt dem Modell Werkzeuge — MCP ist der einheitliche "Stecker" dafür.

- Ein Modell allein erzeugt nur Text: es kann nicht von sich aus suchen, rechnen oder Aktionen auslösen.
- Tool Use / Function Calling: Man stellt Werkzeuge bereit; das Modell entscheidet, wann es welches mit welchen Parametern aufruft.
- MCP (Model Context Protocol, Anthropic 2024): ein offener Standard für die Anbindung — "USB-C für KI".
- MCP kennt drei Bausteine: Tools (Funktionen), Resources (Datenquellen), Prompts (Vorlagen). 2026 faktischer Standard.
- Ablauf von Tool Use: Das Modell erzeugt einen strukturierten Tool-Call, der Client führt das Tool aus und gibt das Ergebnis zurück — das Modell formuliert dann die Antwort gestützt auf dieses Ergebnis.
- MCP-Oekosystem 2026: Tausende Server fuer Gmail, GitHub, Slack, Datenbanken und mehr. MCP-Server sind grundsaetzlich breiter einsetzbar — Clients koennen aber unterschiedliche Features, Transporte und Berechtigungen unterstuetzen. Kompatibilitaet stets anhand der Client-Dokumentation pruefen.
- Vertriebsanwendung: Ein MCP-Server verbindet Claude mit dem CRM (Salesforce/HubSpot). Claude liest Kundenhistorie, schlägt Folgemaßnahmen vor und trägt Gesprächsnotizen ein — direkt aus dem Chat, ohne manuelles Eintragen.
- → Praxis Modul 7: MCP konkret in Claude Code einrichten und eigene Server anbinden — Etappe ‚MCP in der Praxis'.

> 🧠 *MCP = USB-C fuer KI-Werkzeuge: breiter offener Standard, aber Client-Kompatibilitaet immer pruefen.*

#### 3.5 — Agents & Agentic Coding

**Kernsatz:** Ein Agent bekommt ein Ziel und arbeitet selbstständig in Schleifen — mehr als ein einzelner Prompt.

- Prompt Engineering = eine einzelne Frage gut formulieren. Ein Agent verfolgt ein Ziel über viele Schritte.
- Agenten-Schleife: planen → Werkzeug aufrufen → Ergebnis lesen → korrigieren → weiter, bis das Ziel erreicht ist.
- Agentic Coding: Der Agent übernimmt die Schleife aus Code schreiben, ausführen, Fehler lesen, beheben.
- Vibe Coding: schnelles, prompt-geführtes Entwickeln ohne tiefe Architekturplanung — Ziel ist sichtbarer Fortschritt, nicht zwingend sauberer Code. Gut für Prototypen und Wegwerf-Skripte; riskant bei produktivem Code ohne Tests, weil Fehler sich unsichtbar summieren.
- Strukturiertes Agentic Engineering als Gegenpol: Spezifikation → Tests schreiben → Agent implementiert → Mensch prüft. Der Unterschied: Vibe Coding lässt das Modell steuern, strukturierter Ansatz lässt den Menschen mit Spezifikation und Prüfschleife das Steuer behalten.
- Die Rolle des Menschen verschiebt sich: vom Ausführen zum Ziel setzen, Spezifizieren und Prüfen.
- HITL (Human-in-the-Loop): Bei realen, irreversiblen Folgen — Dateien löschen, E-Mails senden, Geld überweisen — immer Menschenbestätigung einbauen. Autonomie und Sicherheit in Balance halten.
- Maschinenbau-Anwendung: Ein Agent liest eine Kundenanfrage, sucht passende Produkte in der Datenbank, erstellt einen Angebotsentwurf und legt ihn im CRM an — der Vertriebsingenieur prüft, ergänzt und sendet. KI übernimmt die Routine, der Mensch die finale Entscheidung.
- → Vertiefung Modul 6: Produktionstaugliche Architekturmuster für Agenten (ReAct, Reflexion, Multi-Agent) — Etappe ‚Agenten-Architekturmuster'.

> 🧠 *Vom Ausführen zum Spezifizieren und Prüfen.*

### Modul 4: Anbieter & Praxis
*Anbieter, Modellwahl, Benchmarks, Multimodalität, Sicherheit, Praxis*

#### 4.1 — Anbieter-Überblick

**Kernsatz:** 2026 gibt es kein pauschal "bestes" Modell — das Feld ist dicht und wettbewerbsintensiv.

- Anthropic (Claude): sicherheits-fokussiert, Constitutional AI. Drei Stufen: Haiku (schnell/günstig), Sonnet (ausgewogen), Opus (am stärksten).
- OpenAI (GPT / ChatGPT): bekanntestes Consumer-Produkt; GPT-5-Familie mit einstellbaren Denktiefen.
- Google (Gemini): nativ multimodal, sehr großes Kontextfenster; treibt u. a. NotebookLM an.
- Offene & günstige Modelle (z. B. DeepSeek, Qwen, Kimi): zunehmend Spitzen-nahe Leistung zu niedrigen Kosten.
- Open-Source-Trend 2026: Meta (Llama), Mistral, DeepSeek treiben quelloffene Modelle voran — Teams können Modelle selbst hosten, was bei Datenschutz und Kosten entscheidend sein kann.
- Preisunterschiede sind enorm: Kosten pro Million Tokens variieren um Faktor 100x zwischen Modellklassen — für Batch-Verarbeitung großer Mengen gibt es noch günstigere Async-APIs.

> 🧠 *Drei große Anbieter plus starke offene Modelle — die Wahl richtet sich nach der Aufgabe.*

#### 4.2 — Das richtige Modell wählen

**Kernsatz:** Die richtige Wahl hängt von der Aufgabe ab — nicht vom Ranking.

- Aufgabentyp: Chat, langes Dokument, agentisches Programmieren, multimodale Analyse.
- Geschwindigkeit vs. Tiefe: schnelle, günstige Modelle für Häufiges; teure Reasoning-Modelle nur für harte Probleme.
- Kosten: Preis pro Million Tokens (Eingabe und Ausgabe getrennt).
- Außerdem wichtig: Kontextfenster, Datenschutz/Hosting, Ökosystem (Tools, MCP).
- Eigene Tests schlagen Benchmarks: 5–10 repräsentative Beispiele aus dem echten Anwendungsfall geben mehr Auskunft über die Eignung eines Modells als öffentliche Ranglisten.
- Anbieterbindung (Vendor Lock-in): Wer stark auf proprietäre Features setzt, riskiert Abhängigkeit. MCP und offene Standards wie OpenAI-kompatible APIs reduzieren dieses Risiko.

> 🧠 *Nicht das teuerste Modell für jede Kleinigkeit — Modellklasse zur Aufgabe wählen.*

#### 4.3 — Benchmarks & ihre Grenzen

**Kernsatz:** Benchmarks vergleichen Modelle — sind aber mit Vorsicht zu lesen.

- Benchmarks = standardisierte Testsätze (z. B. SWE-bench für Code, MMLU für breites Wissen).
- Sättigung: Spitzenmodelle erreichen nahezu perfekte Werte → der Test verliert Unterscheidungskraft.
- Daten-Kontamination: Testaufgaben gerieten ins Training → Glanz durch Erinnerung statt Können.
- Beste Praxis: der eigene, realitätsnahe Test auf den eigenen Aufgaben.
- Neue Benchmarks entstehen ständig, weil alte saturieren: SWE-bench (Software), GPQA Diamond (Wissenschaft), FrontierMath (Mathematik) sind 2026 noch unterscheidungsstark.
- LLM-as-a-Judge: Ein starkes Modell bewertet automatisiert andere — skaliert gut, hat aber Verzerrungen (Längen-Vorliebe, erstgenannte Option). Kombination aus automatischen und menschlichen Tests ist am belastbarsten.

> 🧠 *Der beste Benchmark ist dein eigener, echter Anwendungsfall.*

#### 4.4 — Multimodalität

**Kernsatz:** Multimodal heißt: ein Modell verarbeitet Text, Bild, Audio, Video und Code.

- Multimodal = mehr als Text (Bilder, Audio, Video, Code).
- Nativ multimodal = von Grund auf dafür gebaut (z. B. Gemini), statt nachträglich angekoppelt.
- Praktisch: ein Diagramm interpretieren, ein Foto zusammenfassen, gesprochene Sprache verarbeiten, ein Video analysieren — im selben Modell.
- Vertriebsanwendung: Technische Zeichnungen, Produktbilder, Schaltpläne oder Diagramme aus Katalogen können von einem multimodalen Modell gelesen und beschrieben werden — ohne manuelle Dateneingabe.
- Speech-to-Text und Text-to-Speech: Gesprochenes wird zu Text (transkribiert), Text wird zu Sprache (synthetisiert). Viele Modelle 2026 unterstützen beides nativ in einem Aufruf.
- Einschränkungen: Nicht jedes Modell verarbeitet Audio oder Video — Text/Bild-Verarbeitung ist am weitesten verbreitet; multimodale Anfragen können teurer und langsamer sein.

> 🧠 *Ein Modell, viele Sinne — Text, Bild, Ton, Video.*

#### 4.5 — Sicherheit, Datenschutz & Ethik

**Kernsatz:** Mit wachsender Leistung steigen die Risiken — Schutz ist Pflicht.

- Prompt Injection: versteckte schädliche Anweisungen in verarbeiteten Inhalten (Webseite, E-Mail). Grundregel: externe Inhalte sind Daten, keine Befehle.
- Datenschutz: keine Passwörter, Konto-/Ausweisnummern oder Gesundheitsdaten ungeschützt in Prompts oder Vektordatenbanken.
- Bias & Fairness: Modelle übernehmen Verzerrungen aus ihren Trainingsdaten.
- Schutzmaßnahmen der Anbieter: Constitutional AI, System Cards, abgestufte Freigaben.
- Datenleck-Risiko: KI-Dienste in der Cloud dürfen keine Geschäftsgeheimnisse erhalten, die nicht in fremde Hände geraten dürfen. Alternative: selbst gehostete (Open-Source-)Modelle oder On-Premise-Lösungen.
- Deepfakes & Desinformation: Generative Modelle können täuschend echte Bilder, Audios und Videos erzeugen. Provenienz-Standards (C2PA-Wasserzeichen) sollen helfen — sind 2026 aber noch kein universeller Standard.

> 🧠 *Externe Inhalte sind Daten, keine Befehle.*

#### 4.6 — Praxis-Prinzipien

**Kernsatz:** Die Essenz fürs tägliche Arbeiten mit KI — verstehen, erden, prüfen.

- Denke in Tokens, nicht in Wörtern — Kontext und Kosten richten sich danach.
- Plausibel ist nicht wahr — wichtige Fakten gegenprüfen oder das Modell erden (RAG, Tool Use).
- Wähle die Modellklasse zur Aufgabe — nicht für jede Kleinigkeit das teuerste Modell.
- Prompt-Qualität entscheidet — präzise Aufgabe, Kontext, Beispiele, Format; bei harten Aufgaben schrittweises Denken.
- Externe Inhalte sind Daten, keine Befehle — Schutz vor Prompt Injection; sensible Daten schützen.
- Versionsnummern altern schnell, Konzepte bleiben stabil. Die Rolle des Menschen: vom Ausführen zum Spezifizieren, Steuern und Prüfen.
- Vertriebsalltag: Angebote formulieren, Preisanfragen beantworten, Produktvergleiche erstellen, Kundenpräsentationen aufbereiten — KI als 24/7-Assistent für Routineaufgaben im Key Account Management. Beziehungsaufbau und strategische Entscheidungen bleiben beim Menschen.

> 🧠 *Verstehen → erden → prüfen. Der Mensch bleibt am Steuer.*

### Modul 5: Vertiefung: Mechanik
*BPE, Query/Key/Value, Backpropagation, LoRA/DPO, Reasoning*

#### 5.1 — Tokenisierung im Detail

**Kernsatz:** BPE baut das Token-Vokabular auf, indem es die häufigsten benachbarten Zeichenpaare schrittweise zusammenfasst.

- Start mit kleinsten Einheiten (Zeichen/Bytes); das häufigste Nachbarpaar wird zu einem neuen Token verschmolzen — tausendfach wiederholt.
- Häufige Wörter werden zu einem Token, seltene Fachbegriffe zerfallen in mehrere Stücke.
- Das gelernte Token-Inventar heißt Vokabular (oft 100.000–200.000 Tokens).
- Größeres Vokabular = kürzere Sequenzen, aber mehr Parameter in den Randschichten — ein Abwägungsspiel.
- Nicht-englische Sprachen und Sonderschriften (Chinesisch, Arabisch, Kyrillisch) sind token-teurer — Vokabulare wurden historisch englisch-lastig trainiert.
- Zahlen werden teils seltsam tokenisiert: '42.000' kann zu '42', '.', '000' zerfallen — ein Grundproblem bei Arithmetik in Sprachmodellen.

> 🧠 *Aus „n”+„e” wird „ne”, dann „neu” … häufige Muster werden zu einem Baustein.*

#### 5.2 — Attention-Mechanik

**Kernsatz:** Attention vergleicht die Query jedes Tokens mit allen Keys und mischt daraus die passenden Values.

- Query = „Wonach suche ich?“, Key = „Wofür bin ich relevant?“, Value = „Mein eigentlicher Inhalt“.
- Passt eine Query gut zu einem Key, fließt dessen Value stärker ins Ergebnis ein.
- Multi-Head Attention: mehrere parallele „Köpfe“ achten auf verschiedene Beziehungsarten.
- Der Aufwand wächst quadratisch mit der Textlänge — der Grund, warum lange Kontexte teuer sind.
- Self-Attention vs. Cross-Attention: Bei Self-Attention beziehen sich Tokens auf denselben Text (Normalfall); Cross-Attention verbindet zwei Sequenzen — z. B. Frage auf einen abgerufenen Kontext (RAG).
- Subquadratische Alternativen (z. B. Mamba, RWKV) wollen den Rechenaufwand grundlegend senken — 2026 noch kein klarer Nachfolger fuer die dominante Transformer-Attention. FlashAttention ist dagegen eine speichereffiziente Implementierung der exakten Attention: kein anderes Rechenverfahren, sondern eine Optimierung mit weniger GPU-Speicherzugriffen.

> 🧠 *Wie in einer Bibliothek: Anfrage (Query) trifft Schlagwort (Key), du bekommst den Inhalt (Value).*

#### 5.3 — Embeddings tiefer

**Kernsatz:** Moderne Embeddings sind kontextuell — der Vektor eines Wortes hängt vom umgebenden Satz ab.

- Ein Embedding-Vektor hat eine feste Länge (z. B. 768 oder 1.536); jede Dimension ist eine gelernte „Bedeutungsachse“.
- Positionskodierung (z. B. rotierende Positionskodierung, kurz RoPE = Rotary Position Embedding) gibt dem Modell die Wortstellung — Attention allein ist reihenfolgeblind.
- Statische Embeddings gaben „Bank” immer denselben Punkt; kontextuelle unterscheiden Geldinstitut und Sitzbank je nach Satz.
- Ähnlichkeit als Winkel: Kosinus-Ähnlichkeit misst den Winkel zwischen zwei Vektoren — kleiner Winkel = ähnliche Bedeutung. Das macht Bedeutungsvergleiche rechenbar.
- Spezialisierte Embedding-Modelle: Für Ähnlichkeitssuche sind dedizierte Embedding-Modelle (z. B. text-embedding-3-large) oft besser geeignet als allgemeine Sprachmodelle.
- Praktische Einsätze: semantische Dokumentensuche, Ähnlichkeits-Matching (welcher Artikel passt zur Anfrage?), Duplikat-Erkennung, Clustering verwandter Texte — all das nutzt Embeddings.

> 🧠 *„Bank” liegt je nach Satz woanders im Raum — Bedeutung hängt vom Kontext ab.*

#### 5.4 — Wie Training wirklich abläuft

**Kernsatz:** Lernen heißt: Fehler messen, den Gradienten berechnen und die Parameter ein Stück Richtung kleinerer Fehler verschieben — millionenfach.

- Die Verlustfunktion (Loss, oft Cross-Entropy) misst, wie falsch eine Vorhersage war.
- Backpropagation berechnet, wie stark jeder Parameter zum Fehler beiträgt → ergibt den Gradienten.
- Gradientenabstieg verschiebt die Parameter ein kleines Stück; die Lernrate ist die Schrittgröße.
- Begleiterscheinungen: Overfitting (memorieren statt verallgemeinern), Catastrophic Forgetting, Scaling Laws.
- Skalierungsgesetze (Scaling Laws): empirisch beobachtet — mehr Daten, mehr Parameter, mehr Rechenleistung → höhere Qualität nach vorhersagbaren Kurven. Prägte die Strategie "größer ist besser" — 2026 durch effiziente Architekturen relativiert.
- Chinchilla-Gesetz (Hoffmann et al. 2022): compute-optimales Training erfordert gleichmäßige Skalierung von Parametern und Daten. GPT-3 hatte zu viele Parameter bei zu wenig Daten. Chinchilla (70 Mrd. Parameter, 1,4 Bio. Tokens) schlug 280-Mrd.-Modelle — Datenmenge ist genauso wichtig wie Modellgröße.
- Emergente Fähigkeiten: Bei bestimmten Skalierungsschwellen tauchen Fähigkeiten scheinbar plötzlich auf — z. B. Few-Shot-Reasoning, Arithmetik, mehrsprachige Übersetzung ohne explizites Training. Debatte: echte Emergenz oder Artefakt der Messmetrik? Praxisrelevanz: neue Modellgenerationen können unerwartet neue Fähigkeiten mitbringen.
- Catastrophic Forgetting: Wenn ein Modell auf neuen Daten nachtrainiert wird, kann es älteres Wissen überschreiben — ein zentraler Grund für vorsichtiges, schrittweises Fine-tuning.

> 🧠 *Das Modell tastet sich in einer Fehlerlandschaft bergab ins Tal.*

#### 5.5 — Fine-tuning-Verfahren

**Kernsatz:** Fine-tuning formt Stil und Verhalten — neue Fakten liefert man besser per RAG.

- Supervised Fine-Tuning (SFT): Training auf (Eingabe, idealer Ausgabe)-Paaren — die Grundform.
- Low-Rank Adaptation (LoRA): friert die Gewichte ein und fügt nur kleine, trainierbare Adapter ein → ein Bruchteil der Parameter bei vergleichbarer Qualität (QLoRA = LoRA + Quantisierung).
- Direct Preference Optimization (DPO): vereinfachtes Alignment ohne separates Belohnungsmodell — 2026 Praxisstandard (statt klassischem Reinforcement Learning from Human Feedback / Proximal Policy Optimization).
- Faustregel: wenige hundert sehr saubere Beispiele schlagen Zehntausende schlampige.
- Wann Fine-tuning, wann RAG? Fine-tuning formt Stil, Format und Verhalten — RAG liefert aktuelles Faktenwissen. Meist sinnvoll: zuerst RAG testen, dann Fine-tuning falls nötig.
- LoRA-Adapter sind portabel: Das Ergebnis ist eine kleine Adapter-Datei (oft nur wenige Megabyte), die auf das Basismodell aufgeladen wird — kein neues Vollmodell nötig.
- → Grundlagen Modul 3: Wann RAG die bessere Alternative zu Fine-tuning ist — Etappe ‚RAG — Retrieval Augmented Generation'.

> 🧠 *Stil/Format/Verhalten → Fine-tuning. Neue Fakten → RAG.*

#### 5.6 — Reasoning-Mechanik

**Kernsatz:** Mehr „Nachdenken“ heißt mehr Rechenzeit zur Antwortzeit — das Modell nutzt Zwischenschritte als Arbeitsspeicher.

- Test-Time Compute: durch viele Zwischen-Tokens verschafft sich das Modell mehr Rechenschritte — wie ein Schmierzettel.
- Reasoning-Modelle werden mit bestärkendem Lernen an überprüfbaren Aufgaben (Mathe, Code) trainiert.
- Ein großer Teil des Fortschritts ist erlernte Chain-of-Thought-Arbeitsweise, weniger „echtes Verstehen“.
- Grenzen: mehr Tokens/Zeit/Geld; „Overthinking” kann Antworten sogar verschlechtern.
- Extended Thinking (Anthropic): Claude generiert interne Gedankenketten, die der Nutzer optional einsehen kann — transparent nachvollziehbares Denken statt Black Box.
- Best-of-N Sampling: Das Modell erzeugt mehrere Antworten parallel und wählt die beste — eine einfache Form von Test-Time Compute, die ohne spezielles Reasoning-Training auskommt.

> 🧠 *Schmierzettel im Kopf: Zwischenschritte sind zusätzlicher Arbeitsspeicher.*

### Modul 6: Vertiefung: Systeme & Praxis
*RAG-Pipeline, Agenten-Muster, Context Engineering, Inferenz, Evaluation*

#### 6.1 — RAG als Pipeline

**Kernsatz:** Jeder Schritt der RAG-Pipeline ist eine eigene Qualitätsstellschraube.

- Chunking: zu kleine Stücke verlieren Zusammenhang, zu große verwässern die Relevanz; Überlappung und semantisches Chunking helfen.
- Retrieval: hybride Suche (Bedeutung + exakte Stichwörter) plus ein Re-Ranker, der nach echter Relevanz sortiert.
- Augmentation: zu viel Kontext löst „lost in the middle“ aus, zu wenig lässt Lücken.
- Fortgeschritten: Graph-RAG (Wissensgraphen) und Agentic RAG (ein Agent steuert die Suche).
- Sicherheitshinweis: Vektordatenbanken können Angriffsziel sein — aus Embeddings lassen sich teils Rückschlüsse auf Originaldaten ziehen. Zugriff und Verschlüsselung wie bei normalen Datenbanken behandeln.
- Evaluation der Pipeline: Retrieval-Qualität (findet die Suche die richtigen Stücke?) und Generation-Qualität (nutzt das Modell sie richtig?) müssen getrennt gemessen werden.

> 🧠 *Gute RAG-Qualität entsteht an jeder Stufe — vor allem beim Chunking und Re-Ranking.*

#### 6.2 — Agenten-Architekturmuster

**Kernsatz:** Produktions-Agenten kombinieren Muster wie ReAct, Reflexion, Planung und Multi-Agent — je nach Engpass.

- ReAct (Reasoning + Acting): Schleife aus Thought → Action (Werkzeug) → Observation; Schwäche: Kohärenzverlust bei sehr langen Läufen.
- Reflection: expliziter Selbstkritik-Schritt; auf 2–3 Versuche begrenzen, sonst „oszilliert“ der Agent.
- Plan-and-Execute: erst kompletter Plan, dann Ausführung (braucht Checkpoints). Multi-Agent: ein Orchestrator verteilt an spezialisierte Worker.
- Viele Produktionsfehler 2024–2026 waren Architektur-, keine Modellfehler. Human-in-the-Loop bei realen Folgen.
- Werkzeugwahl ist Architekturentscheidung: Welche Tools darf der Agent nutzen? Zu viele erhöhen das Risiko falscher Aufrufe; zu wenige beschränken die Leistung — bewusst begrenzen.
- Observability: In Produktion jeden Schritt protokollieren (LLM-Aufruf, Tool-Call, Ergebnis) — ohne Logs ist Fehlerdiagnose in Agenten-Systemen sehr schwer.
- Autonome Agenten (Fully Autonomous): laufen ohne menschliche Eingriffe über Stunden — Computer Use, autonomes Coding (z. B. SWE-bench-Szenarien), Web-Research-Pipelines. 2025/2026: zuverlässig bei klar abgegrenzten, gut spezifizierten Aufgaben; fehleranfällig bei Mehrdeutigkeit und unbekannten Ausnahmesituationen.
- Trust Levels: Anthropic unterscheidet Operator (hat das System gebaut und konfiguriert), User (interagiert im Gespräch) und Agent (handelt stellvertretend für den User). Ein autonomer Agent erbt die Vertrauensstufe des Users, nicht des Operators — begrenzt, was er darf, und schützt vor Privilege Escalation.

> 🧠 *Mit dem Muster beginnen, das den größten Engpass löst — nicht alle auf einmal.*

#### 6.3 — Context Engineering

**Kernsatz:** Context Engineering gestaltet den gesamten Kontextinhalt — bei Agenten oft wichtiger als der einzelne Prompt.

- Kontext-Budget: das Fenster ist endlich und token-teuer — was kommt rein (Systemanweisung, RAG-Treffer, Verlauf, Werkzeuge)?
- Kontext-Kompression: lange Verläufe zusammenfassen statt vollständig mitschleppen.
- Reihenfolge gegen „lost in the middle“: Wichtiges an Anfang oder Ende.
- Kontext-Hygiene: Irrelevantes/Veraltetes raushalten; externe Inhalte sind Daten, keine Befehle.
- Prompt-Caching: Wiederholte, identische System-Prompts oder Dokumente können gecacht werden — spart bis zu 90 % Kosten für den unveränderlichen Teil des Kontexts.
- Memory-Management: Externe Gedächtnissysteme (episodisches Gedächtnis, Faktengedächtnis) ergänzen das endliche Kontextfenster — gespeicherte Fakten werden bei Bedarf ins Fenster geladen.

> 🧠 *Nicht nur die Frage zählt, sondern was insgesamt im Fenster steht.*

#### 6.4 — Inferenz-Optimierung

**Kernsatz:** Quantisierung, KV-Caching und Destillation machen große Modelle im Betrieb schnell und billig.

- Quantisierung: Parameter mit weniger Bit speichern (z. B. 4 statt 16) → kleiner und schneller, meist nur geringer Qualitätsverlust; ermöglicht Modelle auf Laptops.
- KV-Caching: bereits berechnete Keys/Values zwischenspeichern → macht die Token-für-Token-Erzeugung praktikabel; Context Caching senkt Kosten wiederholter Anfragen.
- Destillation: ein großes Lehrer-Modell bringt einem kleinen Schüler-Modell sein Verhalten bei.
- Mixture-of-Experts (MoE)-Routing aktiviert nur die nötigen Experten pro Token.
- Speculative Decoding: Ein kleines Entwurfsmodell sagt mehrere Tokens voraus; das große Modell prüft und akzeptiert oder korrigiert in einem Schritt — oft deutlich schnellere Ausgabe.
- Batching: Mehrere Anfragen parallel auf derselben GPU abarbeiten erhöht den Durchsatz — typischer Trade-off im API-Betrieb: mehr Gesamt-Throughput, aber höhere individuelle Latenz.

> 🧠 *Kleiner rechnen (Quantisierung), nicht doppelt rechnen (Caching), schlanker nachbauen (Destillation).*

#### 6.5 — Evaluation

**Kernsatz:** Sinnvoll evaluieren heißt vor allem: ein eigener, realitätsnaher Testsatz auf den echten Aufgaben.

- LLM-as-a-Judge: ein starkes Modell bewertet die Ausgaben eines anderen — skaliert gut, hat aber Verzerrungen (Längen-Vorliebe, erstgenannte Option, eigener Stil).
- Gegen Daten-Kontamination: frische, nachweislich neue Testaufgaben verwenden.
- Eigene Evals sind am aussagekräftigsten — vor und nach jeder Änderung gegen denselben Satz messen.
- Bei Agenten: den ganzen Pfad bewerten (richtige Werkzeuge? unnötige Schleifen?), Observability.
- Eval-Regression: Nach jeder Modell- oder Prompt-Änderung denselben Eval-Satz laufen lassen — Verbesserungen an einer Stelle können Rückschritte an anderer Stelle verursachen.
- Human Eval als Goldstandard: Automatisierte Evals sind skalierbar; für die finale Entscheidung sind qualitative menschliche Urteile unverzichtbar — besonders bei offenen, kreativen Aufgaben.

> 🧠 *Der eigene, realitätsnahe Eval-Satz schlägt jedes öffentliche Ranking.*

### Modul 7: KI-Tools im Alltag
*Claude Code, Skills, Hooks, Subagents, MCP, Sicherheit*

#### 7.1 — Claude Code & das CLI

**Kernsatz:** Claude Code ist ein agentic coding tool im Terminal — es liest Code, schreibt ihn, führt ihn aus und arbeitet selbstständig in Schleifen.

- CLI (Command-Line Interface, dt. Kommandozeilen-Interface): das Terminal ist das Eingabefenster — keine grafische Oberfläche, dafür direkte Systemzugriffe.
- Unterschied zu Chat-Interfaces: Claude Code hat Zugriff auf dein Dateisystem, kann Shell-Befehle ausführen, liest und schreibt Dateien — weit mehr als ein Gespräch.
- Agentic Loop: Aufgabe erhalten → Kontext lesen → planen → Dateien lesen/schreiben → ausführen → Ergebnis prüfen → korrigieren — in Schleifen, bis das Ziel erreicht ist.
- Sessions: Jede Konversation ist eine eigene Session; Claude Code merkt sich Kontext innerhalb der Session, nicht dauerhaft.
- Ideal für: Code refaktorieren, Bugs finden, neue Features umsetzen, Dokumentation schreiben — alles direkt in deiner eigenen Codebase.
- Plan-Modus: Bevor Claude Code handelt, kann es einen detaillierten Plan vorlegen, den du genehmigst — wichtig für komplexe Aufgaben mit vielen Dateien oder irreversiblen Schritten.

> 🧠 *Nicht 'Frag die KI' — sondern 'Gib der KI Zugriff auf dein Werkzeug'.*

#### 7.2 — Skills & Anpassung

**Kernsatz:** Skills sind wiederverwendbare Verhaltensanweisungen — einmal als Markdown-Datei definiert, per Slash-Befehl abrufbar.

- Ein Skill ist eine Markdown-Datei mit Anweisungen, die Claude Code bei Bedarf lädt und ausführt.
- Slash-Befehle (/skill-name): statt jeden Prompt neu zu schreiben, rufst du den fertigen Skill auf — z. B. /commit, /code-review, /debug.
- Globale Skills (~/.claude/skills/): gelten für alle Projekte. Projekt-Skills (.claude/skills/ im Projektordner): nur für das aktuelle Projekt.
- CLAUDE.md: eine spezielle Datei, die Claude die Spielregeln des Projekts erklärt (Coding-Konventionen, Verhaltensregeln, Grenzen).
- Skills sollten klar erklären, warum eine Regel gilt, nicht nur was zu tun ist — das hilft Claude bei unklaren Randfällen.
- Memory-System: Claude Code kann Erkenntnisse aus Gesprächen persistent in Markdown-Dateien speichern — so wächst über Zeit ein Gedächtnis über Präferenzen, Projekte und Kontext.

> 🧠 *Einmal definiert, immer abrufbar — dein persönlicher KI-Assistent nach Maß.*

#### 7.3 — Hooks & Automatisierung

**Kernsatz:** Hooks sind Shell-Befehle, die der Harness (das Claude-Code-Framework) automatisch bei bestimmten Ereignissen ausführt.

- Ein Hook ist an ein Ereignis gebunden: z. B. PreToolUse (vor einem Werkzeug-Aufruf), PostToolUse (danach) oder Stop (wenn Claude fertig ist).
- Konfiguriert in der settings.json-Datei: welcher Hook, auf welches Ereignis, für welche Tools.
- Beispiele: nach jeder Datei-Bearbeitung automatisch Prettier ausführen, Benachrichtigung auslösen wenn Claude fertig ist, Sicherheitsprüfung vor Shell-Befehlen.
- Wichtig: Den Harness führt Hooks aus — nicht Claude selbst. Claude sieht das Ergebnis und kann darauf reagieren.
- Hooks sind auditierbar: die Befehle stehen klar in der Konfiguration und sind transparent nachvollziehbar.
- Sicherheits-Hooks: Vor bestimmten Shell-Befehlen kann ein Hook eine Prüfung auslösen — z. B. um zu verhindern, dass Claude unbeabsichtigt sensible Dateien überschreibt oder löscht.

> 🧠 *Hooks = automatische Bewachter — der Harness handelt, ohne dass du eingreifen musst.*

#### 7.4 — Subagents & parallele Arbeit

**Kernsatz:** Subagents sind separate Claude-Instanzen für Teilaufgaben — parallel arbeitend, unabhängig vom Hauptagenten.

- Dispatching: der Hauptagent (Orchestrator) teilt eine große Aufgabe auf und delegiert Teile an Subagents.
- Parallelisierung: mehrere Subagents arbeiten gleichzeitig — z. B. sechs Dateien gleichzeitig refaktorieren statt nacheinander.
- Jeder Subagent startet 'kalt' ohne Gedächtnis der Hauptkonversation → der Prompt muss vollständig eigenständig und selbsterklärend sein.
- Worktrees: für isolierte Arbeit kann jeder Subagent auf einem eigenen Git-Branch in einem eigenen Verzeichnis arbeiten.
- Vorteil: drastisch schnellere Ergebnisse bei unabhängigen Teilaufgaben; klare Verantwortungstrennung.
- Kosten-Bewusstsein: Jeder Subagent ist ein eigener API-Aufruf. Parallelisierung beschleunigt, erhöht aber Kosten — sinnvoll bei zeitkritischen, wirklich unabhängigen Aufgaben, nicht für jede Kleinigkeit.

> 🧠 *Ein Orchestrator delegiert — jeder Subagent bekommt eine klare, eigenständige Aufgabe.*

#### 7.5 — MCP in der Praxis

**Kernsatz:** MCP-Server (Model Context Protocol-Server) sind die Brücken zwischen Claude und der Außenwelt — jede Verbindung bringt neue Fähigkeiten.

- Ein MCP-Server stellt Tools (Funktionen), Resources (Datenquellen) und Prompts (Vorlagen) für Claude bereit.
- Beispiel Gmail-MCP-Server: Claude kann E-Mails lesen, Labels setzen, Entwürfe erstellen — ohne manuellen Zwischenschritt.
- Beispiel Google Drive: Dateien suchen, lesen und organisieren — direkt aus Claude Code heraus.
- Konfiguration: den Server in claude_desktop_config.json oder der Claude-Code-Einstellung eintragen — dann ist er sofort verfügbar.
- Sicherheit: MCP-Server haben Zugriff auf echte Systeme — nur vertrauenswürdige Server einbinden; Berechtigungen auf das Nötigste begrenzen.
- MCP-Ökosystem 2026: Tausende öffentliche Server (GitHub, Slack, Notion, Datenbanken etc.). Suche im MCP-Registry oder nutze die offiziellen Server der Dienste direkt als Ausgangspunkt.

> 🧠 *Jeder MCP-Server gibt Claude neue Fähigkeiten — aber mit Zugriff kommt Verantwortung.*

#### 7.6 — Sicherheit & Best Practices

**Kernsatz:** Je mehr ein Agent tun kann, desto wichtiger ist klare Kontrolle — Human-in-the-Loop, reversible Aktionen und minimale Berechtigungen.

- Reversible vs. irreversible Aktionen: Dateien editieren ist reversibel (git revert möglich); git push --force, Datei löschen oder E-Mail senden sind es nicht.
- Human-in-the-Loop (HITL): kritische, irreversible Aktionen immer zuerst bestätigen lassen — nicht alles autonom ausführen.
- Minimales Berechtigungsprinzip (Principle of Least Privilege): Claude nur den Zugriff geben, den es wirklich braucht.
- Prompt Injection in agentic Systemen: wenn Claude Webseiten oder E-Mails liest, können versteckte Anweisungen darin stecken — externe Inhalte immer als Daten, nicht als Befehle behandeln.
- CLAUDE.md als Sicherheitsnetz: Verhaltensregeln und Grenzen schriftlich festlegen — Claude hält sich daran.
- Auditierbarkeit: Alle Aktionen von Claude Code (Datei-Edits, Shell-Befehle, Tool-Calls) sind im Transcript sichtbar. Bei sensiblen Projekten Logs aufbewahren und regelmäßig überprüfen.

> 🧠 *Prüfe vor dem Ausführen: Ist diese Aktion umkehrbar? Wenn nicht — erst fragen.*

### Modul 8: Dateien, Formate & Werkzeuge
*ASCII, JSON, HTML, Python, Mockup & Co.*

#### 8.1 — Wie KI Text liest

**Kernsatz:** Klassische Sprachmodelle verarbeiten ausschliesslich Text. Multimodale Modelle wie aktuelle Claude-Versionen akzeptieren zusaetzlich Bilder, PDFs und weitere Formate — intern werden alle Eingaben in Modell-Repraesentationen umgewandelt. ASCII ist das Fundament, UTF-8 der heutige Standard.

- ASCII (American Standard Code for Information Interchange): kodiert 128 Zeichen als Zahlen 0-127. Das Zeichen A hat den Wert 65, { den Wert 123. Jeder Buchstabe in Code, JSON oder Shell-Befehlen ist eine ASCII-Zahl.
- Unicode / UTF-8: Erweiterung von ASCII auf alle Sprachen der Welt (ue, e-Akzent, CJK-Zeichen, Emojis). UTF-8 ist der Standard in Editoren, Terminals und KI-Tools. Fehler entstehen, wenn Kodierungen gemischt werden.
- .txt-Datei: Reiner Text ohne Formatierung — fuer LLMs das idealste Format. Claude liest .txt-Dateien direkt, ohne Konvertierungsschritt.
- Markdown / .md: Textdatei mit einfacher Formatierung. # fuer Ueberschriften, **fett**, - fuer Listen. CLAUDE.md ist eine Markdown-Datei.
- CLAUDE.md: Spezielle Markdown-Datei im Projektordner. Wird beim Start jeder Claude-Code-Sitzung automatisch in den Kontext geladen — als Hinweise, nicht als erzwungene Konfiguration. Fuer strikte Blockaden sind PreToolUse-Hooks der richtige Weg.
- .csv (Comma-Separated Values): Tabellarische Daten als Textdatei, Spalten durch Komma getrennt. LLMs und Python-Scripts lesen CSV direkt — kein Excel noetig.

> 🧠 *Text bleibt das einfachste Format. Moderne multimodale Modelle verarbeiten auch Bilder und PDFs direkt — intern wird jede Eingabe in Modell-Repraesentationen umgewandelt.*

#### 8.2 — Strukturierte Daten & Kommunikation

**Kernsatz:** Claude spricht JSON — bei Tool Use, MCP-Calls und API-Kommunikation ist JSON das universelle Austauschformat zwischen KI und Werkzeugen.

- JSON (JavaScript Object Notation): Leichtgewichtiges Textformat fuer strukturierte Daten. Syntax: {"schluessel": "wert"}, Arrays: [1, 2, 3], Boolean: true/false. Jede Claude-Antwort mit Tool Use kommt als JSON.
- JSON-Struktur: Objekte beginnen mit { und enden mit }. Strings stehen in geraden doppelten Anfuehrungszeichen. Ein fehlendes Komma oder ein falsch kodiertes Zeichen als Delimiter bricht das gesamte JSON.
- YAML (YAML Ain't Markup Language): Konfigurationssprache mit Einrueckung statt geschweifter Klammern. Wird fuer MCP-Server-Konfigurationen, GitHub Actions und Docker genutzt.
- URL (Uniform Resource Locator): Adresse einer Ressource im Web. Aufbau: https://domain.com/pfad?parameter=wert. Claude kann URLs nur mit Tools oder MCP-Verbindungen aufrufen.
- API-Endpunkt: Spezifische URL, ueber die Programme Daten austauschen. Bei direkter Nutzung der Anthropic-API (z. B. in eigenen Programmen) laeuft jeder Request ueber api.anthropic.com — strukturiertes Format, meist JSON. Im Browser-Chat (Claude.ai) geschieht das serverseitig.
- REST-API-Muster: Die meisten modernen Dienste (GitHub, Stripe, Anthropic) bieten eine REST API — standardisierte Endpunkte fuer CRUD-Operationen (Create, Read, Update, Delete). MCP-Server nutzen diese intern.

> 🧠 *JSON ist die Sprache, in der KI und Werkzeuge miteinander reden. Wer JSON versteht, versteht wie Claude unter der Haube kommuniziert.*

#### 8.3 — Code-Dateien

**Kernsatz:** Claude liest, schreibt und erklaert Code-Dateien in jeder Sprache — aber jede Sprache hat ihren Einsatzbereich und ihre Ausfuehrungsumgebung.

- Python (.py): Die beliebteste Sprache fuer Datenanalyse, Automatisierung und KI-Backends. Wird mit python3 skript.py ausgefuehrt. Claude Code schreibt taeglich Python-Scripts.
- JavaScript (.js / .mjs): Laeuft im Browser (Frontend) oder auf dem Server via Node.js (Backend). node skript.js fuehrt es aus. Diese Lern-App besteht zu einem grossen Teil aus JavaScript.
- Shell-Script (.sh): Enthaelt Bash-Shell-Befehle, die nacheinander ausgefuehrt werden. #!/bin/bash am Anfang markiert die Datei als Shell-Script. Claude Code nutzt Shell-Befehle intensiv.
- Was macht eine Datei zu Code? Syntaxregeln, die eine Laufzeitumgebung interpretiert. Ein Tippfehler (fehlende Klammer) bricht die Ausfuehrung. Textdateien haben keine Laufzeitumgebung — Code hat eine.
- Sicherheits-Check vor der Ausfuehrung: node --check datei.js prueft JS-Syntax ohne Ausfuehrung. python3 -m py_compile datei.py prueft Python-Syntax.
- Virtuelle Umgebungen (Python): python3 -m venv .venv isoliert Pakete pro Projekt und verhindert Konflikte zwischen Abhaengigkeiten — Claude Code richtet sie auf Nachfrage ein.

> 🧠 *Python = Daten & Logik. JavaScript = Web & Browser. Shell = Automatisierung & System. Claude beherrscht alle drei.*

#### 8.4 — Web-Formate

**Kernsatz:** Jede Webseite besteht aus drei Schichten: HTML gibt Struktur, CSS gibt Aussehen, JavaScript gibt Verhalten. Diese Lern-App selbst ist ein perfektes Beispiel.

- HTML (HyperText Markup Language): Beschreibt die Struktur einer Seite mit Tags. h1 fuer Ueberschriften, div fuer Bereiche, button fuer Schaltflaechen. Diese App ist eine einzige .html-Datei.
- CSS (Cascading Style Sheets): Beschreibt das Aussehen — Farben, Schriften, Abstaende, Animationen. In dieser App steht alles CSS im style-Block am Anfang.
- DOM (Document Object Model): Die Baumstruktur des HTML im Browser-Speicher. JavaScript manipuliert den DOM: Elemente hinzufuegen, Text aendern, Klassen setzen.
- JavaScript im Browser: Dieselbe Sprache wie Node.js, aber direkt im Browser ausgefuehrt. Reagiert auf Klicks (onclick), veraendert den DOM, liest localStorage.
- Mockup / Wireframe: Visuelle Skizze einer UI, bevor Code geschrieben wird. Klaert Struktur und Layout ohne Logik. Claude kann Mockups als einfaches HTML/CSS generieren.
- URL im Browser: Jede Seite hat eine URL. Innerhalb einer Single-Page-App (wie dieser) simuliert JavaScript die Navigation.

> 🧠 *HTML = Knochen, CSS = Haut, JavaScript = Muskeln. Zusammen ergeben sie eine lebendige Webseite.*

#### 8.5 — Binaer, Bilder & Grenzen von KI

**Kernsatz:** Nicht alles ist fuer LLMs direkt lesbar. Binaerformate brauchen Extraktion, Bilder brauchen multimodale Modelle — und manche Dateien sollten Claude bewusst vorenthalten werden.

- Binaerformat: Datei, die keine lesbare Textstruktur hat — stattdessen Rohdaten in Bytes. PDF, DOCX, XLSX, MP3, PNG, JPG sind Binaerformate. Ein Texteditor oeffnet sie als unlesbaren Zeichensalat.
- PDF: Weit verbreitetes Dokumentformat. Aktuelle Claude-Modelle koennen PDFs ueber die API direkt verarbeiten — Text, Bilder, Tabellen und Diagramme werden analysiert. Grenzen: max. 32 MB, max. 600 Seiten, keine verschluesselten PDFs. Fuer lokale Dokumente ohne API (z. B. ueber MCP) kann vorherige Textextraktion sinnvoll bleiben.
- DOCX / XLSX: Microsoft-Formate fuer Word und Excel — intern ZIP-Archive mit XML. Muessen zu .txt oder .csv konvertiert werden. Der DOCX-Skill erledigt das automatisch.
- PNG / JPG: Bilddateien. Viele aktuelle Modelle (z. B. Claude Sonnet/Opus, Gemini Pro, GPT-4o) koennen Bilder direkt sehen — die konkrete Modellvariante und API-Dokumentation entscheiden. Nicht jede Bereitstellungsform unterstuetzt alle Modalitaeten.
- SVG (Scalable Vector Graphic): Der Sonderfall unter den Bildformaten — SVG ist XML/Text und damit fuer Claude direkt lesbar und schreibbar. Die Schaubilder in dieser App sind SVGs.
- .env-Datei: Textdatei mit Umgebungsvariablen wie API-Keys und Passwoertern. Wird nie in Git committet. Claude Code erkennt .env-Dateien und warnt vor versehentlichem Upload.
- package.json: Konfigurationsdatei fuer Node.js-Projekte im JSON-Format. Listet alle Abhaengigkeiten und Skripte. Claude liest sie, um das Projekt zu verstehen.

> 🧠 *Was Text ist, liest Claude direkt. Was binaer ist, braucht je nach Modell native Unterstuetzung oder Extraktion. Was geheim ist, bleibt geheim.*

---

## Karteikarten / Glossar

Die folgenden Definitionen entstammen den Lern-Karteikarten (Leitner-System).

### Modul 1: Grundlagen

**Künstliche Intelligenz (KI)**
: Oberbegriff für Systeme, die Aufgaben lösen, die sonst menschliche Intelligenz erfordern.

**Machine Learning**
: Teilgebiet der KI; lernt Muster aus Daten statt aus festen Regeln.

**Deep Learning**
: Teilgebiet des ML; nutzt vielschichtige (tiefe) neuronale Netze.

**Generative KI**
: KI, die neue Inhalte erzeugt: Text, Bild, Code, Audio.

**Token**
: Kleinster Textbaustein, den ein Modell verarbeitet (meist ein Wortteil).

**Tokenisierung**
: Das Zerlegen von Text in Tokens.

**Next-Token-Prediction**
: Kernmechanismus: das Modell sagt fortlaufend das wahrscheinlich nächste Token voraus.

**Autoregressiv**
: Die Ausgabe wird schrittweise erzeugt; bereits Erzeugtes dient als Kontext.

**Parameter (Gewichte)**
: Interne, trainierte Stellschrauben des Modells — das geronnene Wissen des Modells.

**Mixture of Experts (MoE)**
: Architektur, bei der pro Anfrage nur wenige spezialisierte Teilnetze aktiv sind — effizienter.

**Embedding**
: Übersetzung von Text in einen Zahlenvektor, der Bedeutung geometrisch abbildet.

**Vektorraum**
: Hochdimensionaler Raum, in dem ähnliche Bedeutungen nah beieinanderliegen.

**Kosinus-Ähnlichkeit**
: Maß für die Ähnlichkeit zweier Vektoren (der Winkel zwischen ihnen).

**Transformer**
: Die vorherrschende Architektur moderner Sprachmodelle (seit 2017).

**Attention**
: Mechanismus, der gewichtet, welche Tokens im Text füreinander relevant sind.

### Modul 2: Wie Modelle arbeiten

**Pretraining**
: Erste, teuerste Trainingsphase auf riesigen Textmengen.

**Fine-tuning**
: Nachschärfen des Modells mit kleineren, gezielten Datensätzen.

**RLHF**
: Reinforcement Learning from Human Feedback: Lernen aus menschlichen Bewertungen.

**Constitutional AI**
: Anthropics Ansatz: das Modell prüft sich gegen schriftliche Prinzipien (eine „Verfassung“).

**Kontextfenster**
: Menge an Tokens, die ein Modell gleichzeitig verarbeiten kann (sein Arbeitsgedächtnis).

**Lost in the middle**
: Phänomen: Inhalte in der Mitte langer Eingaben werden schlechter beachtet.

**Inferenz**
: Die Nutzung des fertig trainierten Modells zur Erzeugung von Antworten.

**Temperature**
: Parameter für die Zufälligkeit/Kreativität der Ausgabe (niedrig = faktentreu).

**Halluzination**
: Plausibel klingende, aber falsche oder erfundene Modellausgabe.

**Wissensstichtag**
: Zeitpunkt, nach dem das Modell von sich aus nichts mehr weiß.

### Modul 3: Mit Modellen arbeiten

**Prompt Engineering**
: Die Fertigkeit, Eingaben so zu formulieren, dass nützliche Ausgaben entstehen.

**Zero-Shot**
: Eine Aufgabe ohne Beispiele stellen.

**Few-Shot**
: Eine Aufgabe mit einigen Beispielen stellen, damit das Modell das Muster überträgt.

**Chain of Thought**
: Das Modell denkt in nachvollziehbaren Zwischenschritten vor der Endantwort.

**Reasoning-Modell**
: Modell, das gezielt darauf trainiert ist, vor der Antwort intern zu „denken“.

**RAG**
: Retrieval Augmented Generation: Anbindung externer Wissensquellen zur Erdung der Antworten.

**Chunking**
: Das Zerlegen von Dokumenten in kleine Stücke für RAG.

**Vektordatenbank**
: Speicher für Embeddings; ermöglicht die Ähnlichkeitssuche.

**Tool Use / Function Calling**
: Das Modell ruft externe Werkzeuge/Funktionen auf (suchen, rechnen, Aktionen). Anfragen und Antworten laufen als JSON über eine API.

**MCP (Model Context Protocol)**
: Offener API-Standard (Anthropic 2024) zur Werkzeug-Anbindung — „USB-C für KI“. Jeder MCP-Server exponiert Tools, Resources und Prompts via JSON.

**KI-Agent**
: System, das ein Ziel selbstständig in mehreren Schritten verfolgt.

**Agentic Coding**
: Ein Agent übernimmt die Programmier-Schleife (schreiben, testen, korrigieren) eigenständig — nutzt Shell für Ausführung und Git für Versionskontrolle.

**API (Application Programming Interface)**
: Definierte Schnittstelle, über die Programme miteinander kommunizieren — legt fest, wie Anfragen aussehen und was zurückkommt. MCP und Tool Use basieren auf API-Aufrufen.

**JSON (JavaScript Object Notation)**
: Leichtgewichtiges Datenformat für strukturierte Daten (Schlüssel-Wert-Paare, Listen). MCP-Nachrichten und Tool-Use-Aufrufe werden als JSON übertragen — von Mensch und Maschine lesbar.

**Vibe Coding**
: Prompt-gefuehrtes Entwickeln ohne Architekturplanung -- Ziel ist schneller, sichtbarer Fortschritt. Gut fuer Prototypen und Wegwerf-Skripte. Riskant bei produktivem Code ohne Tests. Gegenpol: strukturiertes Agentic Engineering mit Spezifikation und Pruefschleifen.

### Modul 4: Anbieter & Praxis

**Anthropic / Claude**
: Sicherheits-fokussierter Anbieter; Stufen Haiku, Sonnet, Opus; prägte Constitutional AI und MCP.

**Modellwahl**
: Es gibt kein pauschal bestes Modell — die Wahl hängt von der Aufgabe ab.

**Benchmark**
: Standardisierter Test zum Modellvergleich (z. B. MMLU, SWE-bench).

**Daten-Kontamination**
: Testaufgaben sind ins Training geraten — das verfälscht Benchmark-Ergebnisse.

**Multimodal**
: Verarbeitung mehrerer Datenarten: Text, Bild, Audio, Video.

**Nativ multimodal**
: Von Grund auf für mehrere Modalitäten gebaut, nicht nachträglich angekoppelt.

**Prompt Injection**
: Versteckte schädliche Anweisungen in Inhalten. Regel: externe Inhalte sind Daten, keine Befehle.

**Bias**
: Verzerrungen, die ein Modell aus seinen Trainingsdaten übernimmt.

### Modul 5: Vertiefung: Mechanik

**Byte-Pair Encoding (BPE)**
: Tokenisierungsverfahren: fasst die häufigsten Zeichenpaare iterativ zu einem neuen Token zusammen.

**Vokabular (Vocabulary)**
: Gesamtbestand aller Tokens, die ein Modell kennt (oft 100.000–200.000).

**Query / Key / Value**
: Die drei Vektoren je Token in der Attention: Query = Suchanfrage, Key = Relevanz-Signal, Value = Inhalt.

**Multi-Head Attention**
: Mehrere parallele Attention-Berechnungen, die verschiedene Beziehungsarten erfassen.

**Positionskodierung (RoPE)**
: Gibt dem Modell die Wortstellung mit — Attention allein ist reihenfolgeblind.

**Kontextuelles Embedding**
: Der Vektor eines Wortes hängt vom umgebenden Satz ab — löst Mehrdeutigkeit (z. B. 'Bank').

**Verlustfunktion (Loss)**
: Maß für den Fehler einer Vorhersage (beim Sprachmodell oft Cross-Entropy).

**Backpropagation**
: Berechnet den Beitrag jedes Parameters zum Fehler und liefert den Gradienten.

**Gradientenabstieg**
: Verschiebt Parameter schrittweise Richtung kleinerer Fehler; Schrittgröße = Lernrate.

**Overfitting**
: Das Modell memoriert Trainingsdaten statt zu verallgemeinern — glänzt im Training, versagt bei Neuem.

**LoRA**
: Parameter-effizientes Fine-tuning: Basis-Gewichte einfrieren, nur kleine Adapter trainieren.

**DPO (Direct Preference Optimization)**
: Vereinfachtes Alignment ohne separates Belohnungsmodell — 2026 Praxisstandard statt RLHF/PPO.

**Test-Time Compute**
: Mehr Rechenleistung zur Antwortzeit durch Zwischen-Tokens (Nachdenken als Arbeitsspeicher).

**Chinchilla-Gesetz**
: Compute-optimales Training (Hoffmann et al. 2022): Parameter und Daten muessen gleichmaessig skaliert werden. Chinchilla (70 Mrd. Parameter, 1,4 Bio. Tokens) schlug 280-Mrd.-Modelle. Lektion: Datenmenge ist genauso wichtig wie Modellgroesse.

### Modul 6: Vertiefung: Systeme & Praxis

**Hybride Suche**
: Kombination aus semantischer Ähnlichkeitssuche und lexikalischer Stichwortsuche.

**Re-Ranker**
: Stufe nach der Suche, die Treffer nach echter Relevanz neu sortiert.

**ReAct**
: Agentenmuster: Schleife aus Thought (Gedanke) → Action (Werkzeug) → Observation (Ergebnis).

**Context Engineering**
: Die Disziplin, den gesamten Kontextinhalt zu gestalten (was, wie viel, Reihenfolge).

**Quantisierung**
: Parameter mit weniger Bit speichern (z. B. 4 statt 16) → kleiner und schneller im Betrieb.

**KV-Caching**
: Zwischenspeichern berechneter Keys/Values für effiziente Token-für-Token-Erzeugung.

**Destillation**
: Ein großes Lehrer-Modell trainiert ein kleines Schüler-Modell — kompakt und leistungsstark.

**LLM-as-a-Judge**
: Ein Modell bewertet automatisiert die Ausgaben eines anderen — skaliert, hat aber Judge-Biases.

**Observability (Agenten)**
: Nachvollziehbarkeit des Agenten-Verhaltens: richtiger Pfad? unnötige Schleifen? sauberer Abbruch?

**Autonome Agenten**
: Agents, die ohne menschliche Eingriffe ueber Stunden laufen -- Computer Use, autonomes Coding, Web-Research. 2026: zuverlaessig bei klar abgegrenzten Aufgaben. Trust Levels: Agent erbt User-Vertrauen, nicht Operator-Vertrauen -- begrenzt Privilege Escalation.

### Modul 7: KI-Tools im Alltag

**CLI (Command-Line Interface)**
: Kommandozeilen-Interface; das Terminal ist das Fenster, die Shell ist die Ausführungsumgebung dahinter — direkter Systemzugriff ohne grafische Oberfläche.

**Claude Code**
: Agentic Coding Tool im Terminal; liest Code, schreibt ihn, führt ihn aus und arbeitet selbstständig in Schleifen bis zum Ziel.

**Agentic Loop**
: Selbstständige Schleife: Aufgabe → Lesen → Ausführen → Prüfen → Korrigieren — wiederholt bis das Ziel erreicht ist.

**Skill (Claude Code)**
: Markdown-Datei mit wiederverwendbaren Verhaltensanweisungen — per Slash-Befehl (/skill-name) abrufbar.

**CLAUDE.md — Rolle im Projekt**
: Markdown-Datei im Projektordner: erklärt Claude Code die Spielregeln, Konventionen und den Kontext des Projekts. Wird beim Sitzungsstart in den Kontext geladen — als Hinweise, nicht als erzwungene Konfiguration. Global: ~/.claude/CLAUDE.md.

**Hook (Claude Code)**
: Shell-Befehl, der automatisch bei bestimmten Ereignissen ausgeführt wird (z. B. nach jeder Datei-Bearbeitung).

**Harness**
: Das Claude-Code-Framework, das Hooks ausführt; Claude selbst sieht nur das Ergebnis und kann darauf reagieren.

**Subagent**
: Separate Claude-Instanz für eine Teilaufgabe — startet kalt ohne Gedächtnis der Hauptkonversation; Prompt muss eigenständig sein.

**Reversible vs. irreversible Aktion**
: Reversibel = leicht rueckgaengig machbar (Datei editieren, git revert, Papierkorb). Schwer reversibel oder irreversibel = E-Mail senden, Zahlung ausloesen. Kontext entscheidet: Git und Backups machen vieles wiederherstellbar — externe Aktionen (Versand, Zahlungen) oft nicht.

**Human-in-the-Loop (HITL)**
: Menschen bestätigen kritische oder irreversible Aktionen vor der Ausführung — Sicherheitsnetz bei agentic KI.

**Shell**
: Befehlszeilen-Umgebung des Betriebssystems — das Programm, das CLI-Befehle entgegennimmt und ausführt (z.B. bash, zsh). Unterschied zum Terminal: die Shell ist das Programm, das Terminal ist das Fenster darum.

**Terminal**
: Programm/Fenster, über das man mit der Shell interagiert (z.B. iTerm2, macOS Terminal, Windows Terminal). Terminal ≠ Shell: das Terminal startet die Shell und zeigt deren Ausgabe.

**Dateisystem**
: Hierarchische Struktur aus Ordnern und Dateien auf dem Computer. Claude Code navigiert eigenständig darin: liest, schreibt und verschiebt Dateien ohne manuelle Eingriffe.

**Pfad (Path)**
: Adresse einer Datei oder eines Ordners im Dateisystem (z.B. ~/Projekte/ki-app/index.html). Absoluter Pfad: von der Wurzel des Systems. Relativer Pfad: vom aktuellen Ordner aus.

**Git**
: Versionskontrollsystem: speichert Codeänderungen in Commits, ermöglicht Branches und Rückgängigmachen. Claude Code führt Git-Operationen aus — Basis für sicheres Agentic Coding.

**Markdown**
: Einfache Textformatierungssprache: # für Überschriften, **fett**, - für Listen. CLAUDE.md und Skills sind Markdown-Dateien — lesbar für Mensch und KI gleichermassen.

### Modul 8: Dateien, Formate & Werkzeuge

**ASCII**
: American Standard Code for Information Interchange: 128 Zeichen (A-Z, 0-9, Sonderzeichen) als Zahlen 0-127. Das Zeichen A = 65, { = 123. Jeder Buchstabe in Code, JSON oder Shell ist eine ASCII-Zahl -- das Fundament aller Textdateien.

**Unicode / UTF-8**
: Erweiterung von ASCII auf alle Sprachen und Symbole (ue, Emojis, CJK-Zeichen). UTF-8 ist der Standard in KI-Tools und Editoren. Fehler entstehen wenn Kodierungen gemischt werden -- z. B. zerstoert U+201D als JS-Delimiter die Syntax.

**.txt-Datei**
: Reiner Text ohne Formatierung -- fuer LLMs das idealste Format. Claude liest .txt direkt ohne Konvertierungsschritt. Grosse Textmengen fuer KI-Analysen immer als .txt uebergeben.

**Markdown / .md**
: Textdatei mit einfacher Formatierung: # Ueberschrift, **fett**, - Liste. Als Plaintext lesbar und als formatierter Text darstellbar. CLAUDE.md ist eine Markdown-Datei -- Claudes wichtigste Konfigurationsdatei.

**CLAUDE.md**
: Markdown-Datei im Projektordner (oder ~/.claude/CLAUDE.md global). Wird beim Start jeder Sitzung in den Kontext geladen -- als Hinweise, nicht erzwungene Konfiguration. Fuer strikte Aktions-Blockaden sind PreToolUse-Hooks der richtige Weg.

**.csv-Datei**
: Comma-Separated Values: tabellarische Daten als Text, Spalten durch Komma getrennt. LLMs und Python-Scripts lesen CSV direkt -- kein Excel noetig. Tabellen immer als CSV exportieren fuer KI-Verarbeitung.

**JSON**
: JavaScript Object Notation: Textformat fuer strukturierte Daten. {"key": "value"}, Arrays [...], Boolean true/false. Bei Tool Use, MCP und API-Calls kommuniziert Claude immer in JSON.

**JSON-Struktur**
: Objekte: {"key": "value"} -- Strings in geraden Anfuehrungszeichen (U+0022). Arrays: [1, 2, 3]. Ein fehlendes Komma oder falsches Anfuehrungszeichen bricht das gesamte JSON -- Syntax ist absolut strikt.

**YAML**
: YAML Ain't Markup Language: Konfigurationssprache mit Einrueckung statt {}. Wird fuer MCP-Server-Konfigurationen, GitHub Actions und Docker genutzt. Lesbarer als JSON, aber strikte Einrueckungs-Regeln.

**URL**
: Uniform Resource Locator: Adresse einer Ressource im Web. Aufbau: https://domain.com/pfad?parameter=wert. Claude kann URLs nur mit Tools oder MCP-Verbindungen aufrufen -- nicht direkt ohne Werkzeug.

**API-Endpunkt**
: Spezifische URL fuer Datenaustausch zwischen Programmen. Bei direkter API-Nutzung laeuft jeder Request ueber api.anthropic.com -- strukturiertes Format, meist JSON. Im Browser-Chat geschieht das serverseitig. MCP-Server sind selbst API-Endpunkte.

**Python-Script (.py)**
: Codedatei in Python. Ausfuehren: python3 skript.py. Claude schreibt, liest und erklaert .py-Dateien -- haeufig fuer Datenanalyse, Automatisierung und KI-Backend. Syntax-Check: python3 -m py_compile skript.py.

**JavaScript-Datei (.js)**
: Laeuft im Browser (Frontend) oder in Node.js (Backend). Ausfuehren: node skript.js. Diese Lern-App enthaelt das gesamte JS fuer Logik, Navigation und Karteikarten-System. Syntax-Check: node --check datei.js.

**Shell-Script (.sh)**
: Enthaelt Bash-Shell-Befehle. #!/bin/bash (Shebang) am Anfang gibt den Interpreter an. Ausfuehren: bash skript.sh. Claude Code nutzt Shell-Befehle intensiv: git, node, python3, grep, find.

**HTML**
: HyperText Markup Language: beschreibt Struktur einer Webseite mit Tags. h1, div, button, ul -- das Grundgeruest. Diese Lern-App ist eine einzige .html-Datei mit allem Wissen darin.

**CSS**
: Cascading Style Sheets: beschreibt Aussehen (Farben, Abstaende, Schriften, Animationen). In dieser App im style-Block. Claude generiert CSS fuer Web-UIs -- z. B. beim Frontend-Design.

**DOM**
: Document Object Model: Baumstruktur des HTML im Browser-Speicher. JavaScript manipuliert den DOM -- Elemente hinzufuegen, Text aendern, Klassen setzen. document.getElementById() ist ein typischer DOM-Zugriff.

**Mockup / Wireframe**
: Visuelle UI-Skizze vor dem Code -- zeigt Layout und Struktur, nicht Logik. Claude generiert Mockups als HTML/CSS in Minuten. Der schnellste Weg, eine UI-Idee sichtbar und diskutierbar zu machen.

**PDF**
: Dokumentformat. Aktuelle Claude-Modelle verarbeiten PDFs direkt ueber die API: Text, Bilder, Tabellen und Diagramme. Grenzen: max. 32 MB, max. 600 Seiten, keine Verschluesselung. Lokal via Claude.ai ueber Datei-Upload. MCP-Tools zur Extraktion bleiben sinnvoll wo keine direkte API-Einbindung besteht.

**DOCX / XLSX**
: Microsoft-Formate fuer Word/Excel -- intern ZIP-Archive mit XML. Muss zu .txt bzw. .csv konvertiert werden, bevor Claude verarbeitet. Anthropic-Skills (DOCX-Skill, XLSX-Skill) erledigen das automatisch.

**PNG / JPG**
: Bilddateien. Viele aktuelle Modelle (z. B. Claude Sonnet/Opus, Gemini Pro, GPT-4o) sind multimodal und koennen Bilder direkt sehen. Die konkrete Modellvariante und API-Dokumentation entscheiden -- nicht jede Variante unterstuetzt alle Modalitaeten.

**SVG**
: Scalable Vector Graphic: Vektorgrafik als XML/Text. Claude kann SVG direkt lesen, schreiben und generieren -- die Schaubilder in dieser App sind von Claude generierte SVGs. Der Sonderfall unter den Bildformaten.

**Binaerformat**
: Datei ohne lesbare Textstruktur -- stattdessen Rohdaten in Bytes. PDF, DOCX, XLSX, MP3, PNG, JPG sind Binaerformate. LLMs brauchen Extraktion oder multimodale Faehigkeiten -- ein Texteditor zeigt nur Zeichensalat.

**.env-Datei**
: Textdatei mit Umgebungsvariablen: API-Keys, Passwoerter, Zugangsdaten. Wird nie in Git committet (.gitignore schuetzt davor). Claude Code erkennt .env-Dateien und warnt vor versehentlichem Upload sensibler Daten.

**package.json**
: Konfigurationsdatei fuer Node.js-Projekte im JSON-Format. Listet Abhaengigkeiten (npm-Pakete), Skripte und Metadaten. Claude liest package.json um das Projekt zu verstehen -- aehnlich wie CLAUDE.md fuer Regeln.

---

*Generiert: 2026-06-09 — Quelle: ki-verstehen.html*
