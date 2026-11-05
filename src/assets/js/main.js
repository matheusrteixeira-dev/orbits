// Page wiring: project visuals, landing buttons, deep links, e-mail copy, language menu.
(function () {
  'use strict';
  const S = window.SITE, T = S.t, reduce = matchMedia('(prefers-reduced-motion: reduce)');
  // Project visuals run only while on screen.
  const cards = [...document.querySelectorAll('canvas[data-viz]')].map(c => ({ c, v: window.VIZ.attach(c, c.dataset.viz), on: false }));
  const io = new IntersectionObserver(es => es.forEach(e => { const k = cards.find(x => x.c === e.target); if (k) k.on = e.isIntersecting; }), { rootMargin: '80px' });
  cards.forEach(k => io.observe(k.c));
  (function tick(now) {
    const busy = window.WORLD && window.WORLD.open_ >= 0;
    if (!busy) for (const k of cards) if (k.on && (!reduce.matches || !k.v.once)) k.v.draw(now, reduce.matches);
    requestAnimationFrame(tick);
  })(performance.now());
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
