C = {
 "name": "English",
 "meta": {
  "title": "Matheus Teixeira · Machine learning engineer and software developer",
  "desc": "Matheus Teixeira, machine learning engineer and software developer from Santos, Brazil. Projects, roadmap, education, experience and contact."
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
 "role": "Machine learning engineer · Software developer",
 "hero": {
  "h": "Everything I build *orbits* something real.",
  "p": "I’m Matheus. I train models in Python and PyTorch and ship tested apps in TypeScript and Rust. Each planet here is one of my projects, circling a spinning black hole. Click one to land on it.",
  "cta": [
   "See the projects",
   "About me"
  ]
 },
 "ui": {
  "pause": "Pause motion",
  "play": "Play motion",
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
   "I’m Matheus, a machine learning engineer and software developer from Santos, Brazil. I have been writing software since 2016, when I started as a web developer and IT support assistant at Orion Benefícios, and I have studied at FEI since 2019.",
   "For my M.Sc. I built a reproducible pipeline that classifies breast cancer histopathology images, combining ResNet-50 features with classical and quantum support vector machines, and ran it on IBM Quantum hardware. I am now doing an MBA in Data Science, AI and Analytics at USP on a full scholarship, and I am enrolled in the Ph.D. at FEI, with a CAPES scholarship and classes from February 2027.",
   "Outside research I build software end to end, from the model or the physics to the interface and the tests. The five projects below are the ones I care about most."
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
    "Machine learning, computer vision, software"
   ]
  ],
  "alt": "Portrait of Matheus Teixeira",
  "term": {
   "who": "Matheus Teixeira: machine learning engineer and software developer",
   "now": [
    "MBA in Data Science, AI and Analytics at USP, in progress",
    "Ph.D. in Electrical Engineering at FEI, enrolled, classes from February 2027",
    "Open to machine learning and software roles"
   ],
   "lang": "pt_BR (native)   en_US (C2, EF SET 92/100)"
  }
 },
 "projects": {
  "h": "Projects",
  "p": "One project per planet. Land on a planet for the full story."
 },
 "proj": {
  "isaac": {
   "sub": "Interactive 3D physics simulations",
   "world": "Volcanic world",
   "sum": "Physics you can play with in the browser. A Rust engine compiled to WebAssembly runs the simulations, and React, TypeScript and Three.js draw them.",
   "lede": "A physics lab in the browser. You change a parameter and the scene, the graphs and the equations respond at once, from a thrown ball to a black hole.",
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
   "sum": "Turns a recording into sheet music you can edit, play and share, entirely in the browser. Live, with a Pro plan.",
   "lede": "Amadeo listens to a sound file, a microphone recording or a video and writes the music down: notes, tempo, meter, key and chords. The score can be edited, played on 35 sampled instruments, practised with falling notes and exported to PDF, MusicXML, MIDI or WAV. Everything runs in the browser.",
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
     "Sound never leaves the device",
     "Transcription runs on TensorFlow.js in the browser, so recordings are not uploaded. Scores stay on the visitor's device and are shared through a link that carries the whole score."
    ],
    [
     "From pitches to music",
     "A list of pitches is not a score. Amadeo follows the tempo, finds the meter, the key and the chords, gives each hand its own line and engraves the result with VexFlow."
    ],
    [
     "A product, not a demo",
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
   "sub": "Local orchestrator for AI coding agents",
   "world": "Storm world",
   "sum": "A desktop app that sends each request to the coding agent of the right project.",
   "lede": "A desktop app that routes each request to the coding agent of the right project, so that several projects can move forward from one place.",
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
     "one Claude Code agent per project"
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
     "Each project has its own Claude Code agent. The router decides where a request belongs and sends it there."
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
   "sum": "Websites for three Brazilian businesses, and an employee portal.",
   "lede": "Websites for two Brazilian companies, Orion Benefícios and LÍDER Plus Telemedicina, and for an independent esthetics studio in Santos, plus an employee portal. All three are built to be fast, secure and accessible.",
   "hl": [
    "Astro and TypeScript, or a small Python generator, on Cloudflare Pages",
    "Employee portal on Workers and D1, with CSP headers",
    "WCAG 2.2 AA tests in three browser engines"
   ],
   "viz": "Lighthouse scores: 95 on mobile, 100 on desktop.",
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
     "Fast",
     "Static pages, built with Astro or with a small Python generator, served by Cloudflare Pages. Lighthouse scores 95 on mobile and 100 on desktop."
    ],
    [
     "Accessible",
     "Automated WCAG 2.2 AA tests run in all three browser engines: Chromium, Firefox and WebKit."
    ],
    [
     "Secure",
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
   "sub": "Crypto market signal research",
   "world": "Gas giant",
   "sum": "Research code that checks whether trading signals hold up out of sample.",
   "lede": "Research software that asks one question of every trading signal: does it still work on data it has never seen, after fees and slippage?",
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
     "luck or skill?"
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
     "Never look ahead",
     "Each strategy is fitted on one window and traded on the next, then the window slides forward. Fees and slippage are paid on every trade."
    ],
    [
     "Luck or skill",
     "Trying many strategies makes some look good by chance. Block-bootstrap tests check each result against that."
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
  "p": "Where I have been and where I am going, drawn as a worldline. Time runs to the right, and the line moves up for the year in Zurich. Dashed parts are planned.",
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
  "p": "I am open to machine learning and software roles, and to research collaborations. Email is the quickest way to reach me."
 },
 "sky": {
  "h": "About this sky",
  "p": [
   "The black hole spins at 90% of the maximum rate and is seen from 18° above its disc. Its image comes from light rays traced through the Kerr metric, and the disc is shaded live on your graphics card, with blackbody colours, Doppler beaming on the approaching side and gravitational redshift.",
   "The planets and the asteroid belt orbit in the plane of the disc, the hole’s equatorial plane, where the spin cannot tilt their orbits. Everything runs on one clock at the Kerr orbital rate: the inner edge of the disc laps in under a second, the outermost planet in about 45 seconds. Their ellipses turn slowly, as general relativity predicts, and each planet keeps one face towards the hole.",
   "One second here is 40 M of time, where M is the hole’s mass in units of time; for a hole of four million suns, like the one at the centre of the Milky Way, that is about 800 times real speed. The camera drifts slowly around the hole, and light from anything behind it, planets, belt or stars, is bent by its gravity.",
   "Distances share one scale, but the planets are drawn hundreds to a thousand times larger than they would be."
  ]
 },
 "nf": {
  "t": "Page not found",
  "p": "This page drifted out of the system.",
  "a": "Back to the home page"
 }
}
