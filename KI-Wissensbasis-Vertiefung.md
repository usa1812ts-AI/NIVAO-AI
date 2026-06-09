# KI & Große Sprachmodelle — Vertiefung (Teil 2)

> ⚠️ **Quellstrategie (P1.5):** Die verbindliche Inhaltsquelle ist `ki-verstehen.html`.
> Diese Datei ist **historische Prosa-Vertiefung** (gut für NotebookLM-Podcast-Generierung).
> Für eine aktuell synchronisierte Version: `python3 export_md.py` → `KI-Wissensbasis-Export.md`.
> Korrekturen und neue Inhalte gehören immer zuerst in `ki-verstehen.html`.

> **Zweck dieses Dokuments**
> Dies ist die zweite, tiefer gehende Wissensbasis für NotebookLM und baut auf der ersten Datei ("KI-Wissensbasis") auf. Wo Teil 1 erklärt *was* die Konzepte sind, erklärt dieser Teil *wie und warum* sie genau funktionieren. Wieder bewusst in zusammenhängender Prosa (gut für Podcast), mit erweitertem Glossar (Karteikarten) und einem anspruchsvolleren Selbsttest (Quiz) am Ende.
>
> **Stand:** Ende Mai 2026. Mechanik und Konzepte sind weitgehend stabil; konkrete Verfahrensnamen, Werkzeuge und Zahlen sind Momentaufnahmen.
>
> **Voraussetzung:** Die Begriffe aus Teil 1 (Token, Next-Token-Prediction, Parameter, Embedding, Transformer, Attention, Kontextfenster, Prompt Engineering, Chain of Thought, RAG, Tool Use, MCP, Agent) sollten geläufig sein. Hier vertiefen wir sie.
>
> **Aufbau:** A Tokenisierung im Detail → B Attention-Mechanik → C Embeddings tiefer → D Wie Training wirklich abläuft → E Fine-tuning-Verfahren → F Reasoning-Mechanik → G RAG als Pipeline → H Agenten-Architekturmuster → I Context Engineering → J Inferenz-Optimierung → K Evaluation → Glossar → Selbsttest → Quellen.

---

## A — Tokenisierung im Detail: Wie Text zu Zahlen wird

In Teil 1 hieß es: Modelle verarbeiten Tokens, nicht Wörter. Aber wie genau entstehen diese Tokens? Das häufigste Verfahren heißt **Byte-Pair Encoding (BPE)**, ergänzt durch Varianten wie WordPiece oder SentencePiece.

Die Grundidee von BPE ist elegant: Man beginnt mit den allerkleinsten Einheiten (einzelnen Zeichen oder sogar Bytes) und sucht dann im Trainingstext wiederholt nach dem häufigsten benachbarten Paar. Dieses Paar wird zu einem neuen, größeren Token zusammengefasst. Das wiederholt man tausendfach. Häufige Wörter wie "und" werden so zu einem einzigen Token, während seltene Fachbegriffe oder Eigennamen in mehrere Stücke zerfallen. Das erklärt, warum "Komponentenvertrieb" mehr Tokens kostet als "Haus": Das Modell hat das seltene Kompositum nie als Ganzes gelernt.

Das gesamte Inventar dieser gelernten Tokens heißt **Vokabular** (Vocabulary). Moderne Modelle haben Vokabulare von oft 100.000 bis 200.000 Tokens. Ein größeres Vokabular bedeutet kürzere Token-Sequenzen (effizienter), aber auch mehr zu lernende Parameter in den ersten und letzten Schichten des Netzes — ein Abwägungsspiel.

Praktische Konsequenzen, die man kennen sollte: Nicht-englische Sprachen, besonders solche mit anderen Schriftsystemen, sind oft token-teurer, weil die Vokabulare englisch-lastig trainiert wurden. Zahlen werden teils seltsam zerlegt, was zu Rechenfehlern beiträgt. Und Tippfehler oder ungewöhnliche Formatierungen können ein Wort in viele Tokens zersplittern und so das Modell verwirren.

---

## B — Die Attention-Mechanik: Query, Key und Value

Teil 1 sagte: Attention gewichtet, welche Tokens füreinander relevant sind. Jetzt der Mechanismus dahinter, ohne Formeln, aber mit dem richtigen Bild.

Für jedes Token erzeugt das Modell drei Vektoren, die man sich mit einer Bibliotheks-Analogie merken kann:

- **Query (Anfrage):** "Wonach suche ich gerade?" — Das aktuelle Token formuliert eine Art Suchanfrage.
- **Key (Schlüssel):** "Wofür bin ich relevant?" — Jedes Token bietet einen Schlüssel an, der beschreibt, welche Information es beisteuern kann.
- **Value (Wert):** "Das ist mein eigentlicher Inhalt." — Die Information, die weitergegeben wird, wenn das Token als relevant erkannt wird.

Der Ablauf: Die Query eines Tokens wird mit den Keys aller anderen Tokens verglichen. Passt eine Query gut zu einem Key (mathematisch: hohes Skalarprodukt), bekommt der zugehörige Value ein hohes Gewicht. Das Modell zieht dann eine gewichtete Mischung aller Values zusammen. So "holt" sich jedes Token genau die Information aus dem Rest des Textes, die es braucht. Im Satz "Der Ingenieur prüfte die Komponente, weil sie defekt war" sendet das Token "sie" eine Query aus, die stark zum Key von "Komponente" passt — und übernimmt dessen Value.

Zwei Begriffe, die man häufig hört:

**Multi-Head Attention:** Das Modell führt diesen Vorgang nicht einmal, sondern mehrfach parallel aus ("Köpfe"). Jeder Kopf kann auf andere Beziehungsarten achten — einer auf grammatische Bezüge, einer auf Themen, einer auf Position. Die Ergebnisse werden zusammengeführt. Das gibt dem Modell mehrere "Blickwinkel" gleichzeitig.

**Self-Attention vs. Cross-Attention:** Bei Self-Attention beziehen sich die Tokens auf denselben Text (das ist der Normalfall in heutigen Modellen). Cross-Attention bezieht eine Sequenz auf eine andere — wichtig etwa bei Übersetzungsarchitekturen.

Eine technisch zentrale Eigenschaft: Der Rechenaufwand von Attention wächst **quadratisch** mit der Länge des Textes (jedes Token vergleicht sich mit jedem anderen). Das ist der eigentliche Grund, warum lange Kontextfenster so teuer sind und warum 2026 viel an effizienteren Varianten geforscht wird — etwa "subquadratischen" Architekturen, die diesen Engpass umgehen wollen (Quelle: WhatLLM.org, Mai 2026).

---

## C — Embeddings tiefer: Dimensionen, Position und das Kontext-Problem

Teil 1 führte Embeddings als bedeutungstragende Vektoren ein. Drei Vertiefungen:

**Dimensionalität:** Ein Embedding-Vektor hat eine feste Länge, die Dimension — etwa 768, 1.536 oder mehr Zahlen. Jede Dimension kann man sich grob als eine erlernte "Bedeutungsachse" vorstellen (auch wenn diese Achsen nicht einzeln menschlich interpretierbar sind). Mehr Dimensionen erlauben feinere Unterscheidungen, kosten aber Speicher und Rechenzeit.

**Positionskodierung (Positional Encoding):** Attention allein ist "reihenfolgeblind" — sie würde "Hund beißt Mann" und "Mann beißt Hund" gleich behandeln. Damit das Modell die Wortstellung kennt, wird jedem Token zusätzlich eine Positionsinformation in seinen Vektor eingerechnet. Moderne Verfahren (etwa rotierende Positionskodierung, "RoPE") sind ein Grund, warum lange Kontextfenster überhaupt funktionieren.

**Statische vs. kontextuelle Embeddings:** Ältere Verfahren gaben einem Wort immer denselben Vektor. Das Problem: "Bank" (Geldinstitut) und "Bank" (Sitzmöbel) bekamen denselben Punkt. Moderne Transformer erzeugen **kontextuelle** Embeddings — der Vektor eines Wortes hängt vom umgebenden Satz ab. Dieselbe "Bank" liegt also je nach Kontext woanders im Raum. Das ist einer der großen Fortschritte gegenüber früheren Methoden.

---

## D — Wie Training wirklich abläuft: Loss, Gradient, Backpropagation

Teil 1 nannte die Phasen (Pretraining, Fine-tuning, RLHF). Hier der Lernvorgang selbst — vereinfacht, aber im Kern korrekt.

Das Lernen läuft als Optimierungsschleife:

1. **Vorhersage:** Das Modell sieht einen Textausschnitt und sagt das nächste Token voraus.
2. **Verlust (Loss):** Man vergleicht die Vorhersage mit dem tatsächlichen nächsten Token im Trainingstext. Die **Verlustfunktion** misst, wie falsch die Vorhersage war — eine einzige Zahl, die den Fehler quantifiziert (beim Sprachmodell typischerweise die "Cross-Entropy").
3. **Gradient:** Per **Backpropagation** (Fehlerrückführung) berechnet man, in welche Richtung und wie stark jeder einzelne Parameter den Fehler beeinflusst hat. Das Ergebnis ist der **Gradient** — gewissermaßen ein Pfeil, der zu kleinerem Fehler zeigt.
4. **Anpassung:** Per **Gradientenabstieg** ("Gradient Descent") werden alle Parameter ein winziges Stück in die fehlerverringernde Richtung verschoben. Wie groß dieser Schritt ist, regelt die **Lernrate** (Learning Rate).

Dieser Vierschritt wiederholt sich über Billionen von Tokens. Bildlich: Das Modell tastet sich in einer riesigen "Fehlerlandschaft" bergab, immer Richtung Tal (geringer Fehler). Ein **Epoch** ist ein vollständiger Durchlauf durch die Trainingsdaten.

Wichtige Begleitphänomene:

- **Overfitting (Überanpassung):** Das Modell "memoriert" die Trainingsdaten, statt verallgemeinerbare Muster zu lernen — es glänzt im Training, versagt aber bei Neuem.
- **Catastrophic Forgetting (katastrophales Vergessen):** Lernt ein fertiges Modell beim Nachtrainieren etwas Neues, kann es zuvor Gelerntes überschreiben. Ein zentraler Grund, warum man beim Fine-tuning vorsichtig sein muss (Quelle: hjLabs.in, 2026).
- **Scaling Laws (Skalierungsgesetze):** Empirisch beobachtete Regelmäßigkeiten, wie Leistung mit mehr Daten, mehr Parametern und mehr Rechenleistung wächst. Sie prägten jahrelang die Strategie "größer ist besser" — die 2026 durch effiziente Architekturen relativiert wird.

---

## E — Fine-tuning-Verfahren: SFT, LoRA, RLHF, DPO und Verwandte

Fine-tuning (Feinabstimmung) ist 2026 ein ganzer Werkzeugkasten. Die wichtigsten Verfahren und wann man sie nimmt:

**Supervised Fine-Tuning (SFT):** Die Grundform. Man trainiert das Modell auf Paaren aus (Eingabe, idealer Ausgabe), um Format, Stil oder Aufgabentyp beizubringen. Fast jede Anpassungs-Pipeline beginnt hier.

**Parameter-effizientes Fine-tuning — LoRA und QLoRA:** Ein komplettes Modell nachzutrainieren ist teuer. **LoRA** (Low-Rank Adaptation) friert die ursprünglichen Gewichte ein und fügt nur kleine, trainierbare Zusatzmatrizen in die Transformer-Schichten ein. Die Erkenntnis dahinter: Die nötige Anpassung hat einen niedrigen "intrinsischen Rang", lässt sich also kompakt darstellen. Praktisch kann LoRA die Zahl trainierbarer Parameter auf einen Bruchteil eines Prozents senken — bei vergleichbarer Qualität. **QLoRA** kombiniert das zusätzlich mit Quantisierung (siehe unten), sodass Feinabstimmung sogar auf bescheidener Hardware möglich wird. Ein LoRA-Ergebnis ist eine kleine "Adapter"-Datei (oft nur Megabyte groß), die man bei Bedarf zuschalten kann (Quellen: mobisoftinfotech.com, hjLabs.in, 2026).

**Alignment per Präferenzdaten — RLHF vs. DPO:** Um ein Modell an menschliche Werte (hilfreich, ehrlich, harmlos) anzupassen, braucht es Präferenzlernen.
- **RLHF** (Teil 1) läuft klassisch dreistufig: erst SFT, dann ein separates **Belohnungsmodell** (Reward Model) aus menschlichen Vergleichsurteilen trainieren, dann das Sprachmodell per bestärkendem Lernen (oft Algorithmus "PPO") auf hohe Belohnung optimieren. Mächtig, aber komplex: Es jongliert mehrere Modelle gleichzeitig und ist instabil im Training.
- **DPO** (Direct Preference Optimization) ist die 2026 in der Praxis dominierende Vereinfachung. Es überspringt das separate Belohnungsmodell und optimiert das Sprachmodell direkt auf Präferenzpaaren (bevorzugte vs. abgelehnte Antwort) über eine klassifikationsartige Verlustfunktion. Ergebnis: deutlich einfacher und stabiler, bei vergleichbarer Qualität für die meisten Aufgaben; Berichte nennen 40–75 Prozent geringere Rechenkosten. Die Standard-Pipeline ist heute oft "SFT, dann DPO" (Quellen: patsnap.com, secondtalent.com, bigdataboutique.com, 2026).
- Verwandte Verfahren je nach Datenlage: **ORPO** (kommt ohne separaten SFT-Schritt aus), **KTO** (genügt mit simplen Daumen-hoch/-runter-Daten), und **RLAIF** (Reinforcement Learning from AI Feedback), bei dem ein KI-Modell statt Menschen die Präferenzurteile liefert — die Grundidee hinter Constitutional AI.

**Die wichtigste Entscheidungsregel 2026:** Fine-tuning ist gut für *Stil, Format und Verhalten*, aber schlecht, um *neue Fakten* einzuspeisen. Für aktuelles oder firmenspezifisches Faktenwissen ist RAG (Abschnitt G) fast immer die bessere Wahl. Eine oft zitierte Faustregel: Wenige hundert sehr saubere Beispiele schlagen Zehntausende schlampig gesammelte (Quelle: bigdataboutique.com, hjLabs.in, 2026).

---

## F — Reasoning-Mechanik: Warum "Nachdenken" funktioniert

Teil 1 führte Chain of Thought und Reasoning-Modelle ein. Warum verbessert mehr "Denken" die Ergebnisse eigentlich?

**Test-Time Compute (Rechenleistung zur Antwortzeit):** Der Kerngedanke. Ein normales Modell hat pro Token nur eine feste Menge Rechenschritte zur Verfügung. Schwere Probleme brauchen aber mehr Schritte, als in eine direkte Antwort passen. Indem das Modell viele Zwischen-Tokens erzeugt (sein "Nachdenken"), verschafft es sich faktisch mehr Rechenzeit und mehr Arbeitsspeicher im Kontext. Es kann Teilergebnisse festhalten und darauf aufbauen — wie ein Mensch, der auf einem Schmierzettel rechnet, statt im Kopf.

**Wie Reasoning-Modelle trainiert werden:** Diese Modelle werden gezielt mit bestärkendem Lernen darauf trainiert, lange, zielführende Gedankenketten zu erzeugen — typischerweise an Aufgaben mit überprüfbarer Lösung (Mathematik, Code), wo man automatisch belohnen kann, ob das Endergebnis stimmt. Das Modell lernt so, welche Denkstrategien zu richtigen Antworten führen (Quelle: OpenAI GPT-5.5 System Card, 2026).

**Eine wichtige Einordnung:** Eine Forschungsarbeit von 2025 legt nahe, dass ein großer Teil der Reasoning-Fortschritte seit GPT-4 darauf zurückgeht, dass Modelle gelernt haben, generische Chain-of-Thought-Strategien automatisch anzuwenden — teils gestützt durch versteckte System-Prompts (Quelle: arXiv 2505.19676). Reasoning ist also weniger "echtes Verstehen" als eine sehr wirksame erlernte Arbeitsweise.

**Praktische Grenzen:** Mehr Denken kostet Tokens, Zeit und Geld. Es hilft stark bei mehrstufiger Logik, Mathematik und Planung — bringt aber wenig bei simplen Abruf- oder Kreativaufgaben. Und es gibt das Phänomen des "Overthinking", bei dem zu langes Grübeln die Antwort sogar verschlechtert. 2026 bieten Anbieter daher abgestufte Denktiefen an, die man zur Aufgabe wählt (siehe Teil 1, Abschnitt 12).

---

## G — RAG als Pipeline: Wo Qualität gewonnen und verloren wird

Teil 1 erklärte RAG in drei Schritten. In der Praxis ist jeder Schritt eine eigene Qualitätsstellschraube.

**Chunking-Strategie:** Wie man Dokumente zerteilt, entscheidet maßgeblich über die Trefferqualität. Zu kleine Stücke verlieren Zusammenhang, zu große verwässern die Relevanz. Gängig sind Überlappungen zwischen Stücken (damit kein Satz an der Schnittkante zerrissen wird) und semantisches Chunking, das an inhaltlichen Grenzen trennt statt stur nach Zeichenzahl.

**Embedding-Qualität:** Das Embedding-Modell bestimmt, wie gut Bedeutung erfasst wird. Für Fachdomänen (etwa technischer Komponentenvertrieb) können speziell angepasste Embedding-Modelle deutlich bessere Treffer liefern als generische.

**Retrieval-Strategie:** Reine semantische Suche übersieht manchmal exakte Begriffe (Artikelnummern, Eigennamen, Abkürzungen). Deshalb ist 2026 die **hybride Suche** Standard: semantische Suche (Bedeutung) plus lexikalische Stichwortsuche (exakte Begriffe), kombiniert. Ein nachgeschalteter **Re-Ranker** sortiert die Kandidaten dann nach echter Relevanz, statt nur nach Vektornähe (Quellen: Pinecone, Google Cloud, techment.com, 2026).

**Augmentation:** Wie die gefundenen Stücke in den Prompt eingebaut werden, beeinflusst die Antwort. Zu viel Kontext kann das "lost in the middle"-Problem auslösen; zu wenig lässt Lücken.

**Fortgeschrittene Varianten 2026:** **Graph-RAG** nutzt Wissensgraphen statt bloßer Vektorähnlichkeit, um Beziehungen zwischen Fakten abzubilden — stark bei vernetztem Wissen. **Agentic RAG** lässt einen Agenten die Suche selbst steuern: Er zerlegt komplexe Fragen, sucht mehrfach gezielt und prüft seine Treffer (Quellen: writer.com; US-Patent 12450217, 2026).

**Sicherheitsaspekt (Wiederholung, weil wichtig):** Eine unverschlüsselte Vektordatenbank ist ein Risiko, da sich aus Embeddings teils Rückschlüsse auf Originaldaten ziehen lassen (Quelle: IBM, 2026).

---

## H — Agenten-Architekturmuster: ReAct, Reflexion, Planung, Multi-Agent

Teil 1 definierte den Agenten allgemein. In der Praxis kristallisierten sich 2022/2023 einige Grundmuster heraus, die 2026 jedes Produktionssystem in irgendeiner Form nutzt. Die Erkenntnis vieler Teams: Die meisten KI-Fehler in der Produktion 2024–2026 waren keine Modellfehler, sondern Architekturfehler — das Modell funktionierte, das Design drumherum nicht (Quelle: innovatrixinfotech.com, 2026).

**ReAct (Reasoning + Acting):** Das Grundmuster. Der Agent wechselt in einer Schleife zwischen drei Phasen: **Thought** (Gedanke: Was ist mein nächster Schritt?), **Action** (Aktion: ein Werkzeug aufrufen, z. B. Websuche oder Datenbankabfrage), **Observation** (Beobachtung: das Ergebnis lesen und ins Denken einarbeiten). So erdet der Agent seine Entscheidungen fortlaufend an echtem Feedback. Gut für interaktive Aufgaben; typische Schwäche: Kohärenzverlust bei sehr langen Läufen (jenseits etwa 50 Schritten) (Quellen: n1n.ai, digitalapplied.com, 2026).

**Reflection / Reflexion (Selbstkritik):** ReAct plus ein expliziter Schritt, in dem der Agent seine eigene Ausgabe kritisiert und die Kritik als Hinweis für den nächsten Versuch nutzt. Reduziert wiederholte Fehler, kostet aber eine zusätzliche Modellrunde je Schritt. Praxisregel: die Kritik-Überarbeitungs-Schleife auf zwei bis drei Versuche begrenzen, sonst "oszilliert" der Agent (Quelle: digitalapplied.com, 2026).

**Plan-and-Execute (Planen und Ausführen):** Der Agent erstellt zuerst einen kompletten Plan und arbeitet ihn dann ab. Effizienter bei komplexen, vorab strukturierbaren Aufgaben, weil nicht bei jedem Schritt neu "nachgedacht" werden muss. Braucht aber Prüf- und Wiederaufsetzpunkte ("Checkpointing"), sonst ist er fragil.

**Multi-Agent-Kollaboration (Orchestrator-Worker):** Mehrere spezialisierte Agenten mit je eigener Rolle und eigenem Werkzeugsatz arbeiten unter einem Orchestrator zusammen, der das Ziel zerlegt und verteilt. Sinnvoll, wenn eine Aufgabe die Fähigkeiten oder das Kontextfenster eines einzelnen Agenten übersteigt. Preis: mehr Koordinationsaufwand und Latenz.

**Human-in-the-Loop:** Der Mensch bestätigt kritische oder unumkehrbare Aktionen (Geld, Löschungen, Versand). 2026 als Risikoschutz quasi Pflicht bei allem, was reale Folgen hat.

**Die übergeordnete Praxisregel:** Nicht alle Muster auf einmal einbauen. Mit dem Muster beginnen, das den größten Engpass löst — halluziniert der Agent, dann Reflection; zu langsam bei Komplexem, dann Plan-and-Execute; Prompt zu überladen, dann Multi-Agent. Jedes Muster kostet, bevor es nützt (Quelle: augmentcode.com, n1n.ai, 2026). Außerdem konvergieren die Standards: Anthropics MCP (Werkzeuganbindung) und Protokolle wie Agent-to-Agent (A2A, Agentenkommunikation) wachsen zu interoperablen Standards zusammen (Quelle: sitepoint.com, 2026).

---

## I — Context Engineering: Die Disziplin nach dem Prompt Engineering

Eine prägende Begriffsverschiebung von 2025/2026: Während Prompt Engineering die *einzelne Anfrage* formuliert, befasst sich **Context Engineering** mit der Frage, *welche Information insgesamt im Kontextfenster steht* — und in welcher Reihenfolge, Struktur und Menge. Bei Agenten und langen Abläufen ist das oft wichtiger als die Formulierung des Prompts selbst. Karpathys Wort von 2023, "die heißeste Programmiersprache ist Englisch", wurde so ergänzt: Es geht heute ebenso um Kontextstruktur, Agenten-Schleifenzustände und Absicherung (Quelle: bits-bytes-nn.github.io, 2026).

Kernthemen des Context Engineering:

- **Kontext-Budget:** Das Fenster ist endlich und token-teuer. Man muss entscheiden, was hineinkommt: Systemanweisung, relevante RAG-Treffer, Gesprächsverlauf, Werkzeugbeschreibungen, Zwischenergebnisse.
- **Kontext-Kompression:** Lange Verläufe werden zusammengefasst, statt sie vollständig mitzuschleppen ("Memory"-Mechaniken).
- **Reihenfolge gegen "lost in the middle":** Wichtiges an Anfang oder Ende platzieren, weil die Mitte schlechter beachtet wird.
- **Kontext-Hygiene:** Irrelevantes oder veraltetes Material verschmutzt die Antwort. Auch hier gilt: Externe Inhalte sind Daten, keine Befehle (Schutz vor Prompt Injection).

---

## J — Inferenz-Optimierung: Quantisierung, Caching, Destillation

Wie macht man große Modelle im Betrieb schneller und billiger? Drei zentrale Techniken, die man dem Namen nach kennen sollte:

**Quantisierung (Quantization):** Parameter werden mit geringerer Zahlengenauigkeit gespeichert (z. B. 8 oder 4 Bit statt 16). Das spart Speicher und beschleunigt Inferenz drastisch — bei meist nur geringem Qualitätsverlust. Quantisierung ist der Grund, warum manche Modelle heute sogar auf Laptops laufen.

**KV-Caching (Key-Value-Caching):** Bei der schrittweisen Erzeugung müsste das Modell für jedes neue Token die Attention über den gesamten bisherigen Text neu berechnen. Stattdessen speichert es die bereits berechneten Keys und Values zwischen. Das macht die Token-für-Token-Erzeugung überhaupt erst praktikabel. Verwandt ist das **Context Caching**, bei dem ein gleichbleibender Vorspann (etwa ein großes Standarddokument) zwischengespeichert wird — was die Kosten wiederholter Anfragen stark senkt (Quelle: ai2.work zu Gemini-Caching, 2026).

**Destillation (Distillation):** Ein großes, starkes "Lehrer"-Modell bringt einem kleinen "Schüler"-Modell sein Verhalten bei. Das Ergebnis: ein kompaktes Modell, das einen Großteil der Leistung zu einem Bruchteil der Kosten liefert. Ein Hauptgrund, warum die kleinen, schnellen Modellklassen 2026 so stark geworden sind.

**MoE-Routing (Wiederaufnahme aus Teil 1):** Bei Mixture-of-Experts entscheidet ein "Router", welche Experten-Teilnetze ein Token bearbeiten. Nur diese werden aktiviert — daher die Effizienz bei großen Gesamtmodellen.

---

## K — Evaluation: Wie man Modellqualität wirklich misst

Teil 1 warnte vor Benchmark-Sättigung und Daten-Kontamination. Wie evaluiert man dann sinnvoll?

**LLM-as-a-Judge (Modell als Bewerter):** 2026 verbreitet — ein starkes Modell bewertet automatisiert die Ausgaben eines anderen anhand vorgegebener Kriterien. Skaliert gut, hat aber bekannte Verzerrungen: etwa eine Vorliebe für längere Antworten, für die erstgenannte Option, oder für den eigenen Schreibstil. Solche "Judge-Biases" muss man kennen und gegensteuern (Quelle: Medium/LLM Evaluation 2026).

**Frische und unverfälschte Tests:** Um Kontamination zu umgehen, nutzt man Benchmarks, die laufend neue, nachweislich nach dem Trainingsstichtag entstandene Aufgaben einspeisen (z. B. fortlaufend gesammelte Programmieraufgaben), oder man entfernt die Lösungshistorie aus den Testdaten (Quelle: Medium/LLM Evaluation 2026).

**Eigene Evals:** Die wichtigste Praxis-Lehre. Ein realitätsnaher Testsatz auf den eigenen, echten Aufgaben sagt mehr über die Eignung eines Modells aus als jedes öffentliche Ranking. Vor und nach jeder Anpassung (Fine-tuning, Prompt-Änderung, Modellwechsel) gegen denselben Eval-Satz messen — sonst optimiert man blind.

**Agentic Evaluation:** Bei Agenten genügt es nicht, die Endantwort zu prüfen. Man bewertet den ganzen Pfad: Wurden die richtigen Werkzeuge gewählt? Wurde unnötig im Kreis gelaufen (und Geld verbrannt)? Wurde sauber abgebrochen? Beobachtbarkeit ("Observability") des Agentenverhaltens ist 2026 eine eigene Disziplin (Quelle: dev.to/gabrielanhaia, 2026).

---

## Glossar (für Karteikarten) — Vertiefung

**Byte-Pair Encoding (BPE):** Tokenisierungsverfahren, das häufige Zeichenpaare iterativ zu größeren Tokens zusammenfasst.

**Vokabular (Vocabulary):** Gesamtbestand aller Tokens, die ein Modell kennt (oft 100k–200k).

**Query / Key / Value:** Die drei Vektoren je Token, über die Attention berechnet, welche Tokens füreinander relevant sind (Anfrage / Schlüssel / Inhalt).

**Multi-Head Attention:** Mehrere parallele Attention-Berechnungen, die unterschiedliche Beziehungsarten erfassen.

**Self-Attention:** Attention innerhalb derselben Textsequenz (Normalfall).

**Quadratischer Aufwand:** Rechenkosten der Attention wachsen mit dem Quadrat der Textlänge — Grund für teure lange Kontexte.

**Dimension (eines Embeddings):** Länge des Vektors; mehr Dimensionen = feinere Bedeutungsunterschiede.

**Positionskodierung (Positional Encoding / RoPE):** Zusatzinformation über die Wortstellung, da Attention sonst reihenfolgeblind wäre.

**Kontextuelles Embedding:** Vektor eines Wortes, der vom umgebenden Satz abhängt (löst Mehrdeutigkeit).

**Verlustfunktion (Loss):** Maß dafür, wie falsch eine Vorhersage war (oft Cross-Entropy).

**Backpropagation:** Verfahren, das berechnet, wie jeder Parameter zum Fehler beiträgt.

**Gradient:** "Richtungspfeil" zu geringerem Fehler.

**Gradientenabstieg (Gradient Descent):** Schrittweises Anpassen der Parameter Richtung kleinerer Fehler.

**Lernrate (Learning Rate):** Schrittgröße beim Gradientenabstieg.

**Epoch:** Ein vollständiger Durchlauf durch die Trainingsdaten.

**Overfitting:** Modell memoriert Trainingsdaten statt zu verallgemeinern.

**Catastrophic Forgetting:** Neues Training überschreibt zuvor Gelerntes.

**Scaling Laws:** Empirische Gesetze, wie Leistung mit Daten/Parametern/Rechenleistung skaliert.

**Supervised Fine-Tuning (SFT):** Anpassung auf (Eingabe, Ideal-Ausgabe)-Paaren.

**LoRA:** Parameter-effizientes Fine-tuning; friert Gewichte ein, fügt kleine Adapter ein.

**QLoRA:** LoRA kombiniert mit Quantisierung für Hardware-Sparsamkeit.

**Reward Model (Belohnungsmodell):** Modell, das in RLHF menschliche Präferenzen als Punktzahl vorhersagt.

**PPO:** Verbreiteter RL-Algorithmus in der RLHF-Optimierung.

**DPO (Direct Preference Optimization):** Vereinfachtes Alignment ohne separates Belohnungsmodell; 2026 Praxisstandard.

**ORPO / KTO:** DPO-Verwandte für bestimmte Datenlagen (ohne SFT-Schritt / mit Daumen-hoch-runter-Daten).

**RLAIF:** Präferenzlernen mit KI-Feedback statt menschlichem (Idee hinter Constitutional AI).

**Test-Time Compute:** Mehr Rechenleistung zur Antwortzeit durch ausführliches "Nachdenken".

**Chunking:** Zerlegen von Dokumenten für RAG.

**Hybride Suche:** Kombination aus semantischer und Stichwortsuche.

**Re-Ranker:** Stufe, die Suchtreffer nach echter Relevanz neu sortiert.

**Graph-RAG:** RAG-Variante mit Wissensgraphen statt nur Vektorähnlichkeit.

**Agentic RAG:** Agent steuert die Suche selbst (zerlegt, sucht mehrfach, prüft).

**ReAct:** Agentenmuster mit Schleife aus Thought, Action, Observation.

**Reflection / Reflexion:** Agentenmuster mit explizitem Selbstkritik-Schritt.

**Plan-and-Execute:** Agentenmuster: erst kompletter Plan, dann Ausführung.

**Multi-Agent / Orchestrator-Worker:** Mehrere spezialisierte Agenten unter einem Koordinator.

**Human-in-the-Loop:** Mensch bestätigt kritische/unumkehrbare Aktionen.

**A2A (Agent-to-Agent):** Aufkommender Standard für Kommunikation zwischen Agenten.

**Context Engineering:** Disziplin, den gesamten Kontextinhalt zu gestalten (was, wie viel, in welcher Reihenfolge).

**Kontext-Kompression:** Zusammenfassen langer Verläufe statt vollständigem Mitschleppen.

**Quantisierung:** Speichern der Parameter mit geringerer Zahlengenauigkeit (schneller, kleiner).

**KV-Caching:** Zwischenspeichern berechneter Keys/Values für effiziente Token-Erzeugung.

**Context Caching:** Zwischenspeichern eines gleichbleibenden Prompt-Vorspanns zur Kostensenkung.

**Destillation (Distillation):** Großes Lehrermodell trainiert kompaktes Schülermodell.

**MoE-Router:** Komponente, die in Mixture-of-Experts die aktiven Experten je Token auswählt.

**LLM-as-a-Judge:** Modell bewertet automatisiert Ausgaben eines anderen Modells.

**Judge-Bias:** Systematische Verzerrung solcher Modellbewertungen (z. B. Längen-Vorliebe).

**Observability:** Nachvollziehbarkeit und Überwachung des (Agenten-)Verhaltens in der Produktion.

---

## Selbsttest-Fragenkatalog (für Quiz) — Vertiefung

1. Wie funktioniert Byte-Pair Encoding im Grundprinzip, und warum kostet "Komponentenvertrieb" mehr Tokens als "Haus"?
2. Was bezeichnet das "Vokabular" eines Modells, und welcher Zielkonflikt steckt in seiner Größe?
3. Erkläre die Rollen von Query, Key und Value in der Attention mit eigener Analogie.
4. Was leistet Multi-Head Attention zusätzlich zu einfacher Attention?
5. Warum wächst der Attention-Aufwand quadratisch, und welche praktische Folge hat das?
6. Wozu dient die Positionskodierung, und welches Problem löst sie?
7. Worin unterscheiden sich statische und kontextuelle Embeddings? Nenne das "Bank"-Beispiel.
8. Beschreibe die vier Schritte der Trainingsschleife (Vorhersage, Loss, Gradient, Anpassung).
9. Was ist der Unterschied zwischen Overfitting und Catastrophic Forgetting?
10. Wie funktioniert LoRA, und warum ist es so viel sparsamer als volles Fine-tuning?
11. Vergleiche RLHF und DPO: Was lässt DPO weg, und warum ist es 2026 Standard?
12. Wann sollte man fine-tunen und wann lieber RAG nutzen? Nenne die Faustregel.
13. Was bedeutet "Test-Time Compute", und warum verbessert mehr Denken die Ergebnisse?
14. An welcher Art von Aufgaben werden Reasoning-Modelle bevorzugt mit RL trainiert, und warum?
15. Warum ist die Chunking-Strategie für RAG-Qualität so entscheidend?
16. Was ist hybride Suche, und welches Problem reiner semantischer Suche behebt sie?
17. Beschreibe die ReAct-Schleife mit ihren drei Phasen.
18. Wann fügt man einem Agenten Reflection hinzu, und welche Gefahr birgt zu viel davon?
19. Wann lohnt sich ein Multi-Agent-System, und was kostet es?
20. Was unterscheidet Context Engineering vom Prompt Engineering?
21. Was bewirkt Quantisierung, und warum ermöglicht sie Modelle auf schwacher Hardware?
22. Wozu dient KV-Caching bei der Inferenz?
23. Wie funktioniert Destillation, und warum sind dadurch kleine Modelle 2026 so stark?
24. Was ist "LLM-as-a-Judge", und welche typischen Verzerrungen hat dieser Ansatz?
25. Warum ist ein eigener, realitätsnaher Eval-Satz aussagekräftiger als ein öffentliches Benchmark-Ranking?

---

## Quellen (Auswahl, Stand Mai 2026)

- Fine-tuning (LoRA/QLoRA/SFT/DPO/RLHF/ORPO/KTO/RLAIF): mobisoftinfotech.com; patsnap.com; futureagi.com; bigdataboutique.com; hjlabs.in; secondtalent.com; arXiv 2309.00267 (RLAIF)
- Reasoning-Mechanik: OpenAI GPT-5.5 System Card; arXiv 2505.19676 (Reasoning Stalls)
- RAG-Vertiefung: Pinecone; Google Cloud; IBM Think; writer.com; techment.com; US-Patent 12450217
- Agenten-Muster (ReAct/Reflexion/Plan-Execute/Multi-Agent): sitepoint.com; augmentcode.com; dev.to (G. Anhaia; L. Hao); digitalapplied.com; n1n.ai; innovatrixinfotech.com
- Inferenz-Optimierung & Architektur: WhatLLM.org (subquadratisch, MoE); ai2.work (Caching)
- Evaluation: Medium/LLM Evaluation in 2026
- Standards (MCP/A2A): sitepoint.com; a2a-mcp.org

*Hinweis: Alle Inhalte sind eigenständig zusammengefasst und paraphrasiert. Verfahrensnamen, Werkzeuge und Zahlen sind Momentaufnahmen von Mai 2026.*
