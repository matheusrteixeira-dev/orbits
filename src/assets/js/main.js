// Page wiring: project visuals, landing buttons, deep links, e-mail copy, language menu.
(function () {
  'use strict';
  const S = window.SITE, T = S.t;
  // The headline waits for its fonts in fonts.js, which loads early.
  // Project visuals run only while on screen.
  const cards = [...document.querySelectorAll('canvas[data-viz]')].map(c => ({ c, v: window.VIZ.attach(c, c.dataset.viz), on: false }));
  const io = new IntersectionObserver(es => es.forEach(e => { const k = cards.find(x => x.c === e.target); if (k) k.on = e.isIntersecting; }), { rootMargin: '80px' });
  cards.forEach(k => io.observe(k.c));
  (function tick(now) {
    const busy = window.WORLD && window.WORLD.open_ >= 0;
    if (!busy) for (const k of cards) if (k.on) k.v.draw(now, false);
    requestAnimationFrame(tick);
  })(performance.now());
  // Sections ease in as they scroll into view; siblings follow one another by a few tenths of a second.
  if ('IntersectionObserver' in window) {
    const rv = [...document.querySelectorAll('.sec .sh, .ab-l, .ab-r, .pt, #roadmap .sh ~ *, .ed > *, .xr, .pub, .to > *, .ct')];
    const seen = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); seen.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px' });
    rv.forEach(el => {
      const k = [...el.parentNode.children].indexOf(el);
      el.classList.add('rv'); el.style.setProperty('--d', Math.min(k, 5) * .07 + 's'); seen.observe(el);
    });
  }
  // Tile screenshots load only as their tile nears the screen.
  const lz = [...document.querySelectorAll('.pt-img img[data-src]')], put = im => { if (im.dataset.srcset) im.srcset = im.dataset.srcset; im.src = im.dataset.src; im.removeAttribute('data-src'); };
  if ('IntersectionObserver' in window) { const lo = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { put(e.target); lo.unobserve(e.target); } }), { rootMargin: '600px 0px' }); lz.forEach(im => lo.observe(im)); }
  else lz.forEach(put);
  document.querySelectorAll('button.land').forEach(b => b.addEventListener('click', () => window.WORLD.open(+b.dataset.i)));
  // Deep link to a project (#isaac, ...): land once the sky has drawn a frame.
  const i = S.projects.findIndex(p => '#' + p.id === location.hash);
  if (i >= 0) setTimeout(() => window.WORLD.open(i, null, { push: false }), 400);
  // Copy the e-mail address.
  const cp = document.getElementById('cp'), st = document.getElementById('cpst');
  cp.addEventListener('click', () => {
    const done = () => { cp.textContent = T.copied; st.textContent = T.copied; setTimeout(() => { cp.textContent = T.copy; st.textContent = ''; }, 1600); };
    const sel = () => { const r = document.createRange(); r.selectNodeContents(cp.previousElementSibling); const s = getSelection(); s.removeAllRanges(); s.addRange(r); };
    try { navigator.clipboard.writeText(S.email).then(done, sel); } catch (_) { sel(); }
  });
  // Header menus (sections on phones, language): close on outside click, Escape or a pick.
  document.querySelectorAll('.top details').forEach(m => {
    document.addEventListener('click', e => { if (m.open && !m.contains(e.target)) m.open = false; });
    m.addEventListener('keydown', e => { if (e.key === 'Escape') { m.open = false; m.querySelector('summary').focus(); } });
    m.addEventListener('toggle', () => { if (m.open) document.querySelectorAll('.top details').forEach(o => { if (o !== m) o.open = false; }); });
    m.querySelectorAll('a[href^="#"]').forEach(a => a.addEventListener('click', () => { m.open = false; }));
  });
  // Solid header once the page scrolls, so content never shows through it.
  const top = document.querySelector('.top'), onScroll = () => top.classList.toggle('sc', scrollY > 8);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();
})();
