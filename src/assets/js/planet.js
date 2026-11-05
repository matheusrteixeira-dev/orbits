// Procedural planets, ray-cast on the GPU (WebGL2). One shader draws the small planets in the
// sky (orthographic tiles) and the full-screen landing view (perspective camera), so a planet
// looks the same from orbit and from low altitude.
(function () {
  'use strict';
  const VS = `#version 300 es
in vec2 p;void main(){gl_Position=vec4(p,0.,1.);}`;
  const FS = `#version 300 es
precision highp float;precision highp int;
uniform vec4 uVp;uniform int uOrtho;uniform float uExt;
uniform vec3 uCam;uniform mat3 uCamM;uniform float uTanF;
uniform mat3 uRot;uniform vec3 uL;uniform vec3 uCol;uniform int uKind;
uniform vec3 uSite;uniform float uTime,uGlow,uSeed,uBg,uGain;
out vec4 o;
uvec3 pcg(uvec3 v){v=v*1664525u+1013904223u;v.x+=v.y*v.z;v.y+=v.z*v.x;v.z+=v.x*v.y;v^=v>>16u;v.x+=v.y*v.z;v.y+=v.z*v.x;v.z+=v.x*v.y;return v;}
float h3(vec3 p){return float(pcg(uvec3(ivec3(floor(p))+32768)).x)*(1./4294967295.);}
float vn(vec3 p){vec3 i=floor(p),f=fract(p),u=f*f*(3.-2.*f);
 return mix(mix(mix(h3(i),h3(i+vec3(1,0,0)),u.x),mix(h3(i+vec3(0,1,0)),h3(i+vec3(1,1,0)),u.x),u.y),
            mix(mix(h3(i+vec3(0,0,1)),h3(i+vec3(1,0,1)),u.x),mix(h3(i+vec3(0,1,1)),h3(i+vec3(1,1,1)),u.x),u.y),u.z);}
float fbm(vec3 p,int n){float s=0.,a=.5,w=0.;for(int k=0;k<10;k++){if(k>=n)break;s+=a*vn(p);w+=a;p=p*2.03+vec3(1.7,9.2,3.1);a*=.5;}return s/w;}
// Surface colour and emission in the planet's own frame (z = spin axis, x = facing the hole).
void surf(vec3 q,int n,float night,out vec3 base,out vec3 emis,out float wet){
 emis=vec3(0);wet=0.;vec3 c=uCol;float lat=q.z;
 if(uKind==0){ // rocky, volcanic
  float h=fbm(q*2.6+uSeed,n),r=1.-abs(2.*fbm(q*5.3+3.1,max(n-1,1))-1.);
  base=mix(vec3(.10,.055,.05),c*.55+vec3(.05,.02,.01),smoothstep(.38,.66,h));
  base=mix(base,vec3(.74,.60,.50),smoothstep(.6,.78,h)*.55);
  emis=vec3(1.,.36,.1)*smoothstep(.9,.985,r)*smoothstep(.56,.4,h)*(.35+1.4*night);
 }else if(uKind==1){ // ocean world
  float h=fbm(q*2.1+uSeed,n),land=smoothstep(.535,.55,h);
  vec3 wat=mix(vec3(.01,.035,.13),c*.55,smoothstep(.25,.53,h));
  vec3 gr=mix(vec3(.12,.23,.09),vec3(.55,.47,.32),smoothstep(.56,.72,h));
  base=mix(wat,gr,land);wet=1.-land;
  base=mix(base,vec3(.93,.96,1.),smoothstep(.8,.86,abs(lat)+.05*h));
  float cl=fbm(q*3.2+vec3(uTime*.004,0,0),max(n-1,1));base=mix(base,vec3(.94,.96,1.),smoothstep(.56,.76,cl)*.85);
 }else if(uKind==2){ // banded gas giant
  vec3 wq=q*vec3(1.,1.,3.2);float w=fbm(wq*1.6+uSeed,n),w2=fbm(wq*4.2+vec3(w*2.),n);float b=sin(lat*21.+w*6.+w2*2.5);
  base=mix(vec3(.40,.23,.07),c,.5+.5*b);base=mix(base,vec3(.98,.92,.78),smoothstep(.55,.8,w2)*.45);base*=.82+.3*fbm(q*11.,n);
 }else if(uKind==3){ // storm world: swirls from domain-warped noise
  vec3 p1=q*1.8+uSeed;vec3 wv=vec3(fbm(p1,max(n-2,2)),fbm(p1+5.2,max(n-2,2)),fbm(p1+9.1,max(n-2,2)));
  float w=fbm(q*3.+wv*3.,n);float b=sin(lat*9.+w*9.);
  base=mix(vec3(.07,.025,.15),c*.9,.5+.45*b);base=mix(base,vec3(.88,.8,1.),smoothstep(.6,.8,w)*.5);base*=.8+.35*fbm(q*12.+wv,n);
  float f=h3(floor(q*7.)+vec3(0,0,floor(uTime*3.)*17.+uSeed));
  emis=vec3(.75,.7,1.)*step(.992,f)*night*2.;
 }else{ // ice world with aurorae
  float h=fbm(q*3.+uSeed,n),r=1.-abs(2.*fbm(q*6.+2.,max(n-1,1))-1.);
  base=mix(vec3(.62,.78,.84),vec3(.95,.98,1.),h);base=mix(base,c*.55,smoothstep(.88,.97,r)*.8);
  float au=smoothstep(.12,0.,abs(abs(lat)-.82+.05*sin(atan(q.y,q.x)*5.+uTime*.3)));
  emis=c*au*(.25+1.3*night)*(.6+.4*fbm(q*9.+vec3(0,0,uTime*.05),2));
 }
}
// The project's site: a lit settlement around a landing ring, in the project's colour.
vec3 site(vec3 q,float fp){
 float d=acos(clamp(dot(q,uSite),-1.,1.));
 vec3 t1=normalize(cross(uSite,abs(uSite.z)<.9?vec3(0,0,1):vec3(1,0,0))),t2=cross(uSite,t1);
 vec2 u=vec2(dot(q,t1),dot(q,t2));
 vec3 e=uCol*exp(-d*d/(.05*.05))*.35;
 float aa=max(fp,1e-5);
 float ring=smoothstep(aa*1.5,0.,abs(d-.02))+smoothstep(aa*1.5,0.,abs(d-.034))*.6+smoothstep(.006+aa,.004,d);
 e+=uCol*ring*(1.2+2.2*uGlow);
 vec2 g=u/.0035;vec2 ci=floor(g);float rn=h3(vec3(ci,uSeed+5.));
 vec2 pt=ci+.5+.35*(vec2(h3(vec3(ci,uSeed+9.)),h3(vec3(ci,uSeed+13.)))-.5)*2.;
 float dens=smoothstep(.13,.02,d)*(.35+.65*smoothstep(.1,.03,d));
 float lit=step(rn,dens*.5)*(.35+.65*h3(vec3(ci,uSeed+21.)));float dd=length(g-pt);
 vec3 lc=mix(vec3(1.,.82,.55),uCol,.35);
 e+=lc*lit*exp(-dd*dd*30.)*1.8*smoothstep(.0012,.00035,aa);
 e+=lc*dens*.5*smoothstep(.0004,.002,aa);
 return e;
}
void main(){
 vec2 fc=gl_FragCoord.xy-uVp.xy;vec2 nd=(fc-.5*uVp.zw)/(.5*uVp.w);
 vec3 ro,rd;float pix;
 if(uOrtho==1){ro=vec3(nd*uExt,10.);rd=vec3(0,0,-1);pix=2.*uExt/uVp.w;}
 else{ro=uCam;rd=normalize(uCamM*vec3(nd*uTanF,-1.));pix=2.*uTanF/uVp.w;}
 float b=dot(ro,rd),c=dot(ro,ro)-1.,D=b*b-c;
 vec4 col=vec4(0);float tS=1e9;
 if(D>0.){
  float t=-b-sqrt(D);
  if(t>0.){
   tS=t;vec3 p=ro+rd*t,n=p,q=transpose(uRot)*n;
   float fp=pix*t;int oc=int(clamp(log2(.5/(3.*fp)),2.,9.));
   float ndl0=dot(n,uL),night=1.-smoothstep(-.05,.25,ndl0);
   if(uKind==0||uKind==1||uKind==4){ // relief: perturb the normal with the height field's gradient
    float ep=max(fp*1.5,4e-4),fq=uKind==0?2.6:uKind==1?2.1:3.;int ob=max(oc-1,2);
    vec3 t1=normalize(cross(q,abs(q.z)<.9?vec3(0,0,1):vec3(1,0,0))),t2=cross(q,t1);
    float h0=fbm(q*fq+uSeed,ob),hx=fbm((q+t1*ep)*fq+uSeed,ob),hy=fbm((q+t2*ep)*fq+uSeed,ob);
    float k=(uKind==0?.9:uKind==1?.5*smoothstep(.53,.56,h0):.35)*ep/max(ep,1e-4);
    vec3 g=(t1*(hx-h0)+t2*(hy-h0))/ep;
    n=normalize(n-uRot*(g*k*.06));
   }
   vec3 base,emis;float wet;surf(q,oc,night,base,emis,wet);
   float ndl=dot(n,uL);
   float dif=pow(clamp(ndl*1.05+.04,0.,1.),.85);
   vec3 cc=base*(.025+dif)+emis+site(q,fp)*(.5+.8*night);
   cc+=wet*pow(max(dot(reflect(rd,n),uL),0.),48.)*.55*dif;
   float fr=pow(1.-max(dot(n,-rd),0.),3.);
   cc+=mix(uCol,vec3(.6,.8,1.),.5)*fr*clamp(ndl+.35,0.,1.)*.75;
   col=vec4(1.-exp(-cc*1.35),1.);
  }
 }
 if(col.a==0.){ // thin atmosphere seen beyond the limb
  float dc=sqrt(max(c-b*b+1.,0.));
  if(b<0.&&dc>1.){vec3 cp=ro-rd*b;float lt=clamp(dot(normalize(cp),uL)+.35,0.,1.);
   float a=exp(-(dc-1.)/.025)*lt*.85;col=vec4(mix(uCol,vec3(.6,.8,1.),.5)*a,a);}
 }
 if(uKind==2){ // rings in the equatorial plane
  vec3 N=uRot[2];float dn=dot(rd,N);
  if(abs(dn)>1e-4){float t=-dot(ro,N)/dn;
   if(t>0.&&t<tS){vec3 p=ro+rd*t;float rr=length(p);
    if(rr>1.45&&rr<2.35){
     float fp=pix*t;float bands=fbm(vec3(rr*38.,0,0),int(clamp(log2(.5/(38.*fp)),1.,6.)));
     float a=smoothstep(1.45,1.52,rr)*smoothstep(2.35,2.25,rr)*(.25+.7*bands)*(rr>1.86&&rr<1.92?.15:1.);
     float bb=dot(p,uL),sh=1.;if(bb<0.){float dd=dot(p,p)-bb*bb;sh=smoothstep(.9,1.05,dd);}
     float lt=.25+.75*abs(dot(N,uL));
     vec3 rc=mix(vec3(.9,.8,.6),uCol,.4)*(.08+.92*sh*lt)*a;
     col=vec4(rc+col.rgb*(1.-a),a+col.a*(1.-a));
    }}}
 }
 if(uBg>0.){ // space behind the planet in the landing view
  vec3 dd=rd*420.;float hs=h3(floor(dd)),hb=h3(floor(dd)+7.);vec3 f=fract(dd)-.5;
  float st=step(.9965,hs)*smoothstep(.5,.1,length(f))*(.35+.65*hb);
  vec3 bgc=vec3(.012,.016,.04)+vec3(.85,.9,1.)*st;
  col=vec4(col.rgb+(1.-col.a)*bgc*uBg,col.a+(1.-col.a)*uBg);
 }
 o=vec4(col.rgb*uGain,col.a); // uGain: Doppler factor g^4 of the orbiting planet (1 at rest)
}`;
  function create(canvas, opts) {
    const gl = canvas.getContext('webgl2', Object.assign({ premultipliedAlpha: true, antialias: false }, opts || {}));
    if (!gl) return null;
    const sh = (t, s) => { const x = gl.createShader(t); gl.shaderSource(x, s); gl.compileShader(x); if (!gl.getShaderParameter(x, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(x)); return x; };
    const pr = gl.createProgram();
    try { gl.attachShader(pr, sh(gl.VERTEX_SHADER, VS)); gl.attachShader(pr, sh(gl.FRAGMENT_SHADER, FS)); } catch (e) { console.warn(e); return null; }
    gl.bindAttribLocation(pr, 0, 'p'); gl.linkProgram(pr);
    if (!gl.getProgramParameter(pr, gl.LINK_STATUS)) { console.warn(gl.getProgramInfoLog(pr)); return null; }
    const buf = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, buf);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
    gl.enableVertexAttribArray(0); gl.vertexAttribPointer(0, 2, gl.FLOAT, false, 0, 0);
    gl.useProgram(pr);
    const U = {}; ['uVp', 'uOrtho', 'uExt', 'uCam', 'uCamM', 'uTanF', 'uRot', 'uL', 'uCol', 'uKind', 'uSite', 'uTime', 'uGlow', 'uSeed', 'uBg', 'uGain'].forEach(n => U[n] = gl.getUniformLocation(pr, n));
    return {
      gl,
      clear() { gl.viewport(0, 0, canvas.width, canvas.height); gl.clearColor(0, 0, 0, 0); gl.clear(gl.COLOR_BUFFER_BIT); },
      // p: {vp:[x,y,w,h], ortho, ext, cam, camM, tanF, rot (9, column-major), L, col, kind, site, time, glow, seed}
      draw(p) {
        gl.viewport(p.vp[0], p.vp[1], p.vp[2], p.vp[3]);
        gl.enable(gl.SCISSOR_TEST); gl.scissor(p.vp[0], p.vp[1], p.vp[2], p.vp[3]);
        gl.uniform4fv(U.uVp, p.vp); gl.uniform1i(U.uOrtho, p.ortho ? 1 : 0); gl.uniform1f(U.uExt, p.ext || 1.2);
        gl.uniform3fv(U.uCam, p.cam || [0, 0, 5]); gl.uniformMatrix3fv(U.uCamM, false, p.camM || [1, 0, 0, 0, 1, 0, 0, 0, 1]);
        gl.uniform1f(U.uTanF, p.tanF || .5); gl.uniformMatrix3fv(U.uRot, false, p.rot);
        gl.uniform3fv(U.uL, p.L); gl.uniform3fv(U.uCol, p.col); gl.uniform1i(U.uKind, p.kind);
        gl.uniform3fv(U.uSite, p.site); gl.uniform1f(U.uTime, p.time); gl.uniform1f(U.uGlow, p.glow || 0); gl.uniform1f(U.uSeed, p.seed || 0); gl.uniform1f(U.uBg, p.bg || 0); gl.uniform1f(U.uGain, p.gain == null ? 1 : p.gain);
        gl.drawArrays(gl.TRIANGLES, 0, 3);
        gl.disable(gl.SCISSOR_TEST);
      },
    };
  }
  window.PlanetGL = { create };
})();
