// The black hole of the hero sky: every pixel traced on the GPU, with a tracer grown from the one in Isaac.
// sky.js runs this file as a worker and hands it the hole's canvas (OffscreenCanvas), so setting up
// WebGL, compiling the shaders and tracing never hold up the page. Where a worker cannot draw WebGL 2,
// sky.js loads it as a plain script instead and calls self.BHmake on the page.
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
(function (G) {
  'use strict';
  // cv: the canvas (an OffscreenCanvas in the worker); A: spin; CAM: camera distance (M); INC: inclination; ISCO.
  function make(cv, A, CAM, INC, ISCO) {
    const D = { HW: 26, HH: 16.25, rIn: ISCO, rOut: 15 };
    let gl = null, par = null, prog = null, cprog = null, u = {}, cu = {}, ok = false, failed = false, row = 0, rows = 0, ready = false;
    let fb = null, tC = null, tG = null, nb = 8, tB = 0;
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
    // Set up in three short steps, each in its own task: the WebGL context, the hole's tracing
    // program, then the disc program and the buffers. Both programs are handed to the driver and
    // checked in link(), once the driver reports them compiled (KHR_parallel_shader_compile).
    // done(true) once all is in place, done(false) without WebGL 2.
    function init(done) {
      let g = null, p1 = null;
      const sh = (t, s) => { const x = g.createShader(t); g.shaderSource(x, s); g.compileShader(x); return x; };
      const mk = fs => { const p = g.createProgram(); g.attachShader(p, sh(g.VERTEX_SHADER, VS)); g.attachShader(p, sh(g.FRAGMENT_SHADER, fs)); g.bindAttribLocation(p, 0, 'p'); g.linkProgram(p); return p; };
      const fail = e => { if (e) console.warn(e); gl = null; failed = true; done(false); };
      const step3 = () => { try {
        cprog = mk(CS); prog = p1; fb = g.createFramebuffer();
        const b = g.createBuffer(); g.bindBuffer(g.ARRAY_BUFFER, b);
        g.bufferData(g.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), g.STATIC_DRAW);
        g.enableVertexAttribArray(0); g.vertexAttribPointer(0, 2, g.FLOAT, false, 0, 0);
        gl = g; done(true);
      } catch (e) { fail(e); } };
      const step2 = () => { try { par = g.getExtension('KHR_parallel_shader_compile'); p1 = mk(FS); setTimeout(step3, 0); } catch (e) { fail(e); } };
      setTimeout(() => { try { g = cv.getContext('webgl2', { premultipliedAlpha: true, antialias: false, alpha: true }); if (!g) return fail(); setTimeout(step2, 0); } catch (e) { fail(e); } }, 0);
    }
    function link() {
      if (!gl || ok) return;
      if (par && !(gl.getProgramParameter(prog, par.COMPLETION_STATUS_KHR) && gl.getProgramParameter(cprog, par.COMPLETION_STATUS_KHR))) return;
      for (const p of [prog, cprog]) if (!gl.getProgramParameter(p, gl.LINK_STATUS)) {
        console.warn(gl.getProgramInfoLog(p) || gl.getShaderInfoLog(gl.getAttachedShaders(p)[1]));
        gl = null; failed = true; return;
      }
      ['uOrig', 'uPix', 'uCam', 'uInc', 'uRin', 'uRout', 'uA'].forEach(n => u[n] = gl.getUniformLocation(prog, n));
      ['uC', 'uG', 'uTau', 'uLite'].forEach(n => cu[n] = gl.getUniformLocation(cprog, n));
      ok = true;
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
      get ready() { return ready; },
      get failed() { return failed; },
      // The canvas is W x H device pixels. A new size starts the trace again; the same size keeps the rows traced so far.
      place(W, H) {
        const done = row;
        row = 0; rows = H; ready = false; nb = Math.round(H / 24); tB = 0;
        if (!gl) return;
        if (cv.width !== W || cv.height !== H || !tC) {
          cv.width = W; cv.height = H;
          if (tC) { gl.deleteTexture(tC); gl.deleteTexture(tG); }
          tC = tex(W, H); tG = tex(W, H);
          gl.bindFramebuffer(gl.FRAMEBUFFER, fb);
          gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, tC, 0);
          gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT1, gl.TEXTURE_2D, tG, 0);
          gl.drawBuffers([gl.COLOR_ATTACHMENT0, gl.COLOR_ATTACHMENT1]);
          gl.viewport(0, 0, W, H); gl.disable(gl.SCISSOR_TEST); gl.clearColor(0, 0, 0, 0); gl.clear(gl.COLOR_BUFFER_BIT);
          gl.bindFramebuffer(gl.FRAMEBUFFER, null);
        } else row = done;
        if (row >= rows) ready = true;
      },
      // Trace the next band of rows (until done), then shade the disc for clock time tau.
      draw(tau, lite) {
        link();
        if (!ok || !tC) return;
        const W = cv.width, H = cv.height;
        if (!ready) {
          // Bands start at 1/24 of the rows and double while frames stay quick, so a fast GPU is done
          // in a few frames and a slow one never gets a long frame.
          const now = performance.now(), dt = tB ? now - tB : 99; tB = now;
          if (dt < 20 && row > 0) nb = Math.min(rows, nb * 2);
          const band = Math.max(8, nb);
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
      },
    };
  }
  if (typeof document === 'undefined') {
    // Worker: sky.js sends the canvas once, then the size on every layout and the clock on every frame.
    // The state goes back only when it changes.
    let bh = null, size = null, was = '';
    const report = () => { const s = [bh.ok, bh.ready, bh.failed].join(); if (s !== was) { was = s; postMessage({ ok: bh.ok, ready: bh.ready, failed: bh.failed }); } };
    onmessage = e => {
      const m = e.data;
      if (m.size) size = m.size;
      if (m.canvas) {
        bh = make(m.canvas, m.k[0], m.k[1], m.k[2], m.k[3]);
        bh.init(ok => { if (ok && size) bh.place(size[0], size[1]); report(); });
        return;
      }
      if (!bh) return;
      if (m.size) bh.place(size[0], size[1]);
      if (m.tau !== undefined) bh.draw(m.tau, m.lite);
      report();
    };
  } else G.BHmake = make;
})(self);
