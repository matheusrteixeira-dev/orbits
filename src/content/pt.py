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
  "shot": "Capturas de tela",
  "cv": "Currículo (PDF)",
  "live": "Usar aqui",
  "liveT": "{n}, ao vivo"
 },
 "about": {
  "h": "Sobre",
  "p": [
   "Sou o Matheus Teixeira, de Santos. Minha pesquisa é em machine learning quântico e correção quântica de erros.",
   "Comecei em 2016 como desenvolvedor web e assistente de suporte de TI na Orion Benefícios. Estudo na FEI desde 2019, primeiro a graduação em Ciência da Computação e depois o mestrado em Engenharia Elétrica, com foco em IA. Minha dissertação é um pipeline híbrido quântico-clássico para histopatologia de câncer de mama, com os dados divididos por paciente, de modo que nenhum paciente aparece no treino e no teste ao mesmo tempo. Agora faço um MBA em Data Science, IA e Analytics na USP, com bolsa integral, e estou matriculado no doutorado da FEI em correção quântica de erros, com bolsa CAPES e aulas a partir de fevereiro de 2027.",
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
  "p": "Pouse em um planeta para ver o projeto de perto."
 },
 "proj": {
  "isaac": {
   "sub": "Simulações de física interativas",
   "world": "Mundo vulcânico",
   "sum": "Feito para estudantes, do ensino médio à pós-graduação. Cada cena roda no navegador.",
   "hl": [
    "Núcleo de física em Rust compilado para WebAssembly",
    "Gráficos ao vivo, equações e explicação guiada em cada cena",
    "Testado com cargo test, Vitest e Playwright de ponta a ponta"
   ],
   "viz": "Um pêndulo duplo integrado com RK4 em passos de 2 ms. O gêmeo apagado começa 0,001 rad ao lado, e o caos separa os dois.",
   "lede": "Feito para estudantes, do ensino médio à pós-graduação. Cada cena roda no navegador.",
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
   "lede": "Transforma gravações de áudio em partituras editáveis, tudo no navegador. A partitura pode ser editada, tocada em 35 instrumentos sampleados e praticada com notas caindo.",
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
     "Andamento, tom e acordes",
     "O Amadeo estima o andamento, o compasso, a tonalidade e os acordes, dá a cada mão a sua linha e grava a partitura com VexFlow."
    ],
    [
     "Em uso",
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
   "sum": "Escrevo o pedido uma vez, e o app descobre a qual projeto ele pertence.",
   "hl": [
    "Cada projeto tem o seu próprio agente",
    "Criptografia em repouso pelo cofre de chaves do sistema operacional",
    "Atualizações assinadas e CI no Windows, macOS e Linux"
   ],
   "viz": "Os pedidos são encaminhados a um agente por projeto.",
   "lede": "Escrevo o pedido uma vez, e o app descobre a qual projeto ele pertence.",
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
   "lede": "Sites da Orion Benefícios e da LÍDER Plus Telemedicina, um site para um estúdio de estética e um portal do colaborador.",
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
     "Páginas estáticas",
     "Páginas estáticas, feitas com Astro ou com um pequeno gerador em Python, servidas pelo Cloudflare Pages."
    ],
    [
     "Acessibilidade testada",
     "Os sites das empresas são testados contra a WCAG 2.2 AA nos três motores de navegador: Chromium, Firefox e WebKit."
    ],
    [
     "O portal do colaborador",
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
   "sum": "Verifica se uma estratégia se sustenta em dados que nunca viu, ou se só pareceu boa por acaso.",
   "hl": [
    "Backtests walk-forward fora da amostra, depois de taxas e slippage",
    "Testes de block bootstrap contra data snooping",
    "Coberto por testes automatizados (pytest)"
   ],
   "viz": "Teste walk-forward: ajusta numa janela, opera na seguinte e nunca olha adiante.",
   "lede": "Verifica se uma estratégia se sustenta em dados que nunca viu, ou se só pareceu boa por acaso.",
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
     "testes automatizados"
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
     "Escrito em Python com pandas, servido por FastAPI e guardado em SQLite, e coberto por testes em pytest."
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
  "p": "Procuro vagas em machine learning e software, e sempre gosto de conversar sobre pesquisa. O e-mail é o melhor jeito de falar comigo."
 },
 "sky": {
  "h": "Sobre este céu",
  "p": [
   "O buraco negro é desenhado com um traçador de raios derivado do Isaac, meu simulador de física. Cada pixel segue um raio de luz de volta pelo espaço-tempo curvo em torno do buraco (que gira a 90% da velocidade máxima que um buraco negro pode ter), visto 18° acima do disco. O disco é gás quente, colorido como um corpo negro, mais brilhante do lado que vem em nossa direção e desviado para o vermelho perto do buraco. O gás gira na velocidade que teria de verdade: a borda interna dá uma volta em menos de um segundo, a externa em cerca de 9. O anel fino e brilhante em volta da sombra é luz que contornou o buraco antes de chegar até nós.",
   "Os planetas e o cinturão de asteroides orbitam no plano do disco, todos no mesmo relógio: o planeta mais interno dá uma volta em cerca de 23 segundos, o mais externo em cerca de 48. As elipses giram devagar, como prevê a relatividade geral, e cada planeta mantém uma face voltada para o buraco.",
   "Um segundo aqui são 40 M de tempo, em que M é a massa do buraco em unidades de tempo. Para um buraco de 100 milhões de sóis, isso é cerca de 20.000 vezes a velocidade real. A câmera gira devagar em torno do buraco.",
   "Duas coisas não estão em escala. As órbitas, o cinturão e os planetas são desenhados sem o desvio da sua luz, que ergueria o lado de trás de cada órbita acima do buraco, e os planetas aparecem milhares de vezes maiores do que seriam."
  ]
 },
 "nf": {
  "t": "Página não encontrada",
  "p": "Não há nenhuma página neste endereço.",
  "a": "Voltar ao início"
 },
 "hero": {
  "h": "Tudo o que eu construo *orbita* algo real.",
  "p": "Sou o Matheus. Desenvolvo modelos de machine learning e software. Cada planeta aqui é um projeto meu, orbitando um buraco negro. Clique em um para pousar nele.",
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
