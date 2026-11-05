// The hero sky: a spinning (Kerr) black hole with five planets, an asteroid belt and a star
// field, all on one clock and one distance scale. Units are G = c = M = 1 (M is the hole's mass).
// The hole is taken as 1e8 solar masses (M = 1.48e8 km, 493 s), so every planet orbits outside
// its Roche limit (a gas giant would be torn apart inside about 6 M). Distances, speeds, light
// paths and delays are to scale; the planets are drawn far larger than they would be.
(function () {
  'use strict';
  const S = window.SITE;
  const A = 0.9, INC = 72 * Math.PI / 180, CI = Math.cos(INC), SI = Math.sin(INC);
  const RATE = 40;                      // M of time per second on screen
  const CAM = 600;                      // camera distance (M), as in tools/kerr.py and tools/plane_lens.py
  const DRIFT = 2 * Math.PI / 10800;    // the camera circles the hole once every three hours on screen (radians per second)
  const SKYV = DRIFT * CAM * SI;        // so the distant stars sweep past at this speed (M per second at the hole), to the right
  const Om = r => 1 / (Math.pow(r, 1.5) + A);                       // prograde Kerr orbital rate
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
  // Exact light paths from the orbital plane (tools/plane_lens.py): for a plane point (r, phi from
  // the camera azimuth) and image k (0 direct, 1 round the hole) -> screen X, Y (M) and light delay T.
  let PT = null;
  fetch(S.base + 'assets/bh/plane.json').then(r => r.ok ? r.json() : null).then(j => {
    if (!j) return;
    const s = atob(j.data), u8 = new Uint8Array(s.length); for (let i = 0; i < s.length; i++) u8[i] = s.charCodeAt(i);
    const dv = new DataView(u8.buffer), q = new Int16Array(u8.length / 2); for (let i = 0; i < q.length; i++) q[i] = dv.getInt16(2 * i, true);
    if (q.length !== 2 * 3 * j.nr * j.nphi) return;
    PT = { rMin: j.rMin, dr: j.dr, nr: j.nr, nphi: j.nphi, sxy: j.scaleXY, st: j.scaleT, q }; needOne = true;
  }).catch(() => {});
  const TAU2 = 2 * Math.PI, NO = -32768;
  function planeImg(k, r, ph) {
    const m = PT, fr = (r - m.rMin) / m.dr; if (fr < 0 || fr > m.nr - 1) return null;
    let fp = ((ph % TAU2) + TAU2) % TAU2 / TAU2 * m.nphi;
    const i = Math.min(m.nr - 2, fr | 0), j = fp | 0, u = fr - i, v = fp - j, j1 = (j + 1) % m.nphi, n = m.nr * m.nphi, out = [0, 0, 0];
    for (let c = 0; c < 3; c++) {
      const o = (k * 3 + c) * n, a = m.q[o + i * m.nphi + j], b = m.q[o + i * m.nphi + j1], d = m.q[o + (i + 1) * m.nphi + j], e = m.q[o + (i + 1) * m.nphi + j1];
      if (a === NO || b === NO || d === NO || e === NO) return null;
      out[c] = ((a * (1 - v) + b * v) * (1 - u) + (d * (1 - v) + e * v) * u) / (c < 2 ? m.sxy : m.st);
    }
    return out;
  }
  // Hole-frame point -> (r, azimuth from the camera).
  const polar = p3 => [Math.hypot(p3[0], p3[1]), Math.atan2(p3[1], p3[0]) - phc];
  // Flat-space perspective projection of a plane point (no bending), for the lens distortion.
  const flatP = (r, ph) => { const x = r * Math.cos(ph), y = r * Math.sin(ph), z = x * SI, f = CAM / (CAM - z); return [y * f, -x * CI * f]; };
  // Image k of a plane point: screen position, delay, and the local lens matrix (screen
  // displacement per flat-sky displacement), from finite differences of the table.
  function imageOf(k, r, ph) {
    const c = planeImg(k, r, ph); if (!c) return null;
    const h = r + .25 > PT.rMin + PT.dr * (PT.nr - 1) ? -.25 : .25, dr = planeImg(k, r + h, ph), dp = planeImg(k, r, ph + .25 / r);
    if (!dr || !dp) return { X: c[0], Y: c[1], T: c[2], M: [1, 0, 0, 1] };
    const f0 = flatP(r, ph), fr = flatP(r + h, ph), fp = flatP(r, ph + .25 / r);
    const J = [dr[0] - c[0], dp[0] - c[0], dr[1] - c[1], dp[1] - c[1]], F = [fr[0] - f0[0], fp[0] - f0[0], fr[1] - f0[1], fp[1] - f0[1]];
    const det = F[0] * F[3] - F[1] * F[2]; if (Math.abs(det) < 1e-9) return { X: c[0], Y: c[1], T: c[2], M: [1, 0, 0, 1] };
    const Fi = [F[3] / det, -F[1] / det, -F[2] / det, F[0] / det];
    return { X: c[0], Y: c[1], T: c[2], M: [J[0] * Fi[0] + J[1] * Fi[2], J[0] * Fi[1] + J[1] * Fi[3], J[2] * Fi[0] + J[3] * Fi[2], J[2] * Fi[1] + J[3] * Fi[3]] };
  }
  // Doppler and gravitational shift of light from a circular prograde orbit at r, seen at screen X:
  // g = 1 / (u^t (1 - Omega L)), L = -X sin(i), as for the disc in tools/kerr.py.
  function gShift(r, X) {
    const om = Om(r), gtt = -(1 - 2 / r), gtp = -2 * A / r, gpp = r * r + A * A + 2 * A * A / r;
    const ut = 1 / Math.sqrt(Math.max(1e-9, -(gtt + 2 * gtp * om + gpp * om * om)));
    return 1 / (ut * (1 + om * X * SI));
  }
  // Weak-field lensing by a point mass (used for the stars, and for the plane until the table loads). X, Y: position on the sky (M); R2: squared Einstein radius.
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

  // ---------- Black hole: geodesic data maps shaded every frame on the GPU ----------
  const BH = (function () {
    const D = { HW: 26, HH: 16.25, rIn: 2.320883041761887, rOut: 24 };
    const NT = 22, P = 90;            // texture terms; lifetime of a generation of disc turbulence (M)
    let gl = null, ok = false, prog = {}, tex = {}, fb = {}, W = 1600, H = 800, terms, bb, FMAX = 1, rect = null;
    const VS = '#version 300 es\nin vec2 p;void main(){gl_Position=vec4(p,0.,1.);}';
    const SHADE = `#version 300 es
precision highp float;precision highp int;
#define NT ${NT}
uniform highp sampler2D uMap;uniform sampler2D uBB;uniform int uH;uniform float uFmax,uRin,uRout,uA;
uniform vec4 uTerm[NT];uniform float uRp[2*NT];uniform vec2 uW,uAge;uniform float uPhc;out vec4 o;
float F(float r){return pow(r,-3.)*max(1.-sqrt(uRin/r),0.);}
// Gas texture: a few broad spiral waves cos(m phi + k ln r), carried round at the Kerr rate and
// wound up by the differential rotation; each generation lives P M of time and cross-fades into
// the next, so the pattern never winds into hairlines. It only modulates the brightness by
// about +-10 per cent, with fine orbital streaks as in Isaac: the light itself is the thin-disc flux.
float tx(float r,float lr,float phi,float dl){
 float Om=1./(pow(r,1.5)+uA),sh=1.5*pow(r,1.5)*Om*Om,acc=0.;
 for(int L=0;L<2;L++){float age=uAge[L],ph=phi-Om*age,n=0.;
  for(int j=0;j<NT;j++){vec4 T=uTerm[j];float k=abs(T.y+T.x*age*sh);
   n+=T.z*clamp(1.2-k*dl*2.,0.,1.)*cos(T.x*ph+T.y*lr+T.w+uRp[L*NT+j]);}
  acc+=uW[L]*n;}
 float n=acc/sqrt(max(dot(uW,uW),1e-3))/3.;
 return (1.+.1*tanh(n))*(.9+.1*sin(r*7.+3.*sin(r*1.7)));}
void main(){ivec2 q=ivec2(gl_FragCoord.xy);
 vec3 a0=floor(texelFetch(uMap,q,0).rgb*255.+.5),p0=floor(texelFetch(uMap,q+ivec2(0,uH),0).rgb*255.+.5);
 vec3 a1=floor(texelFetch(uMap,q+ivec2(0,2*uH),0).rgb*255.+.5),p1=floor(texelFetch(uMap,q+ivec2(0,3*uH),0).rgb*255.+.5);
 float c0=a0.r*256.+a0.g,c1=a1.r*256.+a1.g;
 float r0=c0>.5?uRin+(c0-1.)/65534.*(uRout-uRin):uRin,r1=c1>.5?uRin+(c1-1.)/65534.*(uRout-uRin):uRin;
 float l0=log(r0),l1=log(r1),d0=fwidth(l0),d1=fwidth(l1);
 float tr=1.;vec3 acc=vec3(0);
 for(int k=0;k<2;k++){float cc=k==0?c0:c1;if(cc<.5)continue;
  float r=k==0?r0:r1,lr=k==0?l0:l1,dl=k==0?d0:d1;vec3 aa=k==0?a0:a1,pp=k==0?p0:p1;
  float phi=(pp.r*256.+pp.g)/65536.*6.2831853+uPhc,g=.2+aa.b/255.*1.6;
  // Optically thick thin disc (Novikov-Thorne flux F, zero at the ISCO). Observed bolometric
  // intensity g^4 F; colour from a black body at T proportional to F^(1/4), shifted by g.
  float fl=F(r)/uFmax,T=clamp(g*5200.*pow(fl,.25),1500.,12000.);
  float w=clamp(fwidth(r),.02,.6),edge=smoothstep(uRin,uRin+.2,r)*smoothstep(12.+w,12.-w,r);   // the disc ends sharply at 12 M
  // Exposure: a camera's log-like response, so the cool outer disc stays visible next to the
  // hot inner edge (a display choice; the ratios between points are kept in order).
  float I=pow(g*g*g*g*fl,.55)*tx(r,lr,phi,dl)*2.,al=edge;
  vec3 col=texture(uBB,vec2((T-1500.)/10500.*(255./256.)+.5/256.,.5)).rgb;
  acc+=tr*al*col*I;tr*=1.-al;}
 vec3 img=acc;
 o=vec4(sqrt(clamp(img/4.,0.,1.)),step(127.5,p0.b)*step(.5,tr));}`;
    const BRIGHT = `#version 300 es
precision highp float;uniform sampler2D uS;uniform vec2 uSz;out vec4 o;
void main(){vec3 s=texture(uS,gl_FragCoord.xy/uSz).rgb;o=vec4(max(s*s*4.-.55,0.)/4.,1.);}`;
    const BLUR = `#version 300 es
precision highp float;uniform sampler2D uSrc;uniform vec2 uSz,uStep;uniform float uSig;uniform int uN;out vec4 o;
void main(){vec2 uv=gl_FragCoord.xy/uSz;vec3 s=vec3(0);float w=0.;
 for(int i=-32;i<=32;i++){if(i<-uN||i>uN)continue;float k=exp(-float(i*i)/(2.*uSig*uSig));s+=k*texture(uSrc,uv+uStep*float(i)).rgb;w+=k;}
 o=vec4(s/w,1.);}`;
    const FINAL = `#version 300 es
precision highp float;uniform sampler2D uS,uB1,uB2;uniform vec2 uSz;out vec4 o;
void main(){vec2 uv=gl_FragCoord.xy/uSz;uv.y=1.-uv.y;vec4 s=texture(uS,uv);
 vec3 img=(s.rgb*s.rgb*4.+(.06*texture(uB1,uv).rgb+.03*texture(uB2,uv).rgb)*4.)*.9;
 img=min(img,vec3(1.));
 img*=smoothstep(0.,.03,uv.x)*smoothstep(1.,.97,uv.x)*smoothstep(0.,.05,uv.y)*smoothstep(1.,.95,uv.y);
 o=vec4(img,clamp(max(s.a,max(img.r,max(img.g,img.b))*1.15),0.,1.));}`;

    function rng(seed) { let s = seed; return () => (s = (s * 16807) % 2147483647) / 2147483647; }
    // Blackbody colours (CIE 1931 fit, sRGB primaries, normalised), as in the README banner.
    function bbTable() {
      const n = 81, lam = [...Array(n)].map((_, i) => (380 + i * 5) * 1e-9), h = 6.626e-34, c = 2.998e8, k = 1.381e-23;
      const g_ = (x, mu, s1, s2) => Math.exp(-.5 * Math.pow((x - mu) / (x < mu ? s1 : s2), 2));
      const xb = [], yb = [], zb = [];
      lam.forEach(l => { const L = l * 1e9; xb.push(1.056 * g_(L, 599.8, 37.9, 31) + .362 * g_(L, 442, 16, 26.7) - .065 * g_(L, 501.1, 20.4, 26.2)); yb.push(.821 * g_(L, 568.8, 46.9, 40.5) + .286 * g_(L, 530.9, 16.3, 31.1)); zb.push(1.217 * g_(L, 437, 11.8, 36) + .681 * g_(L, 459, 26, 13.8)); });
      const out = new Uint8Array(256 * 4);
      for (let i = 0; i < 256; i++) {
        const T = 1500 + i / 255 * 10500; let X = 0, Y = 0, Z = 0;
        lam.forEach((l, j) => { const B = 1 / Math.pow(l, 5) / (Math.exp(h * c / (l * k * T)) - 1); X += B * xb[j]; Y += B * yb[j]; Z += B * zb[j]; });
        let rgb = [3.2406 * X - 1.5372 * Y - .4986 * Z, -.9689 * X + 1.8758 * Y + .0415 * Z, .0557 * X - .204 * Y + 1.057 * Z].map(v => Math.max(0, v));
        const m = Math.max(...rgb); rgb = rgb.map(v => v / m);
        out.set([rgb[0] * 255, rgb[1] * 255, rgb[2] * 255, 255].map(Math.round), i * 4);
      }
      return out;
    }
    function compile(fs) {
      const sh = (t, s) => { const x = gl.createShader(t); gl.shaderSource(x, s); gl.compileShader(x); if (!gl.getShaderParameter(x, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(x)); return x; };
      const p = gl.createProgram(); gl.attachShader(p, sh(gl.VERTEX_SHADER, VS)); gl.attachShader(p, sh(gl.FRAGMENT_SHADER, fs));
      gl.bindAttribLocation(p, 0, 'p'); gl.linkProgram(p); if (!gl.getProgramParameter(p, gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(p));
      const u = {}, n = gl.getProgramParameter(p, gl.ACTIVE_UNIFORMS);
      for (let i = 0; i < n; i++) { const nm = gl.getActiveUniform(p, i).name.replace('[0]', ''); u[nm] = gl.getUniformLocation(p, nm); }
      return { p, u };
    }
    function target(w, h) {
      const t = gl.createTexture(); gl.bindTexture(gl.TEXTURE_2D, t);
      gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA8, w, h, 0, gl.RGBA, gl.UNSIGNED_BYTE, null);
      [gl.TEXTURE_MIN_FILTER, gl.TEXTURE_MAG_FILTER].forEach(f => gl.texParameteri(gl.TEXTURE_2D, f, gl.LINEAR));
      [gl.TEXTURE_WRAP_S, gl.TEXTURE_WRAP_T].forEach(f => gl.texParameteri(gl.TEXTURE_2D, f, gl.CLAMP_TO_EDGE));
      const f = gl.createFramebuffer(); gl.bindFramebuffer(gl.FRAMEBUFFER, f); gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, t, 0);
      return { t, f, w, h };
    }
    function init() {
      try {
        gl = bhc.getContext('webgl2', { premultipliedAlpha: true, antialias: false, alpha: true });
        if (!gl) return false;
        prog.shade = compile(SHADE); prog.bright = compile(BRIGHT); prog.blur = compile(BLUR); prog.fin = compile(FINAL);
      } catch (e) { console.warn(e); gl = null; return false; }
      const b = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, b);
      gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
      gl.enableVertexAttribArray(0); gl.vertexAttribPointer(0, 2, gl.FLOAT, false, 0, 0);
      // Disc texture: 22 spiral terms cos(m phi + k_r ln r), m = 1..4, k_r = 2..11.
      const r = rng(9); terms = new Float32Array(NT * 4);
      for (let j = 0; j < NT; j++) { const m = 1 + Math.floor(r() * 4), kr = 2 + r() * 9; terms.set([m, kr, (.3 + .7 * r()) / (1 + .05 * m), r() * 6.2832], j * 4); }
      let fm = 0; for (let i = 0; i < 4000; i++) { const rr = D.rIn + (D.rOut - D.rIn) * i / 3999; fm = Math.max(fm, Math.pow(rr, -3) * Math.max(0, 1 - Math.sqrt(D.rIn / rr))); } FMAX = fm;
      tex.bb = gl.createTexture(); gl.bindTexture(gl.TEXTURE_2D, tex.bb);
      gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA8, 256, 1, 0, gl.RGBA, gl.UNSIGNED_BYTE, bbTable());
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
      const small = Math.min(innerWidth, 1400) * Math.min(devicePixelRatio || 1, 2) < 1100;
      const im = new Image(); im.decoding = 'async';
      im.onload = () => {
        W = im.width; H = im.height / 4;
        tex.map = gl.createTexture(); gl.bindTexture(gl.TEXTURE_2D, tex.map);
        gl.pixelStorei(gl.UNPACK_COLORSPACE_CONVERSION_WEBGL, gl.NONE); gl.pixelStorei(gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL, false);
        gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGB8, gl.RGB, gl.UNSIGNED_BYTE, im);
        [gl.TEXTURE_MIN_FILTER, gl.TEXTURE_MAG_FILTER].forEach(f => gl.texParameteri(gl.TEXTURE_2D, f, gl.NEAREST));
        fb.S = target(W, H); fb.Bh = target(W / 2, H / 2); fb.T1 = target(W / 2, H / 2); fb.B1 = target(W / 2, H / 2); fb.T2 = target(W / 4, H / 4); fb.B2 = target(W / 4, H / 4);
        ok = true; bhc.classList.add('on'); if (still) still.classList.add('off');
      };
      im.src = S.base + 'assets/bh/' + (small ? 'bh-map-s.png' : 'bh-map.png');
      return true;
    }
    function pass(p, f, setup) { gl.useProgram(p.p); gl.bindFramebuffer(gl.FRAMEBUFFER, f ? f.f : null); if (f) gl.viewport(0, 0, f.w, f.h); else gl.viewport(0, 0, bhc.width, bhc.height); setup(p.u); gl.drawArrays(gl.TRIANGLES, 0, 3); }
    function bind(unit, t) { gl.activeTexture(gl.TEXTURE0 + unit); gl.bindTexture(gl.TEXTURE_2D, t); }
    function blur(src, dst, sw, sh, dx, dy, sig) {
      pass(prog.blur, dst, u => { bind(0, src.t); gl.uniform1i(u.uSrc, 0); gl.uniform2f(u.uSz, dst.w, dst.h); gl.uniform2f(u.uStep, dx, dy); gl.uniform1f(u.uSig, sig); gl.uniform1i(u.uN, Math.ceil(sig * 2.6)); });
    }
    return {
      init,
      get ok() { return ok; },
      place(L) {
        const w = 2 * D.HW * L.K, h = 2 * D.HH * L.K;
        rect = { x: L.cx - w / 2, y: L.cy - h / 2, w, h };
        for (const el of [bhc, still]) { if (!el) continue; Object.assign(el.style, { left: rect.x + 'px', top: rect.y + 'px', width: w + 'px', height: h + 'px' }); }
        bhc.width = Math.round(w * dpr); bhc.height = Math.round(h * dpr);
      },
      draw(tau) {
        if (!ok) return;
        const rp = new Float32Array(2 * NT), wv = [0, 0], age = [0, 0];
        for (let L = 0; L < 2; L++) {
          const c = tau / P + .5 * L, gen = Math.floor(c), s = c - gen; wv[L] = 1 - Math.abs(2 * s - 1); age[L] = s * P;
          const r = rng(1 + ((gen * 2 + L) % 100000 + 100000) % 100000 * 7919 % 2147483646);
          for (let j = 0; j < NT; j++) rp[L * NT + j] = r() * 6.2832;
        }
        gl.disable(gl.BLEND);
        pass(prog.shade, fb.S, u => {
          bind(0, tex.map); bind(1, tex.bb); gl.uniform1i(u.uMap, 0); gl.uniform1i(u.uBB, 1); gl.uniform1i(u.uH, H);
          gl.uniform1f(u.uFmax, FMAX); gl.uniform1f(u.uRin, D.rIn); gl.uniform1f(u.uRout, D.rOut); gl.uniform1f(u.uA, A);
          gl.uniform4fv(u.uTerm, terms); gl.uniform1fv(u.uRp, rp); gl.uniform2fv(u.uW, wv); gl.uniform2fv(u.uAge, age); gl.uniform1f(u.uPhc, phc);
        });
        pass(prog.bright, fb.Bh, u => { bind(0, fb.S.t); gl.uniform1i(u.uS, 0); gl.uniform2f(u.uSz, fb.Bh.w, fb.Bh.h); });
        // Two bloom radii, W/160 and W/40 of the image width, as in the banner.
        blur(fb.Bh, fb.T1, 0, 0, 1 / fb.T1.w, 0, W / 320); blur(fb.T1, fb.B1, 0, 0, 0, 1 / fb.B1.h, W / 320);
        blur(fb.Bh, fb.T2, 0, 0, 1 / fb.T2.w, 0, W / 160); blur(fb.T2, fb.B2, 0, 0, 0, 1 / fb.B2.h, W / 160);
        pass(prog.fin, null, u => { bind(0, fb.S.t); bind(1, fb.B1.t); bind(2, fb.B2.t); gl.uniform1i(u.uS, 0); gl.uniform1i(u.uB1, 1); gl.uniform1i(u.uB2, 2); gl.uniform2f(u.uSz, bhc.width, bhc.height); });
      },
    };
  })();

  // ---------- Planets: rendered on the GPU into an atlas, then drawn (and lensed) in 2D ----------
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
    // Image of the planet through the lens matrix M (screen axes, Y up). The Doppler brightening
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
  // Images of a point of the orbital plane, seen now. k = 0: direct image; k = 1: the image whose
  // light passes round the hole. Without the table (first frames, or no network) only the
  // unbent direct image is drawn.
  function planeImages(r, ph) {
    if (!PT) { const f = flatP(r, ph); return [{ k: 0, X: f[0], Y: f[1], T: 0, M: [1, 0, 0, 1] }]; }
    const out = []; for (let k = 0; k < 2; k++) { const im = imageOf(k, r, ph); if (im) { im.k = k; out.push(im); } }
    return out;
  }
  const front = ph => Math.cos(ph) >= 0;   // nearer than the hole: drawn over its canvas
  function orbitLine(ctxF, ctxB, p, on, alpha) {
    const { cx, cy, K } = L, col = on ? `rgba(${p.rgb.join(',')},.8)` : `rgba(160,205,255,${alpha})`;
    const pts = []; for (let n = 0; n <= 240; n++) pts.push(polar(ellipsePt(p, tau, n / 240 * TAU2)));
    for (const which of ['f', 'b']) {   // guide lines: direct image only; planets and belt show both
      const ctx = which === 'f' ? ctxF : ctxB, k = which === 's' ? 1 : 0;
      ctx.strokeStyle = which === 's' ? `rgba(160,205,255,${alpha * .7})` : col; ctx.lineWidth = (on ? 1.6 : 1) * dpr; ctx.beginPath();
      let pen = false;
      for (const [r, ph] of pts) {
        let ok = which === 's' || (which === 'f') === front(ph), q = null;
        if (ok) { q = PT ? planeImg(k, r, ph) : k === 0 ? flatP(r, ph) : null; ok = !!q; }
        if (ok) { const x = (cx + q[0] * K) * dpr, y = (cy - q[1] * K) * dpr; pen ? ctx.lineTo(x, y) : ctx.moveTo(x, y); pen = true; } else pen = false;
      }
      ctx.stroke();
    }
  }
  // Planet state for image k: solve for the emission time tau_e, so that light leaving the
  // planet then reaches the camera now (tau_e + T = tau). Three fixed-point steps converge,
  // since the planet moves at under a fifth of the speed of light.
  function planetImage(p, k) {
    let te = tau, im = null, p3 = null, r = 0, ph = 0;
    for (let n = 0; n < 3; n++) {
      p3 = orbit(p, te); [r, ph] = polar(p3);
      if (!PT) { const f = flatP(r, ph); return { k, X: f[0], Y: f[1], M: [1, 0, 0, 1], p3, r, ph }; }
      im = imageOf(k, r, ph); if (!im) return null;
      te = tau - im.T;
    }
    return Object.assign(im, { k, p3, r, ph });
  }
  function draw() {
    const { w, h, cx, cy, K } = L, W = w * dpr, H = h * dpr;
    bx.setTransform(1, 0, 0, 1, 0, 0); fx.setTransform(1, 0, 0, 1, 0, 0);
    bx.fillStyle = '#03040a'; bx.fillRect(0, 0, W, H); fx.clearRect(0, 0, W, H);
    let g = bx.createRadialGradient(cx * dpr, cy * dpr, 0, cx * dpr, cy * dpr, K * 60 * dpr); g.addColorStop(0, 'rgba(255,150,70,.045)'); g.addColorStop(1, 'rgba(0,0,0,0)'); bx.fillStyle = g; bx.fillRect(0, 0, W, H);
    drawStars(t);
    // Planet states: both images, each at its own emission time; lit and Doppler-shifted as the direct image.
    st = PL.map(p => {
      const ims = [planetImage(p, 0), planetImage(p, 1)].filter(Boolean);
      const d = ims[0] || { p3: orbit(p, tau) }, p3 = d.p3;
      return { p3, ims, v: view(p3), frame: frameOf(p3), gain: d.r ? Math.min(2.2, Math.pow(gShift(d.r, d.X), 4)) : 1 };
    });
    renderAtlas(st, t);
    PL.forEach((p, i) => orbitLine(fx, bx, p, i === hover || i === focusI, .13));
    // Belt: each grain on a circular orbit, seen at its own emission time, brightened by the lens
    // magnification and the Doppler factor.
    for (const b of BELT) {
      const om = Om(b.r), ph0 = b.ph + om * tau - phc;
      for (let k = 0; k < (PT ? 2 : 1); k++) {
        let ph = ph0, im = null;
        if (PT) { const c = planeImg(k, b.r, ph); if (!c) continue; ph = ph0 - om * c[2]; im = imageOf(k, b.r, ph); if (!im) continue; }
        else { const f = flatP(b.r, ph); im = { X: f[0], Y: f[1], M: [1, 0, 0, 1] }; }
        const mu = Math.abs(im.M[0] * im.M[3] - im.M[1] * im.M[2]), a = .5 * b.b * Math.min(3, mu * Math.pow(gShift(b.r, im.X), 4));
        if (a < .02) continue;
        const ctx = k === 0 && front(ph) ? fx : bx;
        ctx.fillStyle = `rgba(214,200,182,${Math.min(1, a)})`; ctx.fillRect((cx + im.X * K) * dpr, (cy - im.Y * K) * dpr, 1.3 * dpr, 1.3 * dpr);
      }
    }
    // Planets, farthest first.
    scr = [];
    const order = PL.map((p, i) => i).sort((a, b) => st[a].v[2] - st[b].v[2]);
    for (const i of order) {
      const p = PL[i], S_ = st[i], R = p.R * K, on = i === hover || i === focusI;
      for (const im of S_.ims.slice().reverse()) {
        const per = CAM / (CAM - im.r * Math.cos(im.ph) * SI), M = im.M.map(v => v * per);
        const ctx = im.k === 0 && front(im.ph) ? fx : bx, Re = R * Math.sqrt(Math.abs(M[0] * M[3] - M[1] * M[2]));
        if (im.k === 0) glow(ctx, p, im.X, im.Y, Re, on);
        drawPlanet(ctx, i, p, im.X, im.Y, M);
        if (im.k === 0) scr[i] = { x: cx + im.X * K, y: cy - im.Y * K, R: Re };
      }
      if (!scr[i]) { scr[i] = { x: -999, y: -999, R: 0 }; }
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
