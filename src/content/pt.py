C = {
 "name": "Português",
 "meta": {
  "title": "Matheus Teixeira · Engenheiro de machine learning e desenvolvedor de software",
  "desc": "Matheus Teixeira, engenheiro de machine learning e desenvolvedor de software de Santos, Brasil. Projetos, roadmap, formação, experiência e contato."
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
 "role": "Engenheiro de machine learning · Desenvolvedor de software",
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
   "Sou o Matheus, engenheiro de machine learning e desenvolvedor de software, de Santos. Escrevo software desde 2016, quando comecei como desenvolvedor web e assistente de suporte de TI na Orion Benefícios, e estudo na FEI desde 2019.",
   "No mestrado construí um pipeline reprodutível que classifica imagens histopatológicas de câncer de mama, combinando características da ResNet-50 com máquinas de vetores de suporte clássicas e quânticas, e o rodei em hardware da IBM Quantum. Agora faço um MBA em Data Science, IA e Analytics na USP, com bolsa integral, e estou matriculado no doutorado da FEI, com bolsa CAPES e aulas a partir de fevereiro de 2027.",
   "Além da pesquisa, desenvolvo software de ponta a ponta, do modelo ou da física até a interface e os testes. Os cinco projetos abaixo são os de que mais gosto."
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
    "Machine learning, visão computacional, software"
   ]
  ],
  "alt": "Retrato de Matheus Teixeira",
  "term": {
   "who": "Matheus Teixeira: engenheiro de machine learning e desenvolvedor de software",
   "now": [
    "MBA em Data Science, IA e Analytics na USP, em andamento",
    "Doutorado em Engenharia Elétrica na FEI, matriculado, aulas a partir de fevereiro de 2027",
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
   "sub": "Simulações de física interativas em 3D",
   "world": "Mundo vulcânico",
   "sum": "Física para experimentar no navegador. Um motor em Rust compilado para WebAssembly roda as simulações, e React, TypeScript e Three.js as desenham.",
   "hl": [
    "Núcleo de física em Rust compilado para WebAssembly",
    "Interface em React, TypeScript e Three.js",
    "Testado com cargo test, Vitest e Playwright de ponta a ponta"
   ],
   "viz": "Um pêndulo duplo integrado com RK4 em passos de 2 ms. O gêmeo apagado começa 0,001 rad ao lado, e o caos separa os dois.",
   "lede": "Um laboratório de física no navegador. Você muda um parâmetro e a cena, os gráficos e as equações respondem na hora, de uma bola arremessada a um buraco negro.",
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
   "sum": "Transforma uma gravação em partitura que você pode editar, tocar e compartilhar, tudo no navegador. No ar, com plano Pro.",
   "hl": [
    "Transcrição neural no navegador, com TensorFlow.js",
    "Editor de partituras, 35 instrumentos sampleados e modo de prática",
    "No ar em nove idiomas, com assinaturas Pro"
   ],
   "viz": "As linhas de altura no espectrograma viram notas na pauta.",
   "lede": "O Amadeo ouve um arquivo de som, uma gravação do microfone ou um vídeo e escreve a música: notas, andamento, compasso, tonalidade e acordes. A partitura pode ser editada, tocada em 35 instrumentos sampleados, praticada com notas caindo e exportada em PDF, MusicXML, MIDI ou WAV. Tudo roda no navegador.",
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
     "O som não sai do aparelho",
     "A transcrição roda com TensorFlow.js no navegador, então as gravações não são enviadas. As partituras ficam no aparelho de quem usa e são compartilhadas por um link que carrega a partitura inteira."
    ],
    [
     "De alturas a música",
     "Uma lista de alturas ainda não é uma partitura. O Amadeo acompanha o andamento, encontra o compasso, a tonalidade e os acordes, dá a cada mão a sua linha e grava o resultado com VexFlow."
    ],
    [
     "Um produto, não uma demonstração",
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
   "sub": "Orquestrador local de agentes de IA para programação",
   "world": "Mundo de tempestades",
   "sum": "Um app desktop que envia cada pedido ao agente de código do projeto certo.",
   "hl": [
    "Node.js e Electron",
    "Criptografia em repouso pelo cofre de chaves do sistema operacional",
    "Atualizações assinadas e CI no Windows, macOS e Linux"
   ],
   "viz": "Os pedidos são encaminhados a um agente por projeto.",
   "lede": "Um app de desktop que encaminha cada pedido para o agente de programação do projeto certo, para que vários projetos avancem a partir de um só lugar.",
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
     "um agente Claude Code por projeto"
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
     "Cada projeto tem o seu agente Claude Code. O roteador decide a qual projeto um pedido pertence e o envia para lá."
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
   "sum": "Sites para três negócios brasileiros e um portal do colaborador.",
   "hl": [
    "Astro e TypeScript, ou um pequeno gerador em Python, no Cloudflare Pages",
    "Portal do colaborador em Workers e D1, com cabeçalhos CSP",
    "Testes WCAG 2.2 AA em três motores de navegador"
   ],
   "viz": "Notas do Lighthouse: 95 no celular, 100 no desktop.",
   "lede": "Sites para duas empresas brasileiras, a Orion Benefícios e a LÍDER Plus Telemedicina, e para um estúdio de estética independente em Santos, além de um portal do colaborador. Os três foram feitos para ser rápidos, seguros e acessíveis.",
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
     "Páginas estáticas, feitas com Astro ou com um pequeno gerador em Python, servidas pelo Cloudflare Pages. O Lighthouse dá 95 no celular e 100 no computador."
    ],
    [
     "Acessíveis",
     "Testes automáticos de WCAG 2.2 AA rodam nos três motores de navegador: Chromium, Firefox e WebKit."
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
   "sub": "Pesquisa de sinais no mercado de cripto",
   "world": "Gigante gasoso",
   "sum": "Código de pesquisa que verifica se sinais de trading se sustentam fora da amostra.",
   "hl": [
    "Backtests walk-forward fora da amostra, depois de taxas e slippage",
    "Testes de block bootstrap contra data snooping",
    "Python, pandas, FastAPI e SQLite, com 221 testes pytest"
   ],
   "viz": "Teste walk-forward: ajusta numa janela, opera na seguinte e nunca olha adiante.",
   "lede": "Software de pesquisa que faz uma só pergunta a cada sinal de trading: ele ainda funciona em dados que nunca viu, depois de taxas e slippage?",
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
     "sorte ou habilidade?"
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
     "Nunca olhar adiante",
     "Cada estratégia é ajustada em uma janela e operada na seguinte, e então a janela avança. Taxas e slippage são pagos em cada operação."
    ],
    [
     "Sorte ou habilidade",
     "Testar muitas estratégias faz algumas parecerem boas por acaso. Testes de block bootstrap conferem cada resultado contra isso."
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
   "Um segundo aqui são 40 M de tempo, em que M é a massa do buraco em unidades de tempo; para um buraco de quatro milhões de sóis, como o do centro da Via Láctea, isso é cerca de 800 vezes a velocidade real. A câmera gira devagar em torno do buraco, e a luz de tudo o que está atrás dele, planetas, cinturão ou estrelas, é desviada pela sua gravidade.",
   "As distâncias estão na mesma escala, mas os planetas aparecem de centenas a mil vezes maiores do que seriam."
  ]
 },
 "nf": {
  "t": "Página não encontrada",
  "p": "Esta página saiu do sistema.",
  "a": "Voltar ao início"
 },
 "hero": {
  "h": "Tudo o que eu construo *orbita* algo real.",
  "p": "Sou o Matheus. Treino modelos em Python e PyTorch e entrego aplicativos testados em TypeScript e Rust. Cada planeta aqui é um dos meus projetos, girando em torno de um buraco negro em rotação. Clique em um para pousar nele.",
  "cta": [
   "Ver os projetos",
   "Sobre mim"
  ]
 },
 "roadmap": {
  "h": "Roadmap",
  "p": "Por onde passei e para onde vou, desenhado como uma linha de universo. O tempo corre para a direita, e a linha sobe no ano em Zurique. As partes tracejadas são planejadas.",
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
