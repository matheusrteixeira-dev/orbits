// Renders the link-preview image (src/static/og.png, 1200 x 630) from the built site, so the
// preview always shows the current homepage. Run after a build, with the site served locally:
//   python3 tools/build.py && (cd dist && python3 -m http.server 8111) & node tools/og.js
// The build then links the image as og.png?v=<hash of the image>, so chat apps and social sites,
// which cache previews per URL, fetch the new image instead of an old copy.
const { chromium } = require('playwright');
const path = require('path');
const URL = process.argv[2] || 'http://localhost:8111/';
const OUT = path.join(__dirname, '..', 'src', 'static', 'og.png');
(async () => {
  const b = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const p = await b.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
  // A software renderer is slow, and the sky would lower its quality; keep it at full quality here.
  await p.route('**/assets/js/sky.js*', async r => {
    const res = await r.fetch();
    r.fulfill({ response: res, body: (await res.text()).replace('slow > 2000', 'slow > 2e9') });
  });
  await p.goto(URL);
  await p.waitForFunction(() => document.getElementById('bh').classList.contains('on') && document.documentElement.classList.contains('fonts'), { timeout: 400000 });
  await p.waitForTimeout(6000);   // detailed planets and a few seconds of motion
  // Wait for a moment when no planet label covers the hole or another label (up to 90 s).
  // HOLE is the shadow and bright inner disc in this 1200 x 630 layout; adjust it if the homepage layout changes.
  const HOLE = { l: 830, r: 940, t: 268, b: 350 };
  await p.waitForFunction(H => {
    const R = [...document.querySelectorAll('#labs > *')].map(b => b.getBoundingClientRect());
    const hit = (a, c) => a.left < c.r + 6 && a.right > c.l - 6 && a.top < c.b + 6 && a.bottom > c.t - 6;
    if (R.some(a => hit(a, H))) return false;
    for (let i = 0; i < R.length; i++) for (let j = i + 1; j < R.length; j++)
      if (hit(R[i], { l: R[j].left, r: R[j].right, t: R[j].top, b: R[j].bottom })) return false;
    return true;
  }, HOLE, { timeout: 90000, polling: 200 });
  await p.screenshot({ path: OUT, timeout: 300000 });
  await b.close();
  console.log('wrote', OUT);
})();
