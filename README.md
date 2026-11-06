# Orbits

Personal website of Matheus Teixeira: a planetary system around a black hole, where each planet
holds one project. Static HTML, CSS and JavaScript in eight languages (en, pt, es, fr, de, zh, hi,
ar), with no framework. The build needs only Python 3.

## Layout

- `src/content/<lang>.py`: all text, one file per language.
- `src/assets/`: CSS, JavaScript, fonts, images and the still of the black hole.
- `src/static/`: files copied to the site root (favicons, Open Graph image, `_headers`).
- `tools/build.py`: writes the site to `dist/` (one `index.html` per language, `404.html`,
  `robots.txt`, `sitemap.xml`).
- `tools/smoke.js`: Playwright smoke test against a local server on port 8111.
- `.github/workflows/pages.yml`: optional manual publish to GitHub Pages.

## Build

    python3 tools/build.py          # writes dist/
    python3 -m http.server -d dist  # preview on http://localhost:8000

`dist/` is not committed. Set `SITE_URL` to build for another address.

## The black hole

`assets/js/sky.js` traces the black hole on the GPU with the same tracer as Isaac
(`isaac3d.com`): every pixel follows its light ray backwards from the camera (600 M away, 18°
above the disc) through the Schwarzschild metric. The ray stays in the plane through the hole that
holds the camera and the ray, where the null geodesic obeys d²u/dφ² = 3u² − u (u = 1/r), integrated
with RK4 until it falls through the horizon, crosses the disc or escapes. The disc is a thin disc
from the ISCO (6 M) to 15 M with the thin-disc flux F, observed as g⁴F with a black-body colour
shifted by g (gravitational redshift, time dilation and Doppler shift). Rays that circle the hole
before reaching the disc draw the thin ring round the shadow. The disc is symmetric about its axis,
so the image is traced once, a band of rows per frame, and kept; four samples per pixel smooth its
edges. `assets/bh/bh-still.webp` is the image shown where WebGL 2 is not available.

The planets and the belt orbit in the plane of the disc on one clock (40 M of time per second) and
one distance scale. Planet orbits precess at Ω − κ, with Ω = r^−1.5 and κ = Ω √(1 − 6/r) the radial
epicyclic frequency, and planets and belt are brightened or dimmed by g⁴ like the disc. The hole is
taken as 10⁸ solar masses, so every planet orbits outside its Roche limit. The camera circles the
hole once every three hours of screen time; the distant stars sweep past at the matching rate and
are lensed with the point-mass lens.

Two display choices are not physical: the orbits, belt and planets are drawn without the bending of
their light (which would lift the far side of every orbit over the hole), and the planets are drawn
thousands of times larger than they would be.

## Deployment (Cloudflare Pages)

1. Push this repository to GitHub.
2. Cloudflare dashboard > Workers & Pages > Create > Pages > Connect to Git, and pick the repository.
3. Build command `python3 tools/build.py`, build output directory `dist`, root directory empty.
   Environment variable `SITE_URL` = the site's address (for example `https://sectus.dev/`);
   it sets canonical links, the sitemap and the social cards. `PYTHON_VERSION` = `3.12`.
4. Pages > Custom domains: add the domain. A domain registered with Cloudflare Registrar is
   connected without DNS changes.

Each push to `main` then builds and deploys. `src/static/_headers` sets the security headers (including a
Content-Security-Policy that allows no inline script: the page data is JSON in `#site-data`) and
the cache headers. `.github/workflows/pages.yml` can publish the same site to GitHub Pages instead; it only
runs when started by hand.

## Project pages

Each project opens on its planet as a case study (`case_study()` in `tools/build.py`): the
product, how its parts fit together, what is checked, engineering notes, screenshots in a browser
frame (`SHOTS` in `tools/build.py`, images in `src/assets/img/`) and a live visual from
`assets/js/viz.js`.
