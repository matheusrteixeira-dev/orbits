C = {
 "name": "Deutsch",
 "meta": {
  "title": "Matheus Teixeira · Machine-Learning-Engineer und Softwareentwickler",
  "desc": "Matheus Teixeira, Machine-Learning-Ingenieur und Softwareentwickler aus Santos, Brasilien. Projekte, Fahrplan, Ausbildung, Erfahrung und Kontakt."
 },
 "skip": "Zum Inhalt springen",
 "nav": {
  "about": "Über mich",
  "projects": "Projekte",
  "education": "Ausbildung",
  "experience": "Erfahrung",
  "contact": "Kontakt",
  "lang": "Sprache",
  "sections": "Abschnitte",
  "roadmap": "Fahrplan"
 },
 "role": "Machine-Learning-Engineer · Softwareentwickler",
 "ui": {
  "pause": "Bewegung anhalten",
  "play": "Bewegung fortsetzen",
  "land": "Auf diesem Planeten landen",
  "landBtn": "Auf dem Planeten landen",
  "back": "Zurück zum System",
  "prev": "Zurück",
  "next": "Weiter",
  "source": "Quellcode auf Anfrage",
  "copy": "Kopieren",
  "copied": "Kopiert",
  "planets": "Planeten des Systems",
  "planet": "Planet {n} von 5",
  "orbit": "Umlaufbahn: {r} M vom Loch, eine Runde alle {p} s auf dem Bildschirm",
  "nogl": "Ihr Browser kann die Live-Darstellung nicht ausführen, daher wird ein Standbild gezeigt.",
  "year": "Jahr",
  "platform": "Plattform",
  "stack": "Technik",
  "visit": "{u} besuchen",
  "how": "Wie die Teile zusammenpassen",
  "checks": "Prüfungen",
  "notes": "Technische Notizen",
  "inside": "Von innen, live",
  "nextp": "Nächster Planet",
  "illus": "Diagramm, live gezeichnet",
  "shot": "Bildschirmfotos"
 },
 "about": {
  "h": "Über mich",
  "p": [
   "Ich bin Matheus, Machine-Learning-Ingenieur und Softwareentwickler aus Santos, Brasilien. Ich schreibe Software seit 2016, als ich als Webentwickler und IT-Support-Assistent bei Orion Benefícios anfing, und studiere seit 2019 an der FEI.",
   "Für meinen Master habe ich eine reproduzierbare Pipeline gebaut, die histopathologische Bilder von Brustkrebs klassifiziert. Sie verbindet ResNet-50-Merkmale mit klassischen und Quanten-Support-Vector-Machines, und ich habe sie auf IBM-Quantum-Hardware ausgeführt. Derzeit mache ich einen MBA in Data Science, KI und Analytics an der USP mit Vollstipendium, und ich bin an der FEI zur Promotion eingeschrieben, mit CAPES-Stipendium und Kursen ab Februar 2027.",
   "Neben der Forschung entwickle ich Software von Anfang bis Ende, vom Modell oder der Physik bis zur Oberfläche und zu den Tests. Die fünf Projekte unten liegen mir am meisten am Herzen."
  ],
  "facts": [
   [
    "Wohnort",
    "Santos, Brasilien"
   ],
   [
    "Sprachen",
    "Portugiesisch (Muttersprache), Englisch (C2)"
   ],
   [
    "Schwerpunkte",
    "Maschinelles Lernen, Computer Vision, Software"
   ]
  ],
  "alt": "Porträt von Matheus Teixeira",
  "term": {
   "who": "Matheus Teixeira: Machine-Learning-Ingenieur und Softwareentwickler",
   "now": [
    "MBA in Data Science, KI und Analytics an der USP, laufend",
    "Promotion in Elektrotechnik an der FEI, eingeschrieben, Kurse ab Februar 2027",
    "Offen für Stellen in Machine Learning und Softwareentwicklung"
   ],
   "lang": "pt_BR (Muttersprache)   en_US (C2, EF SET 92/100)"
  }
 },
 "projects": {
  "h": "Projekte",
  "p": "Ein Projekt pro Planet. Landen Sie auf einem Planeten für die ganze Geschichte."
 },
 "proj": {
  "isaac": {
   "sub": "Interaktive 3D-Physiksimulationen",
   "world": "Vulkanwelt",
   "sum": "Physik zum Ausprobieren im Browser. Eine Rust-Engine, kompiliert zu WebAssembly, rechnet die Simulationen, und React, TypeScript und Three.js zeichnen sie.",
   "hl": [
    "Physikkern in Rust, kompiliert zu WebAssembly",
    "Oberfläche in React, TypeScript und Three.js",
    "Getestet mit cargo test, Vitest und Playwright-End-to-End-Tests"
   ],
   "viz": "Ein Doppelpendel, mit RK4 in Schritten von 2 ms integriert. Der blasse Zwilling startet 0,001 rad daneben, und das Chaos trennt die beiden.",
   "lede": "Ein Physiklabor im Browser. Sie ändern einen Parameter, und Szene, Graphen und Gleichungen reagieren sofort, vom geworfenen Ball bis zum Schwarzen Loch.",
   "platform": "Web",
   "shots": [
    "Ein Doppelpendel mit Live-Graphen",
    "Startseite",
    "Bibliothek der Szenen"
   ],
   "arch": [
    [
     "Rust",
     "Physikkern"
    ],
    [
     "WebAssembly",
     "führt ihn im Browser aus"
    ],
    [
     "TypeScript",
     "Szenen-Engine"
    ],
    [
     "React + Three.js",
     "Oberfläche und 3D-Ansicht"
    ]
   ],
   "tests": [
    [
     "cargo test",
     "Physik gegen exakte Ergebnisse"
    ],
    [
     "Vitest",
     "Unit-Tests"
    ],
    [
     "Playwright",
     "ganze Abläufe, Desktop und Mobil"
    ]
   ],
   "notes": [
    [
     "Physik in Rust",
     "Die Gleichungen werden in einem Rust-Kern integriert, der zu WebAssembly kompiliert ist. TypeScript steuert die Szene, React und Three.js zeichnen Bedienelemente, Graphen und 3D-Ansicht."
    ],
    [
     "Gegen exakte Ergebnisse geprüft",
     "Jede Simulation wird mit cargo test gegen bekannte Lösungen getestet. Vitest deckt die Logik der Oberfläche ab, und Playwright spielt ganze Abläufe auf Desktop und Mobilgeräten durch."
    ],
    [
     "Von der Schule bis zur Promotion",
     "Die Szenen sind nach Gebiet der Physik und nach Niveau geordnet. Jede hat Parameter mit Einheiten, Live-Graphen, die zugrunde liegenden Gleichungen und eine geführte Erklärung."
    ]
   ]
  },
  "amadeo": {
   "sub": "Vom Audio zum Notenblatt",
   "world": "Ozeanwelt",
   "sum": "Macht aus einer Aufnahme Noten, die man bearbeiten, abspielen und teilen kann, ganz im Browser. Online, mit einem Pro-Tarif.",
   "hl": [
    "Neuronale Transkription im Browser, mit TensorFlow.js",
    "Noteneditor, 35 gesampelte Instrumente und ein Übungsmodus",
    "Online in neun Sprachen, mit Pro-Abos"
   ],
   "viz": "Tonhöhenspuren im Spektrogramm werden zu Noten im Notensystem.",
   "lede": "Amadeo hört eine Audiodatei, eine Mikrofonaufnahme oder ein Video und schreibt die Musik auf: Noten, Tempo, Takt, Tonart und Akkorde. Die Partitur lässt sich bearbeiten, auf 35 gesampelten Instrumenten abspielen, mit fallenden Noten üben und als PDF, MusicXML, MIDI oder WAV exportieren. Alles läuft im Browser.",
   "platform": "Web",
   "arch": [
    [
     "Ton",
     "Datei, Mikrofon oder Video"
    ],
    [
     "TensorFlow.js",
     "neuronale Notenerkennung"
    ],
    [
     "Tempo, Tonart, Akkorde",
     "aus den Noten geschätzt"
    ],
    [
     "VexFlow",
     "gesetzte, bearbeitbare Partitur"
    ],
    [
     "Export",
     "PDF · MusicXML · MIDI · WAV"
    ]
   ],
   "tests": [
    [
     "Vitest",
     "das echte Netz auf synthetischer Musik"
    ],
    [
     "Playwright",
     "Chromium, Firefox und WebKit, Desktop und Handy"
    ],
    [
     "Release-Prüfung",
     "562 Seiten ohne Fehler oder tote Links"
    ]
   ],
   "notes": [
    [
     "Der Ton bleibt auf dem Gerät",
     "Die Transkription läuft mit TensorFlow.js im Browser, Aufnahmen werden also nicht hochgeladen. Partituren bleiben auf dem Gerät und werden über einen Link geteilt, der die ganze Partitur enthält."
    ],
    [
     "Von Tonhöhen zur Musik",
     "Eine Liste von Tonhöhen ist noch keine Partitur. Amadeo folgt dem Tempo, findet Takt, Tonart und Akkorde, gibt jeder Hand ihre eigene Stimme und setzt das Ergebnis mit VexFlow."
    ],
    [
     "Ein Produkt, keine Demo",
     "Amadeo ist in neun Sprachen online, mit einem Pro-Tarif über Stripe, einem Repertoire an Arrangements, einem Stimmgerät und einem Metronom. Eine Android-App ist fertig und wartet auf die Veröffentlichung im Store."
    ]
   ],
   "shots": [
    "Start: hochladen, aufnehmen oder Link einfügen",
    "Für Elise als Partitur, mit Akkorden",
    "Dasselbe Stück als Pianorolle"
   ]
  },
  "brectus": {
   "sub": "Lokaler Orchestrator für KI-Coding-Agenten",
   "world": "Sturmwelt",
   "sum": "Eine Desktop-App, die jede Anfrage an den Coding-Agenten des richtigen Projekts schickt.",
   "hl": [
    "Node.js und Electron",
    "Verschlüsselung ruhender Daten über den Schlüsselspeicher des Betriebssystems",
    "Signierte Updates und CI unter Windows, macOS und Linux"
   ],
   "viz": "Anfragen werden an einen Agenten pro Projekt weitergeleitet.",
   "lede": "Eine Desktop-App, die jede Anfrage an den Coding-Agenten des richtigen Projekts schickt, damit mehrere Projekte von einem Ort aus vorankommen.",
   "platform": "Desktop",
   "arch": [
    [
     "Anfrage",
     "einmal geschrieben"
    ],
    [
     "Router",
     "Node.js, Electron"
    ],
    [
     "Agenten",
     "ein Claude-Code-Agent pro Projekt"
    ]
   ],
   "tests": [
    [
     "Schlüsselbund des Systems",
     "Verschlüsselung im Ruhezustand"
    ],
    [
     "Signierte Updates",
     "vor der Installation geprüft"
    ],
    [
     "CI",
     "Windows, macOS, Linux"
    ]
   ],
   "notes": [
    [
     "Ein Agent pro Projekt",
     "Jedes Projekt hat seinen eigenen Claude-Code-Agenten. Der Router entscheidet, zu welchem Projekt eine Anfrage gehört, und schickt sie dorthin."
    ],
    [
     "Im Ruhezustand verschlüsselt",
     "Gespeicherte Daten werden über den Schlüsselbund des Betriebssystems verschlüsselt."
    ],
    [
     "Drei Betriebssysteme",
     "Updates sind signiert, und die Continuous Integration läuft unter Windows, macOS und Linux."
    ]
   ],
   "shots": [
    "Die Karte: jeder Lebensbereich als Knoten",
    "Der Zweig Universität, mit Läufen und Automationen",
    "Wie eine Anfrage den richtigen Agenten erreicht"
   ]
  },
  "websites": {
   "sub": "Orion Benefícios, LÍDER Plus Telemedicina und ein Kosmetikstudio",
   "world": "Eiswelt",
   "sum": "Websites für drei brasilianische Betriebe und ein Mitarbeiterportal.",
   "hl": [
    "Astro und TypeScript oder ein kleiner Python-Generator, auf Cloudflare Pages",
    "Mitarbeiterportal auf Workers und D1, mit CSP-Headern",
    "WCAG-2.2-AA-Tests in drei Browser-Engines"
   ],
   "viz": "Lighthouse-Werte: 95 auf dem Smartphone, 100 auf dem Desktop.",
   "lede": "Websites für zwei brasilianische Unternehmen, Orion Benefícios und LÍDER Plus Telemedicina, und für ein unabhängiges Kosmetikstudio in Santos, dazu ein Mitarbeiterportal. Alle drei sind schnell, sicher und barrierefrei gebaut.",
   "platform": "Web",
   "arch": [
    [
     "Astro + TypeScript",
     "statische Seiten"
    ],
    [
     "Python-Generator",
     "Seiten aus Vorlagen und JSON"
    ],
    [
     "Cloudflare Pages",
     "vom Netzwerkrand ausgeliefert"
    ],
    [
     "Workers + D1",
     "Mitarbeiterportal und seine Datenbank"
    ]
   ],
   "tests": [
    [
     "CSP-Header",
     "Content Security Policy"
    ],
    [
     "WCAG 2.2 AA",
     "Chromium, Firefox, WebKit"
    ],
    [
     "Lighthouse",
     "95 mobil, 100 Desktop"
    ],
    [
     "Site-Validator",
     "Links, Metadaten, strukturierte Daten, Sitemap"
    ]
   ],
   "notes": [
    [
     "Schnell",
     "Statische Seiten, gebaut mit Astro oder einem kleinen Python-Generator, ausgeliefert von Cloudflare Pages. Lighthouse: 95 mobil und 100 am Desktop."
    ],
    [
     "Barrierefrei",
     "Automatische WCAG-2.2-AA-Tests laufen in allen drei Browser-Engines: Chromium, Firefox und WebKit."
    ],
    [
     "Sicher",
     "Das Mitarbeiterportal läuft auf Cloudflare Workers mit einer D1-Datenbank, hinter Content-Security-Policy-Headern."
    ]
   ],
   "shots": [
    "Startseite von LÍDER Plus",
    "Orion Benefícios: über uns",
    "Kosmetikstudio: Startseite",
    "LÍDER Plus: für Unternehmen und Gewerkschaften",
    "Kosmetikstudio: Behandlungskatalog"
   ]
  },
  "allwinner": {
   "sub": "Forschung zu Signalen am Kryptomarkt",
   "world": "Gasriese",
   "sum": "Forschungscode, der prüft, ob Handelssignale außerhalb der Stichprobe bestehen.",
   "hl": [
    "Walk-forward-Backtests außerhalb der Stichprobe, nach Gebühren und Slippage",
    "Block-Bootstrap-Tests gegen Data Snooping",
    "Python, pandas, FastAPI und SQLite, mit 221 pytest-Tests"
   ],
   "viz": "Walk-forward-Test: auf einem Fenster anpassen, im nächsten handeln, nie vorausschauen.",
   "lede": "Forschungssoftware, die jedem Handelssignal eine einzige Frage stellt: Funktioniert es noch auf Daten, die es nie gesehen hat, nach Gebühren und Slippage?",
   "platform": "Python",
   "arch": [
    [
     "Signale",
     "pandas"
    ],
    [
     "Walk-forward",
     "mit Gebühren und Slippage"
    ],
    [
     "Block-Bootstrap",
     "Glück oder Können?"
    ],
    [
     "FastAPI + SQLite",
     "Bewertungen und Ergebnisse"
    ]
   ],
   "tests": [
    [
     "pytest",
     "221 Tests"
    ]
   ],
   "notes": [
    [
     "Nie vorausschauen",
     "Jede Strategie wird auf einem Zeitfenster angepasst und im nächsten gehandelt, dann rückt das Fenster weiter. Gebühren und Slippage fallen bei jedem Trade an."
    ],
    [
     "Glück oder Können",
     "Wer viele Strategien ausprobiert, findet einige, die zufällig gut aussehen. Block-Bootstrap-Tests prüfen jedes Ergebnis genau darauf."
    ],
    [
     "Getesteter Code",
     "In Python mit pandas geschrieben, über FastAPI bereitgestellt und in SQLite gespeichert, mit 221 pytest-Tests."
    ]
   ],
   "shots": [
    "Signalansicht, mit dem Testverlauf des Projekts",
    "Strategie-Rangliste, Walk-forward",
    "Kurs und Haltung des Ensembles"
   ]
  }
 },
 "education": {
  "h": "Ausbildung",
  "items": [
   {
    "y": "2019 – 2023",
    "t": "B.Sc. in Informatik",
    "w": "FEI",
    "p": "Abschlussprojekt: ein variationeller Quantenklassifikator für den Iris-Datensatz, verglichen mit einer klassischen SVM.",
    "em": "Vollstipendium",
    "a": "Projektcode"
   },
   {
    "y": "2024 – 2026",
    "t": "M.Sc. in Elektrotechnik",
    "w": "FEI · KI in Automatisierung und Robotik",
    "p": "Masterarbeit über Quanten-Machine-Learning für die Histopathologie von Brustkrebs: 80,0 % Genauigkeit und 86,0 % F1, wobei kein Patient zugleich in Trainings- und Testdaten vorkommt.",
    "em": "CAPES-Stipendium",
    "a": "Code der Masterarbeit"
   },
   {
    "y": "2026 – 2027",
    "t": "MBA in Data Science, KI und Analytics",
    "w": "USP · laufend",
    "p": "Statistik, Python, Datenanalyse, maschinelles Lernen, künstliche Intelligenz und Analytics.",
    "em": "Vollstipendium"
   },
   {
    "y": "2027 – 2030",
    "t": "Promotion in Elektrotechnik",
    "w": "FEI · eingeschrieben, Vorlesungen ab Februar 2027",
    "p": "Quantenfehlerkorrektur und Decoder mit maschinellem Lernen. Ein Forschungsjahr an der ETH Zürich ist für 2028–2029 geplant.",
    "em": "CAPES-Stipendium"
   }
  ]
 },
 "experience": {
  "h": "Erfahrung",
  "items": [
   {
    "y": "2024 – 2026",
    "t": "Forscher für angewandtes maschinelles Lernen",
    "w": "FEI, São Bernardo do Campo",
    "p": "Klassifikation von Brustkrebs-Histopathologie auf BreaKHis mit ResNet-50, patientenweiser Aufteilung sowie SVM- und QSVM-Modellen; Experimente auf IBM-Quantum-Hardware dazu, wie Rauschen Quantenkernel beeinflusst."
   },
   {
    "y": "2020",
    "t": "Tutor für Analytische Geometrie",
    "w": "FEI, São Bernardo do Campo",
    "p": "Sprechstunden und Übungsblätter zu Matrizen, linearen Gleichungssystemen, Vektoren, Geraden und Ebenen."
   },
   {
    "y": "2016 – 2023",
    "t": "Webentwickler und IT-Support-Assistent",
    "w": "Orion Benefícios, Santos",
    "p": "Aufbau und Pflege der Firmenwebsite und ihrer datenbankgestützten Systeme sowie Support für Rechner, Netzwerke und Infrastruktur."
   }
  ]
 },
 "pub": {
  "k": "Publikation · BRACIS 2026",
  "w": "Mit Reinaldo A. C. Bianchi.",
  "a": "Zum Artikel"
 },
 "tools": {
  "h": "Werkzeuge",
  "groups": [
   "Maschinelles Lernen und Daten",
   "Web und Apps",
   "Systeme",
   "Quanten und Tests"
  ]
 },
 "contact": {
  "h": "Kontakt",
  "p": "Ich bin offen für Stellen im Bereich maschinelles Lernen und Software sowie für Forschungskooperationen. Am schnellsten erreichen Sie mich per E-Mail."
 },
 "sky": {
  "h": "Über diesen Himmel",
  "p": [
   "Das Schwarze Loch rotiert mit 90 % der maximalen Rate und ist 18° über seiner Scheibe zu sehen. Das Bild stammt aus Lichtstrahlen, die durch die Kerr-Metrik verfolgt wurden, und die Scheibe wird live auf Ihrer Grafikkarte schattiert, mit Schwarzkörperfarben, Doppler-Beaming auf der sich nähernden Seite und gravitativer Rotverschiebung.",
   "Die Planeten und der Asteroidengürtel kreisen in der Ebene der Scheibe, der Äquatorebene des Lochs, wo die Rotation ihre Bahnen nicht kippen kann. Alles läuft auf einer Uhr mit der Kerr-Umlauffrequenz: Der Innenrand der Scheibe dreht sich in weniger als einer Sekunde einmal, der äußerste Planet in etwa 45 Sekunden. Ihre Ellipsen drehen sich langsam, wie es die allgemeine Relativitätstheorie vorhersagt, und jeder Planet zeigt dem Loch immer dieselbe Seite.",
   "Eine Sekunde hier entspricht 40 M Zeit, wobei M die Masse des Lochs in Zeiteinheiten ist; für ein Loch von vier Millionen Sonnen wie im Zentrum der Milchstraße ist das etwa 800-fache Echtzeit. Die Kamera kreist langsam um das Loch, und Licht von allem dahinter, Planeten, Gürtel oder Sternen, wird von seiner Schwerkraft abgelenkt.",
   "Die Entfernungen teilen sich einen Maßstab, aber die Planeten sind hundert- bis tausendmal größer gezeichnet, als sie wären."
  ]
 },
 "nf": {
  "t": "Seite nicht gefunden",
  "p": "Diese Seite ist aus dem System gedriftet.",
  "a": "Zur Startseite"
 },
 "hero": {
  "h": "Alles, was ich baue, *kreist* um etwas Echtes.",
  "p": "Ich bin Matheus. Ich trainiere Modelle in Python und PyTorch und liefere getestete Apps in TypeScript und Rust. Jeder Planet hier ist eines meiner Projekte und kreist um ein rotierendes Schwarzes Loch. Klicken Sie auf einen, um dort zu landen.",
  "cta": [
   "Zu den Projekten",
   "Über mich"
  ]
 },
 "roadmap": {
  "h": "Fahrplan",
  "p": "Woher ich komme und wohin ich gehe, gezeichnet als Weltlinie. Die Zeit läuft nach rechts, und für das Jahr in Zürich steigt die Linie nach oben. Gestrichelte Teile sind geplant.",
  "br": "Brasilien",
  "ch": "Zürich",
  "now": "Jetzt",
  "planned": "geplant",
  "ev": {
   "orion": "Erster Job: Web und IT",
   "bsc": "Beginn des Bachelors",
   "bscd": "Bachelor abgeschlossen",
   "msc": "Beginn des Masters",
   "mscd": "Master abgeschlossen",
   "mba": "MBA an der USP",
   "paper": "Paper auf der BRACIS 2026",
   "phd": "Beginn der Promotionskurse",
   "mbad": "MBA abgeschlossen",
   "eth": "Jahr an der ETH Zürich",
   "def": "Verteidigung der Dissertation"
  },
  "spans": {
   "orion": "Orion Benefícios · Web und IT",
   "bsc": "Bachelor · FEI",
   "msc": "Master · FEI",
   "mba": "MBA · USP",
   "phd": "Promotion · FEI"
  },
  "months": [
   "Jan.",
   "Feb.",
   "März",
   "Apr.",
   "Mai",
   "Juni",
   "Juli",
   "Aug.",
   "Sept.",
   "Okt.",
   "Nov.",
   "Dez."
  ]
 }
}
