C = {
 "name": "Deutsch",
 "meta": {
  "title": "Matheus Teixeira · Machine-Learning-Engineer und Softwareingenieur",
  "desc": "Matheus Teixeira, Machine-Learning-Engineer und Softwareingenieur aus Santos, Brasilien. Projekte, Roadmap, Ausbildung, Erfahrung und Kontakt."
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
 "role": "Machine-Learning-Engineer · Softwareingenieur · Forscher in Quantencomputing",
 "ui": {
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
  "inside": "Die Idee, live gezeichnet",
  "nextp": "Nächster Planet",
  "illus": "Diagramm, live gezeichnet",
  "shot": "Bildschirmfotos",
  "cv": "Lebenslauf (PDF)",
  "live": "Live-Seite",
  "liveT": "{n}, live",
  "enl": "Fenster vergrößern",
  "res": "Fenster verkleinern"
 },
 "about": {
  "h": "Über mich",
  "p": [
   "Ich bin Matheus Teixeira aus Santos, Brasilien. Ich forsche zu Quanten-Machine-Learning und Quantenfehlerkorrektur.",
   "Ich habe 2016 als Webentwickler angefangen. An der FEI habe ich einen Bachelor in Informatik und einen Master in Elektrotechnik mit Schwerpunkt KI gemacht. Jetzt mache ich einen MBA in Data Science und KI an der USP und bin für die Promotion zur Quantenfehlerkorrektur an der FEI eingeschrieben, mit Kursen ab Februar 2027.",
   "Unten sind fünf meiner Projekte, eines pro Planet."
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
    "Maschinelles Lernen, Software, Quantencomputing"
   ]
  ],
  "alt": "Porträt von Matheus Teixeira",
  "term": {
   "who": "Matheus Teixeira: Machine-Learning-Engineer, Softwareingenieur, Forscher in Quantencomputing",
   "now": [
    "MBA in Data Science, KI und Analytics an der USP, laufend",
    "Promotion in Elektrotechnik an der FEI zur Quantenfehlerkorrektur, eingeschrieben, Kurse ab Februar 2027",
    "Offen für Stellen in Machine Learning und Softwareentwicklung"
   ],
   "lang": "pt_BR (Muttersprache)   en_US (C2, EF SET 92/100)"
  }
 },
 "projects": {
  "h": "Projekte",
  "p": "Landen Sie auf einem Planeten, um das Projekt aus der Nähe zu sehen."
 },
 "proj": {
  "isaac": {
   "sub": "Interaktive Physiksimulationen",
   "world": "Vulkanwelt",
   "sum": "Für Lernende gemacht, von der Schule bis zum Masterstudium. Jede Szene läuft im Browser.",
   "hl": [
    "Physikkern in Rust, kompiliert zu WebAssembly",
    "Live-Diagramme, Gleichungen und eine geführte Erklärung in jeder Szene",
    "Getestet mit cargo test, Vitest und Playwright-End-to-End-Tests"
   ],
   "viz": "Ein Doppelpendel, mit RK4 in Schritten von 2 ms integriert. Der blasse Zwilling startet 0,001 rad daneben, und das Chaos trennt die beiden.",
   "lede": "Für Lernende gemacht, von der Schule bis zum Masterstudium. Jede Szene läuft im Browser.",
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
   "sum": "Macht aus Audioaufnahmen bearbeitbare Noten, komplett im Browser.",
   "hl": [
    "Neuronale Transkription im Browser, mit TensorFlow.js",
    "Noteneditor, 35 gesampelte Instrumente und ein Übungsmodus",
    "Online in neun Sprachen, mit Pro-Abos"
   ],
   "viz": "Tonhöhenspuren im Spektrogramm werden zu Noten im Notensystem.",
   "lede": "Macht aus Audioaufnahmen bearbeitbare Noten, komplett im Browser.",
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
     "Läuft im Browser",
     "Die Transkription läuft mit TensorFlow.js im Browser, Aufnahmen werden also nicht hochgeladen. Partituren bleiben auf dem Gerät und werden über einen Link geteilt, der die ganze Partitur enthält."
    ],
    [
     "Tempo, Tonart und Akkorde",
     "Amadeo schätzt Tempo, Takt, Tonart und Akkorde, gibt jeder Hand ein eigenes System und setzt die Partitur mit VexFlow."
    ],
    [
     "Im Einsatz",
     "Online in neun Sprachen, mit Pro-Tarif, Stimmgerät und Metronom. Eine Android-App ist fertig."
    ]
   ],
   "shots": [
    "Start: hochladen, aufnehmen oder Link einfügen",
    "Für Elise als Partitur, mit Akkorden",
    "Dasselbe Stück als Pianorolle"
   ]
  },
  "brectus": {
   "sub": "Desktop-App für KI-Coding-Agenten",
   "world": "Sturmwelt",
   "sum": "Eine Anfrage wird einmal geschrieben, und die App erkennt, zu welchem Projekt sie gehört.",
   "hl": [
    "Jedes Projekt hat seinen eigenen Agenten",
    "Verschlüsselung ruhender Daten über den Schlüsselspeicher des Betriebssystems",
    "Signierte Updates und CI unter Windows, macOS und Linux"
   ],
   "viz": "Anfragen werden an einen Agenten pro Projekt weitergeleitet.",
   "lede": "Eine Anfrage wird einmal geschrieben, und die App erkennt, zu welchem Projekt sie gehört.",
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
     "ein KI-Coding-Agent pro Projekt"
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
     "Jedes Projekt hat seinen eigenen KI-Coding-Agenten. Die App entscheidet, zu welchem Projekt eine Anfrage gehört, und schickt sie dorthin."
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
   "sum": "Websites für Orion Benefícios und LÍDER Plus Telemedicina, eine Website für ein Kosmetikstudio und ein Mitarbeiterportal.",
   "hl": [
    "Astro und TypeScript oder ein kleiner Python-Generator, auf Cloudflare Pages",
    "Mitarbeiterportal auf Workers und D1, mit CSP-Headern",
    "WCAG-2.2-AA-Tests in drei Browser-Engines"
   ],
   "viz": "Lighthouse-Werte der Firmenwebsites: 95 auf dem Smartphone, 100 auf dem Desktop.",
   "lede": "Websites für Orion Benefícios und LÍDER Plus Telemedicina, eine Website für ein Kosmetikstudio und ein Mitarbeiterportal.",
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
     "Statische Seiten",
     "Statische Seiten, gebaut mit Astro oder einem kleinen Python-Generator, ausgeliefert über Cloudflare Pages."
    ],
    [
     "Auf Barrierefreiheit getestet",
     "Die Firmenwebsites werden in allen drei Browser-Engines gegen WCAG 2.2 AA getestet: Chromium, Firefox und WebKit."
    ],
    [
     "Das Mitarbeiterportal",
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
   "sub": "Backtesting von Handelsstrategien",
   "world": "Gasriese",
   "sum": "Prüft, ob eine Strategie auf Daten besteht, die sie nie gesehen hat, oder nur zufällig gut aussah.",
   "hl": [
    "Walk-forward-Backtests außerhalb der Stichprobe, nach Gebühren und Slippage",
    "Block-Bootstrap-Tests gegen Data Snooping",
    "Durch automatisierte Tests abgedeckt (pytest)"
   ],
   "viz": "Walk-forward-Test: auf einem Fenster anpassen, im nächsten handeln, nie vorausschauen.",
   "lede": "Prüft, ob eine Strategie auf Daten besteht, die sie nie gesehen hat, oder nur zufällig gut aussah.",
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
     "kein Zufall"
    ],
    [
     "FastAPI + SQLite",
     "Bewertungen und Ergebnisse"
    ]
   ],
   "tests": [
    [
     "pytest",
     "automatisierte Tests"
    ]
   ],
   "notes": [
    [
     "Walk-Forward-Fenster",
     "Jede Strategie wird auf einem Zeitfenster angepasst und im nächsten gehandelt, dann rückt das Fenster weiter. Gebühren und Slippage fallen bei jedem Trade an."
    ],
    [
     "Block-Bootstrap-Tests",
     "Wer viele Strategien ausprobiert, findet einige, die zufällig gut aussehen. Block-Bootstrap-Tests prüfen, dass jedes Ergebnis nicht auf Zufall beruht."
    ],
    [
     "Getesteter Code",
     "In Python mit pandas geschrieben, über FastAPI bereitgestellt, in SQLite gespeichert und durch pytest-Tests abgedeckt."
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
    "p": "Masterarbeit über Quanten-Machine-Learning für die Histopathologie von Brustkrebs: 80,0 % Genauigkeit und 86,0 % F1.",
    "em": "CAPES-Stipendium",
    "a": "Code der Masterarbeit"
   },
   {
    "y": "2026 – 2027",
    "t": "MBA in Data Science, KI und Analytics",
    "w": "USP · laufend",
    "p": "",
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
    "p": "Klassifikation von Brustkrebs-Histopathologie mit ResNet-50, SVM und QSVM; Experimente auf IBM-Quantum-Hardware."
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
  "p": "Ich suche Stellen im Bereich maschinelles Lernen und Software und spreche gern über Forschung. Am besten erreichen Sie mich per E-Mail."
 },
 "sky": {
  "h": "Über diesen Himmel",
  "p": [
   "Das Schwarze Loch wird per Raytracing gezeichnet: Jedes Pixel folgt einem Lichtstrahl durch die gekrümmte Raumzeit um ein rotierendes Loch. Die Scheibe ist heißes Gas, heller auf der Seite, die sich auf uns zubewegt.",
   "Die Planeten laufen nach einer gemeinsamen Uhr, etwa 20.000-mal schneller als um ein echtes Loch von 100 Millionen Sonnen. Ihre Bahnen sind flach gezeichnet und die Planeten weit größer als maßstabsgetreu."
  ]
 },
 "nf": {
  "t": "Seite nicht gefunden",
  "p": "Unter dieser Adresse gibt es keine Seite.",
  "a": "Zur Startseite"
 },
 "hero": {
  "h": "Alles, was ich baue, *kreist* um etwas Echtes.",
  "p": "Ich bin Matheus. Ich entwickle Modelle für maschinelles Lernen und Software. Jeder Planet hier ist eines meiner Projekte und umkreist ein Schwarzes Loch. Klicken Sie auf einen, um darauf zu landen.",
  "cta": [
   "Zu den Projekten",
   "Über mich"
  ]
 },
 "roadmap": {
  "h": "Fahrplan",
  "p": "Mein bisheriger Weg und was als Nächstes kommt. Gestrichelte Teile sind geplant.",
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
