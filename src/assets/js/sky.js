// The hero sky: a spinning (Kerr) black hole with five planets, an asteroid belt and a star field,
// all on one clock and one distance scale. Units are G = c = M = 1 (M is the hole's mass). The
// hole is taken as 1e8 solar masses (M = 1.48e8 km, 493 s), so every planet orbits outside its
// Roche limit (a gas giant would be torn apart inside about 6 M). The hole and its disc are ray
// traced exactly; the planets, belt and orbit lines are drawn without the bending of their light,
// and the planets far larger than they would be.
(function () {
  'use strict';
  const S = window.SITE = window.SITE || JSON.parse(document.getElementById('site-data').textContent);
  const A = 0.9, INC = 72 * Math.PI / 180, CI = Math.cos(INC), SI = Math.sin(INC);
  const RATE = 40;                      // M of time per second on screen
  const CAM = 600;                      // camera distance (M)
  const DRIFT = 2 * Math.PI / 10800;    // the camera circles the hole once every three hours on screen (radians per second)
  const SKYV = DRIFT * CAM * SI;        // so the distant stars sweep past at this speed (M per second at the hole), to the right
  // Innermost stable circular orbit of the spinning hole (prograde), about 2.32 M for A = 0.9.
  const ISCO = (() => { const z1 = 1 + Math.cbrt(1 - A * A) * (Math.cbrt(1 + A) + Math.cbrt(1 - A)), z2 = Math.sqrt(3 * A * A + z1 * z1); return 3 + z2 - Math.sqrt((3 - z1) * (3 + z1 + 2 * z2)); })();
  const Om = r => 1 / (Math.pow(r, 1.5) + A);                       // circular orbital rate (A = spin, here 0)
  const kap = r => Om(r) * Math.sqrt(Math.max(0, 1 - 6 / r + 8 * A / Math.pow(r, 1.5) - 3 * A * A / (r * r))); // radial epicyclic rate
  // The planets and the belt orbit in the hole's equatorial plane, the plane of the disc.
  const E1 = [1, 0, 0], E2 = [0, 1, 0], NR = [0, 0, 1];
  // Hole frame (z = spin axis, x towards the camera's azimuth) to view frame (X right, Y up,
  // Z towards the viewer). The camera sits 18 degrees above the disc and drifts in azimuth by phc.
  let phc = 0, cph = 1, sph = 0;
  const view = p => { const x = p[0] * cph + p[1] * sph, y = -p[0] * sph + p[1] * cph; return [y, -x * CI + p[2] * SI, x * SI + p[2] * CI]; };
  const hex = h => [1, 3, 5].map(i => parseInt(h.slice(i, i + 2), 16));
  const PL = S.projects.map(p => Object.assign({}, p.orbit, { col: p.col, rgb: hex(p.col), kind: p.kind, id: p.id, name: p.name, site: p.site }));
  PL.forEach(p => {
    p.O = Om(p.a); p.K = kap(p.a);
    const la = p.site[0] * Math.PI / 180, lo = p.site[1] * Math.PI / 180;
    p.siteN = [Math.cos(la) * Math.cos(lo), Math.cos(la) * Math.sin(lo), Math.sin(la)];
  });
  const BELT = (() => { let s = 7; const r = () => (s = (s * 16807) % 2147483647) / 2147483647; return [...Array(1500)].map(() => ({ r: 50 + r() * 3, ph: r() * 6.2832, z: (r() - .5) * .5, b: .35 + .65 * r() })); })();

  // Planet position at time tau: a precessing ellipse. The periapsis advances at Omega - kappa
  // (general relativity), the radial motion follows the epicyclic frequency kappa.
  function orbit(p, tau) {
    const M = p.K * tau + p.m0, e = p.e;
    const f = M + 2 * e * Math.sin(M) + 1.25 * e * e * Math.sin(2 * M);
    const r = p.a * (1 - e * e) / (1 + e * Math.cos(f)), w = p.w0 + (p.O - p.K) * tau, psi = w + f;
    const c = Math.cos(psi), s = Math.sin(psi);
    return [r * (c * E1[0] + s * E2[0]), r * (c * E1[1] + s * E2[1]), r * (c * E1[2] + s * E2[2])];
  }
  function ellipsePt(p, tau, f) {
    const e = p.e, r = p.a * (1 - e * e) / (1 + e * Math.cos(f)), psi = p.w0 + (p.O - p.K) * tau + f, c = Math.cos(psi), s = Math.sin(psi);
    return [r * (c * E1[0] + s * E2[0]), r * (c * E1[1] + s * E2[1]), r * (c * E1[2] + s * E2[2])];
  }
  const TAU2 = 2 * Math.PI;
  // Hole-frame point -> (r, azimuth from the camera).
  const polar = p3 => [Math.hypot(p3[0], p3[1]), Math.atan2(p3[1], p3[0]) - phc];
  // Perspective projection of a plane point (r, azimuth from the camera), without the bending of light.
  const flatP = (r, ph) => { const x = r * Math.cos(ph), y = r * Math.sin(ph), z = x * SI, f = CAM / (CAM - z); return [y * f, -x * CI * f]; };
  // Doppler and gravitational shift of light from a circular prograde orbit at r, seen at screen X:
  // g = 1 / (u^t (1 - Omega L)), L = -X sin(i), as for the disc.
  const utOf = r => { const om = Om(r), gtt = -(1 - 2 / r), gtp = -2 * A / r, gpp = r * r + A * A + 2 * A * A / r; return 1 / Math.sqrt(Math.max(1e-9, -(gtt + 2 * gtp * om + gpp * om * om))); };
  function gShift(r, X) { return 1 / (utOf(r) * (1 + Om(r) * X * SI)); }
  BELT.forEach(b => { b.om = Om(b.r); b.ut = utOf(b.r); });   // fixed for each grain
  // Weak-field lensing by a point mass (used for the stars). X, Y: position on the sky (M); R2: squared Einstein radius.
  // Returns both images: [x, y, radial stretch, tangential stretch (signed), magnification].
  function lens(X, Y, R2) {
    const s = Math.max(.05, Math.hypot(X, Y)), q = Math.sqrt(s * s + 4 * R2), ux = X / s, uy = Y / s;
    const tp = (s + q) / 2, tm = (s - q) / 2, rp = (1 + s / q) / 2, rm = (1 - s / q) / 2;
    return [[tp * ux, tp * uy, rp, tp / s, rp * tp / s], [tm * ux, tm * uy, rm, tm / s, Math.abs(rm * tm / s)]];
  }

  // ---------- Canvases and layout ----------
  const sky = document.getElementById('sky'), bg = document.getElementById('bg'), fg = document.getElementById('fg');
  let bhc = document.getElementById('bh');   // replaced by a new canvas if a worker was given the first and cannot draw
  const still = document.getElementById('bhstill'), labs = document.getElementById('labs');
  const bx = bg.getContext('2d'), fx = fg.getContext('2d');
  // Quality steps, lowered one at a time while the frame rate stays low (see loop()).
  const QUAL = [{ dpr: 2, belt: 1, stars: 1, tile: 256 }, { dpr: 1.25, belt: 2, stars: .6, tile: 192 }, { dpr: 1, belt: 3, stars: .35, tile: 128 }];
  let q = 0, dpr = 1, L = null, IR = null;
  function layout() {
    dpr = Math.min(devicePixelRatio || 1, QUAL[q].dpr);
    const w = sky.clientWidth, h = sky.clientHeight, mob = innerWidth < 820;
    const it = document.querySelector('.intro'), ir = it.getBoundingClientRect(), sr = sky.getBoundingClientRect();
    IR = mob ? null : { l: ir.left - sr.left - 24, r: ir.right - sr.left + 24, t: ir.top - sr.top - 20, b: ir.bottom - sr.top + 20 };
    // Desktop: fit the outermost planet's orbit (apoapsis APO) in the space beside the intro text,
    // so no planet ever passes under the headline. The belt may run behind the text.
    const APO = Math.max(...PL.map(p => p.a * (1 + p.e)), 51);   // the outermost orbit, or the belt's middle
    const PAPO = Math.max(...PL.map(p => p.a * (1 + p.e))) + 3;   // the outermost planet with its label room
    let cx = w * .5, cy = h * .5, K;
    if (mob) { K = Math.min((w - 16) / (2 * (PAPO + 2)), h / (2 * 17)); cy = h * .42; } // every planet stays on a phone screen (the belt may run off the edges); the hole sits high enough to show on the first screen
    else {
      const free = S.rtl ? IR.l - 16 : w - IR.r - 16;
      // The planets fit beside the text; the faint belt may pass behind it.
      K = Math.max(5, Math.min(h * .86 / (2 * 19), free / (2 * PAPO + 4), (w - 16) / (2 * APO + 4)));
      cx = S.rtl ? IR.l - 8 - (PAPO + 2) * K : IR.r + 8 + (PAPO + 2) * K;
    }
    K = Math.max(.5, K);   // a hidden or collapsed pane can report no width or height
    for (const c of [bg, fg, sc]) { c.width = Math.round(w * dpr); c.height = Math.round(h * dpr); }
    L = { w, h, cx, cy, K, mob, ps: mob ? 1.7 : 1 };   // planets are drawn larger on phones, so they can be seen and tapped
    BH.place(L, Math.min(devicePixelRatio || 1, 1.5));
    BH.lite = q === 2 ? 1 : 0;
    starT = -1;
    [...labs.children].forEach(b => b._w = null);
    stars = makeStars(L);
  }

  // ---------- Stars: a sheet far behind the hole, lensed (Einstein radius about 49 M for a camera 600 M away) ----------
  let stars = [], starT = -1;
  const sc = document.createElement('canvas'), sx = sc.getContext('2d');   // the star layer, redrawn four times a second
  const STAR_R2 = 4 * 600;
  function bbTint(T) { T /= 100; const r = T <= 66 ? 255 : 329.7 * Math.pow(T - 60, -.1332), g = T <= 66 ? 99.47 * Math.log(T) - 161.1 : 288.1 * Math.pow(T - 60, -.0755), b = T >= 66 ? 255 : T <= 19 ? 0 : 138.5 * Math.log(T - 10) - 305; return [r, g, b].map(v => Math.max(0, Math.min(255, v | 0))); }
  function makeStars(L) {
    let s = 3; const r = () => (s = (s * 16807) % 2147483647) / 2147483647;
    const hx = L.w / 2 / L.K + 60, hy = L.h / 2 / L.K + 60, n = Math.round(Math.min(2600, L.w * L.h / 520) * QUAL[q].stars);
    // Six colour steps from 3200 K to 12200 K: the fill colour changes six times a draw, not once a star.
    return [...Array(n)].map(() => { const m = Math.pow(r(), 3.2); return { x: (r() * 2 - 1) * hx, y: (r() * 2 - 1) * hy, hx, hy, m, c: Math.min(5, r() * 6 | 0) }; }).sort((a, b) => a.c - b.c);
  }
  const TINT = [0, 1, 2, 3, 4, 5].map(k => `rgb(${bbTint(3200 + (k + .5) * 1500).join(',')})`);
  // The layer also carries the sky's ground and the hole's faint glow, so a frame copies one full-screen
  // image instead of filling the screen three times (each full-screen fill costs Firefox up to 20 ms).
  function drawStars(t) {
    const { cx, cy, K } = L, drift = t * SKYV, bx = sx;
    bx.globalAlpha = 1; bx.fillStyle = '#03040a'; bx.fillRect(0, 0, sc.width, sc.height);
    const g = bx.createRadialGradient(cx * dpr, cy * dpr, 0, cx * dpr, cy * dpr, K * 60 * dpr); g.addColorStop(0, 'rgba(255,150,70,.045)'); g.addColorStop(1, 'rgba(0,0,0,0)'); bx.fillStyle = g; bx.fillRect(0, 0, sc.width, sc.height);
    let tc = -1;
    for (const s of stars) {
      if (s.c !== tc) { tc = s.c; bx.fillStyle = TINT[tc]; }
      let x = s.x + drift; x = ((x + s.hx) % (2 * s.hx) + 2 * s.hx) % (2 * s.hx) - s.hx;
      const offX = (cx - L.w / 2) / K, X = x - offX, Y = s.y;   // source position relative to the hole
      const im = lens(X, Y, STAR_R2);
      for (let k = 0; k < 2; k++) {
        const [ix, iy, , , mu] = im[k], a = Math.min(1, (.18 + s.m * .9) * Math.min(mu, 4));
        if (a < .03 || Math.hypot(ix, iy) < 5.4) continue;
        const sz = (s.m > .55 ? 2 : 1) * dpr * (mu > 2 ? 1.5 : 1);
        bx.globalAlpha = a;
        bx.fillRect((cx + ix * K) * dpr - sz / 2, (cy - iy * K) * dpr - sz / 2, sz, sz);
      }
    }
    bx.globalAlpha = 1;
  }

  // ---------- Black hole: traced on the GPU by bh.js ----------
  // Where the browser can, the hole's canvas is handed to bh.js running as a worker (OffscreenCanvas),
  // so setting up WebGL, compiling the shaders and tracing never hold up the page; elsewhere bh.js runs
  // on the page, started after the first paint. The canvas is placed here, over the still (bh-still.webp).
  const BHSRC = ((document.currentScript || document.querySelector('script[src*="sky.js"]') || {}).src || '').replace('sky.js', 'bh.js');
  const BH = (function () {
    const D = { HW: 26, HH: 16.25 }, K4 = [A, CAM, INC, ISCO];
    let eng = null, wk = null, ok = false, ready = false, lite = 0, size = null, paged = false;
    // The still stays beneath the live hole: it fills in while the hole is traced again after a resize,
    // and stands in wherever a browser fails to show the canvas.
    const shown = () => bhc.classList.add('on');
    // bh.js as a plain script, drawing on the page.
    function onPage() {
      if (paged) return; paged = true;
      const go = () => {
        if (!window.BHmake) return;
        eng = window.BHmake(bhc, K4[0], K4[1], K4[2], K4[3]);
        eng.init(o => { if (o && size) eng.place(size[0], size[1]); });
      };
      if (window.BHmake) return go();
      const sc_ = document.createElement('script'); sc_.src = BHSRC; sc_.onload = go; document.head.appendChild(sc_);
    }
    // A canvas handed to a worker cannot come back: if the worker cannot draw, a new canvas takes its place.
    function fresh() {
      const c = document.createElement('canvas');
      for (const a of bhc.getAttributeNames()) c.setAttribute(a, bhc.getAttribute(a));
      bhc.replaceWith(c); bhc = c;
    }
    function fallBack() { if (wk) { wk.terminate(); wk = null; } ok = false; ready = false; fresh(); requestAnimationFrame(() => setTimeout(onPage, 0)); }
    return {
      start() {
        if (!window.BH_MAIN && BHSRC && window.Worker && bhc.transferControlToOffscreen) {
          try {
            const off = bhc.transferControlToOffscreen();
            wk = new Worker(BHSRC);
            wk.onmessage = e => {
              const m = e.data;
              if (m.failed) { if (!ok) fallBack(); return; }   // no WebGL 2 in a worker here: draw on the page
              ok = m.ok; ready = m.ready;
              if (ready) shown();
            };
            wk.onerror = () => fallBack();
            wk.postMessage({ canvas: off, k: K4, size }, [off]);
            return;
          } catch (e) { if (wk) fallBack(); else requestAnimationFrame(() => setTimeout(onPage, 0)); return; }
        }
        requestAnimationFrame(() => setTimeout(onPage, 0));
      },
      get ok() { return ok; },
      get done() { return ready; },
      set lite(v) { lite = v; },
      place(L, d) {
        const w = 2 * D.HW * L.K, h = 2 * D.HH * L.K;
        for (const el of [bhc, still]) { if (!el) continue; Object.assign(el.style, { left: L.cx - w / 2 + 'px', top: L.cy - h / 2 + 'px', width: w + 'px', height: h + 'px' }); }
        size = [Math.max(1, Math.round(w * d)), Math.max(1, Math.round(h * d))];
        ready = false;
        if (eng) { eng.place(size[0], size[1]); ready = eng.ready; }
        else if (wk) wk.postMessage({ size });
      },
      draw(tau) {
        if (eng) {
          eng.draw(tau, lite);
          ok = eng.ok;
          if (eng.ready) { ready = true; shown(); }
        } else if (wk) wk.postMessage({ tau, lite });
      },
    };
  })();

  // ---------- Planets: rendered on the GPU into an atlas, then drawn in 2D ----------
  // The planets are rendered by the landing view's planet program (world.js) and copied into this
  // 2D atlas, which keeps them while a project is open. Until the program is compiled they are drawn
  // as shaded discs, and the detailed ones fade in over them.
  const atlas = document.createElement('canvas'), ax = atlas.getContext('2d');
  let PG = null, pgT = 0, pgFade = 1, pend = -1;
  function pollPG() {
    const G = window.WORLD && window.WORLD.planetGL();
    if (G && !PG) { pgT = performance.now(); pgFade = 0; }
    PG = G || (PG && window.WORLD.open_ >= 0 ? PG : null);
    if (PG && pgFade < 1) pgFade = Math.min(1, (performance.now() - pgT) / 600);
  }
  let tile = 128;
  function frameOf(p3) {
    const r = Math.hypot(...p3), ex = p3.map(v => -v / r), ez = NR;
    const ey = [ez[1] * ex[2] - ez[2] * ex[1], ez[2] * ex[0] - ez[0] * ex[2], ez[0] * ex[1] - ez[1] * ex[0]];
    const X = view(ex), Y = view(ey), Z = view(ez);
    return { rot: [...X, ...Y, ...Z], L: X };
  }
  const ext = p => p.kind === 'gas' ? 2.45 : 1.18;
  function renderAtlas(st, t) {
    if (!PG || window.WORLD.open_ >= 0) return;   // a project is open: its view owns the canvas
    const need = Math.min(QUAL[q].tile, Math.max(...PL.map(p => Math.ceil(2 * ext(p) * p.R * L.ps * L.K * dpr))));
    const gc = PG.gl.canvas;
    if (gc.width !== need * PL.length || gc.height !== need) { gc.width = need * PL.length; gc.height = need; }
    if (atlas.width !== gc.width || atlas.height !== gc.height) { atlas.width = gc.width; atlas.height = gc.height; }
    tile = need; PG.clear();
    PL.forEach((p, i) => {
      const f = st[i].frame;
      PG.draw({ vp: [i * tile, 0, tile, tile], ortho: 1, ext: ext(p), rot: f.rot, L: f.L, col: p.rgb.map(v => v / 255), kind: KIND[p.kind], site: p.siteN, time: t, glow: 0, seed: i * 3.7 + 1, gain: st[i].gain });
    });
    const img = PG.frame ? PG.frame('atlas', gc.width, gc.height) : gc;   // from the planet worker: its last finished atlas
    if (img && img.width === atlas.width && img.height === atlas.height) { ax.clearRect(0, 0, atlas.width, atlas.height); ax.drawImage(img, 0, 0); }
    if (img && img !== gc) img.close();
  }
  const KIND = { rock: 0, ocean: 1, gas: 2, storm: 3, ice: 4 };
  function drawPlanet(ctx, i, p, X, Y, M) {
    // Image of the planet through the matrix M (screen axes, Y up). The Doppler brightening
    // is applied when the planet is rendered into the atlas.
    const { cx, cy, K } = L, half = ext(p) * p.R * L.ps * K * dpr, px = (cx + X * K) * dpr, py = (cy - Y * K) * dpr;
    ctx.save(); ctx.setTransform(M[0], -M[2], -M[1], M[3], px, py);
    if (PG && pgFade >= 1) ctx.drawImage(atlas, i * tile, 0, tile, tile, -half, -half, 2 * half, 2 * half);
    else { const R = p.R * L.ps * K * dpr, g = ctx.createRadialGradient(-R * .35, -R * .35, R * .1, 0, 0, R); g.addColorStop(0, p.col); g.addColorStop(1, '#05060c'); ctx.fillStyle = g; ctx.beginPath(); ctx.arc(0, 0, R, 0, 7); ctx.fill();
      if (PG) { ctx.globalAlpha = pgFade; ctx.drawImage(atlas, i * tile, 0, tile, tile, -half, -half, 2 * half, 2 * half); ctx.globalAlpha = 1; } }   // the detailed planet fades in over the plain disc
    ctx.restore();
  }

  // ---------- Interaction ----------
  let hover = -1, focusI = -1, scr = [];
  const T = S.t;
  PL.forEach((p, i) => {
    const b = document.createElement('button'); b.type = 'button'; b.className = 'lab'; b.style.setProperty('--c', p.col);
    b.innerHTML = `<span>${p.name}</span><small>${S.projects[i].sub}</small>`;
    b.setAttribute('aria-label', `${p.name}. ${S.projects[i].sub}. ${T.land}`);
    b.addEventListener('click', () => land(i));
    const fo = v => () => { focusI = v; };
    b.addEventListener('mouseenter', fo(i)); b.addEventListener('mouseleave', fo(-1)); b.addEventListener('focus', fo(i)); b.addEventListener('blur', fo(-1));
    labs.appendChild(b);
  });
  fg.addEventListener('pointermove', e => {
    const r = fg.getBoundingClientRect(), X = e.clientX - r.left, Y = e.clientY - r.top; hover = -1;
    scr.forEach((s, i) => { if (s && Math.hypot(s.x - X, s.y - Y) < Math.max(s.R + 16, 26)) hover = i; });
    fg.style.cursor = hover >= 0 ? 'pointer' : 'default';
  });
  fg.addEventListener('pointerleave', () => hover = -1);
  fg.addEventListener('click', () => { if (hover >= 0) land(hover); });
  function land(i) {
    const s = scr[i]; if (!window.WORLD) return;
    const r = sky.getBoundingClientRect();
    window.WORLD.open(i, s ? { x: r.left + s.x, y: r.top + s.y, R: s.R, rot: st[i].frame.rot, L: st[i].frame.L } : null);
  }

  // ---------- Clock and drawing ----------
  let tau = 140, t = 0, last = performance.now(), active = true, st = [], hideI = -1;
  const front = ph => Math.cos(ph) >= 0;   // nearer than the hole: drawn over its canvas
  // The near half of each orbit is drawn over the hole, the far half behind it. The two halves are kept
  // as paths and rebuilt when the orbit has precessed by about 2 M of clock time (a fraction of a pixel).
  const OP = [];
  function orbitLine(ctxF, ctxB, p, on, alpha, i) {
    const { cx, cy, K } = L, col = on ? `rgba(${p.rgb.join(',')},.8)` : `rgba(160,205,255,${alpha})`;
    let c = OP[i];
    if (!c || c.L !== L || c.dpr !== dpr || Math.abs(tau - c.tau) > 2 || Math.abs(phc - c.phc) > 1e-3) {
      c = OP[i] = { L, dpr, tau, phc, f: new Path2D(), b: new Path2D() };
      let pen = null;
      for (let n = 0; n <= 240; n++) {
        const [r, ph] = polar(ellipsePt(p, tau, n / 240 * TAU2)), side = front(ph) ? c.f : c.b, v = flatP(r, ph), x = (cx + v[0] * K) * dpr, y = (cy - v[1] * K) * dpr;
        if (pen === side) side.lineTo(x, y); else { side.moveTo(x, y); pen = side; }
      }
    }
    for (const [ctx, path] of [[ctxF, c.f], [ctxB, c.b]]) { ctx.strokeStyle = col; ctx.lineWidth = (on ? 1.6 : 1) * dpr; ctx.stroke(path); }
  }
  // Planet position on screen now, as seen without the bending of light: the orbits stay flat.
  function planetImage(p) {
    const p3 = orbit(p, tau), [r, ph] = polar(p3), f = flatP(r, ph);
    return { X: f[0], Y: f[1], X0: f[0], M: [1, 0, 0, 1], k: 1, p3, r, ph };
  }
  // The part of the sky the hole and its lensed disc cover, in M from the centre (measured from the traced image).
  const HOLE = { x: 17, up: 11, down: 8 };
  function draw() {
    const { w, h, cx, cy, K } = L, W = w * dpr, H = h * dpr;
    bx.setTransform(1, 0, 0, 1, 0, 0); fx.setTransform(1, 0, 0, 1, 0, 0);
    fx.clearRect(0, 0, W, H);
    if (starT < 0 || t - starT > .25 || t < starT) { drawStars(t); starT = t; }
    bx.drawImage(sc, 0, 0);   // opaque: covers the last frame
    // Planet states, lit and Doppler-shifted.
    st = PL.map(p => {
      const d = planetImage(p), p3 = d.p3;
      return { p3, im: d, v: view(p3), frame: frameOf(p3), gain: Math.min(2.2, Math.pow(gShift(d.r, d.X0), 4)) };
    });
    renderAtlas(st, t);
    PL.forEach((p, i) => orbitLine(fx, bx, p, i === hover || i === focusI, .13, i));
    // Belt: each grain on a circular orbit, brightened by the Doppler factor.
    // Grains are batched by brightness into eight paths per layer, one fill each.
    const NB = 8, gs = 1.3 * dpr, bk = [[], []];
    for (let n = 0; n < NB; n++) { bk[0].push([]); bk[1].push([]); }
    for (let j = 0, step = QUAL[q].belt; j < BELT.length; j += step) {
      const b = BELT[j], ph = b.ph + b.om * tau - phc, v = flatP(b.r, ph), g = 1 / (b.ut * (1 + b.om * v[0] * SI)), g2 = g * g, a = .5 * b.b * Math.min(3, g2 * g2);
      if (a < .02) continue;
      bk[front(ph) ? 0 : 1][Math.min(NB - 1, Math.floor(Math.min(1, a) * NB))].push((cx + v[0] * K) * dpr, (cy - v[1] * K) * dpr);
    }
    [fx, bx].forEach((ctx, l) => bk[l].forEach((pts, n) => {
      if (!pts.length) return;
      ctx.fillStyle = `rgba(214,200,182,${((n + .5) / NB).toFixed(3)})`; ctx.beginPath();
      for (let i = 0; i < pts.length; i += 2) ctx.rect(pts[i], pts[i + 1], gs, gs);
      ctx.fill();
    }));
    // Planets, farthest first.
    scr = [];
    const order = PL.map((p, i) => i).sort((a, b) => st[a].v[2] - st[b].v[2]);
    for (const i of order) {
      const p = PL[i], S_ = st[i], R = p.R * L.ps * K, on = i === hover || i === focusI;
      {
        const im = S_.im, per = CAM / (CAM - im.r * Math.cos(im.ph) * SI), M = im.M.map(v => v * per);
        const ctx = front(im.ph) ? fx : bx, Re = R * per * im.k;
        if (i !== hideI) { glow(ctx, p, im.X, im.Y, Re, on); drawPlanet(ctx, i, p, im.X, im.Y, M); }
        scr[i] = { x: cx + im.X * K, y: cy - im.Y * K, R: Re };
      }
      const lb = labs.children[i], s_ = scr[i];
      // Keep labels off the intro text on wide screens.
      const lx = s_.x + s_.R + 8, hid = IR && lx + 110 > IR.l && lx < IR.r && s_.y > IR.t && s_.y < IR.b;
      lb.classList.toggle('hid', !!hid);
      // Put the label on the planet's left when it would run off the right edge.
      lb._w = lb._w || {}; const k_ = on ? 1 : 0; if (!lb._w[k_]) { lb.classList.toggle('on', on); lb._w[k_] = lb.offsetWidth; }
      const lw = lb._w[k_] || 80;
      // A planet in front of or behind the hole takes its label on the outer side, away from the hole.
      let left = s_.x + s_.R + 8 + lw > L.w - 4 || (s_.x < cx && s_.x > cx - HOLE.x * K - lw && s_.x - s_.R - 8 - lw > 4);
      // Keep labels off the hole's shadow and the bright inner disc: try the other side, then move
      // the label just above or below.
      const hx0 = cx - HOLE.x * K, hx1 = cx + HOLE.x * K, hy0 = cy - HOLE.up * K, hy1 = cy + HOLE.down * K;
      const over = (lx0, y) => lx0 < hx1 && lx0 + lw > hx0 && y + 10 > hy0 && y - 10 < hy1;
      const at = l => l ? s_.x - s_.R - 8 - lw : s_.x + s_.R + 8;
      let ly = s_.y;
      let lx_ = null;
      if (over(at(left), ly)) {
        if (!over(at(!left), ly) && at(!left) > 4 && at(!left) + lw < L.w - 4) left = !left;
        else {
          // Neither side is clear: centre the label just above or below the planet, on the side away
          // from the hole; only if that still covers the hole, move it to the hole's edge.
          const up = s_.y < cy - K, cxl = Math.min(L.w - 4 - lw, Math.max(4, s_.x - lw / 2)), yl = up ? s_.y - s_.R - 14 : s_.y + s_.R + 14;
          lx_ = cxl; ly = over(cxl, yl) ? (up ? Math.min(yl, hy0 - 12) : Math.max(yl, hy1 + 12)) : yl;
        }
      }
      lb._x = lx_ !== null ? lx_ : Math.max(4, at(left)); lb._y = ly; lb._lw = lw;
      lb.style.visibility = i === hideI || s_.x < -s_.R || s_.x > L.w + s_.R || s_.y < 0 || s_.y > L.h ? 'hidden' : '';
      lb.classList.toggle('on', on);
    }
    const ls = [...labs.children].sort((a, b) => a._y - b._y);
    for (let a = 0; a < ls.length; a++) for (let b = 0; b < a; b++) {
      const A_ = ls[a], B_ = ls[b];
      if (A_._x < B_._x + B_._lw && B_._x < A_._x + A_._lw && A_._y - B_._y < 20) A_._y = B_._y + 20;
    }
    for (const lb of ls) lb.style.transform = `translate(${Math.round(lb._x)}px,${Math.round(lb._y)}px) translateY(-50%)`;
    BH.draw(tau);
  }
  function glow(ctx, p, X, Y, R, on) {
    const { cx, cy, K } = L, x = (cx + X * K) * dpr, y = (cy - Y * K) * dpr, rr = R * dpr * (on ? 4.2 : 2.8);
    const g = ctx.createRadialGradient(x, y, R * dpr * .9, x, y, rr); g.addColorStop(0, `rgba(${p.rgb.join(',')},${on ? .4 : .16})`); g.addColorStop(1, `rgba(${p.rgb.join(',')},0)`);
    ctx.fillStyle = g; ctx.beginPath(); ctx.arc(x, y, rr, 0, 7); ctx.fill();
    if (on) { ctx.strokeStyle = p.col; ctx.lineWidth = 1.2 * dpr; ctx.beginPath(); ctx.arc(x, y, R * dpr + 7 * dpr, 0, 7); ctx.stroke(); }
  }
  const hero = document.querySelector('.hero');
  let visible = true;
  new IntersectionObserver(es => es.forEach(e => visible = e.isIntersecting)).observe(hero);
  // The sky always moves. Frames are drawn at most about 95 times a second (every other refresh on
  // 120 Hz and faster screens). If the frame rate stays under about 33 per second for two seconds
  // once the hole is traced, the next quality step is taken: fewer pixels, stars and belt grains.
  let ema = 16, slow = 0;
  function loop(now) {
    requestAnimationFrame(loop);
    const ms = now - last;
    if (ms < 10.5) return;
    const dt = Math.min(.1, ms / 1000); last = now;
    if (active) { tau += dt * RATE; t += dt; }
    phc = t * DRIFT; cph = Math.cos(phc); sph = Math.sin(phc);
    if (!visible || !active || L.w < 2 || L.h < 2) return;
    if (BH.done || !BH.ok) {
      if (ms < 250) { ema += (ms - ema) * .08; slow = ema > 30 ? slow + ms : 0; }
      if (slow > 2000 && q < QUAL.length - 1) { q++; slow = 0; ema = 16; layout(); }
    }
    pollPG();
    draw();   // after any resize in layout(), so a cleared canvas is never shown
  }
  // A still of the traced hole (tools/still.js) shows from the first frame; the live hole fades in
  // over it once its rays are traced. Without WebGL 2 the still is all there is.
  // The hole starts at once in its worker; on the page it starts after the first paint, so the page shows first.
  layout();
  if (still) still.classList.add('on');
  BH.start();
  if (document.fonts) document.fonts.ready.then(() => { [...labs.children].forEach(b => b._w = null); });
  let rz; addEventListener('resize', () => { clearTimeout(rz); rz = setTimeout(() => { layout(); if (visible && active) draw(); }, 120); });
  requestAnimationFrame(loop);
  window.SKY = {
    get quality() { return q; },
    // A planet clicked before the landing view is ready: its label pulses until the flight starts.
    pending(i) { if (pend === i) return; pend = i; [...labs.children].forEach((b, k) => b.classList.toggle('busy', k === i)); },
    // Stop (or restart) the sky while a project is open. The planet being flown to is drawn by the
    // landing view instead, so the sky draws one last frame without it.
    setActive(v, i) { hideI = v ? -1 : (i == null ? -1 : i); if (L && L.w >= 2) draw(); active = v; },
    planet(i) { const s = scr[i], r = sky.getBoundingClientRect(); return s ? { x: r.left + s.x, y: r.top + s.y, R: s.R, rot: st[i].frame.rot, L: st[i].frame.L, gain: st[i].gain } : null; },
    orbitInfo(i) { const p = PL[i]; return { a: p.a, period: 2 * Math.PI / p.O / RATE, days: 2 * Math.PI / p.O * 492.6 / 86400 }; },
    planets: PL, KIND,
  };
})();
