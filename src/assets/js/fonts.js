// Loaded early (async): shows the headline and the header once their fonts are in, at most 1.2 s
// after this runs, so they never appear in a stand-in font and re-wrap (site.css hides them until then).
(function () {
  'use strict';
  const done = () => document.documentElement.classList.add('fonts');
  if (!document.fonts || !document.fonts.load) { done(); return; }
  Promise.race([
    Promise.all(['800 40px Unbounded', '400 16px "Space Grotesk"', '600 11px "JetBrains Mono"', '400 12px "JetBrains Mono"'].map(f => document.fonts.load(f))),
    new Promise(r => setTimeout(r, 1200)),
  ]).then(done, done);
})();
