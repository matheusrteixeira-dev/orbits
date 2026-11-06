"""Draw the images used by README.md into docs/readme/ (animated SVG, no external files).

    python3 tools/readme_art.py

header.svg  the black hole still from the site, with the five project planets on their orbits.
light.svg   real light paths around a non-rotating hole, from the same equation as the site's tracer.
"""
import base64
import math
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "readme"
SANS = "'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "'SFMono-Regular', Consolas, 'DejaVu Sans Mono', 'Liberation Mono', Menlo, monospace"

# name, colour, orbit radius in M (as in tools/build.py), radius in px
PLANETS = [("Isaac", "#ff5a3c", 28, 6), ("Amadeo", "#3d7bff", 31.5, 7), ("Brectus", "#b45cff", 35.5, 7.5),
           ("Websites", "#2de0a5", 39.5, 6.5), ("Allwinner", "#ffc23d", 44, 9)]
INC = math.radians(18)  # camera height above the disc, as on the site


def stars(rng, n, w, h, cls=True):
    out = []
    for i in range(n):
        x, y, r, o = rng.uniform(0, w), rng.uniform(0, h), rng.choice((.5, .7, .9, 1.2, 1.4)), rng.uniform(.25, .9)
        c = f' class="tw tw{i % 3}"' if cls and i % 4 == 0 else ""
        out.append(f'<circle{c} cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#dfe8ff" opacity="{o:.2f}"/>')
    return "".join(out)


def ellipse_path(cx, cy, rx, ry):
    # Starts at the far point and runs anticlockwise as seen from above (left to right across the front).
    return f"M{cx:.1f} {cy - ry:.1f} A{rx:.1f} {ry:.1f} 0 1 0 {cx:.1f} {cy + ry:.1f} A{rx:.1f} {ry:.1f} 0 1 0 {cx:.1f} {cy - ry:.1f}"


def header():
    W, H = 1280, 400
    cx, cy, k = 905, 205, 7.2  # hole centre and pixels per M
    still = (ROOT / "src" / "assets" / "bh" / "bh-still.webp").read_bytes()
    iw, ih = 52 * k, 32.5 * k  # the still spans 52 M by 32.5 M around the hole
    rng = random.Random(4)
    back, front, lines = [], [], []
    phase = [.08, .55, .32, .8, .2]  # starting points spread so the labels do not collide
    for (name, col, a, r), f in zip(PLANETS, phase):
        rx, ry = a * k, a * k * math.sin(INC)
        d = ellipse_path(cx, cy, rx, ry)
        lines.append(f'<path d="{d}" fill="none" stroke="#9fb4ff" stroke-opacity=".16" stroke-width="1"/>')
        period = 23 * (a / 28) ** 1.5
        begin = -f * period
        body = (f'<g><animateMotion dur="{period:.1f}s" begin="{begin:.1f}s" repeatCount="indefinite" path="{d}"/>'
                f'<circle r="{r * 2.6:.1f}" fill="{col}" opacity=".16"/><circle r="{r}" fill="url(#p-{name})"/>'
                f'<rect x="{r + 6:.1f}" y="-8" width="2" height="16" fill="{col}"/>'
                f'<text x="{r + 12:.1f}" y="4" font-family="{MONO}" font-size="11" letter-spacing="1.5" fill="#e8eeff">{name.upper()}</text></g>')
        back.append(body)
        front.append(body)
    belt = []
    for _ in range(420):
        a, ph = rng.uniform(47.5, 50.5) * k, rng.uniform(0, 2 * math.pi)
        x, y = cx + a * math.cos(ph), cy + a * math.sin(ph) * math.sin(INC)
        belt.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rng.choice((.6, .8, 1.0))}" fill="#d9d2c4" opacity="{rng.uniform(.25, .8):.2f}"/>')
    grads = "".join(f'<radialGradient id="p-{n}" cx=".35" cy=".35" r=".75"><stop offset="0" stop-color="#ffffff" stop-opacity=".9"/>'
                    f'<stop offset=".25" stop-color="{c}"/><stop offset="1" stop-color="#05060f"/></radialGradient>' for n, c, _, _ in PLANETS)
    img = (f'<image href="data:image/webp;base64,{base64.b64encode(still).decode()}" x="{cx - iw / 2:.1f}" y="{cy - ih / 2:.1f}" '
           f'width="{iw:.1f}" height="{ih:.1f}" preserveAspectRatio="none"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
  <title id="t">Orbits</title>
  <desc id="d">The personal website of Matheus Teixeira: a black hole traced on the GPU, with five project planets on their orbits.</desc>
  <style>
    .tw {{ animation: tw 4s ease-in-out infinite; }} .tw1 {{ animation-delay: 1.3s; }} .tw2 {{ animation-delay: 2.6s; }}
    @keyframes tw {{ 0%,100% {{ opacity: .2; }} 50% {{ opacity: .95; }} }}
    .rise {{ animation: rise 1.2s ease-out both; }} .r2 {{ animation-delay: .25s; }} .r3 {{ animation-delay: .5s; }} .r4 {{ animation-delay: .75s; }}
    @keyframes rise {{ from {{ opacity: 0; transform: translateY(10px); }} to {{ opacity: 1; transform: none; }} }}
    .caret {{ animation: blink 1s steps(1) infinite; }} @keyframes blink {{ 50% {{ opacity: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
  </style>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#03040a"/><stop offset=".6" stop-color="#080c1d"/><stop offset="1" stop-color="#120a22"/></linearGradient>
    <linearGradient id="hud" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#3ff0ff"/><stop offset="1" stop-color="#ff4fd8"/></linearGradient>
    <radialGradient id="glow" cx="{cx}" cy="{cy}" r="230" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#ff9a3c" stop-opacity=".18"/><stop offset="1" stop-color="#03040a" stop-opacity="0"/></radialGradient>
    <clipPath id="far"><rect x="0" y="0" width="{W}" height="{cy}"/></clipPath>
    <clipPath id="near"><rect x="0" y="{cy}" width="{W}" height="{H - cy}"/></clipPath>
    <clipPath id="frame"><rect width="{W}" height="{H}" rx="18"/></clipPath>
    {grads}
  </defs>
  <g clip-path="url(#frame)">
    <rect width="{W}" height="{H}" fill="url(#bg)"/>
    {stars(rng, 170, W, H)}
    <rect width="{W}" height="{H}" fill="url(#glow)"/>
    <g clip-path="url(#far)">{"".join(belt)}{"".join(lines)}{"".join(back)}</g>
    {img}
    <g clip-path="url(#near)">{"".join(belt)}{"".join(lines)}{"".join(front)}</g>
    <text class="rise" x="64" y="96" font-family="{MONO}" font-size="14" letter-spacing="3" fill="#3ff0ff">SECTUS.DEV</text>
    <text class="rise r2" x="60" y="178" font-family="{SANS}" font-size="78" font-weight="800" letter-spacing="-2" fill="#f2f5ff">Orbits</text>
    <text class="rise r3" x="64" y="224" font-family="{SANS}" font-size="22" fill="#c9d3f2">The personal website of Matheus Teixeira</text>
    <text class="rise r4" x="64" y="282" font-family="{MONO}" font-size="13" fill="#9aa6c9">$ python3 tools/build.py<tspan class="caret" fill="#3ff0ff"> ▍</tspan></text>
    <text class="rise r4" x="64" y="306" font-family="{MONO}" font-size="13" fill="#6f7aa0">8 languages · no framework · one black hole</text>
    <rect x="64" y="330" width="220" height="2" fill="url(#hud)" opacity=".8"/>
    <rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="18" fill="none" stroke="#3ff0ff" stroke-opacity=".18"/>
  </g>
</svg>
'''


def ray(b, steps=4000):
    """Light path with impact parameter b (in M), coming in from x = +inf, by RK4 on u'' = 3u^2 - u."""
    u, phi = 1 / 400.0, 0.0
    du = math.sqrt(max(1 / b ** 2 - u ** 2 + 2 * u ** 3, 0))
    h = 0.004
    pts = []
    f = lambda u: 3 * u * u - u
    for _ in range(steps):
        r = 1 / u
        pts.append((r * math.cos(phi), r * math.sin(phi)))
        if u > 0.5 or u <= 0 or (r > 60 and len(pts) > 50 and du < 0):
            break
        k1u, k1v = du, f(u)
        k2u, k2v = du + h / 2 * k1v, f(u + h / 2 * k1u)
        k3u, k3v = du + h / 2 * k2v, f(u + h / 2 * k2u)
        k4u, k4v = du + h * k3v, f(u + h * k3u)
        u += h / 6 * (k1u + 2 * k2u + 2 * k3u + k4u)
        du += h / 6 * (k1v + 2 * k2v + 2 * k3v + k4v)
        phi += h
    return pts, u > 0.5


def light():
    W, H, cx, cy, s = 1280, 460, 830, 230, 13.0
    tx = lambda p: (cx - p[0] * s, cy - p[1] * s)  # light arrives from the left
    paths, n_cap = [], 0
    bc = 3 * math.sqrt(3)
    for b in [2.6, 4.2, bc - 0.004, bc + 0.004, 6.6, 9.5, 13.5, -2.6, -4.2, -(bc - 0.004), -(bc + 0.004), -6.6, -9.5, -13.5]:
        pts, captured = ray(abs(b))
        if b < 0:
            pts = [(x, -y) for x, y in pts]
        pts = [p for p in pts if -34 < p[0] < 30 and abs(p[1]) < 17.5]
        if len(pts) < 2:
            continue
        d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in map(tx, pts[::6] + [pts[-1]]))
        near = abs(b - bc) < .01
        col = "#ffd27a" if near else ("#ff4fd8" if captured else "#3ff0ff")
        n_cap += captured
        paths.append((d, col, near, b))
    lines = "".join(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{1.8 if n else 1.2}" stroke-opacity="{.95 if n else .55}"/>' for d, c, n, _ in paths)
    crit = next(d for d, c, n, b in paths if n and 0 < b < bc)
    rng = random.Random(9)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
  <title id="t">Light paths around a black hole</title>
  <desc id="d">Light rays passing a non-rotating black hole, computed from d2u/dphi2 = 3u^2 - u. Rays closer than 5.2 M fall in, rays near 5.2 M circle the photon sphere at 3 M, and the rest are bent and escape.</desc>
  <style>
    .tw {{ animation: tw 4s ease-in-out infinite; }} .tw1 {{ animation-delay: 1.3s; }} .tw2 {{ animation-delay: 2.6s; }}
    @keyframes tw {{ 0%,100% {{ opacity: .2; }} 50% {{ opacity: .95; }} }}
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} .ph {{ display: none; }} }}
  </style>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#03040a"/><stop offset="1" stop-color="#0b1026"/></linearGradient>
    <radialGradient id="ring" cx="{cx}" cy="{cy}" r="{6 * s}" gradientUnits="userSpaceOnUse"><stop offset=".5" stop-color="#ff9a3c" stop-opacity="0"/><stop offset=".95" stop-color="#ff9a3c" stop-opacity=".16"/><stop offset="1" stop-color="#ff9a3c" stop-opacity="0"/></radialGradient>
    <clipPath id="frame"><rect width="{W}" height="{H}" rx="18"/></clipPath>
  </defs>
  <g clip-path="url(#frame)">
    <rect width="{W}" height="{H}" fill="url(#bg)"/>
    {stars(rng, 90, W, H)}
    {lines}
    <circle cx="{cx}" cy="{cy}" r="{15 * s}" fill="none" stroke="#ff9a3c" stroke-opacity=".25" stroke-dasharray="3 5"/>
    <circle cx="{cx}" cy="{cy}" r="{6 * s}" fill="url(#ring)" stroke="#ff9a3c" stroke-opacity=".5"/>
    <circle cx="{cx}" cy="{cy}" r="{3 * s}" fill="none" stroke="#ffd27a" stroke-opacity=".7" stroke-dasharray="2 3"/>
    <circle cx="{cx}" cy="{cy}" r="{2 * s}" fill="#000"/>
    <circle class="ph" r="3.2" fill="#fff"><animateMotion dur="7s" repeatCount="indefinite" path="{crit}"/></circle>
    <text x="44" y="64" font-family="{MONO}" font-size="13" letter-spacing="3" fill="#3ff0ff">HOW THE HOLE IS DRAWN</text>
    <text x="44" y="108" font-family="{SANS}" font-size="30" font-weight="700" fill="#f2f5ff">d²u/dφ² = 3u² − u</text>
    <text x="44" y="138" font-family="{MONO}" font-size="13" fill="#9aa6c9">u = 1/r, units of M, RK4 per pixel</text>
    <text x="44" y="170" font-family="{MONO}" font-size="12" fill="#c9d3f2">horizon 2 M<tspan fill="#6f7aa0">  ·  </tspan><tspan fill="#ffd27a">photon sphere 3 M</tspan><tspan fill="#6f7aa0">  ·  </tspan><tspan fill="#ff9a3c">disc 6 to 15 M</tspan></text>
    <g font-family="{MONO}" font-size="12">
      <text x="44" y="{H - 82}" fill="#3ff0ff">— bent and escapes</text>
      <text x="44" y="{H - 60}" fill="#ffd27a">— circles the photon sphere (b ≈ 5.2 M)</text>
      <text x="44" y="{H - 38}" fill="#ff4fd8">— falls through the horizon</text>
    </g>
    <rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="18" fill="none" stroke="#3ff0ff" stroke-opacity=".18"/>
  </g>
</svg>
'''


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "header.svg").write_text(header(), encoding="utf-8")
    (OUT / "light.svg").write_text(light(), encoding="utf-8")
    print("wrote", ", ".join(p.name for p in sorted(OUT.glob("*.svg"))))


if __name__ == "__main__":
    main()
