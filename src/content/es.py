C = {
 "name": "Español",
 "meta": {
  "title": "Matheus Teixeira · Ingeniero de machine learning e ingeniero de software",
  "desc": "Matheus Teixeira, ingeniero de machine learning e ingeniero de software de Santos, Brasil. Proyectos, hoja de ruta, formación, experiencia y contacto."
 },
 "skip": "Ir al contenido",
 "nav": {
  "about": "Sobre mí",
  "projects": "Proyectos",
  "education": "Formación",
  "experience": "Experiencia",
  "contact": "Contacto",
  "lang": "Idioma",
  "sections": "Secciones",
  "roadmap": "Hoja de ruta"
 },
 "role": "Ingeniero de machine learning · Ingeniero de software · Investigador en computación cuántica",
 "ui": {
  "pause": "Pausar el movimiento",
  "play": "Reanudar el movimiento",
  "land": "Aterrizar en este planeta",
  "landBtn": "Aterrizar en el planeta",
  "back": "Volver al sistema",
  "prev": "Anterior",
  "next": "Siguiente",
  "source": "Código a petición",
  "copy": "Copiar",
  "copied": "Copiado",
  "planets": "Planetas del sistema",
  "planet": "Planeta {n} de 5",
  "orbit": "Órbita: a {r} M del agujero, una vuelta cada {p} s en pantalla",
  "nogl": "Tu navegador no puede ejecutar el renderizado en vivo, así que se muestra una imagen fija.",
  "year": "Año",
  "platform": "Plataforma",
  "stack": "Tecnologías",
  "visit": "Visitar {u}",
  "how": "Cómo encajan las piezas",
  "checks": "Comprobaciones",
  "notes": "Notas de ingeniería",
  "inside": "Por dentro, en vivo",
  "nextp": "Siguiente planeta",
  "illus": "Diagrama, dibujado en vivo",
  "shot": "Capturas de pantalla"
 },
 "about": {
  "h": "Sobre mí",
  "p": [
   "Soy Matheus Teixeira, de Santos, Brasil. Trabajo en machine learning y software. Mi investigación es en machine learning cuántico y corrección cuántica de errores, y la mayor parte de mi código está en Python, TypeScript, React y Rust.",
   "Empecé en 2016 como desarrollador web y asistente de soporte informático en Orion Benefícios. Estudio en la FEI desde 2019, primero el grado en Ciencias de la Computación y después el máster en Ingeniería Eléctrica en IA. Mi tesis de máster es un pipeline híbrido cuántico-clásico para histopatología de cáncer de mama, con los datos divididos por paciente, de modo que ningún paciente aparece a la vez en entrenamiento y en prueba. Ahora curso un MBA en Data Science, IA y Analytics en la USP con beca completa, y estoy matriculado en el doctorado de la FEI en corrección cuántica de errores, con beca CAPES y clases desde febrero de 2027.",
   "Abajo están cinco de mis proyectos, uno por planeta."
  ],
  "facts": [
   [
    "Vivo en",
    "Santos, Brasil"
   ],
   [
    "Idiomas",
    "Portugués (nativo), inglés (C2)"
   ],
   [
    "Trabajo en",
    "Machine learning, software, computación cuántica"
   ]
  ],
  "alt": "Retrato de Matheus Teixeira",
  "term": {
   "who": "Matheus Teixeira: ingeniero de machine learning, ingeniero de software, investigador en computación cuántica",
   "now": [
    "MBA en Data Science, IA y Analytics en la USP, en curso",
    "Doctorado en Ingeniería Eléctrica en la FEI en corrección cuántica de errores, matriculado, clases desde febrero de 2027",
    "Abierto a puestos de machine learning y software"
   ],
   "lang": "pt_BR (nativo)   en_US (C2, EF SET 92/100)"
  }
 },
 "projects": {
  "h": "Proyectos",
  "p": "Un proyecto por planeta. Aterriza en un planeta para ver la historia completa."
 },
 "proj": {
  "isaac": {
   "sub": "Simulaciones físicas interactivas",
   "world": "Mundo volcánico",
   "sum": "Simulaciones físicas interactivas para estudiantes, con gráficos y ecuaciones en vivo.",
   "hl": [
    "Núcleo de física en Rust compilado a WebAssembly",
    "Interfaz en React, TypeScript y Three.js",
    "Probado con cargo test, Vitest y Playwright de extremo a extremo"
   ],
   "viz": "Un péndulo doble integrado con RK4 en pasos de 2 ms. El gemelo tenue empieza a 0,001 rad, y el caos separa a los dos.",
   "lede": "Simulaciones físicas interactivas para estudiantes, con gráficos y ecuaciones en vivo. Núcleo de física en Rust compilado a WebAssembly; interfaz en React, TypeScript y Three.js; física validada con cargo test, pruebas unitarias en Vitest y pruebas de extremo a extremo en Playwright.",
   "platform": "Web",
   "shots": [
    "Un péndulo doble con gráficos en vivo",
    "Página de inicio",
    "Biblioteca de escenas"
   ],
   "arch": [
    [
     "Rust",
     "núcleo de física"
    ],
    [
     "WebAssembly",
     "lo ejecuta en el navegador"
    ],
    [
     "TypeScript",
     "motor de escenas"
    ],
    [
     "React + Three.js",
     "interfaz y vista 3D"
    ]
   ],
   "tests": [
    [
     "cargo test",
     "física contra resultados exactos"
    ],
    [
     "Vitest",
     "pruebas unitarias"
    ],
    [
     "Playwright",
     "recorridos completos, escritorio y móvil"
    ]
   ],
   "notes": [
    [
     "Física en Rust",
     "Las ecuaciones se integran en un núcleo de Rust compilado a WebAssembly. TypeScript dirige la escena, y React y Three.js dibujan los controles, los gráficos y la vista 3D."
    ],
    [
     "Comprobado con resultados exactos",
     "Cada simulación se prueba contra soluciones conocidas con cargo test. Vitest cubre la lógica de la interfaz y Playwright recorre trayectos completos en escritorio y móvil."
    ],
    [
     "Del instituto al posgrado",
     "Las escenas se ordenan por área de la física y por nivel. Cada una tiene parámetros con unidades, gráficos en vivo, las ecuaciones que hay detrás y una explicación guiada."
    ]
   ]
  },
  "amadeo": {
   "sub": "De audio a partitura",
   "world": "Mundo oceánico",
   "sum": "Convierte grabaciones de audio en partituras editables, todo en el navegador.",
   "hl": [
    "Transcripción neuronal en el navegador, con TensorFlow.js",
    "Editor de partituras, 35 instrumentos muestreados y modo de práctica",
    "En línea en nueve idiomas, con suscripciones Pro"
   ],
   "viz": "Las trazas de tono del espectrograma se convierten en notas en el pentagrama.",
   "lede": "Convierte grabaciones de audio en partituras editables, todo en el navegador: detección neuronal de alturas con TensorFlow.js, estimación de tonalidad y acordes, exportación a PDF, MusicXML y MIDI. React y TypeScript, nueve idiomas, pruebas Playwright en varios navegadores. La partitura se puede editar, tocar con 35 instrumentos muestreados y practicar con notas que caen.",
   "platform": "Web",
   "arch": [
    [
     "Sonido",
     "archivo, micrófono o vídeo"
    ],
    [
     "TensorFlow.js",
     "detección neuronal de notas"
    ],
    [
     "Tempo, tonalidad, acordes",
     "estimados a partir de las notas"
    ],
    [
     "VexFlow",
     "partitura grabada y editable"
    ],
    [
     "Exportación",
     "PDF · MusicXML · MIDI · WAV"
    ]
   ],
   "tests": [
    [
     "Vitest",
     "la red real con música sintetizada"
    ],
    [
     "Playwright",
     "Chromium, Firefox y WebKit, ordenador y móvil"
    ],
    [
     "Revisión de lanzamiento",
     "562 páginas sin errores ni enlaces rotos"
    ]
   ],
   "notes": [
    [
     "Funciona en el navegador",
     "La transcripción funciona con TensorFlow.js en el navegador, así que las grabaciones no se suben. Las partituras se quedan en el dispositivo y se comparten con un enlace que lleva la partitura entera."
    ],
    [
     "Más allá de detectar alturas",
     "Amadeo estima el tempo, el compás, la tonalidad y los acordes, da a cada mano su propia línea y graba la partitura con VexFlow."
    ],
    [
     "En línea",
     "Amadeo está en línea en nueve idiomas, con un plan Pro pagado con Stripe, un repertorio de arreglos, un afinador y un metrónomo. Una app para Android está lista y espera su publicación en la tienda."
    ]
   ],
   "shots": [
    "Inicio: subir, grabar o pegar un enlace",
    "Für Elise como partitura, con acordes",
    "La misma pieza como rollo de piano"
   ]
  },
  "brectus": {
   "sub": "App de escritorio para agentes de IA de programación",
   "world": "Mundo de tormentas",
   "sum": "App de escritorio que envía peticiones a un agente de IA de programación distinto para cada proyecto.",
   "hl": [
    "Node.js y Electron",
    "Cifrado en reposo mediante el almacén de claves del sistema operativo",
    "Actualizaciones firmadas y CI en Windows, macOS y Linux"
   ],
   "viz": "Las peticiones se dirigen a un agente por proyecto.",
   "lede": "App de escritorio que envía peticiones a un agente de IA de programación distinto para cada proyecto. Los datos se cifran en reposo, las actualizaciones van firmadas y la CI se ejecuta en Windows, macOS y Linux. Node.js y Electron.",
   "platform": "Escritorio",
   "arch": [
    [
     "Petición",
     "escrita una vez"
    ],
    [
     "Enrutador",
     "Node.js, Electron"
    ],
    [
     "Agentes",
     "un agente de IA de programación por proyecto"
    ]
   ],
   "tests": [
    [
     "Llavero del sistema",
     "cifrado en reposo"
    ],
    [
     "Actualizaciones firmadas",
     "verificadas antes de instalar"
    ],
    [
     "CI",
     "Windows, macOS, Linux"
    ]
   ],
   "notes": [
    [
     "Un agente por proyecto",
     "Cada proyecto tiene su propio agente de IA de programación. La app decide a qué proyecto pertenece una petición y la envía allí."
    ],
    [
     "Cifrado en reposo",
     "Los datos guardados se cifran mediante el llavero del propio sistema operativo."
    ],
    [
     "Tres sistemas operativos",
     "Las actualizaciones van firmadas, y la integración continua se ejecuta en Windows, macOS y Linux."
    ]
   ],
   "shots": [
    "El mapa: cada área de mi vida como un nodo",
    "La rama de la universidad, con ejecuciones y automatizaciones",
    "Cómo una petición llega al agente correcto"
   ]
  },
  "websites": {
   "sub": "Orion Benefícios, LÍDER Plus Telemedicina y un estudio de estética",
   "world": "Mundo helado",
   "sum": "Sitios de Orion Benefícios y LÍDER Plus Telemedicina, un sitio para un estudio de estética y un portal para empleados.",
   "hl": [
    "Astro y TypeScript, o un pequeño generador en Python, en Cloudflare Pages",
    "Portal para empleados en Workers y D1, con cabeceras CSP",
    "Pruebas WCAG 2.2 AA en tres motores de navegador"
   ],
   "viz": "Lighthouse de los sitios de las empresas: 95 en móvil, 100 en ordenador.",
   "lede": "Sitios de las empresas Orion Benefícios y LÍDER Plus Telemedicina, un sitio para un estudio de estética en Santos y un portal para empleados. Los sitios de las empresas sacan 95 en móvil y 100 en ordenador en Lighthouse y cumplen WCAG 2.2 AA.",
   "platform": "Web",
   "arch": [
    [
     "Astro + TypeScript",
     "páginas estáticas"
    ],
    [
     "Generador en Python",
     "páginas a partir de plantillas y JSON"
    ],
    [
     "Cloudflare Pages",
     "servido desde el borde"
    ],
    [
     "Workers + D1",
     "portal para empleados y su base de datos"
    ]
   ],
   "tests": [
    [
     "Cabeceras CSP",
     "política de seguridad de contenido"
    ],
    [
     "WCAG 2.2 AA",
     "Chromium, Firefox, WebKit"
    ],
    [
     "Lighthouse",
     "95 en móvil, 100 en ordenador"
    ],
    [
     "Validador del sitio",
     "enlaces, metadatos, datos estructurados, sitemap"
    ]
   ],
   "notes": [
    [
     "Rápidos",
     "Páginas estáticas, hechas con Astro o con un pequeño generador en Python, servidas por Cloudflare Pages. Los sitios de las empresas sacan 95 en móvil y 100 en ordenador en Lighthouse."
    ],
    [
     "Accesibles",
     "Los sitios de las empresas se prueban contra WCAG 2.2 AA en los tres motores de navegador: Chromium, Firefox y WebKit."
    ],
    [
     "Seguros",
     "El portal de empleados funciona en Cloudflare Workers con una base de datos D1, detrás de cabeceras Content Security Policy."
    ]
   ],
   "shots": [
    "Página de inicio de LÍDER Plus",
    "Orion Benefícios: la empresa",
    "Estudio de estética: página de inicio",
    "LÍDER Plus: para empresas y sindicatos",
    "Estudio de estética: catálogo de tratamientos"
   ]
  },
  "allwinner": {
   "sub": "Backtesting de estrategias de trading",
   "world": "Gigante gaseoso",
   "sum": "Hace backtesting de estrategias de trading con datos fuera de la muestra, con comisiones y slippage.",
   "hl": [
    "Backtests walk-forward fuera de la muestra, después de comisiones y slippage",
    "Pruebas de block bootstrap contra el data snooping",
    "Python, pandas, FastAPI y SQLite, con 221 pruebas pytest"
   ],
   "viz": "Prueba walk-forward: ajustar en una ventana, operar en la siguiente y nunca mirar adelante.",
   "lede": "Hace backtesting de estrategias de trading con datos fuera de la muestra, con ventanas walk-forward, comisiones y slippage, y usa pruebas de block bootstrap para comprobar que los resultados no se deben al azar. Python, pandas, FastAPI y SQLite, con 221 pruebas en pytest.",
   "platform": "Python",
   "arch": [
    [
     "Señales",
     "pandas"
    ],
    [
     "Walk-forward",
     "con comisiones y slippage"
    ],
    [
     "Block bootstrap",
     "no se debe al azar"
    ],
    [
     "FastAPI + SQLite",
     "puntuaciones y resultados"
    ]
   ],
   "tests": [
    [
     "pytest",
     "221 pruebas"
    ]
   ],
   "notes": [
    [
     "Ventanas walk-forward",
     "Cada estrategia se ajusta en una ventana y se opera en la siguiente, y luego la ventana avanza. Se pagan comisiones y slippage en cada operación."
    ],
    [
     "Pruebas de block bootstrap",
     "Probar muchas estrategias hace que algunas parezcan buenas por azar. Las pruebas de block bootstrap comprueban que cada resultado no se debe al azar."
    ],
    [
     "Código probado",
     "Escrito en Python con pandas, servido con FastAPI y guardado en SQLite, con 221 pruebas en pytest."
    ]
   ],
   "shots": [
    "Pantalla de señales, con el historial de prueba del proyecto",
    "Clasificación de estrategias, walk-forward",
    "Precio y postura del conjunto"
   ]
  }
 },
 "education": {
  "h": "Formación",
  "items": [
   {
    "y": "2019 – 2023",
    "t": "Grado en Ciencias de la Computación",
    "w": "FEI",
    "p": "Proyecto final: un clasificador cuántico variacional para el conjunto Iris, comparado con una SVM clásica.",
    "em": "Beca completa",
    "a": "Código del proyecto"
   },
   {
    "y": "2024 – 2026",
    "t": "Maestría en Ingeniería Eléctrica",
    "w": "FEI · IA aplicada a la automatización y la robótica",
    "p": "Tesis sobre machine learning cuántico para histopatología de cáncer de mama: 80,0% de exactitud y 86,0% de F1, sin ningún paciente a la vez en el conjunto de entrenamiento y en el de prueba.",
    "em": "Beca CAPES",
    "a": "Código de la tesis"
   },
   {
    "y": "2026 – 2027",
    "t": "MBA en Data Science, IA y Analytics",
    "w": "USP · en curso",
    "p": "Estadística, Python, análisis de datos, machine learning, inteligencia artificial y analytics.",
    "em": "Beca completa"
   },
   {
    "y": "2027 – 2030",
    "t": "Doctorado en Ingeniería Eléctrica",
    "w": "FEI · matriculado, clases desde febrero de 2027",
    "p": "Corrección cuántica de errores y decodificadores con machine learning. Está prevista una estancia de un año en la ETH Zurich en 2028–2029.",
    "em": "Beca CAPES"
   }
  ]
 },
 "experience": {
  "h": "Experiencia",
  "items": [
   {
    "y": "2024 – 2026",
    "t": "Investigador en machine learning aplicado",
    "w": "FEI, São Bernardo do Campo",
    "p": "Clasificación de histopatología de cáncer de mama en BreaKHis con ResNet-50, divisiones por paciente y modelos SVM y QSVM; experimentos en hardware de IBM Quantum sobre cómo el ruido afecta a los kernels cuánticos."
   },
   {
    "y": "2020",
    "t": "Ayudante de cátedra, Geometría Analítica",
    "w": "FEI, São Bernardo do Campo",
    "p": "Sesiones de dudas y listas de ejercicios sobre matrices, sistemas lineales, vectores, rectas y planos."
   },
   {
    "y": "2016 – 2023",
    "t": "Desarrollador web y asistente de soporte de TI",
    "w": "Orion Benefícios, Santos",
    "p": "Creé y mantuve el sitio web de la empresa y sus sistemas con base de datos, y di soporte a ordenadores, redes e infraestructura."
   }
  ]
 },
 "pub": {
  "k": "Publicación · BRACIS 2026",
  "w": "Con Reinaldo A. C. Bianchi.",
  "a": "Leer el artículo"
 },
 "tools": {
  "h": "Herramientas",
  "groups": [
   "Machine learning y datos",
   "Web y aplicaciones",
   "Sistemas",
   "Cuántica y pruebas"
  ]
 },
 "contact": {
  "h": "Contacto",
  "p": "Estoy abierto a puestos en machine learning y software, y a colaboraciones de investigación. El correo es la forma más rápida de contactarme."
 },
 "sky": {
  "h": "Sobre este cielo",
  "p": [
   "El agujero negro gira al 90 % de la velocidad máxima y se ve 18° por encima de su disco. Su imagen sale de rayos de luz trazados en la métrica de Kerr, y el disco se sombrea en vivo en tu tarjeta gráfica, con colores de cuerpo negro, haz Doppler en el lado que se acerca y corrimiento al rojo gravitacional.",
   "Los planetas y el cinturón de asteroides orbitan en el plano del disco, el plano ecuatorial del agujero, donde el giro no inclina sus órbitas. Todo sigue un único reloj a la frecuencia orbital de Kerr: el borde interior del disco da una vuelta en menos de un segundo y el planeta más exterior en unos 45 segundos. Sus elipses giran despacio, como predice la relatividad general, y cada planeta muestra siempre la misma cara al agujero.",
   "Un segundo aquí equivale a 40 M de tiempo, donde M es la masa del agujero en unidades de tiempo. Para un agujero de 100 millones de soles, son unas 20.000 veces la velocidad real. La cámara gira despacio alrededor del agujero. La luz de los planetas, el cinturón y las estrellas se curva por la gravedad del agujero, por eso la parte trasera de cada órbita aparece levantada sobre él.",
   "Las distancias comparten una misma escala, pero los planetas se dibujan miles de veces más grandes de lo que serían."
  ]
 },
 "nf": {
  "t": "Página no encontrada",
  "p": "No hay ninguna página en esta dirección.",
  "a": "Volver al inicio"
 },
 "hero": {
  "h": "Todo lo que construyo *orbita* algo real.",
  "p": "Soy Matheus. Trabajo en machine learning y software, y la mayor parte de mi código está en Python, TypeScript, React y Rust. Cada planeta de aquí es uno de mis proyectos, en órbita alrededor de un agujero negro en rotación. Haz clic en uno para aterrizar en él.",
  "cta": [
   "Ver los proyectos",
   "Sobre mí"
  ]
 },
 "roadmap": {
  "h": "Hoja de ruta",
  "p": "Mi camino hasta ahora y lo que viene. El tiempo avanza hacia la derecha, y la línea sube durante el año en Zúrich. Las partes discontinuas están planificadas.",
  "br": "Brasil",
  "ch": "Zúrich",
  "now": "Ahora",
  "planned": "planificado",
  "ev": {
   "orion": "Primer empleo: web e informática",
   "bsc": "Empieza el grado",
   "bscd": "Grado terminado",
   "msc": "Empieza el máster",
   "mscd": "Máster terminado",
   "mba": "MBA en la USP",
   "paper": "Artículo en BRACIS 2026",
   "phd": "Empiezan las clases del doctorado",
   "mbad": "MBA terminado",
   "eth": "Año en la ETH Zúrich",
   "def": "Defensa de la tesis"
  },
  "spans": {
   "orion": "Orion Benefícios · web e informática",
   "bsc": "Grado · FEI",
   "msc": "Máster · FEI",
   "mba": "MBA · USP",
   "phd": "Doctorado · FEI"
  },
  "months": [
   "ene",
   "feb",
   "mar",
   "abr",
   "may",
   "jun",
   "jul",
   "ago",
   "sep",
   "oct",
   "nov",
   "dic"
  ]
 }
}
