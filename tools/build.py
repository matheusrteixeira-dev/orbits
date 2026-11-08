"""Build the static site: one page per language, plus 404, robots.txt and sitemap.xml.

usage: python3 tools/build.py [out_dir]     (default: dist)
Content lives in src/content/<lang>.py (one dict C per language); facts that do not change
between languages (links, colours, orbits, tags) are below.
"""
import hashlib
import html
import importlib.util
import json
import os
import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "dist"
# The preview image is linked with its own hash, so link previews are refetched whenever it changes.
OG_V = hashlib.sha1((ROOT / "src" / "static" / "og.png").read_bytes()).hexdigest()[:10]
# Public address of the site, used for canonical links, the sitemap and social cards. Set SITE_URL
# in the host's build settings (Cloudflare Pages: Settings > Environment variables).
SITE_URL = os.environ.get("SITE_URL", "https://sectus.dev/").rstrip("/") + "/"
LANGS = ["en", "pt", "es", "fr", "de", "zh", "hi", "ar"]
RTL = {"ar"}
GFONTS = {
    "zh": "Noto+Sans+SC:wght@400;500;700;900",
    "hi": "Noto+Sans+Devanagari:wght@400;500;700;800",
    "ar": "Noto+Kufi+Arabic:wght@400;500;700;800",
}
EMAIL = "matheus@sectus.dev"
LINKS = {
    "github": "https://github.com/matheusrteixeira-dev",
    "linkedin": "https://www.linkedin.com/in/matheusrteixeira/",
    "orcid": "https://orcid.org/0009-0001-1816-632X",
    "paper": "https://sol.sbc.org.br/index.php/eniac/article/view/46839",
    "iris": "https://github.com/matheusrteixeira-dev/Quantum-Classifier-for-Iris-Dataset",
    "qml": "https://github.com/matheusrteixeira-dev/Quantum-Machine-Learning-Applications-in-Healthcare",
}
PAPER = "Systematic Review of Quantum Machine Learning for Healthcare"
# Projects in orbit order (innermost first). orbit: semi-major axis a (M), eccentricity e,
# periapsis angle w0 and radial phase m0 at the start, planet radius R (M, exaggerated).
# site: latitude and longitude (degrees) of the project's site; longitude 0 faces the hole.
PROJECTS = [
    {"id": "isaac", "name": "Isaac", "col": "#ff5a3c", "kind": "rock", "urls": ["isaac3d.com"],
     "tags": ["Rust", "WebAssembly", "React", "Three.js"], "orbit": {"a": 27.5, "e": .012, "w0": .5, "m0": 0, "R": 1.06}, "site": [18, 35]},
    {"id": "amadeo", "name": "Amadeo", "col": "#3d7bff", "kind": "ocean", "urls": ["amadeosheets.com"],
     "tags": ["TensorFlow.js", "React", "TypeScript", "VexFlow"], "orbit": {"a": 38.7, "e": .01, "w0": 2.6, "m0": 1, "R": 1.22}, "site": [12, 30]},
    {"id": "brectus", "name": "Brectus", "col": "#b45cff", "kind": "storm", "urls": [],
     "tags": ["Node.js", "Electron"], "orbit": {"a": 34.8, "e": .012, "w0": 4.3, "m0": 2, "R": 1.32}, "site": [-10, 40]},
    {"id": "websites", "name": "Websites", "col": "#2de0a5", "kind": "ice", "urls": ["liderplustelemedicina.com.br"],
     "tags": ["Astro", "TypeScript", "Cloudflare"], "orbit": {"a": 31, "e": .014, "w0": 1.4, "m0": .5, "R": 1.12}, "site": [22, 25]},
    {"id": "allwinner", "name": "Allwinner", "col": "#ffc23d", "kind": "gas", "urls": [],
     "tags": ["Python", "pandas", "FastAPI", "SQLite"], "orbit": {"a": 45, "e": .01, "w0": 3.6, "m0": 3, "R": 1.65}, "site": [8, 30]},
]
TOOLS = [
    ["Python", "PyTorch", "scikit-learn", "TensorFlow", "pandas", "NumPy", "SQL"],
    ["TypeScript", "React", "Three.js", "Astro", "Node.js", "Electron", "FastAPI"],
    ["Rust", "WebAssembly", "C/C++", "Cloudflare Workers", "Linux", "Git"],
    ["Qiskit", "IBM Quantum", "pytest", "cargo test", "Vitest", "Playwright"],
]

e = html.escape


def load(lang):
    spec = importlib.util.spec_from_file_location(lang, SRC / "content" / f"{lang}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.C


def page_path(lang):
    return "" if lang == "en" else f"{lang}/"


def ext_link(url, label=None, cls="u"):
    return f'<a class="{cls}" href="{e(url)}" target="_blank" rel="noopener">{e(label or url)} ↗</a>'


# ---------- Roadmap: a worldline drawn as an SVG spacetime diagram (time to the right) ----------
# Events: key, time in years, place (0 Brazil, 1 Zurich), planned, label date (year, month index or None).
NOW = 2026 + 10.2 / 12          # build date, early November 2026
EVENTS = [
    ("orion", 2016.25, 0, False, (2016, None)),
    ("bsc", 2019.5, 0, False, (2019, None)),
    ("bscd", 2023.45, 0, False, (2023, None)),
    ("msc", 2024.2, 0, False, (2024, None)),
    ("mscd", 2026.2, 0, False, (2026, None)),
    ("mba", 2026 + 7 / 12, 0, False, (2026, 7)),
    ("paper", 2026 + 9 / 12, 0, False, (2026, 9)),
    ("phd", 2027 + 1 / 12, 0, False, (2027, 1)),
    ("eth", 2028 + 8 / 12, 1, True, (2028, 8)),
    ("def", 2030 + 1 / 12, 0, True, (2030, 1)),
]
ETH = (2028 + 8 / 12, 2029 + 7 / 12)
SPANS = [("orion", 2016.25, 2023.5, 0), ("bsc", 2019.5, 2023.45, 1), ("msc", 2024.2, 2026.2, 0), ("mba", 2026 + 7 / 12, 2027 + 7 / 12, 1), ("phd", 2027 + 1 / 12, 2030 + 1 / 12, 0)]


def text_w(s, size):
    """Rough rendered width of a label, enough to keep labels apart."""
    w = 0
    for ch in s:
        o = ord(ch)
        w += 1.0 if (0x2E80 <= o <= 0x9FFF or 0xAC00 <= o <= 0xD7AF) else 0.66 if 0x0900 <= o <= 0x097F else 0.56 if 0x0600 <= o <= 0x06FF else 0.58
    return w * size


def date_label(R, y, m):
    return R.get("datefmt", "{m} {y}").format(m=R["months"][m], y=y) if m is not None else str(y)


def worldline(C, rtl=False):
    """rtl: wrap labels in Unicode isolates so that Arabic reads right to left inside the LTR diagram."""
    R = C["roadmap"]
    iso = (lambda t: "\u2067" + t + "\u2069") if rtl else (lambda t: t)
    W, X0, X1, T0, T1 = 1180, 92, 1110, 2015.8, 2030.9
    YB, YC = 262, 74
    x = lambda t: X0 + (t - T0) / (T1 - T0) * (X1 - X0)
    out = []
    # Year grid and axis.
    for yr in range(2016, 2031):
        xx = x(yr)
        out.append(f'<line class="gy" x1="{xx:.1f}" y1="30" x2="{xx:.1f}" y2="{YB + 26}"/><text class="ty" x="{xx:.1f}" y="{YB + 46}">{yr}</text>')
    out.append(f'<text class="rl" x="12" y="{YB + 4}">{e(iso(R["br"]))}</text><text class="rl" x="12" y="{YC + 4}">{e(iso(R["ch"]))}</text>')
    out.append(f'<line class="rail" x1="{X0}" y1="{YB}" x2="{X1}" y2="{YB}"/><line class="rail" x1="{X0}" y1="{YC}" x2="{X1}" y2="{YC}"/>')
    xn = x(NOW)
    # The worldline: solid up to now, dashed after; up to Zurich and back for the ETH year.
    a0, a1 = ETH
    out.append(f'<path class="wl" d="M{x(2016.25):.1f} {YB} L{xn:.1f} {YB}"/>')
    out.append(f'<path class="wl pl" d="M{xn:.1f} {YB} L{x(a0 - .08):.1f} {YB} L{x(a0):.1f} {YC} L{x(a1):.1f} {YC} L{x(a1 + .08):.1f} {YB} L{x(2030 + 1 / 12):.1f} {YB}"/>')
    # Spans below the axis.
    for k, s0, s1, row in SPANS:
        y0 = YB + 62 + row * 24
        xa, xb, xm = x(s0), x(s1), min(max(x(s0), xn), x(s1))
        lab = R["spans"][k]
        out.append(f'<g class="sp sp-{k}"><rect class="b" x="{xa:.1f}" y="{y0}" width="{xm - xa:.1f}" height="16" rx="3"/>')
        if xb > xm:
            out.append(f'<rect class="b pl" x="{xm:.1f}" y="{y0}" width="{xb - xm:.1f}" height="16" rx="3"/>')
        inside = text_w(lab, 11) + 14 < xb - xa
        tx = xa + 7 if inside else xb + 7
        out.append(f'<text x="{tx:.1f}" y="{y0 + 12}">{e(iso(lab))}</text></g>')
    # Events: dots on the line, labels on rows above it (greedy, so that labels never overlap).
    rows = {0: [], 1: []}
    lab_out = []
    for k, t, place, plan, (yy, mm) in EVENTS:
        xx, y = x(t), (YC if place else YB)
        lab = R["ev"][k]
        wd = max(text_w(lab, 12.5), text_w(date_label(R, yy, mm), 11)) + 10
        # Labels run to the right of their event, unless that would cross the trip to Zurich or the edge.
        xe0, xe1 = x(ETH[0]) - 8, x(ETH[1]) + 8
        left = place == 0 and ((xx < xe0 < xx + wd) or xx + wd > W - 4)
        a_, b_ = (xx - wd, xx + 4) if left else (xx - 4, xx + wd)
        r = 0
        while any(not (b_ < a or a_ > b) for a, b, rr in rows[place] if rr == r):
            r += 1
        rows[place].append((a_, b_, r))
        ly = y - 22 - r * 33
        cls = "ev pl" if plan else "ev"
        tx, anc = (xx - 6, ' text-anchor="end"') if left else (xx + 6, "")
        lab_out.append(f'<g class="{cls}"><line x1="{xx:.1f}" y1="{y - 6}" x2="{xx:.1f}" y2="{ly + 6}"/><circle cx="{xx:.1f}" cy="{y}" r="5"/>'
                       f'<text class="d" x="{tx:.1f}" y="{ly - 13}"{anc}>{e(iso(date_label(R, yy, mm)))}</text><text x="{tx:.1f}" y="{ly + 2}"{anc}>{e(iso(lab))}</text></g>')
    out += lab_out
    out.append(f'<g class="now"><circle cx="{xn:.1f}" cy="{YB}" r="7"/><circle class="halo" cx="{xn:.1f}" cy="{YB}" r="7"/><text x="{xn:.1f}" y="{YB + 24}">{e(iso(R["now"]))}</text></g>')
    svg = f'<svg class="wls" viewBox="0 0 {W} {YB + 118}" role="img" aria-labelledby="h-roadmap" direction="ltr">{"".join(out)}</svg>'
    # The same path as a list, for narrow screens and screen readers.
    items, pl, now_done = [], R["planned"], False
    for k, t, place, plan, (yy, mm) in EVENTS:
        if t > NOW and not now_done:
            items.append(f'<li class="nw"><span class="d"></span><span class="t">{e(R["now"])}</span></li>')
            now_done = True
        d = date_label(R, yy, mm)
        if k == "eth":
            d = f"{date_label(R, 2028, 8)} – {date_label(R, 2029, 7)}"
        em = f"<em>{e(pl)}</em>" if plan else ""
        items.append(f'<li class="{"pl" if plan else ""}{" fut" if t > NOW else ""}"><span class="d">{e(d)}</span><span class="t">{e(R["ev"][k])}</span>{em}</li>')
    return svg, f'<ol class="wll">{"".join(items)}</ol>'


# Open Graph locales, one per page language.
OG_LOCALE = {"en": "en_US", "pt": "pt_BR", "es": "es_ES", "fr": "fr_FR", "de": "de_DE", "zh": "zh_CN", "hi": "hi_IN", "ar": "ar_AR"}


# ---------- Case studies: one article per project, shown on its planet ----------
# Projects used live inside their page: the real site in an iframe, made after landing and removed on
# leaving (world.js lays it out as on a laptop screen and scales it into the window). A site goes in
# LIVE_ON once it lets https://sectus.dev frame it (CSP frame-ancestors, no X-Frame-Options). Isaac's
# embed pages (/embed/<scene>) are made to be framed by any site: the full workspace of the scene, with
# a link that opens it in Isaac. frame-src in src/static/_headers lists the same origins.
# The address takes the page's language where the site has it ({p}: "" for English, "/pt" and so on).
# Isaac opens on a shared state (#s=, deflated JSON, see Isaac's src/engine/share.ts): the double pendulum
# 14 s in with its trail on, {"v":1,"scene":"chaos","level":"undergraduate","time":14,"toggles":{"trail":true,"path":false}},
# so the window shows the tangle that makes the point instead of an empty stage.
ISAAC_START = "DYoxDoAgEAT_sjWNiRW_ueAKJIiGO2iMf_e6mcm8WIhbgCZ2IiIVuRUBjYvNffaDIw85phi9W71823anO-dGRXxhQ6rPNiYDHrGCeEpTft8P"
LIVE = {
    "isaac": ("https://isaac3d.com{p}/embed/chaos#s=" + ISAAC_START, set()),
    "amadeo": ("https://amadeosheets.com{p}", {"pt", "es", "fr", "de", "zh", "hi", "ar"}),
    "websites": ("https://liderplustelemedicina.com.br/", set()),
}
LIVE_ON = {"isaac", "amadeo"}


def live_url(pid, lang):
    t, langs = LIVE[pid]
    return t.format(p=f"/{lang}" if lang in langs else "")

# Whole pages scrolled inside the window, for sites that cannot be framed: a full-page capture cut into
# slices (src/assets/img/page/<name>-d-<n>.webp at 1280 px wide for wide screens, <name>-m-<n>.webp at
# 780 px, a 390 px phone at 2x, for narrow ones) that load as they near the window. tools/page_shots.py
# cuts a capture and prints the slice heights listed here.
PAGES = {
    "lider-home": {"d": [1600, 1600, 1600, 1600, 310], "m": [1600] * 13 + [274]},
    "lider-org": {"d": [1600, 1600, 735], "m": [1600] * 7 + [1178]},
}

SHOTS = {
    "isaac": [("isaac-scene", "isaac3d.com/scene/chaos"), ("isaac-home", "isaac3d.com"), ("isaac-library", "isaac3d.com/library")],
    "amadeo": [("amadeo-home", "amadeosheets.com"), ("amadeo-score", "amadeosheets.com/repertoire/fur-elise"), ("amadeo-keys", "amadeosheets.com/repertoire/fur-elise")],
    # Allwinner is a local app; captured offline on the repository's fixed BTC/USDT test history.
    "allwinner": [("allwinner-signals", "allwinner · local dashboard"), ("allwinner-scoreboard", "allwinner · local dashboard"), ("allwinner-chart", "allwinner · local dashboard")],
    # Orion's site is not live yet: captured from its local build.
    "websites": [("lider-home", "liderplustelemedicina.com.br"), ("orion-about", "orion beneficios · local build"), ("mis-home", "esthetics studio · local build"), ("lider-org", "liderplustelemedicina.com.br/organizacoes/"), ("mis-treatments", "esthetics studio · local build")],
    # Brectus is a desktop app; these are the images published on LinkedIn.
    "brectus": [("brectus-map", "brectus · desktop app"), ("brectus-university", "brectus · desktop app"), ("brectus-how", "brectus · how it works")],
}


def case_study(i, p, C, b, lang):
    T, P = C["ui"], C["proj"][p["id"]]
    pid = p["id"]
    links = "".join(f'<a class="btn" href="https://{e(u)}" target="_blank" rel="noopener">{e(T["visit"].format(u=u))} <span aria-hidden="true">↗</span></a>' for u in p["urls"]) \
        or f'<span class="off">{e(T["source"])}</span>'
    meta = (f'<div><dt>{e(T["year"])}</dt><dd>2026</dd></div><div><dt>{e(T["platform"])}</dt><dd>{e(P["platform"])}</dd></div>'
            f'<div><dt>{e(T["stack"])}</dt><dd>{e(" · ".join(p["tags"]))}</dd></div>')
    if pid in SHOTS:
        sh = SHOTS[pid]
        def view(k, f):
            hid = "" if k == 0 else " hidden"
            if f in PAGES:
                sl = lambda kind, w: "".join(f'<img data-src="{b}assets/img/page/{f}-{kind}-{n}.webp" width="{w}" height="{h}" alt="" decoding="async">' for n, h in enumerate(PAGES[f][kind]))
                return (f'<div class="pg" data-k="{k}" tabindex="0" role="region" aria-label="{e(P["shots"][k])}"{hid}>'
                        f'<div class="pg-d">{sl("d", 1280)}</div><div class="pg-m">{sl("m", 780)}</div></div>')
            return (f'<img src="{b}assets/img/{f}.webp" srcset="{b}assets/img/{f}-s.webp 720w, {b}assets/img/{f}.webp 1440w" sizes="(max-width: 1000px) 92vw, 52vw" width="1440" height="900" alt="{e(P["shots"][k])}" loading="lazy" decoding="async" data-k="{k}"{hid}>')
        imgs = "".join(view(k, f) for k, (f, _) in enumerate(sh))
        tabs = "".join(f'<button type="button" role="tab" aria-selected="{"true" if k == 0 else "false"}" data-k="{k}" data-url="{e(u)}">{e(P["shots"][k])}</button>' for k, (_, u) in enumerate(sh))
        if pid in LIVE_ON:
            lu = live_url(pid, lang)
            tabs = tabs.replace('aria-selected="true"', 'aria-selected="false"', 1)
            tabs = (f'<button type="button" role="tab" aria-selected="true" data-live="{e(lu)}" data-url="{e(lu.split("://", 1)[1].split("#", 1)[0].rstrip("/"))}"'
                    f' data-title="{e(T["liveT"].format(n=p["name"]))}">{e(T["live"])}</button>') + tabs
        # The window can fill the screen (world.js), so a live site gets the room it is made for.
        mx = (f'<button type="button" class="wmax" aria-label="{e(T["enl"])}" title="{e(T["enl"])}"><svg viewBox="0 0 12 12" aria-hidden="true">'
              '<path class="i-on" d="M1 4.5V1h3.5M7.5 1H11v3.5M11 7.5V11H7.5M4.5 11H1V7.5"/><path class="i-off" d="M4.5 1v3.5H1M7.5 1v3.5H11M11 7.5H7.5V11M1 7.5h3.5V11"/></svg></button>')
        media = (f'<figure class="cs-media"><div class="win"><div class="bar"><i></i><i></i><i></i><span class="url">{e(sh[0][1])}</span>{mx}</div><div class="vp">{imgs}</div></div>'
                 f'<div class="tabs" role="tablist" aria-label="{e(T["shot"])}">{tabs}</div></figure>')
        inside = (f'<section class="cs-in"><h3>{e(T["inside"])}</h3><figure class="cs-viz"><canvas data-wviz="{pid}" width="1040" height="780" role="img" aria-label="{e(P["viz"])}"></canvas>'
                  f'<figcaption>{e(P["viz"])}</figcaption></figure></section>')
    else:
        media = (f'<figure class="cs-media"><div class="win viz"><div class="bar"><i></i><i></i><i></i><span class="url">{e(p["name"].lower())} · {e(T["illus"])}</span></div>'
                 f'<div class="vp"><canvas data-wviz="{pid}" width="1040" height="780" role="img" aria-label="{e(P["viz"])}"></canvas></div></div><figcaption>{e(P["viz"])}</figcaption></figure>')
        inside = ""
    pipe = "".join(f'<li><b>{e(a)}</b><span>{e(r)}</span></li>' for a, r in P["arch"])
    checks = "".join(f'<li><b>{e(a)}</b><span>{e(r)}</span></li>' for a, r in P["tests"])
    notes = "".join(f'<div class="note"><h4>{e(h)}</h4><p>{e(t)}</p></div>' for h, t in P["notes"])
    nx = PROJECTS[(i + 1) % len(PROJECTS)]
    return f'''<article class="cs" id="cs-{pid}" data-i="{i}" style="--c:{p["col"]}" hidden>
<div class="cs-top"><div class="cs-hd"><span class="k">{e(T["planet"].format(n=i + 1))} · {e(P["world"])}</span><h2 tabindex="-1">{e(p["name"])}</h2><p class="s">{e(P["sub"])}</p><p class="lede">{e(P["lede"])}</p>
<dl class="meta">{meta}</dl><div class="links">{links}</div><p class="orb"></p></div>{media}</div>
<div class="cs-sheet"><section class="cs-how"><h3>{e(T["how"])}</h3><ol class="pipe">{pipe}</ol><div class="checks"><h4>{e(T["checks"])}</h4><ul>{checks}</ul></div></section>
<section class="cs-notes"><h3>{e(T["notes"])}</h3><div class="grid">{notes}</div></section>{inside}
<button type="button" class="cs-next" data-go="{(i + 1) % len(PROJECTS)}" style="--n:{nx["col"]}"><span class="k">{e(T["nextp"])}</span><b>{e(nx["name"])}</b><span>{e(C["proj"][nx["id"]]["sub"])}</span></button></div>
</article>'''


def hero_title(s):
    a, _, rest = s.partition("*")
    m, _, z = rest.partition("*")
    return f"{e(a)}<em>{e(m)}</em>{e(z)}"


def render(lang, C, ver, all_c):
    b = "./" if lang == "en" else "../"
    rtl = lang in RTL
    T = C["ui"]
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{SITE_URL}{page_path(l)}">' for l in LANGS)
    alts += f'<link rel="alternate" hreflang="x-default" href="{SITE_URL}">'
    gf = ""
    if lang in GFONTS:
        gf = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
              f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={GFONTS[lang]}&display=swap">')
    og_alt = "".join(f'<meta property="og:locale:alternate" content="{OG_LOCALE[l]}">' for l in LANGS if l != lang)
    ld = {"@context": "https://schema.org", "@type": "Person", "name": "Matheus Teixeira", "url": SITE_URL,
          "jobTitle": C["role"].replace(" · ", ", "), "email": f"mailto:{EMAIL}",
          "address": {"@type": "PostalAddress", "addressLocality": "Santos", "addressCountry": "BR"},
          "alumniOf": [{"@type": "CollegeOrUniversity", "name": "Centro Universitário FEI"}, {"@type": "CollegeOrUniversity", "name": "Universidade de São Paulo"}],
          "sameAs": [LINKS["github"], LINKS["linkedin"], LINKS["orcid"]]}
    langmenu = "".join(
        f'<li><a href="{b}{page_path(l)}" hreflang="{l}" lang="{l}"{" aria-current=\"page\"" if l == lang else ""}>{e(all_c[l]["name"])}</a></li>' for l in LANGS)
    nav = C["nav"]

    # Projects section: one tile per planet; the whole tile flies you to it.
    cards = []
    for i, p in enumerate(PROJECTS):
        P = C["proj"][p["id"]]
        if p["id"] in SHOTS:
            f0 = SHOTS[p["id"]][0][0]
            # The image is set from data-src when the tile nears the screen (main.js), so it never competes
            # with the first screen; <noscript> keeps it for visitors without JavaScript.
            im = (f'src="{b}assets/img/{f0}-s.webp" srcset="{b}assets/img/{f0}-s.webp 720w, {b}assets/img/{f0}.webp 1440w" '
                  f'sizes="(max-width: 700px) 92vw, (max-width: 1000px) 46vw, 560px" width="1440" height="900" alt="{e(P["shots"][0])}" decoding="async"')
            fig = (f'<div class="pt-img"><img {"data-" + im.replace(" srcset=", " data-srcset=")}><noscript><img {im}></noscript></div>')
        else:
            fig = f'<div class="pt-img"><canvas data-viz="{p["id"]}" width="800" height="500" role="img" aria-label="{e(P["viz"])}"></canvas></div>'
        cards.append(f'''<article class="pt" id="p-{p["id"]}" style="--c:{p["col"]}">{fig}
<div class="pt-b"><span class="k">{e(T["planet"].format(n=i + 1))} · {e(P["world"])}</span><h3>{e(p["name"])}</h3><p class="s">{e(P["sub"])}</p><p>{e(P["sum"])}</p>
<ul class="tg">{"".join(f"<li>{e(t)}</li>" for t in p["tags"])}</ul>
<button class="land pt-go" type="button" data-i="{i}" aria-label="{e(T["landBtn"])}: {e(p["name"])}">{e(T["landBtn"])} <span aria-hidden="true">→</span></button></div></article>''')

    ed = []
    for i, it in enumerate(C["education"]["items"]):
        link = ""
        if i == 0:
            link = ext_link(LINKS["iris"], it["a"])
        elif i == 1:
            link = ext_link(LINKS["qml"], it["a"])
        ed.append(f'<div class="ec{" pl" if i == 3 else ""}"><span class="y">{e(it["y"])}</span><h3>{e(it["t"])}</h3><div class="w">{e(it["w"])}</div><p>{e(it["p"])}</p><em>{e(it["em"])}</em>{link}</div>')
    xp = "".join(f'<div class="xr"><span class="y">{e(it["y"])}</span><div><h3>{e(it["t"])}</h3><div class="w">{e(it["w"])}</div><p>{e(it["p"])}</p></div></div>' for it in C["experience"]["items"])
    tools = "".join(f'<div><h3>{e(h)}</h3><ul>{"".join(f"<li>{e(x)}</li>" for x in TOOLS[i])}</ul></div>' for i, h in enumerate(C["tools"]["groups"]))
    facts = "".join(f'<div><dt>{e(a)}</dt><dd>{e(v)}</dd></div>' for a, v in C["about"]["facts"])
    footlangs = "".join(f'<a href="{b}{page_path(l)}" hreflang="{l}" lang="{l}"{" aria-current=\"page\"" if l == lang else ""}>{e(all_c[l]["name"])}</a>' for l in LANGS)
    tm = C["about"]["term"]
    pr = '<span class="pp">matheus@orbit</span><span class="pc">:~$</span> '
    term = (f'<div class="term" lang="{lang}" aria-label="Terminal"><div class="tb"><i></i><i></i><i></i><span>matheus — zsh</span></div><pre>'
            f'{pr}<b>whoami</b>\n{e(tm["who"])}\n{pr}<b>cat now.txt</b>\n{e(chr(10).join(tm["now"]))}\n'
            f'{pr}<b>ls ~/shipped</b>\n<span class="ls">isaac3d.com/  amadeosheets.com/  liderplustelemedicina.com.br/  brectus/  allwinner/  quantum-ml-healthcare/</span>\n'
            f'{pr}<b>echo $LANG</b>\n{e(tm["lang"])}\n{pr}<span class="cur"></span></pre></div>')
    wl_svg, wl_list = worldline(C, rtl)
    studies = "".join(case_study(i, p, C, b, lang) for i, p in enumerate(PROJECTS))

    site = {"lang": lang, "base": b, "rtl": rtl, "email": EMAIL,
            "t": {k: T[k] for k in T},
            "projects": [dict(id=p["id"], name=p["name"], col=p["col"], kind=p["kind"], urls=p["urls"], tags=p["tags"], orbit=p["orbit"], site=p["site"],
                              **{k: C["proj"][p["id"]][k] for k in ("sub", "world", "viz")}) for p in PROJECTS]}
    # Page data for the scripts, as JSON (not inline script) so the CSP can stay script-src 'self'.
    site_json = json.dumps(site, ensure_ascii=False).replace("</", "<\\/")
    title = C["meta"]["title"]
    H = C["hero"]
    return f'''<!doctype html>
<html lang="{lang}" dir="{"rtl" if rtl else "ltr"}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(C["meta"]["desc"])}">
<meta name="author" content="Matheus Teixeira">
<meta name="theme-color" content="#03040a">
<meta name="color-scheme" content="dark">
<link rel="canonical" href="{SITE_URL}{page_path(lang)}">
{alts}
<meta property="og:type" content="website"><meta property="og:site_name" content="Matheus Teixeira"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(C["meta"]["desc"])}"><meta property="og:url" content="{SITE_URL}{page_path(lang)}"><meta property="og:image" content="{SITE_URL}og.png?v={OG_V}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:locale" content="{OG_LOCALE[lang]}">{og_alt}
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{b}favicon.svg" type="image/svg+xml"><link rel="icon" href="{b}favicon.png" sizes="64x64" type="image/png"><link rel="apple-touch-icon" href="{b}apple-touch-icon.png">
<link rel="preload" href="{b}assets/fonts/unbounded-800.woff2" as="font" type="font/woff2" crossorigin fetchpriority="high">
<link rel="preload" href="{b}assets/fonts/space-grotesk-400.woff2" as="font" type="font/woff2" crossorigin fetchpriority="high">
<link rel="preload" href="{b}assets/fonts/jetbrains-mono-600.woff2" as="font" type="font/woff2" crossorigin fetchpriority="high">
<link rel="preload" href="{b}assets/fonts/jetbrains-mono-400.woff2" as="font" type="font/woff2" crossorigin>
<style>html{{background:#03040a;color:#e8f0ff}}</style>
<noscript><style>.intro,.top>*{{opacity:1;animation:none}}</style></noscript>
{gf}
<link rel="stylesheet" href="{b}assets/css/site.css?v={ver}">
<script src="{b}assets/js/fonts.js?v={ver}" async></script>
<link rel="preload" href="{b}assets/js/sky.js?v={ver}" as="script">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">{e(C["skip"])}</a>
<header class="top"><a class="brand" href="#top">Matheus Teixeira</a>
<nav aria-label="{e(nav["sections"])}"><a href="#about">{e(nav["about"])}</a><a href="#projects">{e(nav["projects"])}</a><a href="#roadmap">{e(nav["roadmap"])}</a><a href="#education">{e(nav["education"])}</a><a href="#experience">{e(nav["experience"])}</a><a href="#contact">{e(nav["contact"])}</a></nav>
<details class="mnav"><summary aria-label="{e(nav["sections"])}"><i></i><i></i><i></i></summary><ul><li><a href="#about">{e(nav["about"])}</a></li><li><a href="#projects">{e(nav["projects"])}</a></li><li><a href="#roadmap">{e(nav["roadmap"])}</a></li><li><a href="#education">{e(nav["education"])}</a></li><li><a href="#experience">{e(nav["experience"])}</a></li><li><a href="#contact">{e(nav["contact"])}</a></li></ul></details>
<details class="lang"><summary aria-label="{e(nav["lang"])}: {lang.upper()}">{lang.upper()}</summary><ul>{langmenu}</ul></details></header>
<main id="main">
<section class="hero" id="top">
<div class="sky" id="sky"><canvas id="bg" aria-hidden="true"></canvas><img class="still" id="bhstill" src="{b}assets/bh/bh-still.webp?v={ver}" fetchpriority="high" alt="" aria-hidden="true"><canvas id="bh" aria-hidden="true"></canvas><canvas id="fg" aria-hidden="true"></canvas><noscript><picture class="nojs"><source media="(max-width:820px)" srcset="{b}assets/bh/sky-phone.webp" width="780" height="776"><img src="{b}assets/bh/sky-{"rtl" if rtl else "ltr"}.webp" alt="" width="1600" height="900"></picture></noscript><div class="shade"></div>
<div id="labs" role="group" aria-label="{e(T["planets"])}"></div></div>
<div class="intro"><span class="k">{e(C["role"])}</span>
<h1{" class=\"long\"" if len(H["h"]) > 48 else ""}>{hero_title(H["h"])}</h1>
<p>{e(H["p"])}</p>
<div class="row"><a class="btn" href="#projects">{e(H["cta"][0])}</a><a class="btn o" href="#about">{e(H["cta"][1])}</a></div></div>
</section>

<section class="sec" id="about" aria-labelledby="h-about"><div class="sh"><h2 id="h-about">{e(C["about"]["h"])}</h2></div>
<div class="ab"><div class="ab-l"><div class="pf"><i></i><b></b><img src="{b}assets/img/portrait-s.webp" srcset="{b}assets/img/portrait-s.webp 400w, {b}assets/img/portrait.webp 800w" sizes="222px" alt="{e(C["about"]["alt"])}" width="800" height="800" loading="lazy" decoding="async" fetchpriority="low"></div>
<dl>{facts}</dl><div class="ln"><a href="{LINKS["github"]}" target="_blank" rel="noopener">GitHub</a><a href="{LINKS["linkedin"]}" target="_blank" rel="noopener">LinkedIn</a><a href="{LINKS["orcid"]}" target="_blank" rel="noopener">ORCID</a><a href="/cv/Matheus-Teixeira-CV.pdf" download type="application/pdf">{e(T["cv"])}</a></div></div>
<div class="ab-r">{"".join(f"<p>{e(x)}</p>" for x in C["about"]["p"])}{term}</div></div></section>

<section class="sec" id="projects" aria-labelledby="h-projects"><div class="sh"><h2 id="h-projects">{e(C["projects"]["h"])}</h2><p>{e(C["projects"]["p"])}</p></div><div class="pj">{"".join(cards)}</div></section>

<section class="sec" id="roadmap" aria-labelledby="h-roadmap"><div class="sh"><h2 id="h-roadmap">{e(C["roadmap"]["h"])}</h2><p>{e(C["roadmap"]["p"])}</p></div>
<div class="wl">{wl_svg}{wl_list}</div></section>

<section class="sec" id="education" aria-labelledby="h-education"><div class="sh"><h2 id="h-education">{e(C["education"]["h"])}</h2></div><div class="ed">{"".join(ed)}</div></section>

<section class="sec" id="experience" aria-labelledby="h-experience"><div class="sh"><h2 id="h-experience">{e(C["experience"]["h"])}</h2></div>
<div class="xp"><div>{xp}</div><div class="pub"><span class="k">{e(C["pub"]["k"])}</span><h3 lang="en">{e(PAPER)}</h3><p>{e(C["pub"]["w"])}</p>{ext_link(LINKS["paper"], C["pub"]["a"])}</div></div></section>

<section class="sec" id="tools" aria-labelledby="h-tools"><div class="sh"><h2 id="h-tools">{e(C["tools"]["h"])}</h2></div><div class="to">{tools}</div></section>

<section class="sec" id="contact" aria-labelledby="h-contact"><div class="ct"><span class="k" id="h-contact">{e(C["contact"]["h"])}</span>
<p>{e(C["contact"]["p"])}</p>
<div class="em"><a href="mailto:{EMAIL}">{EMAIL}</a><button type="button" id="cp">{e(T["copy"])}</button><span class="sr" aria-live="polite" id="cpst"></span></div>
<div class="ln"><a href="{LINKS["github"]}" target="_blank" rel="noopener">GitHub</a><a href="{LINKS["linkedin"]}" target="_blank" rel="noopener">LinkedIn</a><a href="{LINKS["orcid"]}" target="_blank" rel="noopener">ORCID</a><a href="/cv/Matheus-Teixeira-CV.pdf" download type="application/pdf">{e(T["cv"])}</a></div></div></section>
</main>
<footer><div class="fr"><span>© 2026 Matheus Teixeira</span><nav class="fl" aria-label="{e(nav["lang"])}">{footlangs}</nav></div>
<details class="skynote"><summary>{e(C["sky"]["h"])}</summary>{"".join(f"<p>{e(x)}</p>" for x in C["sky"]["p"])}</details></footer>

<div class="world" id="world" hidden tabindex="-1" role="dialog" aria-modal="true">
<canvas id="wc" aria-hidden="true"></canvas><div class="wv"></div>
<div class="wbar"><button type="button" id="w-back"><span aria-hidden="true">←</span> {e(T["back"])}</button><span class="sp"></span><button type="button" id="w-prev"><span aria-hidden="true">‹</span> <span class="t">{e(T["prev"])}</span></button><button type="button" id="w-next"><span class="t">{e(T["next"])}</span> <span aria-hidden="true">›</span></button></div>
<div class="wp" id="wp">{studies}</div>
</div>
<script type="application/json" id="site-data">{site_json}</script>
<script src="{b}assets/js/sky.js?v={ver}" defer></script>
<script src="{b}assets/js/planet.js?v={ver}" defer></script>
<script src="{b}assets/js/viz.js?v={ver}" defer></script>
<script src="{b}assets/js/world.js?v={ver}" defer></script>
<script src="{b}assets/js/main.js?v={ver}" defer></script>
</body>
</html>
'''


def notfound(C, ver):
    N = C["nf"]
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(N["t"])} · Matheus Teixeira</title><meta name="robots" content="noindex"><link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/css/site.css?v={ver}">
<style>body{{min-height:100vh;display:grid;place-items:center;text-align:center;padding:24px}}h1{{font:800 clamp(40px,8vw,90px)/1 var(--fh);letter-spacing:-.05em;margin:14px 0}}p{{color:var(--soft);font-size:18px;margin:0 0 26px}}</style></head>
<body><main><span class="k">404</span><h1>{e(N["t"])}</h1><p>{e(N["p"])}</p><a class="btn" href="/">{e(N["a"])}</a></main></body></html>
'''


def main():
    global LANGS
    only = os.environ.get("ONLY", "").split(",") if os.environ.get("ONLY") else LANGS
    all_c = {l: load(l) for l in LANGS if l in only and (SRC / "content" / f"{l}.py").exists()}
    langs = [l for l in LANGS if l in all_c]
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    shutil.copytree(SRC / "assets", OUT / "assets", ignore=shutil.ignore_patterns("*.json"))
    for f in (SRC / "static").iterdir():
        if f.is_dir(): shutil.copytree(f, OUT / f.name, dirs_exist_ok=True)
        else: shutil.copy(f, OUT / f.name)
    h = hashlib.sha1()
    for f in sorted((SRC / "assets").rglob("*")):
        if f.is_file():
            h.update(f.read_bytes())
    ver = h.hexdigest()[:8]
    LANGS = langs
    for l in langs:
        d = OUT / page_path(l)
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(render(l, all_c[l], ver, all_c), encoding="utf-8")
    (OUT / "404.html").write_text(notfound(all_c["en"], ver), encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}sitemap.xml\n")
    urls = "".join(
        f'<url><loc>{SITE_URL}{page_path(l)}</loc>' + "".join(f'<xhtml:link rel="alternate" hreflang="{a}" href="{SITE_URL}{page_path(a)}"/>' for a in langs) + '</url>'
        for l in langs)
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">{urls}</urlset>\n')
    (OUT / ".nojekyll").write_text("")
    print("built", ", ".join(langs), "->", OUT, "version", ver)


if __name__ == "__main__":
    main()
