// The hero sky: a spinning (Kerr) black hole with five planets, an asteroid belt and a star field,
// all on one clock and one distance scale. Units are G = c = M = 1 (M is the hole's mass). The
// hole is taken as 1e8 solar masses (M = 1.48e8 km, 493 s), so every planet orbits outside its
// Roche limit (a gas giant would be torn apart inside about 6 M). The hole and its disc are ray
// traced exactly; the planets, belt and orbit lines are drawn without the bending of their light,
// and the planets far larger than they would be.
(function () {
  'use strict';
  const S = window.SITE;
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
    const APO = Math.max(...PL.map(p => p.a * (1 + p.e)));
    let cx = w * .5, cy = h * .5, K;
    if (mob) { K = Math.min((w - 16) / (2 * (APO + 3)), h / (2 * 17)); cy = h * .42; } // every planet stays on a phone screen; the hole sits high enough to show on the first screen
    else {
      const free = S.rtl ? IR.l - 16 : w - IR.r - 16;
      K = Math.max(5, Math.min(h * .86 / (2 * 19), free / (2 * APO + 4)));
      cx = S.rtl ? IR.l - 8 - (APO + 2) * K : IR.r + 8 + (APO + 2) * K;
    }
    K = Math.max(.5, K);   // a hidden or collapsed pane can report no width or height
    for (const c of [bg, fg, sc]) { c.width = Math.round(w * dpr); c.height = Math.round(h * dpr); }
    L = { w, h, cx, cy, K, mob };
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
    return [...Array(n)].map(() => { const m = Math.pow(r(), 3.2); return { x: (r() * 2 - 1) * hx, y: (r() * 2 - 1) * hy, hx, hy, m, c: bbTint(3200 + r() * 9000) }; });
  }
  function drawStars(t) {
    const { cx, cy, K } = L, drift = t * SKYV, bx = sx;
    bx.clearRect(0, 0, sc.width, sc.height);
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

  // ---------- Black hole: every pixel traced on the GPU, with a tracer grown from the one in Isaac ----------
  // Kerr hole with spin A, thin disc from the prograde ISCO to 15 M, camera CAM away at inclination INC.
  // Each ray carries its constants of motion (L, Carter constant Q) from the camera and is integrated in
  // Boyer-Lindquist coordinates and Mino time: r and theta as second-order equations, phi from its first
  // integral. After every step the radial and polar velocities are projected back onto the null cone, so
  // drift cannot fake a turning point. The ray stops when it falls through the horizon, crosses the disc
  // between its edges, or escapes. Disc light: gas on prograde circular orbits, observed as g^4 F with F
  // = (1 - sqrt(rIn/r)) / r^3 the thin-disc flux profile and a black-body colour shifted by g (redshift, frame dragging and Doppler shift).
  // The rays do not depend on time, so they are traced once (a band of rows per frame) into two
  // textures: the light of the smooth disc, and where each ray met the disc (r and azimuth). Every
  // frame a second, cheap pass lays clumps of gas over the disc that orbit at the Kepler rate
  // Omega = 1/(r^1.5 + A) on the site clock, so the inner edge laps in about 0.7 s and the outer in 9 s.
  // Clumps are sheared by the differential rotation and fade after a short life, as turbulence does.
  const BH = (function () {
    const D = { HW: 26, HH: 16.25, rIn: ISCO, rOut: 15 };
    let gl = null, prog = null, cprog = null, u = {}, cu = {}, ok = false, rect = null, row = 0, rows = 0, ready = false;
    let fb = null, tC = null, tG = null, hd = 1, lite = 0;
    const VS = '#version 300 es\nin vec2 p;void main(){gl_Position=vec4(p,0.,1.);}';
    const FS = `#version 300 es
precision highp float;
uniform vec2 uOrig;uniform float uPix,uCam,uInc,uRin,uRout,uA;
layout(location=0) out vec4 o;layout(location=1) out vec4 og;
vec3 blackbody(float T){T=clamp(T,1000.,40000.)/100.;vec3 c;
 if(T<=66.){c.r=1.;c.g=clamp((99.4708025861*log(T)-161.1195681661)/255.,0.,1.);
  c.b=T<=19.?0.:clamp((138.5177312231*log(T-10.)-305.0447927307)/255.,0.,1.);}
 else{c.r=clamp(329.698727446*pow(T-60.,-.1332047592)/255.,0.,1.);c.g=clamp(288.1221695283*pow(T-60.,-.0755148492)/255.,0.,1.);c.b=1.;}
 c=pow(c,vec3(2.2));return c/max(dot(c,vec3(.2126,.7152,.0722)),1e-4);}
vec2 hit;
// Right-hand side of the Kerr geodesic equations (see trace).
void der(float R_,float T_,float U_,float W_,out float dr,out float dt,out float du,out float dw,out float dp,float a,float a2,float L,float K){
 float sn=sin(T_),cs=cos(T_);sn=abs(sn)<1e-3?(sn<0.?-1e-3:1e-3):sn;float,Pp=R_*R_+a2-a*L,Dd=R_*R_-2.*R_+a2;
 dr=U_;dt=W_;du=2.*R_*Pp-(R_-1.)*K;dw=-a2*cs*sn+L*L*cs/(sn*sn*sn);dp=a*Pp/max(Dd,1e-4)+L/(sn*sn)-a;}
vec4 trace(vec2 S){
 // Kerr null geodesic in Boyer-Lindquist coordinates, Mino time, energy 1. From the screen point
 // (alpha, beta) at the hole: L = -alpha sin(th0), Carter Q = beta^2 + (alpha^2 - a^2) cos^2(th0).
 // r and theta follow d2r/dl2 = R'(r)/2 and d2th/dl2 = Th'(th)/2, so turning points need no care.
 hit=vec2(0.);
 float a=uA,a2=a*a,th0=uInc,s0=sin(th0),c0=cos(th0);
 S.x=abs(S.x)<2e-3?2e-3:S.x;   // rays with L = 0 pass over the pole, where the coordinates break down
 float L=-S.x*s0,Q=S.y*S.y+(S.x*S.x-a2)*c0*c0,K=Q+(L-a)*(L-a);
 float r=uCam,th=th0,ph=0.;
 float P0=r*r+a2-a*L,D0=r*r-2.*r+a2;
 float vr=-sqrt(max(P0*P0-D0*K,0.)),vt=-sign(S.y)*sqrt(max(Q+a2*c0*c0-L*L*c0*c0/(s0*s0),0.));
 float rh=1.+sqrt(1.-a2);
 for(int i=0;i<2400;i++){
  float h=.035/(r+1.)*clamp(abs(sin(th))*8.,.01,1.);   // finer steps close to the poles
  // RK4 on (r, th, vr, vt, ph)
  float r1=r,t1=th,u1=vr,w1=vt;
  float k1r,k1t,k1u,k1w,k1p,k2r,k2t,k2u,k2w,k2p,k3r,k3t,k3u,k3w,k3p,k4r,k4t,k4u,k4w,k4p;
  der(r1,t1,u1,w1,k1r,k1t,k1u,k1w,k1p,a,a2,L,K);
  der(r1+.5*h*k1r,t1+.5*h*k1t,u1+.5*h*k1u,w1+.5*h*k1w,k2r,k2t,k2u,k2w,k2p,a,a2,L,K);
  der(r1+.5*h*k2r,t1+.5*h*k2t,u1+.5*h*k2u,w1+.5*h*k2w,k3r,k3t,k3u,k3w,k3p,a,a2,L,K);
  der(r1+h*k3r,t1+h*k3t,u1+h*k3u,w1+h*k3w,k4r,k4t,k4u,k4w,k4p,a,a2,L,K);
  float rp=r,tp=th,pp=ph;
  r+=h/6.*(k1r+2.*k2r+2.*k3r+k4r);th+=h/6.*(k1t+2.*k2t+2.*k3t+k4t);
  vr+=h/6.*(k1u+2.*k2u+2.*k3u+k4u);vt+=h/6.*(k1w+2.*k2w+2.*k3w+k4w);ph+=h/6.*(k1p+2.*k2p+2.*k3p+k4p);
  // Keep the speeds on the null cone: vr^2 = R(r), vt^2 = Th(th), away from turning points. Without
  // this, tiny relative errors made far out grow into false turning points near the hole.
  {float Pp=r*r+a2-a*L,Rr=Pp*Pp-(r*r-2.*r+a2)*K;if(Rr>0.)vr=sign(vr)*sqrt(Rr);
   float sn=sin(th),cs=cos(th),Tt=Q+a2*cs*cs-L*L*cs*cs/max(sn*sn,1e-6);if(Tt>0.)vt=sign(vt)*sqrt(Tt);}
  if(r<=rh*1.01)return vec4(0.,0.,0.,1.);
  if(cos(tp)*cos(th)<0.){float f=cos(tp)/(cos(tp)-cos(th)),rx=mix(rp,r,f);
   if(rx>uRin&&rx<uRout){
    float sq=sqrt(rx),Om=1./(rx*sq+a),ut=(rx*sq+a)/(pow(rx,.75)*sqrt(max(rx*sq-3.*sq+2.*a,1e-4)));
    float g=1./(ut*(1.-Om*L)*sqrt(1.-2./uCam));
    float fl=max(0.,1.-sqrt(uRin/rx))/(rx*rx*rx),rq=49./36.*uRin,lv=fl/((1./7.)/(rq*rq*rq));
    hit=vec2(rx,mix(pp,ph,f));
    return vec4(min(blackbody(4700.*pow(lv,.25)*g)*pow(g,4.)*pow(lv,.7)*.625,vec3(1.)),1.);}}   // brightness shown with a softer curve (exposure), colour from the true temperature
  if(r>uCam*1.05&&vr>0.)return vec4(0.);
 }
 return vec4(0.);}
vec2 pk(float x){x=clamp(x,0.,1.)*65535.;float hi=floor(x/256.);return vec2(hi,x-hi*256.)/255.;}
void main(){vec4 a=vec4(0.);vec2 g0=vec2(0.);
 for(int j=0;j<2;j++)for(int i=0;i<2;i++){a+=trace(uOrig+(gl_FragCoord.xy+vec2(.25+.5*float(i),.25+.5*float(j))-.5)*uPix);if(i+j==0)g0=hit;}
 o=a*.25;   // stored at half brightness, so the clumps can brighten or dim it before it is clipped
 // Where the first sample met the disc: r (0 = it did not) and azimuth, 16 bits each.
 og=g0.x>0.?vec4(pk((g0.x-1.)/15.),pk(fract(g0.y/6.2831853))):vec4(0.);}`;
    const CS = `#version 300 es
precision highp float;
uniform sampler2D uC,uG;uniform float uTau,uLite;out vec4 o;
float hs(vec3 p){p=fract(p*.3183099+.1);p*=17.;return fract(p.x*p.y*p.z*(p.x+p.y+p.z));}
float vn(vec3 x){vec3 i=floor(x),f=fract(x);f=f*f*(3.-2.*f);
 return mix(mix(mix(hs(i),hs(i+vec3(1,0,0)),f.x),mix(hs(i+vec3(0,1,0)),hs(i+vec3(1,1,0)),f.x),f.y),
            mix(mix(hs(i+vec3(0,0,1)),hs(i+vec3(1,0,1)),f.x),mix(hs(i+vec3(0,1,1)),hs(i+vec3(1,1,1)),f.x),f.y),f.z)*2.-1.;}
// Gas in one generation of clumps, born at clock time tb and seen lt later: a clump now at azimuth a
// was at a - Omega lt. Long along the orbit, thin across it.
float gas(float r,float a,float lt,float id){float b=a-lt/(pow(r,1.5)+${A.toFixed(3)});vec3 q=vec3(cos(b)*r*.4,sin(b)*r*.4,r*1.1)+id*vec3(7.13,3.71,11.9);
 float n=vn(q);if(uLite<.5)n=.62*n+.38*vn(q*2.1+vec3(5.2));return n;}
void main(){ivec2 p=ivec2(gl_FragCoord.xy);vec4 c=texelFetch(uC,p,0),g=texelFetch(uG,p,0);
 float rn=(g.x*256.+g.y)*255./65535.;
 if(rn<=0.){o=vec4(min(2.*c.rgb,vec3(c.a)),c.a);return;}
 float r=rn*15.+1.,a=(g.z*256.+g.w)*255./65535.*6.2831853;
 // Two overlapping generations of clumps, each living P = 24 M (0.6 s), faded in and out so that
 // their sum keeps the same contrast. P is the same at every radius: a lifetime that changed with r
 // would put the generation boundaries ever closer together in r as the clock runs.
 float P=24.,s=0.,w2=0.;
 for(int k=0;k<2;k++){float tk=uTau+float(k)*.5*P,cy=floor(tk/P),lt=tk-cy*P,w=1.-abs(2.*lt/P-1.);
  s+=w*gas(r,a,lt,cy*2.+float(k));w2+=w*w;}
 float m=max(.25,1.+.42*s/sqrt(max(w2,1e-3)));
 o=vec4(min(2.*c.rgb*m,vec3(c.a)),c.a);}`;
    function init() {
      try {
        gl = bhc.getContext('webgl2', { premultipliedAlpha: true, antialias: false, alpha: true });
        if (!gl) return false;
        const sh = (t, s) => { const x = gl.createShader(t); gl.shaderSource(x, s); gl.compileShader(x); if (!gl.getShaderParameter(x, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(x)); return x; };
        const mk = fs => { const p = gl.createProgram(); gl.attachShader(p, sh(gl.VERTEX_SHADER, VS)); gl.attachShader(p, sh(gl.FRAGMENT_SHADER, fs)); gl.bindAttribLocation(p, 0, 'p'); gl.linkProgram(p); if (!gl.getProgramParameter(p, gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(p)); return p; };
        prog = mk(FS); cprog = mk(CS);
        ['uOrig', 'uPix', 'uCam', 'uInc', 'uRin', 'uRout', 'uA'].forEach(n => u[n] = gl.getUniformLocation(prog, n));
        ['uC', 'uG', 'uTau', 'uLite'].forEach(n => cu[n] = gl.getUniformLocation(cprog, n));
        fb = gl.createFramebuffer();
      } catch (e) { console.warn(e); gl = null; return false; }
      const b = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, b);
      gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
      gl.enableVertexAttribArray(0); gl.vertexAttribPointer(0, 2, gl.FLOAT, false, 0, 0);
      ok = true; return true;
    }
    function tex(w, h) {
      const t = gl.createTexture(); gl.bindTexture(gl.TEXTURE_2D, t);
      gl.texStorage2D(gl.TEXTURE_2D, 1, gl.RGBA8, w, h);
      for (const k of [gl.TEXTURE_MIN_FILTER, gl.TEXTURE_MAG_FILTER]) gl.texParameteri(gl.TEXTURE_2D, k, gl.NEAREST);
      for (const k of [gl.TEXTURE_WRAP_S, gl.TEXTURE_WRAP_T]) gl.texParameteri(gl.TEXTURE_2D, k, gl.CLAMP_TO_EDGE);
      return t;
    }
    return {
      init,
      get ok() { return ok; },
      get done() { return ready; },
      set lite(v) { lite = v; },
      place(L, d) {
        hd = d;
        const w = 2 * D.HW * L.K, h = 2 * D.HH * L.K;
        rect = { x: L.cx - w / 2, y: L.cy - h / 2, w, h };
        for (const el of [bhc, still]) { if (!el) continue; Object.assign(el.style, { left: rect.x + 'px', top: rect.y + 'px', width: w + 'px', height: h + 'px' }); }
        const W = Math.max(1, Math.round(w * hd)), H = Math.max(1, Math.round(h * hd));
        row = 0; rows = H; ready = false;
        if (!gl) return;
        if (bhc.width !== W || bhc.height !== H || !tC) {
          bhc.width = W; bhc.height = H;
          if (tC) { gl.deleteTexture(tC); gl.deleteTexture(tG); }
          tC = tex(W, H); tG = tex(W, H);
          gl.bindFramebuffer(gl.FRAMEBUFFER, fb);
          gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, tC, 0);
          gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT1, gl.TEXTURE_2D, tG, 0);
          gl.drawBuffers([gl.COLOR_ATTACHMENT0, gl.COLOR_ATTACHMENT1]);
          gl.viewport(0, 0, W, H); gl.disable(gl.SCISSOR_TEST); gl.clearColor(0, 0, 0, 0); gl.clear(gl.COLOR_BUFFER_BIT);
          gl.bindFramebuffer(gl.FRAMEBUFFER, null);
        } else row = rows;   // same size: the rays have not changed, keep them
        if (row >= rows) ready = true;
      },
      // Trace the next band of rows (until done), then shade the disc for clock time tau.
      draw(tau) {
        if (!ok || !rect) return false;
        const W = bhc.width, H = bhc.height;
        if (!ready) {
          const band = Math.max(8, Math.round(H / 24));
          gl.bindFramebuffer(gl.FRAMEBUFFER, fb); gl.useProgram(prog); gl.viewport(0, 0, W, H);
          gl.enable(gl.SCISSOR_TEST); gl.scissor(0, row, W, Math.min(band, rows - row));
          const pix = 2 * D.HW / W;   // M per device pixel
          gl.uniform2f(u.uOrig, -D.HW, -H * pix / 2); gl.uniform1f(u.uPix, pix);
          gl.uniform1f(u.uCam, CAM); gl.uniform1f(u.uInc, INC); gl.uniform1f(u.uRin, D.rIn); gl.uniform1f(u.uRout, D.rOut); gl.uniform1f(u.uA, A);
          gl.drawArrays(gl.TRIANGLES, 0, 3); gl.disable(gl.SCISSOR_TEST);
          gl.bindFramebuffer(gl.FRAMEBUFFER, null);
          row += band;
          if (row >= rows) ready = true;
        }
        gl.useProgram(cprog); gl.viewport(0, 0, W, H);
        gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, tC);
        gl.activeTexture(gl.TEXTURE1); gl.bindTexture(gl.TEXTURE_2D, tG);
        gl.uniform1i(cu.uC, 0); gl.uniform1i(cu.uG, 1); gl.uniform1f(cu.uTau, tau % 1e6); gl.uniform1f(cu.uLite, lite);
        gl.drawArrays(gl.TRIANGLES, 0, 3);
        if (ready && !bhc.classList.contains('on')) { bhc.classList.add('on'); }
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
    const need = Math.min(QUAL[q].tile, Math.max(...PL.map(p => Math.ceil(2 * ext(p) * p.R * L.K * dpr))));
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
  function orbitLine(ctxF, ctxB, p, on, alpha) {
    const { cx, cy, K } = L, col = on ? `rgba(${p.rgb.join(',')},.8)` : `rgba(160,205,255,${alpha})`;
    const pts = []; for (let n = 0; n <= 240; n++) pts.push(polar(ellipsePt(p, tau, n / 240 * TAU2)));
    for (const which of ['f', 'b']) {   // the near half over the hole, the far half behind it
      const ctx = which === 'f' ? ctxF : ctxB;
      ctx.strokeStyle = col; ctx.lineWidth = (on ? 1.6 : 1) * dpr; ctx.beginPath();
      let pen = false;
      for (const [r, ph] of pts) {
        if ((which === 'f') === front(ph)) { const v = flatP(r, ph), x = (cx + v[0] * K) * dpr, y = (cy - v[1] * K) * dpr; pen ? ctx.lineTo(x, y) : ctx.moveTo(x, y); pen = true; } else pen = false;
      }
      ctx.stroke();
    }
  }
  // Planet position on screen now, as seen without the bending of light: the orbits stay flat.
  function planetImage(p) {
    const p3 = orbit(p, tau), [r, ph] = polar(p3), f = flatP(r, ph);
    return { X: f[0], Y: f[1], X0: f[0], M: [1, 0, 0, 1], k: 1, p3, r, ph };
  }
  function draw() {
    const { w, h, cx, cy, K } = L, W = w * dpr, H = h * dpr;
    bx.setTransform(1, 0, 0, 1, 0, 0); fx.setTransform(1, 0, 0, 1, 0, 0);
    bx.fillStyle = '#03040a'; bx.fillRect(0, 0, W, H); fx.clearRect(0, 0, W, H);
    let g = bx.createRadialGradient(cx * dpr, cy * dpr, 0, cx * dpr, cy * dpr, K * 60 * dpr); g.addColorStop(0, 'rgba(255,150,70,.045)'); g.addColorStop(1, 'rgba(0,0,0,0)'); bx.fillStyle = g; bx.fillRect(0, 0, W, H);
    if (starT < 0 || t - starT > .25 || t < starT) { drawStars(t); starT = t; }
    bx.drawImage(sc, 0, 0);
    // Planet states, lit and Doppler-shifted.
    st = PL.map(p => {
      const d = planetImage(p), p3 = d.p3;
      return { p3, im: d, v: view(p3), frame: frameOf(p3), gain: Math.min(2.2, Math.pow(gShift(d.r, d.X0), 4)) };
    });
    renderAtlas(st, t);
    PL.forEach((p, i) => orbitLine(fx, bx, p, i === hover || i === focusI, .13));
    // Belt: each grain on a circular orbit, brightened by the Doppler factor.
    // Grains are batched by brightness into eight paths per layer, one fill each.
    const NB = 8, gs = 1.3 * dpr, bk = [[], []];
    for (let n = 0; n < NB; n++) { bk[0].push([]); bk[1].push([]); }
    for (let j = 0, step = QUAL[q].belt; j < BELT.length; j += step) {
      const b = BELT[j], ph = b.ph + Om(b.r) * tau - phc, v = flatP(b.r, ph), a = .5 * b.b * Math.min(3, Math.pow(gShift(b.r, v[0]), 4));
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
      const p = PL[i], S_ = st[i], R = p.R * K, on = i === hover || i === focusI;
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
      const lw = lb._w[k_] || 80, left = s_.x + s_.R + 8 + lw > L.w - 4;
      const lxp = left ? s_.x - s_.R - 8 - lw : s_.x + s_.R + 8;
      lb._x = Math.max(4, lxp); lb._y = s_.y; lb._lw = lw;
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
    draw();   // after any resize in layout(), so a cleared canvas is never shown
  }
  // The still picture of the hole stands in only where WebGL 2 is missing; otherwise the sky shows
  // stars and planets at once and the traced hole fades in when it is ready (a fraction of a second).
  if (!BH.init() && still) still.classList.add('on');
  layout();
  if (document.fonts) document.fonts.ready.then(() => { [...labs.children].forEach(b => b._w = null); });
  let rz; addEventListener('resize', () => { clearTimeout(rz); rz = setTimeout(() => { layout(); if (visible && active) draw(); }, 120); });
  requestAnimationFrame(loop);
  window.SKY = {
    get quality() { return q; },
    // Stop (or restart) the sky while a project is open. The planet being flown to is drawn by the
    // landing view instead, so the sky draws one last frame without it.
    setActive(v, i) { hideI = v ? -1 : (i == null ? -1 : i); if (L && L.w >= 2) draw(); active = v; },
    planet(i) { const s = scr[i], r = sky.getBoundingClientRect(); return s ? { x: r.left + s.x, y: r.top + s.y, R: s.R, rot: st[i].frame.rot, L: st[i].frame.L, gain: st[i].gain } : null; },
    orbitInfo(i) { const p = PL[i]; return { a: p.a, period: 2 * Math.PI / p.O / RATE, days: 2 * Math.PI / p.O * 492.6 / 86400 }; },
    planets: PL, KIND,
  };
})();
