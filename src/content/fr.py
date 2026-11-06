C = {
 "name": "Français",
 "meta": {
  "title": "Matheus Teixeira · Ingénieur en machine learning et ingénieur logiciel",
  "desc": "Matheus Teixeira, ingénieur en machine learning et ingénieur logiciel, de Santos au Brésil. Projets, feuille de route, formation, expérience et contact."
 },
 "skip": "Aller au contenu",
 "nav": {
  "about": "À propos",
  "projects": "Projets",
  "education": "Formation",
  "experience": "Expérience",
  "contact": "Contact",
  "lang": "Langue",
  "sections": "Sections",
  "roadmap": "Feuille de route"
 },
 "role": "Ingénieur en machine learning · Ingénieur logiciel · Chercheur en informatique quantique",
 "ui": {
  "land": "Se poser sur cette planète",
  "landBtn": "Se poser sur la planète",
  "back": "Retour au système",
  "prev": "Précédent",
  "next": "Suivant",
  "source": "Code sur demande",
  "copy": "Copier",
  "copied": "Copié",
  "planets": "Planètes du système",
  "planet": "Planète {n} sur 5",
  "orbit": "Orbite : à {r} M du trou noir, un tour toutes les {p} s à l’écran",
  "nogl": "Votre navigateur ne peut pas exécuter le rendu en direct ; une image fixe est affichée.",
  "year": "Année",
  "platform": "Plateforme",
  "stack": "Technologies",
  "visit": "Visiter {u}",
  "how": "Comment les pièces s’assemblent",
  "checks": "Vérifications",
  "notes": "Notes d’ingénierie",
  "inside": "À l’intérieur, en direct",
  "nextp": "Planète suivante",
  "illus": "Schéma, dessiné en direct",
  "shot": "Captures d’écran"
 },
 "about": {
  "h": "À propos",
  "p": [
   "Je suis Matheus Teixeira, de Santos, au Brésil. Je conçois des modèles de machine learning et des logiciels, et mes recherches portent sur le machine learning quantique et la correction d’erreurs quantiques.",
   "J’ai commencé en 2016 comme développeur web et assistant de support informatique chez Orion Benefícios. J’étudie à la FEI depuis 2019, d’abord une licence en informatique, puis un master en génie électrique en IA. Mon mémoire est un pipeline hybride quantique-classique pour l’histopathologie du cancer du sein, avec des données séparées par patient, si bien qu’aucun patient n’apparaît à la fois dans l’entraînement et dans le test. Je fais maintenant un MBA en Data Science, IA et Analytics à l’USP avec une bourse complète, et je suis inscrit en doctorat à la FEI sur la correction d’erreurs quantiques, avec une bourse CAPES et des cours à partir de février 2027.",
   "Voici cinq de mes projets, un par planète."
  ],
  "facts": [
   [
    "Basé à",
    "Santos, Brésil"
   ],
   [
    "Langues",
    "Portugais (langue maternelle), anglais (C2)"
   ],
   [
    "Domaines",
    "Machine learning, logiciel, informatique quantique"
   ]
  ],
  "alt": "Portrait de Matheus Teixeira",
  "term": {
   "who": "Matheus Teixeira : ingénieur en machine learning, ingénieur logiciel, chercheur en informatique quantique",
   "now": [
    "MBA en Data Science, IA et Analytics à l’USP, en cours",
    "Doctorat en génie électrique à la FEI sur la correction d’erreurs quantiques, inscrit, cours à partir de février 2027",
    "Ouvert aux postes en machine learning et en logiciel"
   ],
   "lang": "pt_BR (langue maternelle)   en_US (C2, EF SET 92/100)"
  }
 },
 "projects": {
  "h": "Projets",
  "p": "Posez-vous sur une planète pour voir le projet de près."
 },
 "proj": {
  "isaac": {
   "sub": "Simulations de physique interactives",
   "world": "Monde volcanique",
   "sum": "Des simulations de physique interactives pour les étudiants, avec graphiques et équations en direct.",
   "hl": [
    "Cœur physique en Rust compilé en WebAssembly",
    "Interface en React, TypeScript et Three.js",
    "Testé avec cargo test, Vitest et Playwright de bout en bout"
   ],
   "viz": "Un double pendule intégré par RK4 par pas de 2 ms. Son jumeau pâle part à 0,001 rad d’écart, et le chaos les sépare.",
   "lede": "Des simulations de physique interactives pour les étudiants, avec graphiques et équations en direct. Cœur physique en Rust compilé en WebAssembly ; interface en React, TypeScript et Three.js ; physique validée avec cargo test, tests unitaires avec Vitest et tests de bout en bout avec Playwright.",
   "platform": "Web",
   "shots": [
    "Un double pendule avec graphiques en direct",
    "Page d’accueil",
    "Bibliothèque de scènes"
   ],
   "arch": [
    [
     "Rust",
     "cœur physique"
    ],
    [
     "WebAssembly",
     "l’exécute dans le navigateur"
    ],
    [
     "TypeScript",
     "moteur de scènes"
    ],
    [
     "React + Three.js",
     "interface et vue 3D"
    ]
   ],
   "tests": [
    [
     "cargo test",
     "physique comparée aux résultats exacts"
    ],
    [
     "Vitest",
     "tests unitaires"
    ],
    [
     "Playwright",
     "parcours complets, ordinateur et mobile"
    ]
   ],
   "notes": [
    [
     "La physique en Rust",
     "Les équations sont intégrées dans un cœur Rust compilé en WebAssembly. TypeScript pilote la scène, et React et Three.js dessinent les commandes, les graphiques et la vue 3D."
    ],
    [
     "Vérifié contre des résultats exacts",
     "Chaque simulation est testée contre des solutions connues avec cargo test. Vitest couvre la logique de l’interface, et Playwright exécute des parcours entiers sur ordinateur et sur mobile."
    ],
    [
     "Du lycée au doctorat",
     "Les scènes sont classées par domaine de la physique et par niveau. Chacune a des paramètres avec unités, des graphiques en direct, les équations sous-jacentes et une explication guidée."
    ]
   ]
  },
  "amadeo": {
   "sub": "De l’audio à la partition",
   "world": "Monde océanique",
   "sum": "Transforme des enregistrements audio en partitions modifiables, entièrement dans le navigateur.",
   "hl": [
    "Transcription neuronale dans le navigateur, avec TensorFlow.js",
    "Éditeur de partitions, 35 instruments échantillonnés et un mode d’entraînement",
    "En ligne en neuf langues, avec abonnements Pro"
   ],
   "viz": "Les traces de hauteur du spectrogramme deviennent des notes sur la portée.",
   "lede": "Transforme des enregistrements audio en partitions modifiables, entièrement dans le navigateur : détection neuronale des hauteurs avec TensorFlow.js, estimation de la tonalité et des accords, export en PDF, MusicXML et MIDI. React et TypeScript, neuf langues, tests Playwright sur plusieurs navigateurs. La partition peut être modifiée, jouée sur 35 instruments échantillonnés et travaillée avec des notes qui tombent.",
   "platform": "Web",
   "arch": [
    [
     "Son",
     "fichier, micro ou vidéo"
    ],
    [
     "TensorFlow.js",
     "détection neuronale des notes"
    ],
    [
     "Tempo, tonalité, accords",
     "estimés à partir des notes"
    ],
    [
     "VexFlow",
     "partition gravée et modifiable"
    ],
    [
     "Export",
     "PDF · MusicXML · MIDI · WAV"
    ]
   ],
   "tests": [
    [
     "Vitest",
     "le vrai réseau sur de la musique synthétisée"
    ],
    [
     "Playwright",
     "Chromium, Firefox et WebKit, ordinateur et mobile"
    ],
    [
     "Revue de mise en ligne",
     "562 pages sans erreur ni lien cassé"
    ]
   ],
   "notes": [
    [
     "Dans le navigateur",
     "La transcription tourne avec TensorFlow.js dans le navigateur, donc les enregistrements ne sont pas envoyés. Les partitions restent sur l’appareil et se partagent par un lien qui contient toute la partition."
    ],
    [
     "Tempo, tonalité et accords",
     "Amadeo estime le tempo, la mesure, la tonalité et les accords, donne à chaque main sa propre portée et grave la partition avec VexFlow."
    ],
    [
     "En service",
     "Amadeo est en ligne en neuf langues, avec un abonnement Pro payé via Stripe, un répertoire d’arrangements, un accordeur et un métronome. Une application Android est prête et attend sa sortie sur le store."
    ]
   ],
   "shots": [
    "Accueil : importer, enregistrer ou coller un lien",
    "La Lettre à Élise en partition, avec accords",
    "Le même morceau en rouleau de piano"
   ]
  },
  "brectus": {
   "sub": "Application de bureau pour agents de code IA",
   "world": "Monde d’orages",
   "sum": "Application de bureau qui envoie les demandes à un agent de code IA distinct pour chaque projet.",
   "hl": [
    "Node.js et Electron",
    "Chiffrement au repos via le trousseau du système d’exploitation",
    "Mises à jour signées et CI sous Windows, macOS et Linux"
   ],
   "viz": "Les demandes sont acheminées vers un agent par projet.",
   "lede": "Application de bureau qui envoie les demandes à un agent de code IA distinct pour chaque projet. Les données sont chiffrées au repos, les mises à jour sont signées et la CI tourne sous Windows, macOS et Linux. Node.js et Electron.",
   "platform": "Bureau",
   "arch": [
    [
     "Demande",
     "écrite une fois"
    ],
    [
     "Routeur",
     "Node.js, Electron"
    ],
    [
     "Agents",
     "un agent de code IA par projet"
    ]
   ],
   "tests": [
    [
     "Trousseau du système",
     "chiffrement au repos"
    ],
    [
     "Mises à jour signées",
     "vérifiées avant l’installation"
    ],
    [
     "CI",
     "Windows, macOS, Linux"
    ]
   ],
   "notes": [
    [
     "Un agent par projet",
     "Chaque projet a son propre agent de code IA. L’application détermine à quel projet appartient une demande et l’y envoie."
    ],
    [
     "Chiffré au repos",
     "Les données stockées sont chiffrées par le trousseau du système d’exploitation lui-même."
    ],
    [
     "Trois systèmes d’exploitation",
     "Les mises à jour sont signées, et l’intégration continue tourne sous Windows, macOS et Linux."
    ]
   ],
   "shots": [
    "La carte : chaque domaine de ma vie est un nœud",
    "La branche université, avec exécutions et automatisations",
    "Comment une demande atteint le bon agent"
   ]
  },
  "websites": {
   "sub": "Orion Benefícios, LÍDER Plus Telemedicina et un institut d’esthétique",
   "world": "Monde de glace",
   "sum": "Les sites d’Orion Benefícios et de LÍDER Plus Telemedicina, un site pour un institut d’esthétique et un portail pour les salariés.",
   "hl": [
    "Astro et TypeScript, ou un petit générateur en Python, sur Cloudflare Pages",
    "Portail des employés sur Workers et D1, avec en-têtes CSP",
    "Tests WCAG 2.2 AA dans trois moteurs de navigateur"
   ],
   "viz": "Scores Lighthouse des sites des entreprises : 95 sur mobile, 100 sur ordinateur.",
   "lede": "Les sites des entreprises Orion Benefícios et LÍDER Plus Telemedicina, un site pour un institut d’esthétique à Santos et un portail pour les salariés. Les sites des entreprises obtiennent 95 sur mobile et 100 sur ordinateur dans Lighthouse et respectent le WCAG 2.2 AA.",
   "platform": "Web",
   "arch": [
    [
     "Astro + TypeScript",
     "pages statiques"
    ],
    [
     "Générateur en Python",
     "pages à partir de modèles et de JSON"
    ],
    [
     "Cloudflare Pages",
     "servies depuis la périphérie du réseau"
    ],
    [
     "Workers + D1",
     "portail des employés et sa base de données"
    ]
   ],
   "tests": [
    [
     "En-têtes CSP",
     "politique de sécurité du contenu"
    ],
    [
     "WCAG 2.2 AA",
     "Chromium, Firefox, WebKit"
    ],
    [
     "Lighthouse",
     "95 sur mobile, 100 sur ordinateur"
    ],
    [
     "Validateur du site",
     "liens, métadonnées, données structurées, sitemap"
    ]
   ],
   "notes": [
    [
     "Pages statiques",
     "Des pages statiques, faites avec Astro ou avec un petit générateur Python, servies par Cloudflare Pages. Les sites des entreprises obtiennent 95 sur mobile et 100 sur ordinateur dans Lighthouse."
    ],
    [
     "Accessibilité testée",
     "Les sites des entreprises sont testés selon le WCAG 2.2 AA dans les trois moteurs de navigateur : Chromium, Firefox et WebKit."
    ],
    [
     "Le portail des employés",
     "Le portail des employés tourne sur Cloudflare Workers avec une base D1, derrière des en-têtes Content Security Policy."
    ]
   ],
   "shots": [
    "Page d’accueil de LÍDER Plus",
    "Orion Benefícios : l’entreprise",
    "Institut d’esthétique : page d’accueil",
    "LÍDER Plus : pour les entreprises et les syndicats",
    "Institut d’esthétique : catalogue des soins"
   ]
  },
  "allwinner": {
   "sub": "Backtest de stratégies de trading",
   "world": "Géante gazeuse",
   "sum": "Backteste des stratégies de trading sur des données hors échantillon, avec frais et slippage.",
   "hl": [
    "Backtests walk-forward hors échantillon, après frais et slippage",
    "Tests de block bootstrap contre le data snooping",
    "Python, pandas, FastAPI et SQLite, avec 221 tests pytest"
   ],
   "viz": "Test walk-forward : ajuster sur une fenêtre, trader sur la suivante, sans jamais regarder en avant.",
   "lede": "Backteste des stratégies de trading sur des données hors échantillon, avec des fenêtres walk-forward, des frais et du slippage, et utilise des tests de block bootstrap pour vérifier que les résultats ne sont pas dus au hasard. Python, pandas, FastAPI et SQLite, avec 221 tests pytest.",
   "platform": "Python",
   "arch": [
    [
     "Signaux",
     "pandas"
    ],
    [
     "Walk-forward",
     "frais et slippage compris"
    ],
    [
     "Block bootstrap",
     "pas dû au hasard"
    ],
    [
     "FastAPI + SQLite",
     "scores et résultats"
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
     "Fenêtres walk-forward",
     "Chaque stratégie est ajustée sur une fenêtre et négociée sur la suivante, puis la fenêtre avance. Les frais et le slippage sont payés à chaque opération."
    ],
    [
     "Tests de block bootstrap",
     "Essayer beaucoup de stratégies en fait paraître certaines bonnes par hasard. Les tests de block bootstrap vérifient que chaque résultat n’est pas dû au hasard."
    ],
    [
     "Du code testé",
     "Écrit en Python avec pandas, servi par FastAPI et stocké dans SQLite, avec 221 tests pytest."
    ]
   ],
   "shots": [
    "Écran des signaux, sur l’historique de test du projet",
    "Classement des stratégies, walk-forward",
    "Prix et position de l’ensemble"
   ]
  }
 },
 "education": {
  "h": "Formation",
  "items": [
   {
    "y": "2019 – 2023",
    "t": "Licence en informatique",
    "w": "FEI",
    "p": "Projet de fin d’études : un classifieur quantique variationnel pour le jeu de données Iris, comparé à une SVM classique.",
    "em": "Bourse complète",
    "a": "Code du projet"
   },
   {
    "y": "2024 – 2026",
    "t": "Master en génie électrique",
    "w": "FEI · IA appliquée à l’automatisation et à la robotique",
    "p": "Mémoire sur le machine learning quantique pour l’histopathologie du cancer du sein : 80,0 % d’exactitude et 86,0 % de F1, sans qu’aucun patient figure à la fois dans l’ensemble d’entraînement et dans celui de test.",
    "em": "Bourse CAPES",
    "a": "Code du mémoire"
   },
   {
    "y": "2026 – 2027",
    "t": "MBA en data science, IA et analytics",
    "w": "USP · en cours",
    "p": "Statistiques, Python, analyse de données, machine learning, intelligence artificielle et analytics.",
    "em": "Bourse complète"
   },
   {
    "y": "2027 – 2030",
    "t": "Doctorat en génie électrique",
    "w": "FEI · inscrit, cours dès février 2027",
    "p": "Correction quantique d’erreurs et décodeurs par machine learning. Un séjour d’un an à l’ETH Zurich est prévu en 2028–2029.",
    "em": "Bourse CAPES"
   }
  ]
 },
 "experience": {
  "h": "Expérience",
  "items": [
   {
    "y": "2024 – 2026",
    "t": "Chercheur en machine learning appliqué",
    "w": "FEI, São Bernardo do Campo",
    "p": "Classification d’histopathologie du cancer du sein sur BreaKHis avec ResNet-50, séparation par patient et modèles SVM et QSVM ; expériences sur du matériel IBM Quantum sur l’effet du bruit sur les noyaux quantiques."
   },
   {
    "y": "2020",
    "t": "Moniteur de géométrie analytique",
    "w": "FEI, São Bernardo do Campo",
    "p": "Permanences et feuilles d’exercices sur les matrices, les systèmes linéaires, les vecteurs, les droites et les plans."
   },
   {
    "y": "2016 – 2023",
    "t": "Développeur web et assistant de support informatique",
    "w": "Orion Benefícios, Santos",
    "p": "Création et maintenance du site de l’entreprise et de ses systèmes avec base de données, et support des postes, des réseaux et de l’infrastructure."
   }
  ]
 },
 "pub": {
  "k": "Publication · BRACIS 2026",
  "w": "Avec Reinaldo A. C. Bianchi.",
  "a": "Lire l’article"
 },
 "tools": {
  "h": "Outils",
  "groups": [
   "Machine learning et données",
   "Web et applications",
   "Systèmes",
   "Quantique et tests"
  ]
 },
 "contact": {
  "h": "Contact",
  "p": "Je cherche un poste en machine learning ou en logiciel, et je parle volontiers de recherche. Le mieux pour me joindre est l’e-mail."
 },
 "sky": {
  "h": "À propos de ce ciel",
  "p": [
   "Le trou noir est dessiné avec le même lancer de rayons qu’Isaac, mon simulateur de physique. Chaque pixel suit un rayon de lumière à rebours dans l’espace-temps courbe autour du trou (qui ne tourne pas sur lui-même), vu 18° au-dessus de son disque. Le disque est un gaz chaud, coloré comme un corps noir, plus brillant du côté qui vient vers nous et décalé vers le rouge près du trou. Le gaz tourne à la vitesse qu’il aurait réellement : le bord intérieur fait un tour en 2 secondes environ, le bord extérieur en 9. L’anneau fin et brillant autour de l’ombre est de la lumière qui a fait le tour du trou avant de nous atteindre.",
   "Les planètes et la ceinture d’astéroïdes orbitent dans le plan du disque, toutes sur la même horloge : la planète la plus proche fait un tour en environ 23 secondes, la plus éloignée en environ 46. Leurs ellipses tournent lentement, comme le prévoit la relativité générale, et chaque planète garde une face tournée vers le trou.",
   "Une seconde ici vaut 40 M de temps, où M est la masse du trou exprimée en temps. Pour un trou de 100 millions de soleils, cela fait environ 20 000 fois la vitesse réelle. La caméra tourne lentement autour du trou.",
   "La lumière des planètes, de la ceinture et des orbites est déviée par le trou, comme celle des étoiles : l’arrière de chaque orbite paraît donc relevé au-dessus de lui. Seules les planètes ne sont pas à l’échelle : elles sont dessinées des milliers de fois plus grandes qu’elles ne le seraient."
  ]
 },
 "nf": {
  "t": "Page introuvable",
  "p": "Il n’y a aucune page à cette adresse.",
  "a": "Retour à l’accueil"
 },
 "hero": {
  "h": "Tout ce que je construis *gravite* autour de quelque chose de réel.",
  "p": "Je suis Matheus. Je conçois des modèles de machine learning et des logiciels. Chaque planète ici est l’un de mes projets, en orbite autour d’un trou noir. Cliquez sur l’une d’elles pour y atterrir.",
  "cta": [
   "Voir les projets",
   "À propos"
  ]
 },
 "roadmap": {
  "h": "Feuille de route",
  "p": "Mon parcours jusqu’ici et la suite. Le temps s’écoule vers la droite, et la ligne monte pendant l’année à Zurich. Les parties en pointillé sont prévues.",
  "br": "Brésil",
  "ch": "Zurich",
  "now": "Maintenant",
  "planned": "prévu",
  "ev": {
   "orion": "Premier emploi : web et informatique",
   "bsc": "Début de la licence",
   "bscd": "Licence obtenue",
   "msc": "Début du master",
   "mscd": "Master obtenu",
   "mba": "MBA à l’USP",
   "paper": "Article à BRACIS 2026",
   "phd": "Début des cours du doctorat",
   "mbad": "MBA terminé",
   "eth": "Année à l’ETH Zurich",
   "def": "Soutenance de thèse"
  },
  "spans": {
   "orion": "Orion Benefícios · web et informatique",
   "bsc": "Licence · FEI",
   "msc": "Master · FEI",
   "mba": "MBA · USP",
   "phd": "Doctorat · FEI"
  },
  "months": [
   "janv.",
   "févr.",
   "mars",
   "avr.",
   "mai",
   "juin",
   "juil.",
   "août",
   "sept.",
   "oct.",
   "nov.",
   "déc."
  ]
 }
}
