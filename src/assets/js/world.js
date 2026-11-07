// Landing on a planet: the camera flies from the planet's place in the sky down to the project's
// site on its surface, and the project opens there.
(function () {
  'use strict';
  // world.js is the first script to read the page data, which the page carries as JSON.
  window.SITE = window.SITE || JSON.parse(document.getElementById('site-data').textContent);
  const S = window.SITE, T = S.t;
  const el = document.getElementById('world'), wc = document.getElementById('wc'), wp = document.getElementById('wp');
  const arts = [...wp.querySelectorAll('article.cs')];
  const bBack = document.getElementById('w-back'), bPrev = document.getElementById('w-prev'), bNext = document.getElementById('w-next');
  // The planet shader is compiled in the background once the page is up (see the end of this file);
  // pg() finishes it, waiting for it only if a landing starts before it is ready.
  let PG = null, PGH = null, pgDone = false;
  function pg() {
    if (!pgDone) { if (!PGH && window.PlanetGL) PGH = window.PlanetGL.begin(wc); PG = PGH ? PGH.finish() : null; pgDone = true; }
    return PG;
  }
  const KIND = { rock: 0, ocean: 1, gas: 2, storm: 3, ice: 4 };
  const hex = h => [1, 3, 5].map(i => parseInt(h.slice(i, i + 2), 16) / 255);
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]);
  // Small vector and quaternion helpers.
  const add = (a, b) => a.map((v, i) => v + b[i]), sub = (a, b) => a.map((v, i) => v - b[i]), mul = (a, s) => a.map(v => v * s);
  const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2], len = a => Math.sqrt(dot(a, a)), nrm = a => mul(a, 1 / len(a));
  const cross = (a, b) => [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];
  const mv = (m, v) => [m[0] * v[0] + m[3] * v[1] + m[6] * v[2], m[1] * v[0] + m[4] * v[1] + m[7] * v[2], m[2] * v[0] + m[5] * v[1] + m[8] * v[2]];
  function slerpV(a, b, t) { const d = Math.max(-1, Math.min(1, dot(a, b))), w = Math.acos(d); if (w < 1e-4) return nrm(add(mul(a, 1 - t), mul(b, t))); const s = Math.sin(w); return add(mul(a, Math.sin((1 - t) * w) / s), mul(b, Math.sin(t * w) / s)); }
  function m2q(m) { // column-major 3x3 to quaternion [x,y,z,w]
    const [a, b, c, d, e, f, g, h, i] = m, tr = a + e + i; let q;
    if (tr > 0) { const s = Math.sqrt(tr + 1) * 2; q = [(f - h) / s, (g - c) / s, (b - d) / s, s / 4]; }
    else if (a > e && a > i) { const s = Math.sqrt(1 + a - e - i) * 2; q = [s / 4, (d + b) / s, (g + c) / s, (f - h) / s]; }
    else if (e > i) { const s = Math.sqrt(1 + e - a - i) * 2; q = [(d + b) / s, s / 4, (h + f) / s, (g - c) / s]; }
    else { const s = Math.sqrt(1 + i - a - e) * 2; q = [(g + c) / s, (h + f) / s, s / 4, (b - d) / s]; }
    return q;
  }
  function q2m(q) { const [x, y, z, w] = q; return [1 - 2 * (y * y + z * z), 2 * (x * y + z * w), 2 * (x * z - y * w), 2 * (x * y - z * w), 1 - 2 * (x * x + z * z), 2 * (y * z + x * w), 2 * (x * z + y * w), 2 * (y * z - x * w), 1 - 2 * (x * x + y * y)]; }
  function slerpQ(a, b, t) { let d = a[0] * b[0] + a[1] * b[1] + a[2] * b[2] + a[3] * b[3]; if (d < 0) { b = b.map(v => -v); d = -d; } if (d > .9995) { const r = a.map((v, i) => v + (b[i] - v) * t), l = Math.hypot(...r); return r.map(v => v / l); } const w = Math.acos(d), s = Math.sin(w); return a.map((v, i) => (v * Math.sin((1 - t) * w) + b[i] * Math.sin(t * w)) / s); }
  function basis(pos, aim, upHint) { const f = nrm(sub(aim, pos)), r = nrm(cross(f, upHint)), u = cross(r, f); return [...r, ...u, ...f.map(v => -v)]; }

  const TANF = Math.tan(25 * Math.PI / 180);
  let cur = -1, st = null, viz = null, raf = 0, last = 0, pushed = false, opener = null, q = 1;
  function size() { q = Math.min(devicePixelRatio || 1, 1.5) * (innerWidth * innerHeight > 2.2e6 ? .8 : 1); const w = Math.round(innerWidth * q), h = Math.round(innerHeight * q); if (wc.width !== w || wc.height !== h) { wc.width = w; wc.height = h; } }

  function fill(i) {
    const p = S.projects[i], art = arts[i];
    arts.forEach((a, k) => { a.hidden = k !== i; });
    const o = window.SKY ? window.SKY.orbitInfo(i) : null, orb = art.querySelector('.orb');
    if (orb) orb.textContent = o ? T.orbit.replace('{r}', o.a).replace('{p}', Math.round(o.period)) : '';
    el.style.setProperty('--c', p.col);
    el.setAttribute('aria-label', p.name);
    const cv = art.querySelector('canvas[data-wviz]');
    viz = cv && window.VIZ ? window.VIZ.attach(cv, p.id) : null;
    bPrev.setAttribute('aria-label', `${T.prev}: ${S.projects[(i + 4) % 5].name}`); bNext.setAttribute('aria-label', `${T.next}: ${S.projects[(i + 1) % 5].name}`);
  }
  // Screenshot tabs and the next-planet buttons inside the case studies.
  arts.forEach(art => {
    const tabs = [...art.querySelectorAll('.tabs button')], imgs = [...art.querySelectorAll('.vp img')], url = art.querySelector('.url');
    tabs.forEach(t => t.addEventListener('click', () => {
      tabs.forEach(x => x.setAttribute('aria-selected', String(x === t)));
      imgs.forEach(im => { im.hidden = im.dataset.k !== t.dataset.k; });
      if (url && t.dataset.url) url.textContent = t.dataset.url;
    }));
    const nx = art.querySelector('.cs-next');
    if (nx) nx.addEventListener('click', () => switchTo(+nx.dataset.go));
  });
  // Camera at the start: the planet (radius 1, at the origin) appears where it was in the sky, at the same size.
  function startCam(from) {
    const W = innerWidth, H = innerHeight;
    const f = from || { x: W * .62, y: H * .5, R: H * .12 };
    const ta = Math.max(.002, f.R * TANF / (H / 2)), D0 = 1 / Math.sin(Math.atan(ta));
    const c = nrm([(f.x - W / 2) / (H / 2) * TANF, -(f.y - H / 2) / (H / 2) * TANF, -1]);
    return { pos: mul(c, -D0), q: [0, 0, 0, 1], c };
  }
  // Camera at the end: low over the site, looking ahead so that the horizon shows; the site sits
  // to the side of the text on wide screens and above it on narrow ones.
  function endCam(n, t) {
    const up0 = Math.abs(n[1]) < .95 ? [0, 1, 0] : [1, 0, 0], td = nrm(sub(up0, mul(n, dot(up0, n))));
    const pos = add(mul(n, 1.2), mul(td, -.3)), wide = innerWidth > 1000;
    let M = basis(pos, n, n);
    const d = len(sub(n, pos)), r = M.slice(0, 3), u = M.slice(3, 6);
    const aim = wide ? sub(sub(n, mul(r, (S.rtl ? -1 : 1) * .55 * TANF * d * Math.min(1.6, innerWidth / innerHeight))), mul(u, .42 * TANF * d)) : sub(n, mul(u, .5 * TANF * d));
    M = basis(pos, aim, n);
    const sway = .025 * Math.sin(t * .11);
    return { pos: add(pos, mul(M.slice(0, 3), sway)), q: m2q(M) };
  }
  function render(cam, glow, bg, time, gain) {
    const p = S.projects[cur], s = st;
    PG.clear();
    PG.draw({ vp: [0, 0, wc.width, wc.height], ortho: 0, cam: cam.pos, camM: q2m(cam.q), tanF: TANF, rot: s.rot, L: s.L, col: hex(p.col), kind: KIND[p.kind], site: s.site, time, glow, seed: cur * 3.7 + 1, bg, gain: gain == null ? 1 : gain });
  }
  // Camera orientation from pos that keeps the planet's centre in the camera direction c (camera
  // axes), with no roll: at the start of the flight this is the starting orientation itself.
  function lookQ(pos, c) {
    const up = [0, 1, 0], d = nrm(mul(pos, -1));
    const rc = nrm(cross(c, up)), uc = cross(rc, c), rw = nrm(cross(d, up)), uw = cross(rw, d);
    const col = j => add(add(mul(d, c[j]), mul(uw, uc[j])), mul(rw, rc[j]));
    return m2q([...col(0), ...col(1), ...col(2)]);
  }
  // A gentle start and stop; with the log-linear distance this reads as a steady approach.
  const glide = x => .5 - .5 * Math.cos(Math.PI * x);
  const sstep = (a, b, x) => { const k = Math.min(1, Math.max(0, (x - a) / (b - a))); return k * k * (3 - 2 * k); };
  // The flight, for progress e from 0 (the planet where it is in the sky) to 1 (low over the site).
  // The distance shrinks at a constant rate (log-linear), so the planet grows steadily. For the first
  // part the camera only moves straight towards the planet, which therefore grows in place on the
  // screen; then it swings round to the site. Space behind the planet fades in late, so the page is
  // seen behind the planet until it fills much of the screen; the way back is the same path reversed.
  function flight(n, e) {
    const a = st.a, b = endCam(n, st.time), da = len(a.pos), db = len(b.pos), w = sstep(.38, 1, e);
    const pos = mul(slerpV(nrm(a.pos), nrm(b.pos), w), Math.exp(Math.log(da) + (Math.log(db) - Math.log(da)) * e));
    // While the camera swings, it keeps turning to the planet (lookQ) and only near the end settles
    // on the view over the site, so the planet never leaves the screen.
    const q = slerpQ(lookQ(pos, a.c), b.q, sstep(.5, 1, e));
    return { cam: { pos, q }, bg: st.sw ? 1 : sstep(.4, .86, e), glow: sstep(.35, 1, e), gain: 1 + ((st.gain || 1) - 1) * (1 - sstep(0, .4, e)) };
  }

  function loop(now) {
    raf = requestAnimationFrame(loop);
    const dt = last ? (now - last) / 1000 : 0; last = now;
    if (!st) return;
    st.time += dt;
    const n = mv(st.rot, st.site);
    if (st.phase === 'in' || st.phase === 'out') {
      const k = Math.min(1, (now - st.t0) / st.dur), e = glide(st.phase === 'in' ? k : 1 - k), f = flight(n, e);
      el.style.setProperty('--bgA', f.bg);
      if (PG) render(f.cam, f.glow, f.bg, st.time, f.gain);
      if (k >= 1) { if (st.phase === 'in') landed(); else closed(); }
    } else if (st.phase === 'landed') {
      // The surface is hidden once the case study covers the screen; skip drawing it then.
      if (PG && wp.scrollTop < innerHeight * .9) render(endCam(n, st.time), 1, 1, st.time);
      if (viz) viz.draw(now, false);
    }
  }
  function landed() { st.phase = 'landed'; el.classList.add('landed'); el.classList.remove('fly'); const h = arts[cur] && arts[cur].querySelector('h2'); if (h) h.focus({ preventScroll: true }); }
  function closed() {
    cancelAnimationFrame(raf); raf = 0; st = null; viz = null;
    el.classList.remove('on', 'landed', 'fly'); el.hidden = true;
    setInert(false); document.documentElement.style.overflow = '';
    if (window.SKY) window.SKY.setActive(true);
    if (opener && document.contains(opener)) opener.focus({ preventScroll: true });
    cur = -1;
  }
  function setInert(v) { for (const s of ['main', 'header.top', 'footer', '.skip']) { const n = document.querySelector(s); if (n) n.inert = v; } }

  let waitT = 0;
  function open(i, from, opts) {
    opts = opts || {};
    if (cur === i && st) return;
    // A planet clicked while its shader is still compiling: keep the sky running and start the flight
    // as soon as the shader is ready, instead of freezing the page while it compiles.
    if (!pgDone && window.PlanetGL) {
      if (!PGH) PGH = window.PlanetGL.begin(wc);
      if (PGH && !PGH.ready()) {
        clearTimeout(waitT); document.documentElement.classList.add('wait');
        waitT = setTimeout(() => open(i, null, opts), 80); return;
      }
    }
    document.documentElement.classList.remove('wait');
    const P = window.SKY ? window.SKY.planet(i) : null;
    from = from || P;
    if (!from || !from.rot) { // no sky position (no WebGL or not drawn yet): open without the flight
      from = Object.assign({ x: innerWidth * .62, y: innerHeight * .5, R: innerHeight * .1 }, P || {});
    }
    pg();
    if (cur < 0) opener = document.activeElement;
    const switching = cur >= 0;
    cur = i; size(); fill(i);
    const p = S.projects[i], la = p.site[0] * Math.PI / 180, lo = p.site[1] * Math.PI / 180;
    const rot = from.rot || [1, 0, 0, 0, 1, 0, 0, 0, 1];
    st = { phase: 'in', t0: performance.now(), dur: !PG ? 1 : switching ? 1700 : 2200, sw: switching, gain: switching ? 1 : from.gain, a: startCam(switching ? { x: innerWidth * .5, y: innerHeight * .45, R: innerHeight * .16 } : from), rot, L: from.L || [-.6, .3, .74], site: [Math.cos(la) * Math.cos(lo), Math.cos(la) * Math.sin(lo), Math.sin(la)], time: 0 };
    el.classList.remove('landed'); el.classList.add('fly');
    if (el.hidden) { el.hidden = false; void el.offsetWidth; }
    el.classList.add('on');
    wp.scrollTo({ top: 0, behavior: 'instant' }); el.classList.remove('sc');
    setInert(true); document.documentElement.style.overflow = 'hidden';
    if (window.SKY) window.SKY.setActive(false, i);
    if (opts.push !== false) { const h = '#' + p.id; if (location.hash !== h) { history.pushState({ w: i }, '', h); pushed = true; } }
    if (!raf) { last = 0; raf = requestAnimationFrame(loop); }
    if (!PG) { el.classList.add('nogl'); landed(); }
    el.focus({ preventScroll: true });
  }
  function close(fromPop) {
    if (!st) return;
    if (!fromPop && pushed) { pushed = false; history.back(); return; }
    if (!fromPop) history.replaceState(null, '', location.pathname + location.search);
    pushed = false;
    if (!PG) { closed(); return; }
    // Fly back to where the planet is in the sky (after a switch the flight started elsewhere).
    const P = window.SKY ? window.SKY.planet(cur) : null;
    if (P && P.rot) { st.a = startCam(P); st.rot = P.rot; st.L = P.L; st.gain = P.gain; st.sw = false; }
    el.classList.remove('landed'); el.classList.add('fly');
    st.phase = 'out'; st.t0 = performance.now(); st.dur = 1800;
  }
  bBack.addEventListener('click', () => close(false));
  bPrev.addEventListener('click', () => switchTo((cur + 4) % 5));
  bNext.addEventListener('click', () => switchTo((cur + 1) % 5));
  function switchTo(i) { const h = '#' + S.projects[i].id; history.replaceState({ w: i }, '', h); open(i, null, { push: false }); }
  addEventListener('popstate', () => {
    const i = S.projects.findIndex(p => '#' + p.id === location.hash);
    if (i >= 0) { pushed = false; open(i, null, { push: false }); }
    else if (st) close(true);
  });
  el.addEventListener('keydown', e => {
    if (e.key === 'Escape') { e.preventDefault(); close(false); return; }
    if (e.key !== 'Tab') return;
    const f = [...el.querySelectorAll('button,a[href],[tabindex="-1"]')].filter(n => n.offsetParent !== null && n.tabIndex >= 0);
    if (!f.length) return;
    const a = f[0], z = f[f.length - 1];
    if (e.shiftKey && document.activeElement === a) { e.preventDefault(); z.focus(); }
    else if (!e.shiftKey && document.activeElement === z) { e.preventDefault(); a.focus(); }
  });
  addEventListener('resize', () => { if (st) size(); });
  wp.addEventListener('scroll', () => el.classList.toggle('sc', wp.scrollTop > 40), { passive: true });
  // Compile the planet shader in the background once the sky's planets are ready (the two would
  // otherwise compete for the driver), then draw one frame so the first landing does not stall.
  const idle = window.requestIdleCallback || (f => setTimeout(f, 300));
  function warm() {
    if (st || pgDone) return;
    if (!PGH) {
      if (!window.PlanetGL) { pgDone = true; return; }
      if (window.SKY && !window.SKY.planetsReady) { setTimeout(warm, 100); return; }
      PGH = window.PlanetGL.begin(wc); if (!PGH) { pgDone = true; return; }
    }
    if (!PGH.ready()) { setTimeout(warm, 100); return; }
    if (!pg()) return;
    size(); PG.clear(); PG.draw({ vp: [0, 0, wc.width, wc.height], ortho: 0, cam: [0, 0, 3], camM: [1, 0, 0, 0, 1, 0, 0, 0, 1], tanF: TANF, rot: [1, 0, 0, 0, 1, 0, 0, 0, 1], L: [0, 0, 1], col: [1, 1, 1], kind: 0, site: [0, 0, 1], time: 0, glow: 0, seed: 1, bg: 1 });
  }
  requestAnimationFrame(() => setTimeout(warm, 0));
  // Decode the first screenshot of each project while the page is idle, so showing a project does not stall.
  idle(() => arts.forEach(a => { const im = a.querySelector('.vp img:not([hidden])'); if (im && im.decode) { im.loading = 'eager'; im.decode().catch(() => {}); } }));
  window.WORLD = { open, close: () => close(false), get open_() { return cur; } };
})();
