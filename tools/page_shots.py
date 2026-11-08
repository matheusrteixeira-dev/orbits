"""Cut a full-page capture into the slices of a whole-page view (PAGES in tools/build.py).

    python3 tools/page_shots.py <capture.png> <name> <d|m>

d: a capture 1280 px wide (wide screens). m: a phone capture 390 px wide at 2x, so 780 px.
Writes src/assets/img/page/<name>-<kind>-<n>.webp, 1600 px tall each (the last one shorter), and prints
the heights to copy into PAGES. Needs Pillow; the site build itself does not.
"""
import sys
from pathlib import Path

from PIL import Image

SLICE = 1600
WIDTH = {"d": 1280, "m": 780}


def main(src, name, kind):
    im = Image.open(src).convert("RGB")
    if im.width != WIDTH[kind]:
        im = im.resize((WIDTH[kind], round(im.height * WIDTH[kind] / im.width)), Image.LANCZOS)
    out = Path(__file__).resolve().parent.parent / "src" / "assets" / "img" / "page"
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob(f"{name}-{kind}-*.webp"):
        old.unlink()
    heights = []
    for n, top in enumerate(range(0, im.height, SLICE)):
        part = im.crop((0, top, im.width, min(im.height, top + SLICE)))
        part.save(out / f"{name}-{kind}-{n}.webp", quality=80, method=6)
        heights.append(part.height)
    total = sum((out / f"{name}-{kind}-{n}.webp").stat().st_size for n in range(len(heights)))
    print(f'"{kind}": {heights}  # {len(heights)} slices, {total // 1024} KB')


if __name__ == "__main__":
    main(*sys.argv[1:4])
