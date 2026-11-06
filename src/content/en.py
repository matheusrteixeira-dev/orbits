C = {
 "name": "English",
 "meta": {
  "title": "Matheus Teixeira · Machine learning engineer and software engineer",
  "desc": "Matheus Teixeira, machine learning engineer and software engineer from Santos, Brazil. Projects, roadmap, education, experience and contact."
 },
 "skip": "Skip to content",
 "nav": {
  "about": "About",
  "projects": "Projects",
  "roadmap": "Roadmap",
  "education": "Education",
  "experience": "Experience",
  "contact": "Contact",
  "lang": "Language",
  "sections": "Sections"
 },
 "role": "Machine learning engineer · Software engineer · Quantum computing researcher",
 "hero": {
  "h": "Everything I build *orbits* something real.",
  "p": "I’m Matheus. I build machine learning models and software. Each planet here is a project of mine, orbiting a black hole. Click one to land on it.",
  "cta": [
   "See the projects",
   "About me"
  ]
 },
 "ui": {
  "land": "Land on this planet",
  "landBtn": "Land on the planet",
  "back": "Back to the system",
  "prev": "Previous",
  "next": "Next",
  "source": "Source on request",
  "copy": "Copy",
  "copied": "Copied",
  "planets": "Planets of the system",
  "planet": "Planet {n} of 5",
  "orbit": "Orbit: {r} M from the hole, one lap every {p} s on screen",
  "nogl": "Your browser cannot run the live rendering, so a still image is shown.",
  "year": "Year",
  "platform": "Platform",
  "stack": "Stack",
  "visit": "Visit {u}",
  "how": "How it fits together",
  "checks": "Checks",
  "notes": "Engineering notes",
  "inside": "Inside, live",
  "nextp": "Next planet",
  "illus": "Diagram, drawn live",
  "shot": "Screenshot"
 },
 "about": {
  "h": "About",
  "p": [
   "I’m Matheus Teixeira, from Santos, Brazil. I build machine learning models and software, and my research is on quantum machine learning and quantum error correction.",
   "I started in 2016 as a web developer and IT support assistant at Orion Benefícios. I have studied at FEI since 2019, first a B.Sc. in Computer Science and then an M.Sc. in Electrical Engineering in AI. My dissertation is a hybrid quantum-classical pipeline for breast cancer histopathology, with the data split by patient so that no patient appears in both training and test sets. I am now doing an MBA in Data Science, AI and Analytics at USP on a full scholarship, and I am enrolled in the Ph.D. at FEI on quantum error correction, with a CAPES scholarship and classes from February 2027.",
   "Below are five of my projects, one per planet."
  ],
  "facts": [
   [
    "Based in",
    "Santos, Brazil"
   ],
   [
    "Languages",
    "Portuguese (native), English (C2)"
   ],
   [
    "Works on",
    "Machine learning, software, quantum computing"
   ]
  ],
  "alt": "Portrait of Matheus Teixeira",
  "term": {
   "who": "Matheus Teixeira: machine learning engineer, software engineer, quantum computing researcher",
   "now": [
    "MBA in Data Science, AI and Analytics at USP, in progress",
    "Ph.D. in Electrical Engineering at FEI on quantum error correction, enrolled, classes from February 2027",
    "Open to machine learning and software roles"
   ],
   "lang": "pt_BR (native)   en_US (C2, EF SET 92/100)"
  }
 },
 "projects": {
  "h": "Projects",
  "p": "Land on a planet to see the project up close."
 },
 "proj": {
  "isaac": {
   "sub": "Interactive physics simulations",
   "world": "Volcanic world",
   "sum": "Interactive physics simulations for students, with live graphs and equations.",
   "lede": "Interactive physics simulations for students, with live graphs and equations. Physics core in Rust compiled to WebAssembly; interface in React, TypeScript and Three.js; physics validated with cargo test, unit tests in Vitest and end-to-end tests in Playwright.",
   "hl": [
    "Rust physics core compiled to WebAssembly",
    "Interface in React, TypeScript and Three.js",
    "Tested with cargo test, Vitest and Playwright end to end"
   ],
   "viz": "A double pendulum integrated with RK4 in 2 ms steps. The faint twin starts 0.001 rad away, and chaos pulls the two apart.",
   "platform": "Web",
   "shots": [
    "A double pendulum with live graphs",
    "Home page",
    "Library of scenes"
   ],
   "arch": [
    [
     "Rust",
     "physics core"
    ],
    [
     "WebAssembly",
     "runs it in the browser"
    ],
    [
     "TypeScript",
     "scene engine"
    ],
    [
     "React + Three.js",
     "interface and 3D view"
    ]
   ],
   "tests": [
    [
     "cargo test",
     "physics against exact results"
    ],
    [
     "Vitest",
     "unit tests"
    ],
    [
     "Playwright",
     "full journeys, desktop and mobile"
    ]
   ],
   "notes": [
    [
     "Physics in Rust",
     "The equations are integrated in a Rust core compiled to WebAssembly. TypeScript runs the scene, and React and Three.js draw the controls, graphs and 3D view."
    ],
    [
     "Checked against exact results",
     "Each simulation is tested against known solutions with cargo test. Vitest covers the interface logic, and Playwright runs whole journeys on desktop and mobile."
    ],
    [
     "From school to graduate level",
     "Scenes are organised by area of physics and by level. Each has parameters with units, live graphs, the equations behind it and a guided explanation."
    ]
   ]
  },
  "amadeo": {
   "sub": "Audio to sheet music",
   "world": "Ocean world",
   "sum": "Turns audio recordings into editable sheet music, all in the browser.",
   "lede": "Turns audio recordings into editable sheet music, all in the browser: neural pitch detection on TensorFlow.js, key and chord estimation, export to PDF, MusicXML and MIDI. React and TypeScript, nine languages, cross-browser Playwright tests. The score can be edited, played on 35 sampled instruments and practised with falling notes.",
   "hl": [
    "Neural transcription in the browser, on TensorFlow.js",
    "Score editor, 35 sampled instruments and a practice mode",
    "Live in nine languages, with Pro subscriptions"
   ],
   "viz": "Pitch tracks in the spectrogram become notes on the staff.",
   "platform": "Web",
   "arch": [
    [
     "Sound",
     "file, microphone or video"
    ],
    [
     "TensorFlow.js",
     "neural note detection"
    ],
    [
     "Tempo, key, chords",
     "estimated from the notes"
    ],
    [
     "VexFlow",
     "engraved, editable score"
    ],
    [
     "Export",
     "PDF · MusicXML · MIDI · WAV"
    ]
   ],
   "tests": [
    [
     "Vitest",
     "the real network on synthesised music"
    ],
    [
     "Playwright",
     "Chromium, Firefox and WebKit, desktop and phone"
    ],
    [
     "Release review",
     "562 pages with no errors or broken links"
    ]
   ],
   "notes": [
    [
     "Runs in the browser",
     "Transcription runs on TensorFlow.js in the browser, so recordings are not uploaded. Scores stay on the device and are shared through a link that carries the whole score."
    ],
    [
     "Tempo, key and chords",
     "Amadeo estimates the tempo, meter, key and chords, gives each hand its own line and engraves the score with VexFlow."
    ],
    [
     "In use",
     "Amadeo is live in nine languages, with a Pro plan paid through Stripe, a repertoire of arrangements, a tuner and a metronome. An Android app is built and waiting for its store release."
    ]
   ],
   "shots": [
    "Home: upload, record or paste a link",
    "Für Elise as a score, with chords",
    "The same piece as a piano roll"
   ]
  },
  "brectus": {
   "sub": "Desktop app for AI coding agents",
   "world": "Storm world",
   "sum": "Desktop app that sends requests to a separate AI coding agent for each project.",
   "lede": "Desktop app that sends requests to a separate AI coding agent for each project. Data is encrypted at rest, updates are signed, and CI runs on Windows, macOS and Linux. Node.js and Electron.",
   "hl": [
    "Node.js and Electron",
    "Encryption at rest through the operating system’s keystore",
    "Signed updates and CI on Windows, macOS and Linux"
   ],
   "viz": "Requests are routed to one agent per project.",
   "platform": "Desktop",
   "arch": [
    [
     "Request",
     "written once"
    ],
    [
     "Router",
     "Node.js, Electron"
    ],
    [
     "Agents",
     "one AI coding agent per project"
    ]
   ],
   "tests": [
    [
     "OS keystore",
     "encryption at rest"
    ],
    [
     "Signed updates",
     "checked before install"
    ],
    [
     "CI",
     "Windows, macOS, Linux"
    ]
   ],
   "notes": [
    [
     "One agent per project",
     "Each project has its own AI coding agent. The app decides which project a request belongs to and sends it there."
    ],
    [
     "Encrypted at rest",
     "Stored data is encrypted through the operating system’s own keystore."
    ],
    [
     "Three operating systems",
     "Updates are signed, and continuous integration runs on Windows, macOS and Linux."
    ]
   ],
   "shots": [
    "The map: every area of my life as a node",
    "The university branch, with runs and automations",
    "How one request reaches the right agent"
   ]
  },
  "websites": {
   "sub": "Orion Benefícios, LÍDER Plus Telemedicina and an esthetics studio",
   "world": "Ice world",
   "sum": "Company websites for Orion Benefícios and LÍDER Plus Telemedicina, a website for an esthetics studio, and an employee portal.",
   "lede": "Company websites for Orion Benefícios and LÍDER Plus Telemedicina, a website for an esthetics studio in Santos, and an employee portal. The company websites score 95 on mobile and 100 on desktop in Lighthouse and meet WCAG 2.2 AA.",
   "hl": [
    "Astro and TypeScript, or a small Python generator, on Cloudflare Pages",
    "Employee portal on Workers and D1, with CSP headers",
    "WCAG 2.2 AA tests in three browser engines"
   ],
   "viz": "Lighthouse scores of the company websites: 95 on mobile, 100 on desktop.",
   "platform": "Web",
   "arch": [
    [
     "Astro + TypeScript",
     "static pages"
    ],
    [
     "Python generator",
     "pages from templates and JSON"
    ],
    [
     "Cloudflare Pages",
     "served from the edge"
    ],
    [
     "Workers + D1",
     "employee portal and its database"
    ]
   ],
   "tests": [
    [
     "CSP headers",
     "content security policy"
    ],
    [
     "WCAG 2.2 AA",
     "Chromium, Firefox, WebKit"
    ],
    [
     "Lighthouse",
     "95 mobile, 100 desktop"
    ],
    [
     "Site validator",
     "links, metadata, structured data, sitemap"
    ]
   ],
   "notes": [
    [
     "Static pages",
     "Static pages, built with Astro or with a small Python generator, served by Cloudflare Pages. The company websites score 95 on mobile and 100 on desktop in Lighthouse."
    ],
    [
     "Tested for accessibility",
     "The company websites are tested against WCAG 2.2 AA in all three browser engines: Chromium, Firefox and WebKit."
    ],
    [
     "The employee portal",
     "The employee portal runs on Cloudflare Workers with a D1 database, behind Content Security Policy headers."
    ]
   ],
   "shots": [
    "LÍDER Plus home page",
    "Orion Benefícios: about",
    "Esthetics studio: home page",
    "LÍDER Plus: for companies and unions",
    "Esthetics studio: treatment catalogue"
   ]
  },
  "allwinner": {
   "sub": "Backtesting trading strategies",
   "world": "Gas giant",
   "sum": "Backtests trading strategies on out-of-sample data, with fees and slippage.",
   "lede": "Backtests trading strategies on out-of-sample data with walk-forward windows, fees and slippage, and uses block-bootstrap tests to check that results are not due to chance. Python, pandas, FastAPI and SQLite, with 221 pytest tests.",
   "hl": [
    "Walk-forward, out-of-sample backtests after fees and slippage",
    "Block-bootstrap tests against data snooping",
    "Python, pandas, FastAPI and SQLite, with 221 pytest tests"
   ],
   "viz": "Walk-forward testing: fit on one window, trade the next, never look ahead.",
   "platform": "Python",
   "arch": [
    [
     "Signals",
     "pandas"
    ],
    [
     "Walk-forward",
     "fees and slippage included"
    ],
    [
     "Block bootstrap",
     "not due to chance"
    ],
    [
     "FastAPI + SQLite",
     "scores and results"
    ]
   ],
   "tests": [
    [
     "pytest",
     "221 tests"
    ]
   ],
   "notes": [
    [
     "Walk-forward windows",
     "Each strategy is fitted on one window and traded on the next, then the window slides forward. Fees and slippage are paid on every trade."
    ],
    [
     "Block-bootstrap tests",
     "Trying many strategies makes some look good by chance. Block-bootstrap tests check that each result is not due to chance."
    ],
    [
     "Tested code",
     "Written in Python with pandas, served through FastAPI and stored in SQLite, with 221 pytest tests."
    ]
   ],
   "shots": [
    "Signals screen, on the project's test history",
    "Strategy scoreboard, walk-forward",
    "Price and ensemble stance"
   ]
  }
 },
 "roadmap": {
  "h": "Roadmap",
  "p": "My path so far and what comes next. Time runs to the right, and the line goes up for the year in Zurich. Dashed parts are planned.",
  "br": "Brazil",
  "ch": "Zurich",
  "now": "Now",
  "planned": "planned",
  "ev": {
   "orion": "First job: web and IT",
   "bsc": "B.Sc. starts",
   "bscd": "B.Sc. done",
   "msc": "M.Sc. starts",
   "mscd": "M.Sc. done",
   "mba": "MBA at USP",
   "paper": "BRACIS 2026 paper",
   "phd": "Ph.D. classes begin",
   "mbad": "MBA done",
   "eth": "ETH Zurich year",
   "def": "Thesis defence"
  },
  "spans": {
   "orion": "Orion Benefícios · web and IT",
   "bsc": "B.Sc. · FEI",
   "msc": "M.Sc. · FEI",
   "mba": "MBA · USP",
   "phd": "Ph.D. · FEI"
  },
  "months": [
   "Jan",
   "Feb",
   "Mar",
   "Apr",
   "May",
   "Jun",
   "Jul",
   "Aug",
   "Sep",
   "Oct",
   "Nov",
   "Dec"
  ]
 },
 "education": {
  "h": "Education",
  "items": [
   {
    "y": "2019 – 2023",
    "t": "B.Sc. in Computer Science",
    "w": "FEI",
    "p": "Final project: a variational quantum classifier for the Iris dataset, compared with a classical SVM.",
    "em": "Full scholarship",
    "a": "Project code"
   },
   {
    "y": "2024 – 2026",
    "t": "M.Sc. in Electrical Engineering",
    "w": "FEI · AI applied to automation and robotics",
    "p": "Dissertation on quantum machine learning for breast cancer histopathology: 80.0% accuracy and 86.0% F1, with no patient in both the training and the test set.",
    "em": "CAPES scholarship",
    "a": "Dissertation code"
   },
   {
    "y": "2026 – 2027",
    "t": "MBA in Data Science, AI and Analytics",
    "w": "USP · in progress",
    "p": "Statistics, Python, data analysis, machine learning, artificial intelligence and analytics.",
    "em": "Full scholarship"
   },
   {
    "y": "2027 – 2030",
    "t": "Ph.D. in Electrical Engineering",
    "w": "FEI · enrolled, classes from February 2027",
    "p": "Quantum error correction and machine learning decoders. A sandwich year at ETH Zurich is planned for 2028–2029.",
    "em": "CAPES scholarship"
   }
  ]
 },
 "experience": {
  "h": "Experience",
  "items": [
   {
    "y": "2024 – 2026",
    "t": "Applied machine learning researcher",
    "w": "FEI, São Bernardo do Campo",
    "p": "Breast cancer histopathology classification on BreaKHis with ResNet-50, patient-wise splits and SVM and QSVM models; experiments on IBM Quantum hardware on how noise affects quantum kernels."
   },
   {
    "y": "2020",
    "t": "Teaching assistant, Analytical Geometry",
    "w": "FEI, São Bernardo do Campo",
    "p": "Help sessions and exercise lists on matrices, linear systems, vectors, lines and planes."
   },
   {
    "y": "2016 – 2023",
    "t": "Web developer and IT support assistant",
    "w": "Orion Benefícios, Santos",
    "p": "Built and maintained the company website and its database-backed systems, and supported computers, networks and infrastructure."
   }
  ]
 },
 "pub": {
  "k": "Publication · BRACIS 2026",
  "w": "With Reinaldo A. C. Bianchi.",
  "a": "Read the paper"
 },
 "tools": {
  "h": "Tools",
  "groups": [
   "Machine learning and data",
   "Web and apps",
   "Systems",
   "Quantum and testing"
  ]
 },
 "contact": {
  "h": "Contact",
  "p": "I’m looking for machine learning and software roles, and I’m always glad to talk about research. Email is the best way to reach me."
 },
 "sky": {
  "h": "About this sky",
  "p": [
   "The black hole is drawn with the same ray tracer as Isaac, my physics simulator. Every pixel follows a light ray back through the curved spacetime around the hole (which does not spin), seen from 18° above its disc. The disc is hot gas, coloured as a black body, brighter on the side moving towards us and redshifted close to the hole. The gas orbits as fast as it really would: the inner edge goes round in about 2 seconds, the outer edge in about 9. The thin bright ring around the shadow is light that circled the hole before reaching us.",
   "The planets and the asteroid belt orbit in the plane of the disc, all on one clock: the innermost planet laps in about 23 seconds, the outermost in about 46. Their ellipses turn slowly, as general relativity predicts, and each planet keeps one face towards the hole.",
   "One second here is 40 M of time, where M is the hole’s mass in units of time. For a hole of 100 million suns, that is about 20,000 times real speed. The camera drifts slowly around the hole.",
   "The light of the planets, the belt and the orbits is bent by the hole, like the light of the stars, so the far side of every orbit appears lifted over it. Only the planets are not to scale: they are drawn thousands of times larger than they would be."
  ]
 },
 "nf": {
  "t": "Page not found",
  "p": "There is no page at this address.",
  "a": "Back to the home page"
 }
}
