"""Shade the Kerr geometry from kerr.py into a seamless loop of RGBA frames.

Follows the profile README banner (shade.py): Novikov-Thorne-like flux
F ~ r^-3 (1 - sqrt(r_in/r)), local temperature T ~ F^(1/4), observed
temperature g*T and beaming g^3, blackbody colours, front-to-back alpha
compositing of the direct and lensed disc images, bloom and a filmic tone
map. Differences: the background is left transparent (the page draws the
stars and the planets behind the hole), and the disc turns at the Kerr
rate Omega = 1 / (r^1.5 + a), rounded to whole turns per loop.

usage: shade2.py geo.npz frames out_prefix out_width
"""
import sys

import numpy as np
from PIL import Image, ImageFilter

geo = np.load(sys.argv[1])
NFR, OUT, OW = int(sys.argv[2]), sys.argv[3], int(sys.argv[4])
W, H = int(geo["W"]), int(geo["H"])
hit_r, hit_phi, g, captured = geo["hit_r"], geo["hit_phi"], geo["g"], geo["captured"]
A, R_IN, R_OUT = float(geo["a"]), float(geo["rIn"]), float(geo["rOut"])


def bb_rgb(T):
    lam = np.linspace(380e-9, 780e-9, 81)
    h, c, k = 6.626e-34, 2.998e8, 1.381e-23

    def g_(x, mu, s1, s2):
        return np.exp(-0.5 * ((x - mu) / np.where(x < mu, s1, s2)) ** 2)
    l = lam * 1e9
    xb = 1.056 * g_(l, 599.8, 37.9, 31.0) + 0.362 * g_(l, 442.0, 16.0, 26.7) - 0.065 * g_(l, 501.1, 20.4, 26.2)
    yb = 0.821 * g_(l, 568.8, 46.9, 40.5) + 0.286 * g_(l, 530.9, 16.3, 31.1)
    zb = 1.217 * g_(l, 437.0, 11.8, 36.0) + 0.681 * g_(l, 459.0, 26.0, 13.8)
    out = []
    for t in T:
        B = 1.0 / lam ** 5 / (np.exp(h * c / (lam * k * t)) - 1.0)
        X, Y, Z = (B * xb).sum(), (B * yb).sum(), (B * zb).sum()
        rgb = np.array([[3.2406, -1.5372, -0.4986], [-0.9689, 1.8758, 0.0415], [0.0557, -0.2040, 1.0570]]) @ np.array([X, Y, Z])
        rgb = np.clip(rgb, 0, None)
        out.append(rgb / rgb.max())
    return np.array(out)


TT = np.linspace(1500, 12000, 256)
TAB = bb_rgb(TT)


def colour(T):
    return TAB[np.clip((T - TT[0]) / (TT[-1] - TT[0]) * 255, 0, 255).astype(int)]


# Whole turns per loop, proportional to the Kerr angular velocity at each radius.
OM_IN = 1 / (R_IN ** 1.5 + A)


def turns(r):
    return np.maximum(1, np.round(3 * (1 / (r ** 1.5 + A)) / OM_IN))


def texture(r, phi, t):
    lr = np.log(r)
    ph = phi - 2 * np.pi * turns(r) * t
    n = np.zeros_like(r)
    gen = np.random.default_rng(9)
    for _ in range(22):
        m = gen.integers(1, 7)
        kr = gen.uniform(2, 22)
        a = gen.uniform(0.3, 1.0) / (1 + 0.05 * m)
        n += a * np.cos(m * ph + kr * lr + gen.uniform(0, 2 * np.pi))
    n = n / 4.0
    rings = 0.88 + 0.12 * np.cos(55 * lr + 0.7) * np.cos(23 * lr + 1.3)
    return np.clip(0.62 + 0.38 * np.tanh(n), 0, 1.4) * rings


def F(r):
    return r ** -3 * np.clip(1 - np.sqrt(R_IN / r), 0, None)


FMAX = F(np.linspace(R_IN, R_OUT, 4000)).max()
T_IN = 9000.0
cx = W // 2


def frame(t):
    trans = np.ones(W * H, np.float32)
    acc = np.zeros((W * H, 3), np.float32)
    for k in range(hit_r.shape[1]):
        m = np.isfinite(hit_r[:, k])
        r, ph, gg = hit_r[m, k], hit_phi[m, k], g[m, k]
        flux = F(r) / FMAX
        Tobs = np.clip(gg * T_IN * flux ** 0.25, 1500, 12000)
        edge = np.clip((r - R_IN) / 0.4, 0, 1) * np.clip((R_OUT - r) / 9.0, 0, 1) ** 1.5
        dens = texture(r, ph, t) * edge
        I = gg ** 3 * flux * dens * 8.0
        alpha = np.clip(dens * 0.95, 0, 0.97)
        acc[m] += trans[m, None] * alpha[:, None] * colour(Tobs) * I[:, None]
        trans[m] *= 1 - alpha
    img = acc.reshape(H, W, 3) * np.array([1.08, 0.93, 0.78])
    # Rays launched within a few pixels of alpha = 0 pass over the poles, where Boyer-Lindquist
    # coordinates are singular; interpolate those columns from their neighbours before the bloom.
    tr2 = trans.reshape(H, W)
    for d in range(-5, 5):
        f = (d + 6) / 11
        img[:, cx + d] = img[:, cx - 6] * (1 - f) + img[:, cx + 5] * f
        tr2[:, cx + d] = tr2[:, cx - 6] * (1 - f) + tr2[:, cx + 5] * f
    lum = np.clip(img - 0.55, 0, None)
    pil = Image.fromarray(np.clip(lum / 4 * 255, 0, 255).astype(np.uint8))
    b1 = np.asarray(pil.filter(ImageFilter.GaussianBlur(W / 160)), np.float32) / 255 * 4
    b2 = np.asarray(pil.filter(ImageFilter.GaussianBlur(W / 40)), np.float32) / 255 * 4
    img = img + 0.55 * b1 + 0.45 * b2
    img = (1 - np.exp(-1.5 * img)) ** (1 / 1.1)
    # Opacity: the shadow (and the disc in front of it) is opaque; light elsewhere is drawn as glow.
    cap2 = captured.reshape(H, W).astype(np.float32)
    cap2[:, cx - 5:cx + 5] = np.maximum(cap2[:, cx - 6:cx - 5], cap2[:, cx + 5:cx + 6])
    occ = cap2 * (tr2 > 0.5)
    al = np.clip(np.maximum(occ, img.max(2) * 1.15), 0, 1)
    rgb = np.where(al[..., None] > 1e-4, img / np.maximum(al[..., None], 1e-4), 0)
    out = np.dstack([np.clip(rgb, 0, 1), al])
    im = Image.fromarray(np.round(out * 255).astype(np.uint8), 'RGBA')
    return im.resize((OW, round(OW * H / W)), Image.LANCZOS)


for f in range(NFR):
    frame(f / NFR).save(f"{OUT}_{f:02d}.webp", quality=82, method=6)
    print("frame", f, flush=True)
