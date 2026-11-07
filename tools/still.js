// Renders the still of the traced black hole (src/assets/bh/bh-still.webp), shown from the first frame
// until the live hole is traced. Run after a build, with the site served locally:
//   python3 tools/build.py && (cd dist && python3 -m http.server 8111) & node tools/still.js /tmp/still.png
// then convert: python3 -c "from PIL import Image; Image.open('/tmp/still.png').save('src/assets/bh/bh-still.webp', quality=88, method=6, alpha_quality=90)"
const { chromium } = require('playwright');
const fs = require('fs');
const OUT = process.argv[2] || 'still.png';
(async () => {
  const b = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 2 });
  // A software renderer is slow, and the sky would lower its quality; keep it at full quality here.
  await p.route('**/assets/js/sky.js*', async r => { const res = await r.fetch(); r.fulfill({ response: res, body: (await res.text()).replace('slow > 2000', 'slow > 2e9') }); });
  await p.goto(process.argv[3] || 'http://localhost:8111/');
  await p.waitForFunction(() => document.getElementById('bh').classList.contains('on'), { timeout: 600000 });
  await p.waitForTimeout(1500);
  // Read the canvas right after the sky has drawn it in the same frame.
  const url = await p.evaluate(() => new Promise(res => requestAnimationFrame(() => requestAnimationFrame(() => res(document.getElementById('bh').toDataURL('image/png'))))));
  fs.writeFileSync(OUT, Buffer.from(url.split(',')[1], 'base64'));
  await b.close();
  console.log('wrote', OUT);
})();
