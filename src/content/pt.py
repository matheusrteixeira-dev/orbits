C = {
 "name": "Português",
 "meta": {
  "title": "Matheus Teixeira · Engenheiro de machine learning e engenheiro de software",
  "desc": "Matheus Teixeira, engenheiro de machine learning e engenheiro de software de Santos, Brasil. Projetos, roadmap, formação, experiência e contato."
 },
 "skip": "Ir para o conteúdo",
 "nav": {
  "about": "Sobre",
  "projects": "Projetos",
  "education": "Formação",
  "experience": "Experiência",
  "contact": "Contato",
  "lang": "Idioma",
  "sections": "Seções",
  "roadmap": "Roadmap"
 },
 "role": "Engenheiro de machine learning · Engenheiro de software · Pesquisador em computação quântica",
 "ui": {
  "pause": "Pausar movimento",
  "play": "Retomar movimento",
  "land": "Pousar neste planeta",
  "landBtn": "Pousar no planeta",
  "back": "Voltar ao sistema",
  "prev": "Anterior",
  "next": "Próximo",
  "source": "Código sob consulta",
  "copy": "Copiar",
  "copied": "Copiado",
  "planets": "Planetas do sistema",
  "planet": "Planeta {n} de 5",
  "orbit": "Órbita: {r} M do buraco negro, uma volta a cada {p} s na tela",
  "nogl": "Seu navegador não executa a renderização ao vivo, por isso é mostrada uma imagem estática.",
  "year": "Ano",
  "platform": "Plataforma",
  "stack": "Tecnologias",
  "visit": "Visitar {u}",
  "how": "Como as peças se encaixam",
  "checks": "Verificações",
  "notes": "Notas de engenharia",
  "inside": "Por dentro, ao vivo",
  "nextp": "Próximo planeta",
  "illus": "Diagrama, desenhado ao vivo",
  "shot": "Capturas de tela"
 },
 "about": {
  "h": "Sobre",
  "p": [
   "Sou o Matheus Teixeira, de Santos. Trabalho com machine learning e software. Minha pesquisa é em machine learning quântico e correção quântica de erros, e a maior parte do meu código é em Python, TypeScript, React e Rust.",
   "Comecei em 2016 como desenvolvedor web e assistente de suporte de TI na Orion Benefícios. Estudo na FEI desde 2019, primeiro a graduação em Ciência da Computação e depois o mestrado em Engenharia Elétrica em IA. Minha dissertação é um pipeline híbrido quântico-clássico para histopatologia de câncer de mama, com os dados divididos por paciente, de modo que nenhum paciente aparece no treino e no teste ao mesmo tempo. Agora faço um MBA em Data Science, IA e Analytics na USP, com bolsa integral, e estou matriculado no doutorado da FEI em correção quântica de erros, com bolsa CAPES e aulas a partir de fevereiro de 2027.",
   "Abaixo estão cinco dos meus projetos, um por planeta."
  ],
  "facts": [
   [
    "Moro em",
    "Santos, Brasil"
   ],
   [
    "Idiomas",
    "Português (nativo), inglês (C2)"
   ],
   [
    "Trabalho com",
    "Machine learning, software, computação quântica"
   ]
  ],
  "alt": "Retrato de Matheus Teixeira",
  "term": {
   "who": "Matheus Teixeira: engenheiro de machine learning, engenheiro de software, pesquisador em computação quântica",
   "now": [
    "MBA em Data Science, IA e Analytics na USP, em andamento",
    "Doutorado em Engenharia Elétrica na FEI em correção quântica de erros, matriculado, aulas a partir de fevereiro de 2027",
    "Aberto a vagas em machine learning e software"
   ],
   "lang": "pt_BR (nativo)   en_US (C2, EF SET 92/100)"
  }
 },
 "projects": {
  "h": "Projetos",
  "p": "Um projeto por planeta. Pouse em um planeta para ver a história completa."
 },
 "proj": {
  "isaac": {
   "sub": "Simulações de física interativas",
   "world": "Mundo vulcânico",
   "sum": "Simulações de física interativas para estudantes, com gráficos e equações ao vivo.",
   "hl": [
    "Núcleo de física em Rust compilado para WebAssembly",
    "Interface em React, TypeScript e Three.js",
    "Testado com cargo test, Vitest e Playwright de ponta a ponta"
   ],
   "viz": "Um pêndulo duplo integrado com RK4 em passos de 2 ms. O gêmeo apagado começa 0,001 rad ao lado, e o caos separa os dois.",
   "lede": "Simulações de física interativas para estudantes, com gráficos e equações ao vivo. Núcleo de física em Rust compilado para WebAssembly; interface em React, TypeScript e Three.js; física validada com cargo test, testes unitários em Vitest e testes de ponta a ponta em Playwright.",
   "platform": "Web",
   "shots": [
    "Um pêndulo duplo com gráficos ao vivo",
    "Página inicial",
    "Biblioteca de cenas"
   ],
   "arch": [
    [
     "Rust",
     "núcleo de física"
    ],
    [
     "WebAssembly",
     "roda o núcleo no navegador"
    ],
    [
     "TypeScript",
     "motor das cenas"
    ],
    [
     "React + Three.js",
     "interface e visão 3D"
    ]
   ],
   "tests": [
    [
     "cargo test",
     "física contra resultados exatos"
    ],
    [
     "Vitest",
     "testes unitários"
    ],
    [
     "Playwright",
     "jornadas completas, desktop e celular"
    ]
   ],
   "notes": [
    [
     "Física em Rust",
     "As equações são integradas em um núcleo Rust compilado para WebAssembly. O TypeScript conduz a cena, e React e Three.js desenham os controles, os gráficos e a visão 3D."
    ],
    [
     "Conferido contra resultados exatos",
     "Cada simulação é testada contra soluções conhecidas com cargo test. O Vitest cobre a lógica da interface, e o Playwright percorre jornadas inteiras no desktop e no celular."
    ],
    [
     "Do ensino médio à pós-graduação",
     "As cenas são organizadas por área da física e por nível. Cada uma tem parâmetros com unidades, gráficos ao vivo, as equações por trás e uma explicação guiada."
    ]
   ]
  },
  "amadeo": {
   "sub": "De áudio a partitura",
   "world": "Mundo oceânico",
   "sum": "Transforma gravações de áudio em partituras editáveis, tudo no navegador.",
   "hl": [
    "Transcrição neural no navegador, com TensorFlow.js",
    "Editor de partituras, 35 instrumentos sampleados e modo de prática",
    "No ar em nove idiomas, com assinaturas Pro"
   ],
   "viz": "As linhas de altura no espectrograma viram notas na pauta.",
   "lede": "Transforma gravações de áudio em partituras editáveis, tudo no navegador: detecção neural de altura com TensorFlow.js, estimativa de tonalidade e acordes, exportação em PDF, MusicXML e MIDI. React e TypeScript, nove idiomas, testes Playwright em vários navegadores. A partitura pode ser editada, tocada em 35 instrumentos sampleados e praticada com notas caindo.",
   "platform": "Web",
   "arch": [
    [
     "Som",
     "arquivo, microfone ou vídeo"
    ],
    [
     "TensorFlow.js",
     "detecção neural de notas"
    ],
    [
     "Andamento, tonalidade, acordes",
     "estimados a partir das notas"
    ],
    [
     "VexFlow",
     "partitura gravada e editável"
    ],
    [
     "Exportação",
     "PDF · MusicXML · MIDI · WAV"
    ]
   ],
   "tests": [
    [
     "Vitest",
     "a rede real com música sintetizada"
    ],
    [
     "Playwright",
     "Chromium, Firefox e WebKit, computador e celular"
    ],
    [
     "Revisão de lançamento",
     "562 páginas sem erros nem links quebrados"
    ]
   ],
   "notes": [
    [
     "Roda no navegador",
     "A transcrição roda com TensorFlow.js no navegador, então as gravações não são enviadas. As partituras ficam no aparelho e são compartilhadas por um link que carrega a partitura inteira."
    ],
    [
     "Além da detecção de altura",
     "O Amadeo estima o andamento, o compasso, a tonalidade e os acordes, dá a cada mão a sua linha e grava a partitura com VexFlow."
    ],
    [
     "No ar",
     "O Amadeo está no ar em nove idiomas, com plano Pro pago pelo Stripe, um repertório de arranjos, afinador e metrônomo. Um app para Android está pronto e aguarda a publicação na loja."
    ]
   ],
   "shots": [
    "Início: enviar, gravar ou colar um link",
    "Für Elise como partitura, com acordes",
    "A mesma peça como rolo de piano"
   ]
  },
  "brectus": {
   "sub": "App desktop para agentes de IA de programação",
   "world": "Mundo de tempestades",
   "sum": "App desktop que envia pedidos para um agente de IA de programação separado para cada projeto.",
   "hl": [
    "Node.js e Electron",
    "Criptografia em repouso pelo cofre de chaves do sistema operacional",
    "Atualizações assinadas e CI no Windows, macOS e Linux"
   ],
   "viz": "Os pedidos são encaminhados a um agente por projeto.",
   "lede": "App desktop que envia pedidos para um agente de IA de programação separado para cada projeto. Os dados são criptografados em repouso, as atualizações são assinadas e a CI roda no Windows, no macOS e no Linux. Node.js e Electron.",
   "platform": "Desktop",
   "arch": [
    [
     "Pedido",
     "escrito uma vez"
    ],
    [
     "Roteador",
     "Node.js, Electron"
    ],
    [
     "Agentes",
     "um agente de IA de programação por projeto"
    ]
   ],
   "tests": [
    [
     "Chaveiro do sistema",
     "criptografia em repouso"
    ],
    [
     "Atualizações assinadas",
     "verificadas antes de instalar"
    ],
    [
     "CI",
     "Windows, macOS, Linux"
    ]
   ],
   "notes": [
    [
     "Um agente por projeto",
     "Cada projeto tem o seu agente de IA de programação. O app decide a qual projeto um pedido pertence e o envia para lá."
    ],
    [
     "Criptografado em repouso",
     "Os dados guardados são criptografados pelo chaveiro do próprio sistema operacional."
    ],
    [
     "Três sistemas operacionais",
     "As atualizações são assinadas, e a integração contínua roda no Windows, no macOS e no Linux."
    ]
   ],
   "shots": [
    "O mapa: cada área da minha vida como um nó",
    "O ramo da universidade, com execuções e automações",
    "Como um pedido chega ao agente certo"
   ]
  },
  "websites": {
   "sub": "Orion Benefícios, LÍDER Plus Telemedicina e um estúdio de estética",
   "world": "Mundo gelado",
   "sum": "Sites da Orion Benefícios e da LÍDER Plus Telemedicina, um site para um estúdio de estética e um portal do colaborador.",
   "hl": [
    "Astro e TypeScript, ou um pequeno gerador em Python, no Cloudflare Pages",
    "Portal do colaborador em Workers e D1, com cabeçalhos CSP",
    "Testes WCAG 2.2 AA em três motores de navegador"
   ],
   "viz": "Lighthouse dos sites das empresas: 95 no celular, 100 no computador.",
   "lede": "Sites das empresas Orion Benefícios e LÍDER Plus Telemedicina, um site para um estúdio de estética em Santos e um portal do colaborador. Os sites das empresas têm Lighthouse 95 no celular e 100 no computador e atendem à WCAG 2.2 AA.",
   "platform": "Web",
   "arch": [
    [
     "Astro + TypeScript",
     "páginas estáticas"
    ],
    [
     "Gerador em Python",
     "páginas a partir de modelos e JSON"
    ],
    [
     "Cloudflare Pages",
     "servido a partir da borda"
    ],
    [
     "Workers + D1",
     "portal do colaborador e seu banco de dados"
    ]
   ],
   "tests": [
    [
     "Cabeçalhos CSP",
     "política de segurança de conteúdo"
    ],
    [
     "WCAG 2.2 AA",
     "Chromium, Firefox, WebKit"
    ],
    [
     "Lighthouse",
     "95 no celular, 100 no computador"
    ],
    [
     "Validador do site",
     "links, metadados, dados estruturados, sitemap"
    ]
   ],
   "notes": [
    [
     "Rápidos",
     "Páginas estáticas, feitas com Astro ou com um pequeno gerador em Python, servidas pelo Cloudflare Pages. Os sites das empresas têm Lighthouse 95 no celular e 100 no computador."
    ],
    [
     "Acessíveis",
     "Os sites das empresas são testados contra a WCAG 2.2 AA nos três motores de navegador: Chromium, Firefox e WebKit."
    ],
    [
     "Seguros",
     "O portal do colaborador roda em Cloudflare Workers com um banco D1, protegido por cabeçalhos Content Security Policy."
    ]
   ],
   "shots": [
    "Página inicial da LÍDER Plus",
    "Orion Benefícios: a empresa",
    "Estúdio de estética: página inicial",
    "LÍDER Plus: para empresas e sindicatos",
    "Estúdio de estética: catálogo de tratamentos"
   ]
  },
  "allwinner": {
   "sub": "Backtest de estratégias de trading",
   "world": "Gigante gasoso",
   "sum": "Faz backtest de estratégias de trading em dados fora da amostra, com taxas e slippage.",
   "hl": [
    "Backtests walk-forward fora da amostra, depois de taxas e slippage",
    "Testes de block bootstrap contra data snooping",
    "Python, pandas, FastAPI e SQLite, com 221 testes pytest"
   ],
   "viz": "Teste walk-forward: ajusta numa janela, opera na seguinte e nunca olha adiante.",
   "lede": "Faz backtest de estratégias de trading em dados fora da amostra, com janelas walk-forward, taxas e slippage, e usa testes de block bootstrap para verificar que os resultados não são obra do acaso. Python, pandas, FastAPI e SQLite, com 221 testes em pytest.",
   "platform": "Python",
   "arch": [
    [
     "Sinais",
     "pandas"
    ],
    [
     "Walk-forward",
     "com taxas e slippage"
    ],
    [
     "Block bootstrap",
     "não é obra do acaso"
    ],
    [
     "FastAPI + SQLite",
     "pontuações e resultados"
    ]
   ],
   "tests": [
    [
     "pytest",
     "221 testes"
    ]
   ],
   "notes": [
    [
     "Janelas walk-forward",
     "Cada estratégia é ajustada em uma janela e operada na seguinte, e então a janela avança. Taxas e slippage são pagos em cada operação."
    ],
    [
     "Testes de block bootstrap",
     "Testar muitas estratégias faz algumas parecerem boas por acaso. Testes de block bootstrap verificam que cada resultado não é obra do acaso."
    ],
    [
     "Código testado",
     "Escrito em Python com pandas, servido por FastAPI e guardado em SQLite, com 221 testes em pytest."
    ]
   ],
   "shots": [
    "Tela de sinais, com o histórico de teste do projeto",
    "Placar das estratégias, walk-forward",
    "Preço e posição do conjunto"
   ]
  }
 },
 "education": {
  "h": "Formação",
  "items": [
   {
    "y": "2019 – 2023",
    "t": "Bacharelado em Ciência da Computação",
    "w": "FEI",
    "p": "Trabalho de conclusão: um classificador quântico variacional para o conjunto Iris, comparado com uma SVM clássica.",
    "em": "Bolsa integral",
    "a": "Código do projeto"
   },
   {
    "y": "2024 – 2026",
    "t": "Mestrado em Engenharia Elétrica",
    "w": "FEI · IA aplicada à automação e robótica",
    "p": "Dissertação sobre machine learning quântico para histopatologia de câncer de mama: 80,0% de acurácia e 86,0% de F1, sem nenhum paciente nos conjuntos de treino e de teste ao mesmo tempo.",
    "em": "Bolsa CAPES",
    "a": "Código da dissertação"
   },
   {
    "y": "2026 – 2027",
    "t": "MBA em Data Science, IA e Analytics",
    "w": "USP · em andamento",
    "p": "Estatística, Python, análise de dados, machine learning, inteligência artificial e analytics.",
    "em": "Bolsa integral"
   },
   {
    "y": "2027 – 2030",
    "t": "Doutorado em Engenharia Elétrica",
    "w": "FEI · matriculado, aulas a partir de fevereiro de 2027",
    "p": "Correção quântica de erros e decodificadores com machine learning. Doutorado sanduíche na ETH Zurich planejado para 2028–2029.",
    "em": "Bolsa CAPES"
   }
  ]
 },
 "experience": {
  "h": "Experiência",
  "items": [
   {
    "y": "2024 – 2026",
    "t": "Pesquisador em machine learning aplicado",
    "w": "FEI, São Bernardo do Campo",
    "p": "Classificação de histopatologia de câncer de mama no BreaKHis com ResNet-50, divisão por paciente e modelos SVM e QSVM; experimentos em hardware da IBM Quantum sobre o efeito do ruído em kernels quânticos."
   },
   {
    "y": "2020",
    "t": "Monitor de Geometria Analítica",
    "w": "FEI, São Bernardo do Campo",
    "p": "Plantões de dúvidas e listas de exercícios sobre matrizes, sistemas lineares, vetores, retas e planos."
   },
   {
    "y": "2016 – 2023",
    "t": "Desenvolvedor web e assistente de suporte de TI",
    "w": "Orion Benefícios, Santos",
    "p": "Criei e mantive o site da empresa e seus sistemas com banco de dados, e dei suporte a computadores, redes e infraestrutura."
   }
  ]
 },
 "pub": {
  "k": "Publicação · BRACIS 2026",
  "w": "Com Reinaldo A. C. Bianchi.",
  "a": "Ler o artigo"
 },
 "tools": {
  "h": "Ferramentas",
  "groups": [
   "Machine learning e dados",
   "Web e apps",
   "Sistemas",
   "Quântica e testes"
  ]
 },
 "contact": {
  "h": "Contato",
  "p": "Estou aberto a vagas em machine learning e software, e a colaborações de pesquisa. O e-mail é o jeito mais rápido de falar comigo."
 },
 "sky": {
  "h": "Sobre este céu",
  "p": [
   "O buraco negro gira a 90% da velocidade máxima e é visto 18° acima do seu disco. A imagem vem de raios de luz traçados na métrica de Kerr, e o disco é sombreado ao vivo na sua placa de vídeo, com cores de corpo negro, feixe Doppler no lado que se aproxima e desvio gravitacional para o vermelho.",
   "Os planetas e o cinturão de asteroides orbitam no plano do disco, o plano equatorial do buraco, onde a rotação não inclina as órbitas. Tudo segue um só relógio, na taxa orbital de Kerr: a borda interna do disco dá uma volta em menos de um segundo, o planeta mais externo em cerca de 45 segundos. As elipses giram devagar, como prevê a relatividade geral, e cada planeta mantém uma face voltada para o buraco.",
   "Um segundo aqui são 40 M de tempo, em que M é a massa do buraco em unidades de tempo. Para um buraco de 100 milhões de sóis, isso é cerca de 20.000 vezes a velocidade real. A câmera gira devagar em torno do buraco. A luz dos planetas, do cinturão e das estrelas é desviada pela gravidade do buraco, por isso o lado de trás de cada órbita aparece erguido acima dele.",
   "As distâncias estão na mesma escala, mas os planetas aparecem milhares de vezes maiores do que seriam."
  ]
 },
 "nf": {
  "t": "Página não encontrada",
  "p": "Não há nenhuma página neste endereço.",
  "a": "Voltar ao início"
 },
 "hero": {
  "h": "Tudo o que eu construo *orbita* algo real.",
  "p": "Sou o Matheus. Trabalho com machine learning e software, e a maior parte do meu código é em Python, TypeScript, React e Rust. Cada planeta aqui é um dos meus projetos, orbitando um buraco negro em rotação. Clique em um para pousar nele.",
  "cta": [
   "Ver os projetos",
   "Sobre mim"
  ]
 },
 "roadmap": {
  "h": "Roadmap",
  "p": "Meu caminho até aqui e o que vem a seguir. O tempo corre para a direita, e a linha sobe no ano em Zurique. As partes tracejadas são planejadas.",
  "br": "Brasil",
  "ch": "Zurique",
  "now": "Agora",
  "planned": "planejado",
  "ev": {
   "orion": "Primeiro emprego: web e TI",
   "bsc": "Início do bacharelado",
   "bscd": "Bacharelado concluído",
   "msc": "Início do mestrado",
   "mscd": "Mestrado concluído",
   "mba": "MBA na USP",
   "paper": "Artigo no BRACIS 2026",
   "phd": "Início das aulas do doutorado",
   "mbad": "MBA concluído",
   "eth": "Ano na ETH Zurich",
   "def": "Defesa da tese"
  },
  "spans": {
   "orion": "Orion Benefícios · web e TI",
   "bsc": "Bacharelado · FEI",
   "msc": "Mestrado · FEI",
   "mba": "MBA · USP",
   "phd": "Doutorado · FEI"
  },
  "months": [
   "jan",
   "fev",
   "mar",
   "abr",
   "mai",
   "jun",
   "jul",
   "ago",
   "set",
   "out",
   "nov",
   "dez"
  ]
 }
}
