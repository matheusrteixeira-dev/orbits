// The hero sky: a black hole (Schwarzschild) with five planets, an asteroid belt and a star field,
// all on one clock and one distance scale. Units are G = c = M = 1 (M is the hole's mass). The
// hole is taken as 1e8 solar masses (M = 1.48e8 km, 493 s), so every planet orbits outside its
// Roche limit (a gas giant would be torn apart inside about 6 M). The hole and its disc are ray
// traced exactly; the planets, belt and orbit lines are drawn without the bending of their light,
// and the planets far larger than they would be.
(function () {
  'use strict';
  const S = window.SITE;
  const A = 0, INC = 72 * Math.PI / 180, CI = Math.cos(INC), SI = Math.sin(INC);
  const RATE = 40;                      // M of time per second on screen
  const CAM = 600;                      // camera distance (M)
  const DRIFT = 2 * Math.PI / 10800;    // the camera circles the hole once every three hours on screen (radians per second)
  const SKYV = DRIFT * CAM * SI;        // so the distant stars sweep past at this speed (M per second at the hole), to the right
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
  const BELT = (() => { let s = 7; const r = () => (s = (s * 16807) % 2147483647) / 2147483647; return [...Array(1500)].map(() => ({ r: 47.5 + r() * 3, ph: r() * 6.2832, z: (r() - .5) * .5, b: .35 + .65 * r() })); })();

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
  function gShift(r, X) {
    const om = Om(r), gtt = -(1 - 2 / r), gtp = -2 * A / r, gpp = r * r + A * A + 2 * A * A / r;
    const ut = 1 / Math.sqrt(Math.max(1e-9, -(gtt + 2 * gtp * om + gpp * om * om)));
    return 1 / (ut * (1 + om * X * SI));
  }
  // Weak-field lensing by a point mass (used for the stars). X, Y: position on the sky (M); R2: squared Einstein radius.
  // Returns both images: [x, y, radial stretch, tangential stretch (signed), magnification].
  function lens(X, Y, R2) {
    const s = Math.max(.05, Math.hypot(X, Y)), q = Math.sqrt(s * s + 4 * R2), ux = X / s, uy = Y / s;
    const tp = (s + q) / 2, tm = (s - q) / 2, rp = (1 + s / q) / 2, rm = (1 - s / q) / 2;
    return [[tp * ux, tp * uy, rp, tp / s, rp * tp / s], [tm * ux, tm * uy, rm, tm / s, Math.abs(rm * tm / s)]];
  }

  // ---------- Canvases and layout ----------
  const sky = document.getElementById('sky'), bg = document.getElementById('bg'), fg = document.getElementById('fg'), bhc = document.getElementById('bh');
  const still = document.getElementById('bhstill'), labs = document.getElementById('labs'), pauseBtn = document.getElementById('pause');
  const bx = bg.getContext('2d'), fx = fg.getContext('2d');
  let dpr = 1, L = null, IR = null;
  function layout() {
    dpr = Math.min(devicePixelRatio || 1, 2);
    const w = sky.clientWidth, h = sky.clientHeight, mob = innerWidth < 820;
    const it = document.querySelector('.intro'), ir = it.getBoundingClientRect(), sr = sky.getBoundingClientRect();
    IR = mob ? null : { l: ir.left - sr.left - 24, r: ir.right - sr.left + 24, t: ir.top - sr.top - 20, b: ir.bottom - sr.top + 20 };
    // Desktop: fit the outermost planet's orbit (apoapsis APO) in the space beside the intro text,
    // so no planet ever passes under the headline. The belt may run behind the text.
    const APO = Math.max(...PL.map(p => p.a * (1 + p.e)));
    let cx = w * .5, cy = h * .5, K;
    if (mob) K = Math.min((w - 16) / (2 * (APO + 3)), h / (2 * 17)); // every planet stays on a phone screen
    else {
      const free = S.rtl ? IR.l - 16 : w - IR.r - 16;
      K = Math.max(5, Math.min(h * .86 / (2 * 19), free / (2 * APO + 4)));
      cx = S.rtl ? IR.l - 8 - (APO + 2) * K : IR.r + 8 + (APO + 2) * K;
    }
    for (const c of [bg, fg]) { c.width = Math.round(w * dpr); c.height = Math.round(h * dpr); }
    L = { w, h, cx, cy, K, mob };
    BH.place(L);
    [...labs.children].forEach(b => b._w = null);
    stars = makeStars(L);
  }

  // ---------- Stars: a sheet far behind the hole, lensed (Einstein radius about 49 M for a camera 600 M away) ----------
  let stars = [];
  const STAR_R2 = 4 * 600;
  function bbTint(T) { T /= 100; const r = T <= 66 ? 255 : 329.7 * Math.pow(T - 60, -.1332), g = T <= 66 ? 99.47 * Math.log(T) - 161.1 : 288.1 * Math.pow(T - 60, -.0755), b = T >= 66 ? 255 : T <= 19 ? 0 : 138.5 * Math.log(T - 10) - 305; return [r, g, b].map(v => Math.max(0, Math.min(255, v | 0))); }
  function makeStars(L) {
    let s = 3; const r = () => (s = (s * 16807) % 2147483647) / 2147483647;
    const hx = L.w / 2 / L.K + 60, hy = L.h / 2 / L.K + 60, n = Math.min(2600, Math.round(L.w * L.h / 520));
    return [...Array(n)].map(() => { const m = Math.pow(r(), 3.2); return { x: (r() * 2 - 1) * hx, y: (r() * 2 - 1) * hy, hx, hy, m, c: bbTint(3200 + r() * 9000) }; });
  }
  function drawStars(t) {
    const { cx, cy, K } = L, drift = t * SKYV;
    for (const s of stars) {
      let x = s.x + drift; x = ((x + s.hx) % (2 * s.hx) + 2 * s.hx) % (2 * s.hx) - s.hx;
      const offX = (cx - L.w / 2) / K, X = x - offX, Y = s.y;   // source position relative to the hole
      const im = lens(X, Y, STAR_R2);
      for (let k = 0; k < 2; k++) {
        const [ix, iy, , , mu] = im[k], a = Math.min(1, (.18 + s.m * .9) * Math.min(mu, 4));
        if (a < .03 || Math.hypot(ix, iy) < 5.4) continue;
        const sz = (s.m > .55 ? 2 : 1) * dpr * (mu > 2 ? 1.5 : 1);
        bx.fillStyle = `rgba(${s.c[0]},${s.c[1]},${s.c[2]},${a})`;
        bx.fillRect((cx + ix * K) * dpr - sz / 2, (cy - iy * K) * dpr - sz / 2, sz, sz);
      }
    }
  }

  // ---------- Black hole: every pixel traced on the GPU, with the tracer of Isaac ----------
  // Schwarzschild hole, thin disc from the ISCO (6 M) to 15 M, camera CAM away at inclination INC.
  // Each ray stays in the plane through the hole that holds the camera and the ray, where the
  // exact null geodesic obeys d2u/dphi2 = 3u^2 - u (u = 1/r); it is integrated with RK4 until it
  // falls through the horizon, crosses the disc between its edges, or escapes. Disc light: gas on
  // circular orbits, observed as g^4 F with F the thin-disc flux and a black-body colour shifted by
  // g (gravitational redshift, time dilation and Doppler shift together). The disc is symmetric
  // about its axis, so the picture does not change as the camera drifts round: it is traced once
  // (a band of rows per frame) and kept.
  const BH = (function () {
    const D = { HW: 26, HH: 16.25, rIn: 6, rOut: 15 };
    let gl = null, prog = null, u = {}, ok = false, rect = null, row = 0, rows = 0, ready = false;
    const VS = '#version 300 es\nin vec2 p;void main(){gl_Position=vec4(p,0.,1.);}';
    const FS = `#version 300 es
precision highp float;
uniform vec2 uOrig;uniform float uPix,uCam,uInc,uRin,uRout;out vec4 o;
vec3 blackbody(float T){T=clamp(T,1000.,40000.)/100.;vec3 c;
 if(T<=66.){c.r=1.;c.g=clamp((99.4708025861*log(T)-161.1195681661)/255.,0.,1.);
  c.b=T<=19.?0.:clamp((138.5177312231*log(T-10.)-305.0447927307)/255.,0.,1.);}
 else{c.r=clamp(329.698727446*pow(T-60.,-.1332047592)/255.,0.,1.);c.g=clamp(288.1221695283*pow(T-60.,-.0755148492)/255.,0.,1.);c.b=1.;}
 c=pow(c,vec3(2.2));return c/max(dot(c,vec3(.2126,.7152,.0722)),1e-4);}
vec4 trace(vec2 S){
 vec3 P=vec3(0.,uCam*cos(uInc),uCam*sin(uInc)),f=-normalize(P),ex=vec3(1.,0.,0.),ey=cross(ex,f);
 vec3 dir=normalize(f*uCam+ex*S.x+ey*S.y);
 float r0=length(P);vec3 er=P/r0;float c=dot(dir,er);vec3 tp=dir-c*er;float s=length(tp);
 vec3 ep=s>1e-6?tp/s:vec3(1.,0.,0.);s=max(s,1e-6);
 float u0=1./r0,u=u0,du=-u*sqrt(max(1.-2.*u,0.))*c/s;
 float ly=-cross(P,dir).y/sqrt(max(1.-2.*u0,1e-6)),rFar=1.5*r0,phi=0.;vec3 prev=P;
 for(int i=0;i<2000;i++){
  float h=u>.08?.012:(u>.02?.03:.07),uPrev=u;
  float k1u=du,k1v=3.*u*u-u,u2=u+.5*h*k1u,v2=du+.5*h*k1v,k2u=v2,k2v=3.*u2*u2-u2;
  float u3=u+.5*h*k2u,v3=du+.5*h*k2v,k3u=v3,k3v=3.*u3*u3-u3,u4=u+h*k3u,v4=du+h*k3v,k4u=v4,k4v=3.*u4*u4-u4;
  u+=h/6.*(k1u+2.*k2u+2.*k3u+k4u);du+=h/6.*(k1v+2.*k2v+2.*k3v+k4v);phi+=h;
  if(u>=.5)return vec4(0.,0.,0.,1.);
  vec3 pos=(cos(phi)*er+sin(phi)*ep)/max(u,1e-6);
  if(prev.y*pos.y<0.){vec3 X=mix(prev,pos,prev.y/(prev.y-pos.y));float r=length(X);
   if(r>uRin&&r<uRout){float Om=pow(r,-1.5),g=sqrt(max(1.-3./r,0.))/(sqrt(1.-2.*u0)*(1.-Om*ly));
    float fl=max(0.,1.-sqrt(uRin/r))/(r*r*r),rp=49./36.*uRin,lv=fl/((1./7.)/(rp*rp*rp));
    float st=.9+.1*sin(r*7.+3.*sin(r*1.7));
    return vec4(min(blackbody(4700.*pow(lv,.25)*g)*pow(g,4.)*lv*st*1.25,vec3(1.)),1.);}}
  if((u<1./rFar&&du<0.)||u<0.)return vec4(0.);
  prev=pos;}
 return vec4(0.);}
void main(){vec4 a=vec4(0.);
 for(int j=0;j<2;j++)for(int i=0;i<2;i++)a+=trace(uOrig+(gl_FragCoord.xy+vec2(.25+.5*float(i),.25+.5*float(j))-.5)*uPix*vec2(1.,1.));
 a*=.25;o=vec4(a.rgb,a.a);}`;
    function init() {
      try {
        gl = bhc.getContext('webgl2', { premultipliedAlpha: true, antialias: false, alpha: true, preserveDrawingBuffer: true });
        if (!gl) return false;
        const sh = (t, s) => { const x = gl.createShader(t); gl.shaderSource(x, s); gl.compileShader(x); if (!gl.getShaderParameter(x, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(x)); return x; };
        prog = gl.createProgram(); gl.attachShader(prog, sh(gl.VERTEX_SHADER, VS)); gl.attachShader(prog, sh(gl.FRAGMENT_SHADER, FS));
        gl.bindAttribLocation(prog, 0, 'p'); gl.linkProgram(prog); if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(prog));
        ['uOrig', 'uPix', 'uCam', 'uInc', 'uRin', 'uRout'].forEach(n => u[n] = gl.getUniformLocation(prog, n));
      } catch (e) { console.warn(e); gl = null; return false; }
      const b = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, b);
      gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
      gl.enableVertexAttribArray(0); gl.vertexAttribPointer(0, 2, gl.FLOAT, false, 0, 0);
      ok = true; return true;
    }
    return {
      init,
      get ok() { return ok; },
      get done() { return ready; },
      place(L) {
        const w = 2 * D.HW * L.K, h = 2 * D.HH * L.K;
        rect = { x: L.cx - w / 2, y: L.cy - h / 2, w, h };
        for (const el of [bhc, still]) { if (!el) continue; Object.assign(el.style, { left: rect.x + 'px', top: rect.y + 'px', width: w + 'px', height: h + 'px' }); }
        bhc.width = Math.round(w * dpr); bhc.height = Math.round(h * dpr);
        row = 0; rows = bhc.height; ready = false;
        if (gl) { gl.viewport(0, 0, bhc.width, bhc.height); gl.disable(gl.SCISSOR_TEST); gl.clearColor(0, 0, 0, 0); gl.clear(gl.COLOR_BUFFER_BIT); }
      },
      // Trace the next band of rows; returns true while there is more to do.
      draw() {
        if (!ok || ready || !rect) return false;
        const band = Math.max(8, Math.round(bhc.height / 24));
        gl.useProgram(prog); gl.viewport(0, 0, bhc.width, bhc.height);
        gl.enable(gl.SCISSOR_TEST); gl.scissor(0, row, bhc.width, Math.min(band, rows - row));
        const pix = 2 * D.HW / bhc.width;   // M per device pixel
        gl.uniform2f(u.uOrig, -D.HW, -bhc.height * pix / 2); gl.uniform1f(u.uPix, pix);
        gl.uniform1f(u.uCam, CAM); gl.uniform1f(u.uInc, INC); gl.uniform1f(u.uRin, D.rIn); gl.uniform1f(u.uRout, D.rOut);
        gl.drawArrays(gl.TRIANGLES, 0, 3); gl.disable(gl.SCISSOR_TEST);
        row += band;
        if (row >= rows) { ready = true; bhc.classList.add('on'); if (still) still.classList.add('off'); }
        return !ready;
      },
    };
  })();

  // ---------- Planets: rendered on the GPU into an atlas, then drawn in 2D ----------
  const atlas = document.createElement('canvas');
  const PG = window.PlanetGL && window.PlanetGL.create(atlas, { preserveDrawingBuffer: true });
  let tile = 128;
  function frameOf(p3) {
    const r = Math.hypot(...p3), ex = p3.map(v => -v / r), ez = NR;
    const ey = [ez[1] * ex[2] - ez[2] * ex[1], ez[2] * ex[0] - ez[0] * ex[2], ez[0] * ex[1] - ez[1] * ex[0]];
    const X = view(ex), Y = view(ey), Z = view(ez);
    return { rot: [...X, ...Y, ...Z], L: X };
  }
  const ext = p => p.kind === 'gas' ? 2.45 : 1.18;
  function renderAtlas(st, t) {
    if (!PG) return;
    const need = Math.min(256, Math.max(...PL.map(p => Math.ceil(2 * ext(p) * p.R * L.K * dpr))));
    if (atlas.width !== need * PL.length || atlas.height !== need) { atlas.width = need * PL.length; atlas.height = need; }
    tile = need; PG.clear();
    PL.forEach((p, i) => {
      const f = st[i].frame;
      PG.draw({ vp: [i * tile, 0, tile, tile], ortho: 1, ext: ext(p), rot: f.rot, L: f.L, col: p.rgb.map(v => v / 255), kind: KIND[p.kind], site: p.siteN, time: t, glow: 0, seed: i * 3.7 + 1, gain: st[i].gain });
    });
  }
  const KIND = { rock: 0, ocean: 1, gas: 2, storm: 3, ice: 4 };
  function drawPlanet(ctx, i, p, X, Y, M) {
    // Image of the planet through the matrix M (screen axes, Y up). The Doppler brightening
    // is applied when the planet is rendered into the atlas.
    const { cx, cy, K } = L, half = ext(p) * p.R * K * dpr, px = (cx + X * K) * dpr, py = (cy - Y * K) * dpr;
    ctx.save(); ctx.setTransform(M[0], -M[2], -M[1], M[3], px, py);
    if (PG) ctx.drawImage(atlas, i * tile, 0, tile, tile, -half, -half, 2 * half, 2 * half);
    else { const R = p.R * K * dpr, g = ctx.createRadialGradient(-R * .35, -R * .35, R * .1, 0, 0, R); g.addColorStop(0, p.col); g.addColorStop(1, '#05060c'); ctx.fillStyle = g; ctx.beginPath(); ctx.arc(0, 0, R, 0, 7); ctx.fill(); }
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
    const fo = v => () => { focusI = v; needOne = true; };
    b.addEventListener('mouseenter', fo(i)); b.addEventListener('mouseleave', fo(-1)); b.addEventListener('focus', fo(i)); b.addEventListener('blur', fo(-1));
    labs.appendChild(b);
  });
  fg.addEventListener('pointermove', e => {
    const r = fg.getBoundingClientRect(), X = e.clientX - r.left, Y = e.clientY - r.top; hover = -1;
    scr.forEach((s, i) => { if (s && Math.hypot(s.x - X, s.y - Y) < Math.max(s.R + 16, 26)) hover = i; });
    fg.style.cursor = hover >= 0 ? 'pointer' : 'default'; needOne = true;
  });
  fg.addEventListener('pointerleave', () => hover = -1);
  fg.addEventListener('click', () => { if (hover >= 0) land(hover); });
  function land(i) {
    const s = scr[i]; if (!window.WORLD) return;
    const r = sky.getBoundingClientRect();
    window.WORLD.open(i, s ? { x: r.left + s.x, y: r.top + s.y, R: s.R, rot: st[i].frame.rot, L: st[i].frame.L } : null);
  }

  // ---------- Clock and drawing ----------
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  let running = !reduce.matches, tau = 140, t = 0, last = performance.now(), active = true, st = [], needOne = true;
  function setRun(v) { running = v; pauseBtn.setAttribute('aria-pressed', String(!v)); pauseBtn.textContent = v ? T.pause : T.play; needOne = true; }
  pauseBtn.addEventListener('click', () => setRun(!running));
  reduce.addEventListener && reduce.addEventListener('change', () => setRun(!reduce.matches));
  setRun(running);
  const front = ph => Math.cos(ph) >= 0;   // nearer than the hole: drawn over its canvas
  function orbitLine(ctxF, ctxB, p, on, alpha) {
    const { cx, cy, K } = L, col = on ? `rgba(${p.rgb.join(',')},.8)` : `rgba(160,205,255,${alpha})`;
    const pts = []; for (let n = 0; n <= 240; n++) pts.push(polar(ellipsePt(p, tau, n / 240 * TAU2)));
    for (const which of ['f', 'b']) {   // the near half over the hole, the far half behind it
      const ctx = which === 'f' ? ctxF : ctxB;
      ctx.strokeStyle = col; ctx.lineWidth = (on ? 1.6 : 1) * dpr; ctx.beginPath();
      let pen = false;
      for (const [r, ph] of pts) {
        if ((which === 'f') === front(ph)) { const q = flatP(r, ph), x = (cx + q[0] * K) * dpr, y = (cy - q[1] * K) * dpr; pen ? ctx.lineTo(x, y) : ctx.moveTo(x, y); pen = true; } else pen = false;
      }
      ctx.stroke();
    }
  }
  // Planet position on screen now, as seen without the bending of light.
  function planetImage(p) {
    const p3 = orbit(p, tau), [r, ph] = polar(p3), f = flatP(r, ph);
    return { X: f[0], Y: f[1], M: [1, 0, 0, 1], p3, r, ph };
  }
  function draw() {
    const { w, h, cx, cy, K } = L, W = w * dpr, H = h * dpr;
    bx.setTransform(1, 0, 0, 1, 0, 0); fx.setTransform(1, 0, 0, 1, 0, 0);
    bx.fillStyle = '#03040a'; bx.fillRect(0, 0, W, H); fx.clearRect(0, 0, W, H);
    let g = bx.createRadialGradient(cx * dpr, cy * dpr, 0, cx * dpr, cy * dpr, K * 60 * dpr); g.addColorStop(0, 'rgba(255,150,70,.045)'); g.addColorStop(1, 'rgba(0,0,0,0)'); bx.fillStyle = g; bx.fillRect(0, 0, W, H);
    drawStars(t);
    // Planet states, lit and Doppler-shifted.
    st = PL.map(p => {
      const d = planetImage(p), p3 = d.p3;
      return { p3, im: d, v: view(p3), frame: frameOf(p3), gain: Math.min(2.2, Math.pow(gShift(d.r, d.X), 4)) };
    });
    renderAtlas(st, t);
    PL.forEach((p, i) => orbitLine(fx, bx, p, i === hover || i === focusI, .13));
    // Belt: each grain on a circular orbit, brightened by the Doppler factor.
    for (const b of BELT) {
      const ph = b.ph + Om(b.r) * tau - phc, f = flatP(b.r, ph), a = .5 * b.b * Math.min(3, Math.pow(gShift(b.r, f[0]), 4));
      if (a < .02) continue;
      const ctx = front(ph) ? fx : bx;
      ctx.fillStyle = `rgba(214,200,182,${Math.min(1, a)})`; ctx.fillRect((cx + f[0] * K) * dpr, (cy - f[1] * K) * dpr, 1.3 * dpr, 1.3 * dpr);
    }
    // Planets, farthest first.
    scr = [];
    const order = PL.map((p, i) => i).sort((a, b) => st[a].v[2] - st[b].v[2]);
    for (const i of order) {
      const p = PL[i], S_ = st[i], R = p.R * K, on = i === hover || i === focusI;
      {
        const im = S_.im, per = CAM / (CAM - im.r * Math.cos(im.ph) * SI), M = im.M.map(v => v * per);
        const ctx = front(im.ph) ? fx : bx, Re = R * per;
        glow(ctx, p, im.X, im.Y, Re, on);
        drawPlanet(ctx, i, p, im.X, im.Y, M);
        scr[i] = { x: cx + im.X * K, y: cy - im.Y * K, R: Re };
      }
      const lb = labs.children[i], s_ = scr[i];
      // Keep labels off the intro text on wide screens.
      const lx = s_.x + s_.R + 8, hid = IR && lx + 110 > IR.l && lx < IR.r && s_.y > IR.t && s_.y < IR.b;
      lb.classList.toggle('hid', !!hid);
      // Put the label on the planet's left when it would run off the right edge.
      lb._w = lb._w || {}; const k_ = on ? 1 : 0; if (!lb._w[k_]) { lb.classList.toggle('on', on); lb._w[k_] = lb.offsetWidth; }
      const lw = lb._w[k_] || 80, left = s_.x + s_.R + 8 + lw > L.w - 4;
      const lxp = left ? s_.x - s_.R - 8 - lw : s_.x + s_.R + 8;
      lb._x = Math.max(4, lxp); lb._y = s_.y; lb._lw = lw;
      lb.style.visibility = s_.x < -s_.R || s_.x > L.w + s_.R || s_.y < 0 || s_.y > L.h ? 'hidden' : '';
      lb.classList.toggle('on', on);
    }
    const ls = [...labs.children].sort((a, b) => a._y - b._y);
    for (let a = 0; a < ls.length; a++) for (let b = 0; b < a; b++) {
      const A_ = ls[a], B_ = ls[b];
      if (A_._x < B_._x + B_._lw && B_._x < A_._x + A_._lw && A_._y - B_._y < 20) A_._y = B_._y + 20;
    }
    for (const lb of ls) lb.style.transform = `translate(${Math.round(lb._x)}px,${Math.round(lb._y)}px) translateY(-50%)`;
    if (BH.draw()) needOne = true;
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
  function loop(now) {
    const dt = Math.min(.1, Math.max(0, (now - last) / 1000)); last = now;
    if (running && active) { tau += dt * RATE; t += dt; }
    phc = t * DRIFT; cph = Math.cos(phc); sph = Math.sin(phc);
    if (visible && active && (running || needOne)) { draw(); needOne = false; }
    requestAnimationFrame(loop);
  }
  BH.init();
  layout();
  if (document.fonts) document.fonts.ready.then(() => { [...labs.children].forEach(b => b._w = null); needOne = true; });
  let rz; addEventListener('resize', () => { clearTimeout(rz); rz = setTimeout(() => { layout(); needOne = true; }, 120); });
  requestAnimationFrame(loop);
  window.SKY = {
    setActive(v) { active = v; },
    planet(i) { const s = scr[i], r = sky.getBoundingClientRect(); return s ? { x: r.left + s.x, y: r.top + s.y, R: s.R, rot: st[i].frame.rot, L: st[i].frame.L } : null; },
    orbitInfo(i) { const p = PL[i]; return { a: p.a, period: 2 * Math.PI / p.O / RATE, days: 2 * Math.PI / p.O * 492.6 / 86400 }; },
    planets: PL, KIND,
  };
})();
