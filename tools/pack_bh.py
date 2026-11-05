"""Pack the Kerr geometry (kerr.py output) into one RGB PNG data map for the WebGL shader.

The map is W x 4H, four bands stacked vertically, every channel an exact byte (no alpha, so
browsers cannot premultiply it away):
  band 0: R,G = radius of the first disc crossing, 16 bits over [r_in, r_out] (0 = no crossing)
          B   = redshift factor g of that crossing, 8 bits over [0.2, 1.8]
  band 1: R,G = its azimuth phi, 16 bits over [0, 2 pi);  B = 255 where the ray falls into the hole
  band 2: as band 0 for the second crossing (the lensed image that forms the photon ring)
  band 3: R,G = azimuth of the second crossing;  B = 0
Rays launched within a few pixels of alpha = 0 pass over the poles, where Boyer-Lindquist
coordinates are singular; those columns are interpolated between their nearest good neighbours
(azimuth the short way round), so no seam shows down the middle of the image.
A half-resolution map (every second texel) is written for small screens.

usage: pack_bh.py kerr.npz out_dir [inclination_deg]
"""
import json
import sys

import numpy as np
from PIL import Image

d = np.load(sys.argv[1])
out = sys.argv[2]
W, H = int(d["W"]), int(d["H"])
rin, rout, a = float(d["rIn"]), float(d["rOut"]), float(d["a"])
hr = d["hit_r"].reshape(H, W, -1).copy()
hp = d["hit_phi"].reshape(H, W, -1).copy()
g = d["g"].reshape(H, W, -1).copy()
cap = d["captured"].reshape(H, W).copy()
cx = W // 2
L_, R_ = cx - 12, cx + 11                   # good columns either side of the polar gap (|alpha| > 0.35 M)
for c in range(L_ + 1, R_):
    w = (c - L_) / (R_ - L_)
    near = L_ if w < .5 else R_
    both = np.isfinite(hr[:, L_]) & np.isfinite(hr[:, R_])
    lin = lambda v: (1 - w) * v[:, L_] + w * v[:, R_]
    # azimuth: interpolate the short way round the circle
    dphi = np.angle(np.exp(1j * (hp[:, R_] - hp[:, L_])))
    hr[:, c] = np.where(both, lin(hr), hr[:, near])
    g[:, c] = np.where(both, lin(g), g[:, near])
    hp[:, c] = np.where(both, hp[:, L_] + w * dphi, hp[:, near])
    cap[:, c] = cap[:, near]


def bands(k):
    r = hr[..., k]
    ok = np.isfinite(r)
    q = np.where(ok, 1 + np.round((np.clip(r, rin, rout) - rin) / (rout - rin) * 65534), 0).astype(np.uint32)
    p = np.where(ok, np.round(np.mod(hp[..., k], 2 * np.pi) / (2 * np.pi) * 65535) % 65536, 0).astype(np.uint32)
    gg = np.where(ok, np.clip(np.round((g[..., k] - 0.2) / 1.6 * 255), 0, 255), 0).astype(np.uint32)
    third = cap.astype(np.uint32) * 255 if k == 0 else np.zeros_like(q)
    return np.dstack([q >> 8, q & 255, gg]), np.dstack([p >> 8, p & 255, third])


b0, b1 = bands(0)
b2, b3 = bands(1)
full = np.concatenate([b0, b1, b2, b3], 0).astype(np.uint8)
Image.fromarray(full, "RGB").save(out + "/bh-map.png", optimize=True)
half = np.concatenate([b[::2, ::2] for b in (b0, b1, b2, b3)], 0).astype(np.uint8)
Image.fromarray(half, "RGB").save(out + "/bh-map-s.png", optimize=True)
json.dump({"W": W, "H": H, "halfWidthM": float(d["halfWidthM"]), "a": a, "rIn": rin, "rOut": rout,
           "inclinationDeg": float(sys.argv[3]) if len(sys.argv) > 3 else 85.0, "gLo": 0.2, "gHi": 1.8}, open(out + "/bh.json", "w"), indent=1)
print("ok", W, H)
