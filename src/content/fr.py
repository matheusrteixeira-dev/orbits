C = {
 "name": "Français",
 "meta": {
  "title": "Matheus Teixeira · Ingénieur en machine learning et développeur logiciel",
  "desc": "Matheus Teixeira, ingénieur en machine learning et développeur logiciel de Santos, au Brésil. Projets, feuille de route, formation, expérience et contact."
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
 "role": "Ingénieur en machine learning · Développeur logiciel",
 "ui": {
  "pause": "Mettre en pause",
  "play": "Reprendre le mouvement",
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
   "Je suis Matheus, ingénieur en machine learning et développeur logiciel, originaire de Santos, au Brésil. J’écris du logiciel depuis 2016, quand j’ai commencé comme développeur web et assistant de support informatique chez Orion Benefícios, et j’étudie à la FEI depuis 2019.",
   "Pour mon master, j’ai construit un pipeline reproductible qui classe des images histopathologiques de cancer du sein, en combinant des caractéristiques ResNet-50 avec des machines à vecteurs de support classiques et quantiques, et je l’ai exécuté sur du matériel IBM Quantum. Je suis maintenant un MBA en Data Science, IA et Analytics à l’USP avec une bourse complète, et je suis inscrit en doctorat à la FEI, avec une bourse CAPES et des cours à partir de février 2027.",
   "En dehors de la recherche, je développe des logiciels de bout en bout, du modèle ou de la physique jusqu’à l’interface et aux tests. Les cinq projets ci-dessous sont ceux qui me tiennent le plus à cœur."
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
    "Machine learning, vision par ordinateur, logiciel"
   ]
  ],
  "alt": "Portrait de Matheus Teixeira",
  "term": {
   "who": "Matheus Teixeira : ingénieur en machine learning et développeur logiciel",
   "now": [
    "MBA en Data Science, IA et Analytics à l’USP, en cours",
    "Doctorat en génie électrique à la FEI, inscrit, cours à partir de février 2027",
    "Ouvert aux postes en machine learning et en logiciel"
   ],
   "lang": "pt_BR (langue maternelle)   en_US (C2, EF SET 92/100)"
  }
 },
 "projects": {
  "h": "Projets",
  "p": "Un projet par planète. Posez-vous sur une planète pour lire l’histoire complète."
 },
 "proj": {
  "isaac": {
   "sub": "Simulations physiques interactives en 3D",
   "world": "Monde volcanique",
   "sum": "De la physique à manipuler dans le navigateur. Un moteur en Rust compilé en WebAssembly calcule les simulations, et React, TypeScript et Three.js les affichent.",
   "hl": [
    "Cœur physique en Rust compilé en WebAssembly",
    "Interface en React, TypeScript et Three.js",
    "Testé avec cargo test, Vitest et Playwright de bout en bout"
   ],
   "viz": "Un double pendule intégré par RK4 par pas de 2 ms. Son jumeau pâle part à 0,001 rad d’écart, et le chaos les sépare.",
   "lede": "Un laboratoire de physique dans le navigateur. Vous changez un paramètre et la scène, les graphiques et les équations répondent aussitôt, d’une balle lancée jusqu’à un trou noir.",
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
   "sum": "Transforme un enregistrement en partition que l’on peut modifier, jouer et partager, entièrement dans le navigateur. En ligne, avec une offre Pro.",
   "hl": [
    "Transcription neuronale dans le navigateur, avec TensorFlow.js",
    "Éditeur de partitions, 35 instruments échantillonnés et un mode d’entraînement",
    "En ligne en neuf langues, avec abonnements Pro"
   ],
   "viz": "Les traces de hauteur du spectrogramme deviennent des notes sur la portée.",
   "lede": "Amadeo écoute un fichier audio, un enregistrement au micro ou une vidéo et écrit la musique : notes, tempo, mesure, tonalité et accords. La partition peut être modifiée, jouée sur 35 instruments échantillonnés, travaillée avec des notes qui tombent et exportée en PDF, MusicXML, MIDI ou WAV. Tout se passe dans le navigateur.",
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
     "Le son ne quitte pas l’appareil",
     "La transcription tourne avec TensorFlow.js dans le navigateur : les enregistrements ne sont pas envoyés. Les partitions restent sur l’appareil de l’utilisateur et se partagent par un lien qui contient toute la partition."
    ],
    [
     "Des hauteurs à la musique",
     "Une liste de hauteurs n’est pas encore une partition. Amadeo suit le tempo, trouve la mesure, la tonalité et les accords, donne à chaque main sa propre ligne et grave le résultat avec VexFlow."
    ],
    [
     "Un produit, pas une démo",
     "Amadeo est en ligne en neuf langues, avec une offre Pro payée via Stripe, un répertoire d’arrangements, un accordeur et un métronome. Une application Android est prête et attend sa publication sur le store."
    ]
   ],
   "shots": [
    "Accueil : importer, enregistrer ou coller un lien",
    "La Lettre à Élise en partition, avec accords",
    "Le même morceau en rouleau de piano"
   ]
  },
  "brectus": {
   "sub": "Orchestrateur local d’agents de code IA",
   "world": "Monde d’orages",
   "sum": "Une application de bureau qui envoie chaque demande à l’agent de code du bon projet.",
   "hl": [
    "Node.js et Electron",
    "Chiffrement au repos via le trousseau du système d’exploitation",
    "Mises à jour signées et CI sous Windows, macOS et Linux"
   ],
   "viz": "Les demandes sont acheminées vers un agent par projet.",
   "lede": "Une application de bureau qui envoie chaque demande à l’agent de programmation du bon projet, pour faire avancer plusieurs projets depuis un seul endroit.",
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
     "un agent Claude Code par projet"
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
     "Chaque projet a son propre agent Claude Code. Le routeur décide à quel projet appartient une demande et la lui transmet."
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
   "sum": "Des sites pour trois entreprises brésiliennes, et un portail pour les employés.",
   "hl": [
    "Astro et TypeScript, ou un petit générateur en Python, sur Cloudflare Pages",
    "Portail des employés sur Workers et D1, avec en-têtes CSP",
    "Tests WCAG 2.2 AA dans trois moteurs de navigateur"
   ],
   "viz": "Scores Lighthouse : 95 sur mobile, 100 sur ordinateur.",
   "lede": "Des sites pour deux entreprises brésiliennes, Orion Benefícios et LÍDER Plus Telemedicina, et pour un institut d’esthétique indépendant à Santos, ainsi qu’un portail pour les employés. Les trois sont conçus pour être rapides, sûrs et accessibles.",
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
     "Rapides",
     "Des pages statiques, construites avec Astro ou avec un petit générateur en Python, servies par Cloudflare Pages. Lighthouse donne 95 sur mobile et 100 sur ordinateur."
    ],
    [
     "Accessibles",
     "Des tests automatiques WCAG 2.2 AA tournent dans les trois moteurs de navigateur : Chromium, Firefox et WebKit."
    ],
    [
     "Sûrs",
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
   "sub": "Recherche de signaux sur le marché crypto",
   "world": "Géante gazeuse",
   "sum": "Du code de recherche qui vérifie si des signaux de trading tiennent hors échantillon.",
   "hl": [
    "Backtests walk-forward hors échantillon, après frais et slippage",
    "Tests de block bootstrap contre le data snooping",
    "Python, pandas, FastAPI et SQLite, avec 221 tests pytest"
   ],
   "viz": "Test walk-forward : ajuster sur une fenêtre, trader sur la suivante, sans jamais regarder en avant.",
   "lede": "Un logiciel de recherche qui pose une seule question à chaque signal de trading : fonctionne-t-il encore sur des données qu’il n’a jamais vues, après frais et slippage ?",
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
     "chance ou compétence ?"
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
     "Ne jamais regarder en avant",
     "Chaque stratégie est ajustée sur une fenêtre et négociée sur la suivante, puis la fenêtre avance. Les frais et le slippage sont payés à chaque opération."
    ],
    [
     "Chance ou compétence",
     "Essayer beaucoup de stratégies en fait paraître certaines bonnes par hasard. Des tests de block bootstrap confrontent chaque résultat à ce risque."
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
  "p": "Je suis ouvert aux postes en machine learning et en logiciel, ainsi qu’aux collaborations de recherche. Le plus rapide pour me joindre est l’e-mail."
 },
 "sky": {
  "h": "À propos de ce ciel",
  "p": [
   "Le trou noir tourne à 90 % de la vitesse maximale et il est vu 18° au-dessus de son disque. Son image vient de rayons lumineux tracés dans la métrique de Kerr, et le disque est ombré en direct sur votre carte graphique, avec des couleurs de corps noir, l’effet Doppler relativiste du côté qui s’approche et le décalage gravitationnel vers le rouge.",
   "Les planètes et la ceinture d’astéroïdes orbitent dans le plan du disque, le plan équatorial du trou noir, où sa rotation ne peut pas incliner leurs orbites. Tout suit une seule horloge, à la fréquence orbitale de Kerr : le bord intérieur du disque fait un tour en moins d’une seconde, la planète la plus éloignée en 45 secondes environ. Leurs ellipses tournent lentement, comme le prévoit la relativité générale, et chaque planète montre toujours la même face au trou noir.",
   "Une seconde ici vaut 40 M de temps, où M est la masse du trou noir en unités de temps ; pour un trou noir de quatre millions de soleils, comme celui du centre de la Voie lactée, cela fait environ 800 fois la vitesse réelle. La caméra tourne lentement autour du trou noir, et la lumière de tout ce qui se trouve derrière, planètes, ceinture ou étoiles, est déviée par sa gravité.",
   "Les distances partagent une même échelle, mais les planètes sont dessinées des centaines à mille fois plus grandes qu’elles ne le seraient."
  ]
 },
 "nf": {
  "t": "Page introuvable",
  "p": "Cette page a quitté le système.",
  "a": "Retour à l’accueil"
 },
 "hero": {
  "h": "Tout ce que je construis *gravite* autour de quelque chose de réel.",
  "p": "Je suis Matheus. J’entraîne des modèles en Python et PyTorch et je livre des applications testées en TypeScript et en Rust. Chaque planète ici est l’un de mes projets, en orbite autour d’un trou noir en rotation. Cliquez sur l’une d’elles pour vous y poser.",
  "cta": [
   "Voir les projets",
   "À propos"
  ]
 },
 "roadmap": {
  "h": "Feuille de route",
  "p": "D’où je viens et où je vais, dessiné comme une ligne d’univers. Le temps s’écoule vers la droite, et la ligne monte pendant l’année à Zurich. Les parties en pointillé sont prévues.",
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
