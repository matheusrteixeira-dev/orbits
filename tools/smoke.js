const {chromium}=require('playwright');
(async()=>{
 const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});
 // The sky moves even when the system asks for reduced motion.
 let p=await b.newPage({viewport:{width:1280,height:800},reducedMotion:'reduce'});const e=[];p.on('pageerror',x=>e.push(x.message));
 await p.goto('http://localhost:8111/fr/');await p.waitForTimeout(3000);
 const pos=()=>p.evaluate(()=>[...document.querySelectorAll('#labs .lab')].map(l=>l.style.transform).join());
 const p0=await pos();await p.waitForTimeout(1500);
 console.log('reduced motion: planets moving =',p0!==await pos(),'| pause button =',!!(await p.$('#pause')),'| errors',e.length);
 await p.click('button.land >> nth=2');await p.waitForTimeout(3500);
 console.log('landed:',await p.evaluate(()=>document.getElementById('world').className),location=await p.evaluate(()=>location.hash));
 await p.keyboard.press('Escape');await p.waitForTimeout(2500);
 console.log('after esc hidden:',await p.evaluate(()=>document.getElementById('world').hidden),'hash',await p.evaluate(()=>location.hash));
 await p.close();
 // No WebGL
 const b2=await chromium.launch({args:['--disable-webgl','--disable-webgl2']});
 p=await b2.newPage({viewport:{width:1280,height:800}});const e2=[];p.on('pageerror',x=>e2.push(x.message));
 await p.goto('http://localhost:8111/#amadeo');await p.waitForTimeout(2500);
 console.log('nogl errors',e2,'world',await p.evaluate(()=>document.getElementById('world').className));
 await p.screenshot({path:'shots/nogl.png'});
 // Horizontal overflow check across widths and languages
 for(const l of ['','pt/','es/','fr/','de/','zh/','hi/','ar/']) for(const w of [360,390,768,1024,1440]){
  const q=await b2.newPage({viewport:{width:w,height:800}});await q.goto('http://localhost:8111/'+l);await q.waitForTimeout(300);
  const o=await q.evaluate(()=>document.documentElement.scrollWidth-innerWidth);if(o>0)console.log('overflow',l,w,o);await q.close()}
 console.log('done');await b.close();await b2.close()})();
