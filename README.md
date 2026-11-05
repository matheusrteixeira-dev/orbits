# matheusrteixeira-dev.github.io

Personal website of Matheus Teixeira: a planetary system around a spinning black hole, where each
planet holds one project. Static HTML, CSS and JavaScript in eight languages (en, pt, es, fr, de,
zh, hi, ar), with no framework. The build needs only Python 3; the black hole tools also need
NumPy, Pillow and SciPy.

## Layout

- `src/content/<lang>.py`: all text, one file per language.
- `src/assets/`: CSS, JavaScript, fonts, the portrait and the black hole data maps.
- `src/static/`: files copied to the site root (favicons, Open Graph image).
- `tools/build.py`: writes the site to `dist/` (one `index.html` per language, `404.html`,
  `robots.txt`, `sitemap.xml`).
- `tools/kerr.py`, `tools/kerr_part.py`, `tools/pack_bh.py`, `tools/plane_lens.py`: the light-path
  pipeline (below); `tools/shade2.py` renders a still of the disc offline.
- `tools/smoke.js`: Playwright smoke test against a local server on port 8111.
- `.github/workflows/pages.yml`: builds `dist/` and publishes it to GitHub Pages on every push to `main`.

## Build

    python3 tools/build.py          # writes dist/
    python3 -m http.server -d dist  # preview on http://localhost:8000

`dist/` is not committed. GitHub Pages is set to "GitHub Actions" as its source, and the workflow
builds and deploys on each push to `main`.

## The black hole

`tools/kerr.py` traces null geodesics backwards from the camera through the Kerr metric
(spin a = 0.9, camera 18° above the disc, i = 72°) with RK4 in Boyer–Lindquist coordinates, and
records the first two crossings of the equatorial disc for every pixel together with the redshift
factor of a circular prograde emitter. `tools/kerr_part.py` is the same tracer for a band of rows,
so that four processes can share the image. `tools/pack_bh.py` packs the geometry into `bh-map.png`.
In the browser, `assets/js/sky.js` shades the disc from those maps every frame on the GPU: an
optically thick thin disc with the Novikov–Thorne flux, observed bolometric intensity g⁴F,
blackbody colours shifted by g, a slowly evolving spiral texture carried round at the Kerr rate
Ω = 1 / (r^1.5 + a), and a camera-like exposure curve and bloom. The gas is drawn out to about
16 M.

The planets and the belt orbit in the equatorial plane, the plane of the disc, so frame dragging
does not precess their orbital planes. Disc, planets and belt share one clock (40 M of time per
second) and one distance scale. Planet orbits precess at Ω − κ, with κ the Kerr radial epicyclic
frequency. The hole is taken as 10⁸ solar masses, so every planet orbits outside its Roche limit.

`tools/plane_lens.py` traces about 890,000 rays from the same camera and inverts their equatorial
crossings into `assets/bh/plane.json`: for each point of the plane between r = 25 and 53 M, where
its direct image and its image round the hole land on the screen, and how long its light takes.
Every entry is checked by tracing it forward. In the browser each planet and belt grain is drawn
at both images, at the moment its light left it (light-travel delay), stretched by the local lens
matrix and brightened or dimmed by g⁴ like the disc. The camera circles the hole once every three
hours of screen time; the distant stars sweep past at the matching rate, and are lensed with the
point-mass lens. Planet sizes, the exposure and the disc texture are display choices; positions,
motions, light paths, delays and Doppler shifts are computed.

    for k in 0 1 2 3; do python3 tools/kerr_part.py 1600 1000 part$k 0.9 72 $((k*250)) $((k*250+250)) & done; wait
    # merge part0..3.npz into kerr.npz (hit_r, hit_phi, g, captured stacked by rows; W, H, halfWidthM, a, rIn, rOut)
    python3 tools/pack_bh.py kerr.npz src/assets/bh 72
    python3 tools/plane_lens.py 4    # needs numpy and scipy; writes src/assets/bh/plane.json

## Project pages

Each project opens on its planet as a case study (`case_study()` in `tools/build.py`): the
product, how its parts fit together, what is checked, engineering notes, screenshots in a browser
frame (`SHOTS` in `tools/build.py`, images in `src/assets/img/`) and a live visual from
`assets/js/viz.js`.
