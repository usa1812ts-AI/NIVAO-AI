# KI & Große Sprachmodelle — Eine umfassende Wissensbasis

> ⚠️ **Quellstrategie (P1.5):** Die verbindliche Inhaltsquelle ist `ki-verstehen.html`.
> Diese Datei ist **historische Prosa-Fassung** (gut für NotebookLM-Podcast-Generierung).
> Für eine aktuell synchronisierte Version: `python3 export_md.py` → `KI-Wissensbasis-Export.md`.
> Korrekturen und neue Inhalte gehören immer zuerst in `ki-verstehen.html`.

> **Zweck dieses Dokuments**
> Diese Datei ist als Quellmaterial für NotebookLM gedacht. Aus ihr lassen sich Quiz, Karteikarten und ein Audio-Podcast erzeugen. Sie ist deshalb bewusst in zusammenhängender Prosa geschrieben (gut für Podcast-Erzeugung), enthält am Ende aber zusätzlich ein kompaktes Glossar (gut für Karteikarten) und einen Selbsttest-Fragenkatalog (gut für Quiz).
>
> **Stand:** Ende Mai 2026. Modellversionen und Preise ändern sich im KI-Bereich teils im Wochentakt — die *Konzepte* sind stabil, die konkreten *Versionsnummern* sind Momentaufnahmen.
>
> **Aufbau:** Teil 1 Grundlagen → Teil 2 Wie Modelle entstehen und arbeiten → Teil 3 Mit Modellen arbeiten → Teil 4 Die Anbieter-Landschaft 2026 → Teil 5 Praxis-Prinzipien → Glossar → Selbsttest → Quellen.

---

## Teil 1 — Die Grundlagen

### 1. Die Begriffspyramide: KI, Machine Learning, Deep Learning, Generative KI

Diese vier Begriffe werden oft synonym verwendet, stehen aber in einer klaren Hierarchie zueinander, von weit zu eng:

**Künstliche Intelligenz (KI / AI)** ist der Oberbegriff. Er umfasst jedes System, das Aufgaben löst, die normalerweise menschliche Intelligenz erfordern — von einfachen Regelwerken bis zu lernenden Systemen.

**Machine Learning (ML)** ist eine Teilmenge der KI. Statt feste Regeln zu programmieren, lernt das System Muster aus Daten. Man gibt ihm Beispiele, nicht Anweisungen. Ein Spam-Filter, der aus Tausenden markierter E-Mails lernt, ist klassisches ML.

**Deep Learning** ist wiederum eine Teilmenge von ML. Es nutzt künstliche neuronale Netze mit vielen Schichten ("tief"). Diese Tiefe erlaubt es, sehr komplexe Muster zu erfassen — etwa in Bildern, Sprache oder Text.

**Generative KI (GenAI)** ist die jüngste Ausprägung. Während klassisches ML oft *klassifiziert* ("Spam oder nicht Spam?"), *erzeugt* generative KI neue Inhalte: Text, Bilder, Code, Audio. Große Sprachmodelle gehören hierher.

Merksatz: Jedes große Sprachmodell ist generative KI, ist Deep Learning, ist Machine Learning, ist KI — aber nicht jede KI ist ein Sprachmodell.

### 2. Tokens und Tokenisierung — die Bausteine

Ein Sprachmodell verarbeitet Sprache nicht in ganzen Wörtern, sondern in **Tokens**. Ein Token ist ein Textbaustein: meist ein Wortteil, manchmal ein ganzes kurzes Wort, manchmal ein Satzzeichen. Das Wort "Maschinenbau" könnte ein Modell etwa in "Maschinen" und "bau" zerlegen.

Der Prozess, Text in Tokens zu zerlegen, heißt **Tokenisierung**. Eine grobe Faustregel für Englisch lautet: ein Token entspricht etwa 0,75 Wörtern, oder etwa vier Zeichen. Deutsch ist "teurer", weil lange zusammengesetzte Wörter (Komposita wie "Komponentenvertrieb") in mehr Tokens zerfallen.

Warum das praktisch wichtig ist: Sowohl das **Kontextfenster** eines Modells (wie viel es gleichzeitig "lesen" kann) als auch die **Kosten** bei der Nutzung über eine Programmierschnittstelle (API) werden in Tokens gemessen — nicht in Wörtern oder Zeichen. Wer mit KI arbeitet, denkt deshalb in Tokens.

### 3. Next-Token-Prediction — der eine Kernmechanismus

Dies ist das wichtigste Konzept überhaupt, um zu verstehen, was ein Sprachmodell tut. Im Kern macht ein großes Sprachmodell nur **eine einzige Sache**: Es sagt das wahrscheinlich nächste Token voraus. Dann hängt es dieses Token an, betrachtet die nun längere Sequenz und sagt erneut das nächste Token voraus. Token für Token, bis die Antwort fertig ist. Dieses schrittweise Erzeugen nennt man auch "autoregressiv".

Das hat eine tiefgreifende Konsequenz: Ein Sprachmodell "versteht" einen Text nicht im menschlichen Sinn und besitzt keine Datenbank mit Fakten, die es nachschlägt. Es berechnet Wahrscheinlichkeiten auf Basis der Muster, die es während des Trainings in riesigen Textmengen gesehen hat. Es ist im Grunde eine extrem ausgefeilte Vervollständigungsmaschine.

Genau hieraus erklärt sich auch das Phänomen der **Halluzination** (siehe Abschnitt 10): Ein flüssig formulierter, aber faktisch falscher Satz kann statistisch genauso "plausibel" wirken wie ein korrekter. Das Modell optimiert auf Plausibilität der Fortsetzung, nicht auf Wahrheit. Eine selbstbewusst vorgetragene Falschaussage ist daher kein "Programmfehler", sondern eine systembedingte Eigenschaft des Mechanismus.

### 4. Parameter und Modellgröße

**Parameter** sind die internen Stellschrauben eines neuronalen Netzes, technisch "Gewichte" genannt. Während des Trainings werden sie millionen- bis milliardenfach justiert, bis das Modell gute Vorhersagen trifft. Eine Angabe wie "70B" bedeutet 70 Milliarden Parameter. Man kann sich Parameter als das "geronnene Wissen" des Modells vorstellen — alles, was es gelernt hat, steckt in diesen Zahlenwerten.

Lange galt: mehr Parameter gleich besser. Das stimmt nur noch eingeschränkt. 2026 zeigen kleinere, effizient gebaute Modelle teils Leistung nahe an den größten Modellen — bei einem Bruchteil der Rechenkosten. Möglich macht das vor allem eine Architektur namens **Mixture of Experts (MoE)**: Das Modell besteht aus vielen spezialisierten Teilnetzen ("Experten"), aber pro Anfrage wird nur ein kleiner Teil davon aktiviert. So kann ein Modell viele Gesamtparameter haben, aber nur wenige "aktive" Parameter pro Token verarbeiten — das spart Rechenleistung. Ein Beispiel aus dem Frühjahr 2026 ist ein quelloffenes Modell mit 8 Milliarden Gesamtparametern, von denen nur rund 760 Millionen pro Token aktiv sind, das dennoch nahe an Spitzenleistung im logischen Schließen reicht (Quelle: WhatLLM.org, Mai 2026).

### 5. Embeddings und Vektorräume — wie Bedeutung berechenbar wird

Ein **Embedding** ist die Übersetzung eines Tokens, Wortes, Satzes oder ganzen Dokuments in eine Liste von Zahlen — einen **Vektor**. Dieser Vektor lebt in einem hochdimensionalen Raum (oft Hunderte oder Tausende Dimensionen). Der entscheidende Trick: Inhalte mit ähnlicher Bedeutung erhalten ähnliche Vektoren und liegen im Raum dicht beieinander.

Ein klassisches Beispiel: Die Vektoren für "König" und "Königin" liegen nahe beieinander, ebenso "Mann" und "Frau". Bemerkenswerterweise lassen sich sogar Rechenoperationen durchführen, die Bedeutung abbilden — die berühmte Analogie "König minus Mann plus Frau ergibt ungefähr Königin". Bedeutung wird so zu Geometrie, und Geometrie ist berechenbar.

Wie misst man Ähnlichkeit zwischen zwei Vektoren? Häufig über die **Kosinus-Ähnlichkeit** — vereinfacht: den Winkel zwischen den Vektoren. Kleiner Winkel bedeutet ähnliche Bedeutung.

Embeddings sind das Fundament für die **semantische Suche** (Suche nach Bedeutung statt nach exakten Stichwörtern) und für RAG (siehe Abschnitt 13). Sie sind einer der Gründe, warum moderne KI nach Sinn und nicht nur nach Buchstaben suchen kann.

### 6. Die Transformer-Architektur und der Attention-Mechanismus

Fast alle modernen Sprachmodelle beruhen auf der **Transformer-Architektur**, vorgestellt 2017 im Aufsatz "Attention Is All You Need". Sie löste ältere Ansätze ab, die Text strikt Wort für Wort von links nach rechts verarbeiteten und dabei Mühe mit langen Zusammenhängen hatten.

Das Herzstück des Transformers ist der **Attention-Mechanismus** (Aufmerksamkeit). Vereinfacht erlaubt er dem Modell, beim Verarbeiten jedes Tokens zu gewichten, *welche anderen Tokens im Text gerade besonders relevant sind*. Im Satz "Der Ingenieur prüfte die Komponente, weil sie defekt war" muss das Modell erkennen, dass sich "sie" auf "die Komponente" bezieht, nicht auf "der Ingenieur". Attention macht genau das: Es richtet die Aufmerksamkeit auf die relevanten Bezüge — und das parallel über den gesamten Text, nicht nur sequenziell.

Diese Parallelverarbeitung ist auch der Grund, warum Transformer sich so gut auf riesigen Rechenclustern trainieren lassen. Der Buchstabe "T" in GPT steht genau dafür: **G**enerative **P**re-trained **T**ransformer.

---

## Teil 2 — Wie Modelle entstehen und arbeiten

### 7. Die Trainingsphasen: Pretraining, Fine-tuning, RLHF und Constitutional AI

Ein modernes Sprachmodell entsteht in mehreren Stufen:

**Pretraining (Vortraining):** Das Modell lernt aus enormen Textmengen — großen Teilen des öffentlich zugänglichen Internets, lizenzierten Datenbeständen und weiteren Quellen — schlicht, das nächste Token vorherzusagen. In dieser Phase baut es sein breites Sprach- und Weltwissen auf. Das ist der mit Abstand teuerste und rechenintensivste Schritt.

**Fine-tuning (Feinabstimmung):** Das vortrainierte Modell wird mit kleineren, gezielten Datensätzen nachgeschärft, etwa um Anweisungen besser zu folgen ("Instruction Tuning") oder um in einer bestimmten Fachdomäne besser zu werden.

**RLHF — Reinforcement Learning from Human Feedback:** Hier bewerten Menschen verschiedene Modellantworten, und das Modell lernt, Antworten zu bevorzugen, die Menschen hilfreicher, ehrlicher und harmloser finden. RLHF war ein zentraler Grund, warum Sprachmodelle ab etwa 2022 plötzlich so brauchbar als Assistenten wurden.

**Constitutional AI (CAI):** Ein von Anthropic entwickelter Ansatz, der RLHF ergänzt. Statt sich allein auf menschliche Einzelbewertungen zu stützen, gibt man dem Modell einen Satz schriftlicher Prinzipien (eine "Verfassung") und lässt es sein eigenes Verhalten gegen diese Prinzipien prüfen und verbessern. Die Idee: ethisches Urteilsvermögen, das mit der Modellfähigkeit mitwächst, statt eines starren Regelfilters. Laut mehreren Branchenberichten wuchs diese Verfassung von ursprünglich 75 Leitsätzen (2022) auf rund 23.000 Wörter im Jahr 2026 an und enthält inzwischen auch die Begründung hinter jeder Regel (Quellen: webwallah.in, buildfastwithai.com, 2026).

### 8. Das Kontextfenster

Das **Kontextfenster** ist die Menge an Text (gemessen in Tokens), die ein Modell bei einer einzelnen Anfrage gleichzeitig "im Blick" behalten kann — Eingabe und Ausgabe zusammen. Es ist eine Art Arbeitsgedächtnis. Was außerhalb des Fensters liegt, "sieht" das Modell nicht.

Die Fenster sind dramatisch gewachsen. 2026 bieten Spitzenmodelle von Anthropic, OpenAI und Google Kontextfenster von rund einer Million Tokens — genug für ganze Code-Repositorys oder umfangreiche Dokumentensammlungen (Quellen: Modellkarten von Anthropic, Google DeepMind; OpenAI-Dokumentation, 2026). Wichtig: Ein großes Fenster bedeutet nicht, dass das Modell jeden Teil gleich gut nutzt. Bei sehr langen Eingaben kann die Aufmerksamkeit "in der Mitte" nachlassen — ein Phänomen, das gern als "lost in the middle" bezeichnet wird.

Das Kontextfenster ist nicht zu verwechseln mit dauerhaftem Gedächtnis: Standardmäßig "vergisst" ein Modell nach einer Anfrage alles wieder. Funktionen wie persistente Erinnerung oder das Mitsenden bisheriger Gesprächsverläufe sind nachgelagerte Mechaniken, kein eingebautes Langzeitgedächtnis des Modells selbst.

### 9. Inferenz, Temperature und Sampling

**Inferenz** ist der Vorgang, bei dem ein fertig trainiertes Modell tatsächlich genutzt wird, um Antworten zu erzeugen (im Gegensatz zum Training). Inferenz ist heute ein erheblicher Kostenfaktor im Betrieb von KI-Diensten.

Bei jedem Schritt der Next-Token-Prediction erzeugt das Modell eine Wahrscheinlichkeitsverteilung über mögliche nächste Tokens. Wie daraus eines ausgewählt wird, steuern Parameter:

**Temperature (Temperatur):** Sie regelt die Zufälligkeit. Eine niedrige Temperatur (nahe 0) macht das Modell deterministischer und konservativer — es wählt fast immer das wahrscheinlichste Token. Eine höhere Temperatur erhöht die Vielfalt und "Kreativität", aber auch das Risiko von Abwegigem. Für faktische Aufgaben wählt man niedrig, für kreatives Schreiben eher höher.

**Top-p / Top-k:** Weitere Stellschrauben, die die Auswahl auf die wahrscheinlichsten Kandidaten eingrenzen (etwa: nur aus den Tokens wählen, die zusammen 90 Prozent der Wahrscheinlichkeit ausmachen).

### 10. Halluzinationen und systembedingte Grenzen

Eine **Halluzination** ist eine Modellausgabe, die plausibel klingt, aber faktisch falsch oder frei erfunden ist — etwa eine erfundene Quelle, ein falsches Datum, eine nicht existierende Funktion. Wie in Abschnitt 3 erklärt, ist das kein Zufallsfehler, sondern eine Folge des Grundmechanismus: Das Modell erzeugt die plausibelste Fortsetzung, nicht die nachweislich wahre.

Gegenmaßnahmen sind unter anderem: das Modell mit verlässlichen Quellen "erden" (RAG, Abschnitt 13), ihm Werkzeuge zum Nachschlagen geben (Tool Use, Abschnitt 14), niedrigere Temperatur, und das Modell zum schrittweisen Nachdenken anregen (Chain of Thought, Abschnitt 12). Neuere Modelle bauen teils Selbstprüfung ein, bei der sie eigene Ausgaben gegenprüfen.

Weitere systembedingte Grenzen: Modelle haben einen **Wissensstichtag** (alles nach dem Training kennen sie nicht von sich aus), sie können bei einfachen logischen oder arithmetischen Aufgaben überraschend scheitern, und ihre Leistung hängt stark von der Qualität der Eingabe ab. Forschungsarbeiten von 2025 und 2026 zeigen, dass selbst Spitzenmodelle bei bestimmten "eigentlich leichten" Denkaufgaben patzen (Quellen: arXiv-Aufsätze, Google DeepMind u. a.).

---

## Teil 3 — Mit Modellen arbeiten

### 11. Prompt Engineering

**Prompt Engineering** ist die Fertigkeit, Eingaben (Prompts) so zu formulieren, dass das Modell möglichst nützliche Ausgaben liefert. Es ist keine reine Faktenkenntnis, sondern eine Übungssache. Wichtige Grundtechniken:

**Zero-Shot-Prompting:** Man stellt die Aufgabe direkt, ohne Beispiele. "Übersetze diesen Satz ins Englische." Funktioniert bei einfachen, klaren Aufgaben gut.

**Few-Shot-Prompting:** Man gibt dem Modell einige Beispiele für das gewünschte Eingabe-Ausgabe-Muster, bevor man die eigentliche Aufgabe stellt. Das Modell erkennt das Muster und überträgt es. Sehr wirksam, um Format und Stil zu steuern.

**Rollen- und Kontextvorgabe:** Man weist dem Modell eine Rolle zu ("Du bist ein erfahrener Vertriebsingenieur") und liefert relevanten Kontext. Das verschiebt die Wahrscheinlichkeitsverteilung in Richtung passender Antworten.

**Strukturvorgaben:** Klare Anweisungen zu Format, Länge, Ton und Negativbeispiele ("vermeide Fachjargon") verbessern die Ergebnisse erheblich.

Faustregeln für gute Prompts: präzise und detailliert sein; positive wie negative Beispiele geben; schrittweises Denken anregen; bei strukturierten Ausgaben das gewünschte Format explizit verlangen; Länge und Form festlegen.

### 12. Chain of Thought und Reasoning-Modelle

**Chain of Thought (CoT)** — auf Deutsch "Gedankenkette" — bezeichnet die Technik, ein Modell dazu zu bringen, ein Problem in nachvollziehbaren Zwischenschritten zu durchdenken, statt sofort eine Endantwort auszuwerfen. Der berühmte Auslöser ist die simple Anweisung "Lass uns Schritt für Schritt denken". Erstaunlicherweise verbessert das die Trefferquote bei logischen, mathematischen und mehrstufigen Aufgaben deutlich — weil das Modell so seine eigene Zwischenarbeit als Kontext nutzt und nicht in einem Sprung zur Antwort springen muss.

Aus dieser Idee sind die **Reasoning-Modelle** (Denk- oder "Thinking"-Modelle) hervorgegangen — eine der prägenden Entwicklungen seit 2024/2025. Diese Modelle wurden gezielt darauf trainiert (unter anderem mit bestärkendem Lernen), vor der eigentlichen Antwort intern ausführlich zu "denken". Sie erzeugen oft viele interne Denk-Tokens, die der Nutzer gar nicht oder nur zusammengefasst sieht. 2026 bieten die großen Anbieter abgestufte Denktiefen an: OpenAI etwa erlaubt bei GPT-5.5 eine einstellbare "reasoning effort" von niedrig bis sehr hoch; Anthropic nutzt bei Claude Mechanismen wie adaptives Nachdenken und Effort-Steuerung; Google bietet bei Gemini einstellbare Denkstufen (Quellen: OpenAI-Dokumentation; Lorka.ai; MindStudio, 2026).

Wichtig zu wissen: Mehr Denken kostet mehr Tokens, mehr Zeit und mehr Geld. Für einfache Aufgaben ist ein schnelles Standardmodell oft die bessere Wahl als ein langsames Reasoning-Modell.

### 13. RAG — Retrieval Augmented Generation

**RAG** verbindet ein Sprachmodell mit einer externen Wissensquelle, damit es Antworten auf Basis aktueller, firmenspezifischer oder sonst nicht im Training enthaltener Daten geben kann. RAG ist eine der wichtigsten Methoden, um Halluzinationen zu senken und Modelle mit Fachwissen zu "erden".

Der Ablauf in drei Schritten (Retrieve, Augment, Generate):

1. **Vorbereitung (einmalig):** Die externen Dokumente werden in kleine Stücke zerlegt ("Chunking"), jedes Stück wird per Embedding-Modell in einen Vektor übersetzt und in einer **Vektordatenbank** gespeichert.
2. **Retrieve (Abrufen):** Kommt eine Nutzerfrage, wird auch sie in einen Vektor übersetzt. Die Vektordatenbank sucht per Ähnlichkeit (semantische Suche) die passendsten Textstücke heraus. Moderne Systeme kombinieren das oft mit klassischer Stichwortsuche zu einer **hybriden Suche** und sortieren die Treffer per "Re-Ranker" nach.
3. **Augment & Generate (Anreichern & Erzeugen):** Die gefundenen Textstücke werden zusammen mit der ursprünglichen Frage als Kontext an das Modell gegeben. Das Modell formuliert die Antwort gestützt auf diese mitgelieferten Fakten.

Der große Vorteil: Man muss das Modell nicht neu trainieren, um es mit neuem Wissen zu versorgen — man aktualisiert einfach die Datenbank. RAG liefert zudem nachvollziehbare Quellen und ist deshalb 2026 ein Standardbaustein in Unternehmen, gerade wo Erklärbarkeit und geprüfter Zugriff auf eigenes Wissen zählen (Quellen: IBM, AWS, Google Cloud, Pinecone, 2025/2026). Ein Sicherheitshinweis aus der Praxis: Eine unverschlüsselte Vektordatenbank kann ein Angriffsziel sein, da sich aus Embeddings teils Rückschlüsse auf die Originaldaten ziehen lassen (Quelle: IBM, 2026).

### 14. Tool Use, Function Calling und das Model Context Protocol (MCP)

Ein Sprachmodell allein kann nur Text erzeugen. Es kann von sich aus nicht im Web suchen, keine E-Mail senden, keine Datenbank abfragen, nicht rechnen mit garantierter Genauigkeit. **Tool Use** (Werkzeugnutzung), auch **Function Calling** genannt, behebt das: Man stellt dem Modell eine Liste von Werkzeugen (Funktionen) bereit. Das Modell entscheidet dann selbst, wann es welches Werkzeug mit welchen Parametern aufruft, erhält das Ergebnis zurück und arbeitet damit weiter. So kann es rechnen, suchen, Aktionen auslösen.

Lange musste jede Verbindung zwischen einem Modell und einem Werkzeug einzeln, maßgeschneidert programmiert werden — ein Flickenteppich. Hier setzt das **Model Context Protocol (MCP)** an: ein offener, herstellerneutraler Standard, den Anthropic Ende 2024 veröffentlichte. MCP definiert einheitlich, wie KI-Anwendungen mit externen Werkzeugen und Datenquellen sprechen — vergleichbar mit der Rolle, die USB-C für Geräteanschlüsse spielt, oder REST für Web-Dienste. Statt für jede Kombination aus Modell und Dienst eine Einzellösung zu bauen, schreibt man einen MCP-Server einmal, und jeder MCP-fähige Client kann ihn nutzen.

MCP kennt im Kern drei Bausteine: **Tools** (ausführbare Funktionen, die das Modell aufrufen kann), **Resources** (lesbare Datenquellen als Kontext) und **Prompts** (wiederverwendbare Vorlagen für wiederkehrende Abläufe). Technisch läuft die Kommunikation über JSON-RPC.

Die Verbreitung war rasant: Nach dem Start Ende 2024 übernahmen innerhalb von Monaten auch OpenAI, Google DeepMind und Microsoft den Standard; bis 2026 entstanden Tausende öffentlicher MCP-Server (etwa für GitHub, Slack, Datenbanken) und die Governance ging an eine herstellerübergreifende Stiftung über (Quellen: sitepoint.com, a2a-mcp.org, devstarsj, 2026). MCP gilt damit 2026 als faktischer Standard für die Anbindung von KI-Agenten an die Außenwelt.

### 15. Agents und Agentic Coding — und die Abgrenzung zum Prompt Engineering

Hier liegt eine der wichtigsten begrifflichen Unterscheidungen, und sie wird oft verwechselt.

**Prompt Engineering** (Abschnitt 11) ist *die Kunst, eine einzelne Anfrage gut zu formulieren*. Der Mensch stellt eine Frage, das Modell antwortet, fertig. Es ist eine wertvolle Grundfertigkeit und bleibt auch 2026 relevant — aber es ist nur ein Baustein.

Ein **KI-Agent** geht darüber hinaus: Er bekommt ein *Ziel* statt einer Einzelfrage und arbeitet dann selbstständig in einer Schleife, um es zu erreichen. Er plant Schritte, ruft Werkzeuge auf (Tool Use, MCP), liest deren Ergebnisse, korrigiert sich und macht weiter — oft über viele Schritte und längere Zeiträume ("long-horizon tasks"). Was einen Agenten ausmacht, ist diese *anhaltende, eigenständige Ausführung*, nicht das bessere Formulieren einer Frage.

**Agentic Coding** (auch "Agentic Engineering") ist die Anwendung dieses Prinzips auf Softwareentwicklung. Traditionell sah die Entwicklungsschleife so aus: Code schreiben, Tests laufen lassen, Fehler lesen, Code korrigieren, wiederholen — mit dem Menschen als ständigem Treiber bei jedem Schritt. Beim Agentic Coding übernimmt ein KI-Agent diese Schleife selbst: Er schreibt Code, führt ihn aus, liest die Ausgabe, behebt, was gebrochen ist, und macht weiter, bis die Aufgabe erledigt ist. Der Mensch setzt das Ziel und prüft das Ergebnis (Quellen: MindStudio, IBM, CIO, 2026).

Abzugrenzen davon ist **Vibe Coding**, ein Begriff, den Andrej Karpathy 2025 prägte: das eher freie, sprunghafte Erzeugen von Code per Prompt, ohne strenge Struktur — gut für schnelle Experimente, riskant für ernsthafte Software. Agentic Engineering ist gewissermaßen das "erwachsen gewordene" Vibe Coding: Was es vom bloßen Drauflosprompten unterscheidet, sind Struktur, Spezifikationen, Test-Gerüste ("harnesses") und Prüfschleifen (Quelle: MindStudio, IBM, 2026).

Die übergeordnete Beobachtung von 2026: Die Rolle des Entwicklers verschwindet nicht, sie verschiebt sich. Karpathy formulierte 2023 noch "die heißeste neue Programmiersprache ist Englisch". Drei Jahre später dreht sich vieles eher um Kontextgestaltung, Agenten-Steuerung und Absicherung — Englisch (das natürlichsprachliche Prompten) ist weiterhin Bestandteil, aber nicht mehr das ganze System. Der Engpass wandert vom "Kann ich diesen Code schreiben?" zum "Kann ich die Aufgabe klar genug spezifizieren, dass ein Agent sie zuverlässig ausführt?" (Quellen: bits-bytes-nn.github.io, CIO, 2026). Anthropics terminalbasiertes Werkzeug Claude Code ist ein bekanntes Beispiel für ein agentisches Coding-Werkzeug; bei den Benchmarks für agentisches Programmieren führten 2026 wiederholt Modelle der Claude-Opus-Reihe (Quelle: MindStudio, 2026).

---

## Teil 4 — Die Anbieter-Landschaft 2026

### 16. Die großen Anbieter im Überblick

Das Frühjahr 2026 war ungewöhnlich dicht an Modellveröffentlichungen — innerhalb weniger Wochen brachten mehrere Anbieter neue Spitzenmodelle heraus. Das Feld ist wettbewerbsintensiv und unübersichtlich geworden; "welches Modell soll ich nehmen?" verlangt heute eine echte, aufgabenabhängige Antwort (Quelle: AI/ML API Blog, 2026).

**Anthropic (Claude).** Gegründet 2021 von ehemaligen OpenAI-Forschern (Dario und Daniela Amodei), positioniert als Sicherheits-fokussiertes Unternehmen. Kennzeichen ist Constitutional AI (Abschnitt 7). Die Modelle erscheinen seit Claude 3 in drei Stufen: **Haiku** (am schnellsten und günstigsten), **Sonnet** (ausgewogenes Arbeitstier), **Opus** (am leistungsfähigsten, für komplexes Denken, Schreiben und Programmieren). Die Opus-Reihe führte 2026 wiederholt Benchmarks im Programmieren und bei anspruchsvollem Fachwissen an und bietet ein Kontextfenster von rund einer Million Tokens. Im Lauf des Jahres folgten in kurzer Taktung Versionen wie Opus 4.6, 4.7 und 4.8. Anthropic prägte außerdem das MCP (Abschnitt 14) und bietet das agentische Coding-Werkzeug Claude Code (Quellen: startuphub.ai, webwallah.in, releasebot.io, 2026).

**OpenAI (GPT / ChatGPT).** Anbieter des bekanntesten Consumer-Produkts ChatGPT mit über 200 Millionen wöchentlichen Nutzern. Die frühere getrennte "o-Reihe" reiner Reasoning-Modelle ist inzwischen in die GPT-5-Familie eingeflossen. Das Spitzenmodell GPT-5.5 (April 2026) ist stark auf langlaufende agentische Aufgaben ausgelegt und bietet einstellbare Denktiefen (von "none" bis "xhigh"). Ein leichteres "Instant"-Modell dient als schneller Standard im ChatGPT-Alltag (Quellen: OpenAI, MindStudio, TechCrunch, 2026).

**Google (Gemini).** Die Gemini-3-Reihe (etwa Gemini 3.1 Pro, Februar 2026) ist von Grund auf **nativ multimodal** — sie verarbeitet Text, Bilder, Audio, Video und Code in einem einzigen Modell, ohne separate Spezialmodelle. Sie nutzt eine Transformer-basierte Mixture-of-Experts-Architektur, bietet ein Kontextfenster von rund einer Million Tokens und einstellbare Denkstufen. Bemerkenswert für dich: Google Gemini treibt unter anderem NotebookLM an — das Werkzeug, in das diese Datei eingespielt wird (Quellen: Google DeepMind Modellkarte, blog.google, llm-stats.com, 2026).

**Quelloffene und kostengünstige Anbieter.** 2026 ist nicht mehr nur ein Rennen der drei Großen. Modelle wie DeepSeek V4, Alibabas Qwen-Reihe oder Kimi bieten zunehmend Spitzen-nahe Leistung — teils unter offenen Lizenzen und mit drastisch gesenkten Kosten. Damit haben auch budgetbeschränkte Teams einen glaubwürdigen Weg zu hochwertiger Reasoning- und Coding-Leistung, ohne Spitzenpreise zu zahlen. Geschlossene Spitzenmodelle behalten ihren Vorsprung dort, wo es am schwersten ist: bei den härtesten akademischen Denkaufgaben, den breitesten Agenten-Ökosystemen und den komplexesten multimodalen Abläufen (Quelle: AI/ML API Blog, 2026).

### 17. Wie man das richtige Modell auswählt

Es gibt 2026 kein pauschal "bestes" Modell mehr — die richtige Wahl hängt von der Aufgabe ab. Sinnvolle Auswahlkriterien:

- **Aufgabentyp:** Reine Chat-Antwort, langes Dokument, agentisches Programmieren, multimodale Analyse — jede Aufgabe hat andere passende Modelle.
- **Geschwindigkeit vs. Tiefe:** Schnelle, günstige Modelle (Haiku-/Flash-/Instant-Klasse) für einfache, häufige Aufgaben; teure Reasoning-Modelle nur für wirklich harte Probleme.
- **Kosten:** Gemessen in Preis pro Million Tokens (Eingabe und Ausgabe getrennt). Sehr lange Eingaben können überproportional teuer werden.
- **Kontextfenster:** Wie viel Material muss das Modell gleichzeitig verarbeiten?
- **Datenschutz und Hosting:** Cloud-API versus selbst gehostetes, quelloffenes Modell für sensible Daten.
- **Ökosystem:** Verfügbarkeit von Werkzeugen, MCP-Servern, Integrationen.

### 18. Benchmarks und ihre Grenzen

**Benchmarks** sind standardisierte Testsätze, mit denen Modelle verglichen werden — etwa SWE-bench (Programmieren), GPQA (Wissenschaft auf Promotionsniveau), MMLU (breites Wissen), AIME (Mathematik) oder ARC-AGI (abstraktes Schließen).

Man sollte Benchmark-Zahlen mit Vorsicht lesen. 2026 sind viele klassische Benchmarks "gesättigt" — Spitzenmodelle erreichen nahezu perfekte Werte, womit der Test seine Unterscheidungskraft verliert. Schlimmer noch: Es gibt das Problem der **Daten-Kontamination** — wenn Testaufgaben (oder deren Lösungen) ins Trainingsmaterial geraten sind, glänzt das Modell nicht durch Können, sondern durch Erinnerung. Die Branche reagiert mit ständig erneuerten Tests und Aufgaben, die nachweislich nach dem Trainingsstichtag entstanden sind (Quelle: Medium/LLM Evaluation 2026; arXiv, 2026). Praktische Lehre: Der beste "Benchmark" ist oft der eigene, realitätsnahe Test auf den eigenen Aufgaben.

### 19. Multimodalität

**Multimodalität** bedeutet, dass ein Modell mehr als nur Text verarbeiten kann — etwa Bilder, Audio, Video und Code. **Nativ multimodal** heißt, dass das Modell von Grund auf für mehrere Modalitäten gebaut wurde (wie Gemini 3), statt nachträglich Spezialmodule anzukoppeln. Praktisch erlaubt das, ein Diagramm zu interpretieren, ein Foto einer Präsentation zusammenzufassen, gesprochene Sprache zu verarbeiten oder lange Videos zu analysieren — alles im selben Modell.

### 20. Sicherheit, Datenschutz und Ethik

Mit wachsender Leistungsfähigkeit steigen die Risiken. Wichtige Themenfelder:

- **Prompt Injection:** Schädliche Anweisungen, die in Inhalten versteckt sind, die ein Modell verarbeitet (etwa in einer Webseite oder E-Mail), und das Modell zu unerwünschten Aktionen verleiten sollen. Besonders heikel bei Agenten mit Werkzeugzugriff. Grundregel: Inhalte aus externen Quellen sind Daten, keine Befehle.
- **Datenschutz:** Sensible Daten (Passwörter, Konto- und Ausweisnummern, Gesundheitsdaten) gehören nicht ungeschützt in Prompts oder Vektordatenbanken.
- **Bias und Fairness:** Modelle übernehmen Verzerrungen aus ihren Trainingsdaten.
- **Cybersicherheit:** KI kann zunehmend Software-Schwachstellen finden — was Verteidigern wie Angreifern hilft. Anbieter investieren daher stark in Schutzmaßnahmen.
- **Sicherheitskultur der Anbieter:** Ansätze wie Constitutional AI, Modell-"System Cards" und abgestufte Freigaben sollen Risiken senken; vorsichtigere Modelle lehnen manche Anfragen eher ab.

---

## Teil 5 — Praxis-Prinzipien (worauf du achten musst)

- **Denke in Tokens, nicht in Wörtern.** Kontext und Kosten richten sich danach; Deutsch ist token-teurer als Englisch.
- **Verwechsle Plausibilität nicht mit Wahrheit.** Ein flüssiger Satz kann falsch sein. Bei wichtigen Fakten gegenprüfen oder das Modell erden (RAG, Tool Use).
- **Wähle die Modellklasse zur Aufgabe.** Nicht für jede Kleinigkeit das teuerste Reasoning-Modell; nicht für harte Logik das schnellste Billigmodell.
- **Prompt-Qualität entscheidet.** Präzise Aufgabe, Kontext, Beispiele, Formatvorgabe. Few-Shot schlägt oft Zero-Shot.
- **Bei mehrstufigen Problemen: schrittweises Denken anregen** (Chain of Thought) oder ein Reasoning-Modell nutzen.
- **Externe Inhalte sind Daten, keine Befehle.** Schutz vor Prompt Injection, gerade bei Agenten mit Werkzeugzugriff.
- **Sensible Daten schützen.** Keine Geheimnisse in Prompts; Vektordatenbanken absichern.
- **Benchmarks kritisch lesen.** Der eigene, realitätsnahe Test zählt mehr als ein Ranking.
- **Versionsnummern altern schnell.** Konzepte bleiben stabil, konkrete Modelle nicht — Datum im Blick behalten.
- **Die Rolle des Menschen verschiebt sich.** Vom Ausführen zum Spezifizieren, Steuern und Prüfen — besonders im agentischen Arbeiten.

---

## Glossar (für Karteikarten)

**Künstliche Intelligenz (KI):** Oberbegriff für Systeme, die Aufgaben lösen, die menschliche Intelligenz erfordern.

**Machine Learning (ML):** Teilgebiet der KI; lernt Muster aus Daten statt fester Regeln.

**Deep Learning:** Teilgebiet des ML; nutzt vielschichtige neuronale Netze.

**Generative KI:** KI, die neue Inhalte erzeugt (Text, Bild, Code, Audio).

**Großes Sprachmodell (LLM):** Generatives KI-Modell, das auf Basis riesiger Textmengen Sprache verarbeitet und erzeugt.

**Token:** Kleinster Textbaustein, den ein Modell verarbeitet (meist ein Wortteil).

**Tokenisierung:** Zerlegung von Text in Tokens.

**Next-Token-Prediction:** Kernmechanismus; das Modell sagt fortlaufend das wahrscheinlich nächste Token voraus.

**Autoregressiv:** Eigenschaft, Ausgabe schrittweise zu erzeugen und das bereits Erzeugte als Kontext zu nutzen.

**Parameter (Gewichte):** Interne, trainierte Stellschrauben des Modells; "geronnenes Wissen".

**Mixture of Experts (MoE):** Architektur, bei der pro Anfrage nur ein Teil spezialisierter Teilnetze aktiv ist — effizienter.

**Embedding:** Übersetzung von Text in einen Zahlenvektor, der Bedeutung geometrisch abbildet.

**Vektor / Vektorraum:** Zahlenliste bzw. hochdimensionaler Raum, in dem ähnliche Bedeutungen nah beieinanderliegen.

**Kosinus-Ähnlichkeit:** Maß für die Ähnlichkeit zweier Vektoren (Winkel zwischen ihnen).

**Semantische Suche:** Suche nach Bedeutung statt nach exakten Stichwörtern.

**Transformer:** Vorherrschende Architektur moderner Sprachmodelle (2017).

**Attention (Aufmerksamkeit):** Mechanismus, der relevante Bezüge im Text gewichtet.

**Pretraining:** Erste, teuerste Trainingsphase auf riesigen Textmengen.

**Fine-tuning:** Nachschärfen des Modells mit gezielten Datensätzen.

**RLHF:** Reinforcement Learning from Human Feedback; Lernen aus menschlichen Bewertungen.

**Constitutional AI (CAI):** Anthropics Ansatz; Modell prüft sich gegen schriftliche Prinzipien ("Verfassung").

**Kontextfenster:** Menge an Tokens, die ein Modell gleichzeitig verarbeiten kann (Arbeitsgedächtnis).

**Inferenz:** Nutzung des fertigen Modells zur Erzeugung von Antworten.

**Temperature:** Parameter für die Zufälligkeit/Kreativität der Ausgabe.

**Halluzination:** Plausibel klingende, aber falsche oder erfundene Modellausgabe.

**Wissensstichtag:** Zeitpunkt, nach dem das Modell von sich aus nichts mehr weiß.

**Prompt:** Eingabe an das Modell.

**Prompt Engineering:** Fertigkeit, Prompts wirksam zu formulieren.

**Zero-Shot:** Aufgabe ohne Beispiele stellen.

**Few-Shot:** Aufgabe mit einigen Beispielen stellen.

**Chain of Thought (CoT):** Schrittweises Durchdenken vor der Endantwort.

**Reasoning-Modell:** Modell, das gezielt vor der Antwort intern "nachdenkt".

**RAG (Retrieval Augmented Generation):** Anbindung externer Wissensquellen zur Erdung der Antworten.

**Chunking:** Zerlegen von Dokumenten in kleine Stücke für RAG.

**Vektordatenbank:** Speicher für Embeddings; ermöglicht Ähnlichkeitssuche.

**Hybride Suche:** Kombination aus semantischer und Stichwortsuche.

**Tool Use / Function Calling:** Modell ruft externe Werkzeuge/Funktionen auf.

**MCP (Model Context Protocol):** Offener Standard (Anthropic, 2024) zur Anbindung von Werkzeugen/Daten — "USB-C für KI".

**KI-Agent:** System, das ein Ziel selbstständig in mehreren Schritten verfolgt.

**Agentic Coding:** Agent übernimmt die Programmier-Schleife (schreiben, testen, korrigieren) eigenständig.

**Vibe Coding:** Freies Code-Erzeugen per Prompt ohne strenge Struktur.

**Multimodal:** Verarbeitung mehrerer Datenarten (Text, Bild, Audio, Video).

**Benchmark:** Standardisierter Test zum Modellvergleich.

**Daten-Kontamination:** Testaufgaben gerieten ins Training — verfälscht Benchmark-Ergebnisse.

**Prompt Injection:** Versteckte schädliche Anweisungen in verarbeiteten Inhalten.

---

## Selbsttest-Fragenkatalog (für Quiz)

1. Ordne KI, Machine Learning, Deep Learning und Generative KI in ihrer Hierarchie. Welcher Begriff ist der weiteste?
2. Warum denkt man bei KI in Tokens statt in Wörtern? Nenne zwei praktische Gründe.
3. Beschreibe in einem Satz, was ein Sprachmodell im Kern tut.
4. Warum sind Halluzinationen kein Programmfehler, sondern systembedingt?
5. Was bedeutet die Angabe "70B" bei einem Modell?
6. Was ist der Vorteil einer Mixture-of-Experts-Architektur?
7. Was ist ein Embedding, und warum macht es Bedeutung berechenbar?
8. Welche Aufgabe erfüllt der Attention-Mechanismus im Transformer?
9. Nenne die wichtigsten Trainingsphasen eines Sprachmodells in der richtigen Reihenfolge.
10. Was unterscheidet Constitutional AI von reinem RLHF?
11. Was ist das Kontextfenster, und was bedeutet "lost in the middle"?
12. Wofür dient der Parameter Temperature?
13. Erkläre Zero-Shot- und Few-Shot-Prompting und wann welches sinnvoll ist.
14. Was bewirkt Chain-of-Thought-Prompting, und warum hilft es?
15. Beschreibe die drei Schritte von RAG (Retrieve, Augment, Generate).
16. Warum reduziert RAG Halluzinationen, ohne dass man das Modell neu trainieren muss?
17. Was ist der Unterschied zwischen Prompt Engineering und einem KI-Agenten?
18. Wie unterscheidet sich Agentic Coding von Vibe Coding?
19. Welches Problem löst das Model Context Protocol (MCP)? Welche drei Bausteine kennt es?
20. Nenne die drei Modellstufen von Anthropic und ihre jeweilige Stärke.
21. Was bedeutet "nativ multimodal" am Beispiel von Gemini?
22. Warum sind gesättigte Benchmarks und Daten-Kontamination ein Problem?
23. Was ist Prompt Injection, und welche Grundregel schützt davor?
24. Nach welchen Kriterien wählt man 2026 ein passendes Modell aus?
25. Inwiefern verschiebt sich die Rolle des Menschen im agentischen Arbeiten?

---

## Quellen (Auswahl, Stand Mai 2026)

- AI/ML API Blog: Top LLM Models in 2026 — aimlapi.com
- Medium (M. Nair): LLM Evaluation in 2026
- WhatLLM.org: New AI Models May 2026
- MindStudio: What Is Agentic Engineering / Agentic Coding / GPT-5.5
- IBM Think: What Is Agentic Engineering; What is RAG; Vector Databases for RAG
- CIO: How agentic AI will reshape engineering workflows in 2026
- TechTarget: Prompt engineering takes shape for devs as agentic AI dawns
- bits-bytes-nn.github.io: From Prompts to Harnesses — Four Years of AI Agentic Patterns
- Anthropic / StartupHub.ai / buildfastwithai.com / webwallah.in / NxCode / Releasebot: Claude-Modelle, Constitutional AI, Opus 4.6–4.8
- OpenAI: Introducing GPT-5 / GPT-5.5; GPT-5.5 System Card; API-Dokumentation; TechCrunch (GPT-5.5 Instant)
- Google DeepMind: Gemini 3 / 3.1 Pro Modellkarten; blog.google; llm-stats.com; almcorp.com
- RAG: AWS, Google Cloud, Pinecone, Writer.com, techment.com
- MCP: sitepoint.com, a2a-mcp.org, devstarsj.github.io, essamamdani.com, n1n.ai
- arXiv: Aufsätze zu Reasoning-Grenzen von Frontier-Modellen (2025/2026)

*Hinweis: Alle Inhalte sind eigenständig zusammengefasst und paraphrasiert. Konkrete Versionsnummern, Preise und Benchmark-Werte sind Momentaufnahmen von Mai 2026 und ändern sich laufend.*
