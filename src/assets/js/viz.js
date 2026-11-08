// Live visuals of the five projects. Each one shows what the project does, not a picture of it.
(function () {
  'use strict';
  const MONO = '"JetBrains Mono",ui-monospace,monospace';
  function rng(seed) { let s = seed; return () => (s = (s * 16807) % 2147483647) / 2147483647; }
  function frame(x, W, H) { x.fillStyle = '#02030a'; x.fillRect(0, 0, W, H); x.strokeStyle = 'rgba(255,255,255,.04)'; x.lineWidth = 1; const g = W / 16; x.beginPath(); for (let i = g; i < W; i += g) { x.moveTo(i, 0); x.lineTo(i, H); } for (let j = g; j < H; j += g) { x.moveTo(0, j); x.lineTo(W, j); } x.stroke(); }
  function label(x, s, X, Y, u, col, align) { x.font = `${Math.round(11 * u)}px ${MONO}`; x.fillStyle = col || 'rgba(200,214,240,.75)'; x.textAlign = align || 'left'; x.textBaseline = 'alphabetic'; x.fillText(s, X, Y); }

  // Isaac: a chaotic double pendulum, RK4 with 2 ms steps, and a twin started 0.001 rad away.
  function pendulum() {
    const g = 9.81, h = .002;
    let A, B, T, trail, E0;
    function reset() { A = [120 * Math.PI / 180, -20 * Math.PI / 180, 0, 0]; B = [A[0] + .001, A[1], 0, 0]; T = 0; trail = [[], []]; E0 = energy(A); }
    function deriv(s) {
      const [t1, t2, w1, w2] = s, d = t1 - t2, den = 3 - Math.cos(2 * d);
      const a1 = (-3 * g * Math.sin(t1) - g * Math.sin(t1 - 2 * t2) - 2 * Math.sin(d) * (w2 * w2 + w1 * w1 * Math.cos(d))) / den;
      const a2 = (2 * Math.sin(d) * (2 * w1 * w1 + 2 * g * Math.cos(t1) + w2 * w2 * Math.cos(d))) / den;
      return [w1, w2, a1, a2];
    }
    function rk4(s) {
      const k1 = deriv(s), k2 = deriv(s.map((v, i) => v + h / 2 * k1[i])), k3 = deriv(s.map((v, i) => v + h / 2 * k2[i])), k4 = deriv(s.map((v, i) => v + h * k3[i]));
      return s.map((v, i) => v + h / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]));
    }
    function energy(s) { const [t1, t2, w1, w2] = s; return .5 * w1 * w1 + .5 * (w1 * w1 + w2 * w2 + 2 * w1 * w2 * Math.cos(t1 - t2)) - 2 * g * Math.cos(t1) - g * Math.cos(t2); }
    reset();
    return function (x, W, H, dt, u) {
      const n = Math.round(Math.min(dt, .05) / h);
      for (let k = 0; k < n; k++) { A = rk4(A); B = rk4(B); T += h; }
      if (T > 36) reset();
      frame(x, W, H);
      const cx = W / 2, cy = H * .3, l = H * .3;
      const pos = s => { const x1 = cx + l * Math.sin(s[0]), y1 = cy + l * Math.cos(s[0]); return [x1, y1, x1 + l * Math.sin(s[1]), y1 + l * Math.cos(s[1])]; };
      const pa = pos(A), pb = pos(B);
      trail[0].push([pa[2], pa[3]]); trail[1].push([pb[2], pb[3]]);
      for (const tr of trail) if (tr.length > 260) tr.shift();
      [[trail[1], '63,240,255', .5], [trail[0], '255,90,60', .9]].forEach(([tr, c, a]) => {
        for (let i = 1; i < tr.length; i++) { x.strokeStyle = `rgba(${c},${a * i / tr.length})`; x.lineWidth = 2 * u * i / tr.length + .5; x.beginPath(); x.moveTo(tr[i - 1][0], tr[i - 1][1]); x.lineTo(tr[i][0], tr[i][1]); x.stroke(); }
      });
      [[pb, 'rgba(63,240,255,.55)', 3], [pa, '#ff5a3c', 4]].forEach(([p, c, r]) => {
        x.strokeStyle = c; x.lineWidth = 2 * u; x.beginPath(); x.moveTo(cx, cy); x.lineTo(p[0], p[1]); x.lineTo(p[2], p[3]); x.stroke();
        x.fillStyle = c; for (const [X, Y, R] of [[p[0], p[1], r * 2], [p[2], p[3], r * 2.6]]) { x.beginPath(); x.arc(X, Y, R * u, 0, 7); x.fill(); }
      });
      x.fillStyle = '#e8f0ff'; x.beginPath(); x.arc(cx, cy, 4 * u, 0, 7); x.fill();
      const sep = Math.hypot(pa[2] - pb[2], pa[3] - pb[3]) / l, dE = Math.abs((energy(A) - E0) / E0);
      label(x, `t = ${T.toFixed(1)} s`, 16 * u, H - 40 * u, u);
      label(x, `|Δx| = ${sep.toFixed(3)} L`, 16 * u, H - 22 * u, u);
      label(x, `ΔE/E = ${dE < 1e-12 ? '0' : dE.toExponential(1)}`, W - 16 * u, H - 22 * u, u, null, 'right');
      label(x, 'RK4 · h = 2 ms', W - 16 * u, H - 40 * u, u, null, 'right');
    };
  }

  // Amadeo: a spectrogram scrolls past a detector; detected pitches become notes on a staff.
  function amadeo() {
    const MEL = [60, 64, 67, 72, 71, 67, 64, 65, 69, 67, 64, 62, 60, 62, 64, 67, 65, 64, 62, 60], DUR = .42, CH = ['C', 'G7', 'Am', 'C', 'F'];
    const STEP = { 0: 0, 2: 1, 4: 2, 5: 3, 7: 4, 9: 5, 11: 6 };
    const dia = m => Math.floor(m / 12) * 7 + STEP[m % 12];
    const note = s => MEL[Math.floor(s / DUR) % MEL.length], onset = s => (s / DUR) % 1;
    let off = null, T = 4.6;
    const r = rng(5);
    return function (x, W, H, dt, u) {
      T += Math.min(dt, .05);
      const sh = H * .56, px = Math.round(W * .7), span = 4.2; // seconds visible
      if (!off || off.width !== W) { off = document.createElement('canvas'); off.width = W; off.height = Math.round(sh); off.getContext('2d').fillStyle = '#02030a'; off.getContext('2d').fillRect(0, 0, W, off.height); off.last = Math.max(0, T - 4.2); }
      const o = off.getContext('2d'), Ho = off.height, fy = f => Ho - (Math.log2(f / 110) / 5) * Ho; // 110 Hz to 3.5 kHz
      // Shift left and paint the new columns at the detector.
      // At most a tenth of the width per frame, so the first fill is spread over a few frames.
      const pxPerS = px / span, cols = Math.min(Math.round((T - off.last) * pxPerS), Math.max(8, Math.round(px / 10)));
      if (cols > 0) {
        o.drawImage(off, -cols, 0); off.last += cols / pxPerS;
        const img = o.createImageData(cols, Ho);
        for (let c = 0; c < cols; c++) {
          const ts = off.last - (cols - c) / pxPerS, m = note(ts), f0 = 440 * Math.pow(2, (m - 69) / 12), on = onset(ts), env = Math.exp(-on * 1.6) * (on < .94 ? 1 : 0);
          for (let j = 0; j < Ho; j++) {
            const f = 110 * Math.pow(2, (Ho - j) / Ho * 5); let v = r() * .05;
            for (let k = 1; k <= 6; k++) { const d = Math.log2(f / (f0 * k)) * 48; v += env / k * Math.exp(-d * d / 2); }
            v = Math.min(1, v); const i = (j * cols + c) * 4;
            img.data[i] = 40 * v + 250 * v * v * v; img.data[i + 1] = 90 * v + 140 * v * v; img.data[i + 2] = 60 + 195 * v; img.data[i + 3] = 255;
          }
        }
        o.putImageData(img, px - cols, 0);
        o.fillStyle = '#02030a'; o.fillRect(px, 0, W - px, Ho);
      }
      frame(x, W, H); x.drawImage(off, 0, 0);
      // Detector and the pitch track it reads.
      x.strokeStyle = 'rgba(61,123,255,.9)'; x.lineWidth = 1.5 * u; x.beginPath(); x.moveTo(px, 0); x.lineTo(px, H); x.stroke();
      x.strokeStyle = '#3ff0ff'; x.lineWidth = 1.6 * u; x.beginPath();
      for (let X = 0; X <= px; X += 2) { const ts = T - (px - X) / pxPerS; if (ts < 0) continue; const f0 = 440 * Math.pow(2, (note(ts) - 69) / 12), Y = fy(f0); onset(ts) < .03 ? x.moveTo(X, Y) : x.lineTo(X, Y); }
      x.stroke();
      // Staff below, on the same time axis.
      const top = sh + H * .1, gap = H * .052, bot = top + 4 * gap, E4 = dia(64);
      x.strokeStyle = 'rgba(232,240,255,.55)'; x.lineWidth = 1; x.beginPath(); for (let k = 0; k < 5; k++) { x.moveTo(8 * u, top + k * gap); x.lineTo(W - 8 * u, top + k * gap); } x.stroke();
      const n0 = Math.floor((T - span) / DUR), n1 = Math.floor(T / DUR);
      for (let n = Math.max(0, n0); n <= n1; n++) {
        const ts = n * DUR, X = px - (T - ts) * pxPerS + 10 * u; if (X > px - 4 * u || X < 0) continue;
        const m = MEL[n % MEL.length], st = dia(m) - E4, Y = bot - st * gap / 2;
        x.strokeStyle = 'rgba(232,240,255,.55)';
        for (let lst = -2; lst >= st; lst -= 2) { const ly = bot - lst * gap / 2; x.beginPath(); x.moveTo(X - gap * .9, ly); x.lineTo(X + gap * .9, ly); x.stroke(); }
        x.fillStyle = '#e8f0ff'; x.save(); x.translate(X, Y); x.rotate(-.35); x.beginPath(); x.ellipse(0, 0, gap * .62, gap * .43, 0, 0, 7); x.fill(); x.restore();
        x.strokeStyle = '#e8f0ff'; x.lineWidth = 1.4 * u; x.beginPath(); const up = st < 4; x.moveTo(X + (up ? gap * .56 : -gap * .56), Y); x.lineTo(X + (up ? gap * .56 : -gap * .56), Y + (up ? -1 : 1) * gap * 3.3); x.stroke();
        // A bar line and the estimated chord every four notes.
        if (n % 4 === 0) {
          x.strokeStyle = 'rgba(232,240,255,.35)'; x.lineWidth = 1; x.beginPath(); x.moveTo(X - gap * 1.2, top); x.lineTo(X - gap * 1.2, bot); x.stroke();
          x.font = `600 ${Math.round(15 * u)}px ${MONO}`; x.fillStyle = '#7fb0ff'; x.textAlign = 'left'; x.fillText(CH[(n / 4) % CH.length], X - gap * .6, sh + H * .05);
        }
      }
      label(x, 'TensorFlow.js · pitch', 12 * u, 18 * u, u, 'rgba(200,214,240,.7)');
      label(x, 'key: C major', W - 12 * u, H - 12 * u, u, '#7fb0ff', 'right');
    };
  }

  // Brectus: requests go through a router to one coding agent per project.
  function brectus() {
    const r = rng(3), names = ['isaac', 'amadeo', 'allwinner', 'websites'];
    let pk = [], T = 0, next = 0;
    return function (x, W, H, dt, u) {
      T += Math.min(dt, .05);
      frame(x, W, H);
      const R = [W * .45, H * .46], src = [W * .1, H * .46], ag = names.map((n, i) => [W * .82, H * (.17 + i * .19)]), ks = [W * .45, H * .86];
      if (T > next) { const k = Math.floor(r() * 4); pk.push({ k, t: T }); next = T + .55 + r() * .5; }
      x.lineWidth = 1.2 * u;
      x.strokeStyle = 'rgba(180,92,255,.35)'; x.beginPath(); x.moveTo(src[0], src[1]); x.lineTo(R[0], R[1]); ag.forEach(a => { x.moveTo(R[0], R[1]); x.lineTo(a[0], a[1]); }); x.stroke();
      x.setLineDash([4 * u, 4 * u]); x.strokeStyle = 'rgba(255,194,61,.5)'; x.beginPath(); x.moveTo(R[0], R[1]); x.lineTo(ks[0], ks[1]); x.stroke(); x.setLineDash([]);
      pk = pk.filter(p => T - p.t < 2.6);
      for (const p of pk) {
        const s = T - p.t, a = ag[p.k]; let X, Y, c = '#e8f0ff';
        if (s < .8) { const f = s / .8; X = src[0] + (R[0] - src[0]) * f; Y = src[1] + (R[1] - src[1]) * f; }
        else if (s < 1.6) { const f = (s - .8) / .8; X = R[0] + (a[0] - R[0]) * f; Y = R[1] + (a[1] - R[1]) * f; c = '#b45cff'; }
        else { const f = (s - 1.6) / 1; X = a[0] + (src[0] - a[0]) * f; Y = a[1] + (src[1] - a[1]) * f; c = 'rgba(63,240,255,.0)'; }
        x.fillStyle = c; x.beginPath(); x.arc(X, Y, 4.5 * u, 0, 7); x.fill();
        if (s >= 1.6 && s < 2.1) { x.strokeStyle = `rgba(180,92,255,${1 - (s - 1.6) * 2})`; x.lineWidth = 2 * u; x.beginPath(); x.arc(a[0], a[1], 20 * u + (s - 1.6) * 40 * u, 0, 7); x.stroke(); }
      }
      const box = (X, Y, w, h, txt, col, fill) => { x.fillStyle = fill || '#090d1c'; x.strokeStyle = col; x.lineWidth = 1.4 * u; x.beginPath(); x.rect(X - w / 2, Y - h / 2, w, h); x.fill(); x.stroke(); label(x, txt, X, Y + 4 * u, u, '#e8f0ff', 'center'); };
      box(src[0], src[1], 92 * u, 34 * u, 'request', 'rgba(232,240,255,.5)');
      const hx = 46 * u; x.fillStyle = '#160a26'; x.strokeStyle = '#b45cff'; x.lineWidth = 1.8 * u; x.beginPath(); for (let k = 0; k < 6; k++) { const an = k / 6 * 6.283 + .5236; x.lineTo(R[0] + Math.cos(an) * hx, R[1] + Math.sin(an) * hx); } x.closePath(); x.fill(); x.stroke();
      label(x, 'router', R[0], R[1] + 4 * u, u, '#e8f0ff', 'center');
      ag.forEach((a, i) => box(a[0], a[1], 130 * u, 32 * u, names[i] + '/agent', 'rgba(180,92,255,.7)'));
      box(ks[0], ks[1], 110 * u, 28 * u, 'OS keystore', 'rgba(255,194,61,.7)');
    };
  }

  // Websites: Lighthouse scores and the three browser engines the accessibility tests run in.
  function websites() {
    let T = 2.4;
    return function (x, W, H, dt, u) {
      T += Math.min(dt, .05); const c = Math.min(T, 9), f = Math.min(1, c / 2.2), e = 1 - Math.pow(1 - f, 3);
      frame(x, W, H);
      const ring = (X, Y, R, v, icon) => {
        x.lineWidth = 10 * u; x.strokeStyle = 'rgba(45,224,165,.15)'; x.beginPath(); x.arc(X, Y, R, 0, 7); x.stroke();
        x.strokeStyle = '#2de0a5'; x.lineCap = 'round'; x.beginPath(); x.arc(X, Y, R, -Math.PI / 2, -Math.PI / 2 + 6.2832 * v / 100 * e); x.stroke(); x.lineCap = 'butt';
        x.font = `700 ${Math.round(R * .62)}px ${MONO}`; x.fillStyle = '#e8f0ff'; x.textAlign = 'center'; x.textBaseline = 'middle'; x.fillText(String(Math.round(v * e)), X, Y + 2 * u); x.textBaseline = 'alphabetic';
        icon(X, Y + R + 30 * u);
      };
      const phone = (X, Y) => { x.strokeStyle = 'rgba(232,240,255,.7)'; x.lineWidth = 1.6 * u; x.strokeRect(X - 9 * u, Y - 15 * u, 18 * u, 30 * u); x.fillStyle = 'rgba(232,240,255,.7)'; x.fillRect(X - 3 * u, Y + 10 * u, 6 * u, 1.6 * u); };
      const desk = (X, Y) => { x.strokeStyle = 'rgba(232,240,255,.7)'; x.lineWidth = 1.6 * u; x.strokeRect(X - 22 * u, Y - 14 * u, 44 * u, 26 * u); x.beginPath(); x.moveTo(X, Y + 12 * u); x.lineTo(X, Y + 18 * u); x.moveTo(X - 10 * u, Y + 18 * u); x.lineTo(X + 10 * u, Y + 18 * u); x.stroke(); };
      ring(W * .2, H * .36, H * .17, 95, phone); ring(W * .47, H * .36, H * .17, 100, desk);
      // Three engines, each running the WCAG 2.2 AA checks.
      ['Chromium', 'Firefox', 'WebKit'].forEach((n, i) => {
        const X = W * .67, Y = H * (.12 + i * .26), w = W * .29, h = H * .21, done = c > 2.6 + i * .7;
        x.fillStyle = '#090d1c'; x.strokeStyle = 'rgba(45,224,165,.45)'; x.lineWidth = 1.2 * u; x.fillRect(X, Y, w, h); x.strokeRect(X, Y, w, h);
        x.fillStyle = 'rgba(232,240,255,.12)'; x.fillRect(X, Y, w, h * .17);
        [0, 1, 2].forEach(k => { x.fillStyle = 'rgba(232,240,255,.35)'; x.beginPath(); x.arc(X + (8 + k * 9) * u, Y + h * .085, 2.4 * u, 0, 7); x.fill(); });
        x.fillStyle = 'rgba(232,240,255,.16)'; x.fillRect(X + w * .08, Y + h * .3, w * .5, h * .1); x.fillRect(X + w * .08, Y + h * .5, w * .76, h * .07); x.fillRect(X + w * .08, Y + h * .64, w * .6, h * .07);
        label(x, n, X + w * .08, Y + h * .92, u * .95, 'rgba(232,240,255,.8)');
        if (done) { x.strokeStyle = '#2de0a5'; x.lineWidth = 2.6 * u; x.beginPath(); const cx = X + w * .86, cy = Y + h * .62; x.moveTo(cx - 9 * u, cy); x.lineTo(cx - 2 * u, cy + 7 * u); x.lineTo(cx + 10 * u, cy - 8 * u); x.stroke(); }
      });
      label(x, 'Lighthouse', W * .335, H * .82, u, 'rgba(200,214,240,.7)', 'center');
      label(x, 'WCAG 2.2 AA', W * .815, H * .93, u, 'rgba(200,214,240,.7)', 'center');
    };
  }

  // Allwinner: walk-forward testing. Fit on one window, trade the next, then roll forward.
  function allwinner() {
    const r = rng(17), N = 420, px = [100];
    for (let i = 1; i < N; i++) { const reg = Math.sin(i / 60) * .0016; px.push(px[i - 1] * Math.exp(reg + (r() - .5) * .028)); }
    const ret = px.map((v, i) => i ? Math.log(v / px[i - 1]) : 0);
    // A momentum signal; position decided from data up to the previous step only.
    const sig = ret.map((_, i) => { let s = 0; for (let k = Math.max(1, i - 20); k < i; k++) s += ret[k]; return s > 0 ? 1 : 0; });
    let T = 0;
    return function (x, W, H, dt, u) {
      T += Math.min(dt, .05);
      frame(x, W, H);
      const fit = 120, test = 40, steps = Math.floor((N - fit) / test), k = Math.floor(T / 1.1) % (steps + 3), s0 = Math.min(k, steps - 1) * test;
      const lo = Math.min(...px) * .97, hi = Math.max(...px) * 1.03, top = H * .08, ph = H * .48, X = i => 14 * u + i / (N - 1) * (W - 28 * u), Y = v => top + ph - (v - lo) / (hi - lo) * ph;
      x.fillStyle = 'rgba(141,155,184,.13)'; x.fillRect(X(s0), top, X(s0 + fit) - X(s0), ph);
      x.fillStyle = 'rgba(255,194,61,.2)'; x.fillRect(X(s0 + fit), top, X(Math.min(N - 1, s0 + fit + test)) - X(s0 + fit), ph);
      x.strokeStyle = 'rgba(232,240,255,.8)'; x.lineWidth = 1.3 * u; x.beginPath(); px.forEach((v, i) => i ? x.lineTo(X(i), Y(v)) : x.moveTo(X(i), Y(v))); x.stroke();
      // Out-of-sample equity: only the test windows seen so far, after a fee on each trade.
      const end = Math.min(N - 1, s0 + fit + test), eq = [], bh = [];
      let e = 1, b = 1, prev = 0;
      for (let i = fit; i <= end; i++) { const pos = sig[i]; e *= Math.exp(pos * ret[i]) * (pos !== prev ? .998 : 1); prev = pos; b *= Math.exp(ret[i]); eq.push([i, e]); bh.push([i, b]); }
      const all = eq.concat(bh).map(p => p[1]), elo = Math.min(1, ...all) * .97, ehi = Math.max(1, ...all) * 1.03, et = H * .66, eh = H * .27, EY = v => et + eh - (v - elo) / (ehi - elo) * eh;
      x.strokeStyle = 'rgba(255,255,255,.12)'; x.beginPath(); x.moveTo(X(fit), EY(1)); x.lineTo(X(N - 1), EY(1)); x.stroke();
      x.strokeStyle = 'rgba(141,155,184,.7)'; x.lineWidth = 1.2 * u; x.beginPath(); bh.forEach((p, i) => i ? x.lineTo(X(p[0]), EY(p[1])) : x.moveTo(X(p[0]), EY(p[1]))); x.stroke();
      x.strokeStyle = '#ffc23d'; x.lineWidth = 2 * u; x.beginPath(); eq.forEach((p, i) => i ? x.lineTo(X(p[0]), EY(p[1])) : x.moveTo(X(p[0]), EY(p[1]))); x.stroke();
      label(x, 'fit', X(s0) + 6 * u, top + 16 * u, u);
      label(x, 'test', X(s0 + fit) + 6 * u, top + 16 * u, u, '#ffc23d');
      label(x, 'out-of-sample', X(fit), et - 6 * u, u, '#ffc23d');
    };
  }

  const MAKERS = { isaac: pendulum, amadeo, brectus, websites, allwinner };
  function attach(canvas, id) {
    const draw = MAKERS[id](); let last = 0;
    return {
      draw(now, still) {
        const d = Math.min(devicePixelRatio || 1, 2), w = Math.round(canvas.clientWidth * d), h = Math.round(w * .75);
        if (!w) return;
        if (canvas.width !== w || canvas.height !== h) { canvas.width = w; canvas.height = h; }
        // A step of at most 0.1 s, so a drawing that comes back on screen picks up where it left off.
        const dt = still ? 0 : last ? Math.min(.1, (now - last) / 1000) : 0; last = now;
        draw(canvas.getContext('2d'), w, h, still && !this.once ? 6 : dt, w / 640); this.once = true;
      },
    };
  }
  window.VIZ = { attach };
})();
