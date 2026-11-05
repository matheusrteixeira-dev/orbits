"""Kerr black hole ray tracer for the Orbits homepage.

Units G = c = M = 1. Spin a = 0.9. Null geodesics are integrated backwards
from a distant observer with Hamilton's equations in Boyer-Lindquist
coordinates (the traced, time-reversed photon has p_t = +1 and p_phi = L conserved; r, theta, p_r, p_theta evolved
with RK4, derivatives of H by central differences). Initial conditions come
from Bardeen's image-plane coordinates (alpha, beta).

The thin disc lies in the equatorial plane from the prograde ISCO to R_OUT.
For each pixel the first two disc crossings are stored (direct image and the
lensed image that forms the photon ring), with the redshift factor
g = 1 / (u^t (1 - Omega L)) of a circular prograde Keplerian emitter,
Omega = 1 / (r^1.5 + a). The browser only rotates the disc texture with
Omega(r) over time, so every frame shares the same geodesics.

Output: three RGBA PNGs (values premultiplied by a hit flag so that linear
filtering gives soft, correct edges) and a JSON file with the parameters.
"""
import json
import sys
import time

import numpy as np
from PIL import Image

W, H = int(sys.argv[1]), int(sys.argv[2])
OUT = sys.argv[3]
A = float(sys.argv[4]) if len(sys.argv) > 4 else 0.9
INC_DEG = float(sys.argv[5]) if len(sys.argv) > 5 else 85.0
INC = np.radians(INC_DEG)       # observer angle from the spin axis
R0 = 600.0                      # observer distance
HALF_W = 26.0                   # image half-width in units of M
R_OUT = 24.0
Z1 = 1 + (1 - A * A) ** (1 / 3) * ((1 + A) ** (1 / 3) + (1 - A) ** (1 / 3))
Z2 = np.sqrt(3 * A * A + Z1 * Z1)
R_IN = 3 + Z2 - np.sqrt((3 - Z1) * (3 + Z1 + 2 * Z2))   # prograde ISCO
R_H = 1 + np.sqrt(1 - A * A)
print(f"ISCO {R_IN:.4f}  horizon {R_H:.4f}", flush=True)

t0 = time.time()
j, i = np.mgrid[0:H, 0:W].astype(np.float64)
scale = 2 * HALF_W / W
alpha = ((i + 0.5) - W / 2) * scale
beta = -((j + 0.5) - H / 2) * scale
alpha, beta = alpha.ravel(), beta.ravel()
N = alpha.size

# Traced photon is the time reverse of the physical one: p -> -p, so p_t = +1,
# L_t = -L_phys = alpha sin(i) (Bardeen: L_phys = -alpha sin i) and p_theta,t = -beta.
L = alpha * np.sin(INC)
L_phys = -L


def inv_metric(r, th):
    s2 = np.maximum(np.sin(th) ** 2, 1e-10)
    c2 = np.cos(th) ** 2
    sig = r * r + A * A * c2
    dl = r * r - 2 * r + A * A
    gtt = -((r * r + A * A) ** 2 - A * A * dl * s2) / (sig * dl)
    gtp = -2 * A * r / (sig * dl)
    gpp = (dl - A * A * s2) / (sig * dl * s2)
    grr = dl / sig
    ghh = 1 / sig
    return gtt, gtp, gpp, grr, ghh


def ham(r, th, pr, ph, Lz):
    gtt, gtp, gpp, grr, ghh = inv_metric(r, th)
    return 0.5 * (gtt + 2 * gtp * Lz + gpp * Lz * Lz + grr * pr * pr + ghh * ph * ph)


def rhs(r, th, pr, ph, Lz):
    gtt, gtp, gpp, grr, ghh = inv_metric(r, th)
    er = 1e-6 * r
    eh = 1e-6
    dHdr = (ham(r + er, th, pr, ph, Lz) - ham(r - er, th, pr, ph, Lz)) / (2 * er)
    dHdh = (ham(r, th + eh, pr, ph, Lz) - ham(r, th - eh, pr, ph, Lz)) / (2 * eh)
    return grr * pr, ghh * ph, gtp + gpp * Lz, -dHdr, -dHdh


r = np.full(N, R0)
th = np.full(N, INC)
phi = np.zeros(N)
pth = -beta.copy()
gtt, gtp, gpp, grr, ghh = inv_metric(r, th)
rest = gtt + 2 * gtp * L + gpp * L * L + ghh * pth * pth
pr = -np.sqrt(np.maximum(-rest, 0) / grr)

MAXHIT = 2
hit_r = np.zeros((N, MAXHIT))
hit_phi = np.zeros((N, MAXHIT))
nhit = np.zeros(N, dtype=np.int8)
captured = np.zeros(N, dtype=bool)
active = np.arange(N)
step = 0
while active.size and step < 4000:
    rr, tt, pp, qr, qh, Lz = r[active], th[active], phi[active], pr[active], pth[active], L[active]
    h = np.clip(0.02 * (rr - R_H), 0.002, 15.0)
    k1 = rhs(rr, tt, qr, qh, Lz)
    k2 = rhs(rr + h / 2 * k1[0], tt + h / 2 * k1[1], qr + h / 2 * k1[3], qh + h / 2 * k1[4], Lz)
    k3 = rhs(rr + h / 2 * k2[0], tt + h / 2 * k2[1], qr + h / 2 * k2[3], qh + h / 2 * k2[4], Lz)
    k4 = rhs(rr + h * k3[0], tt + h * k3[1], qr + h * k3[3], qh + h * k3[4], Lz)
    upd = [h / 6 * (a1 + 2 * a2 + 2 * a3 + a4) for a1, a2, a3, a4 in zip(k1, k2, k3, k4)]
    rn, tn, pn = rr + upd[0], tt + upd[1], pp + upd[2]
    qrn, qhn = qr + upd[3], qh + upd[4]

    # Equatorial-plane crossings: cos(theta) changes sign.
    cross = np.sign(np.cos(tt)) != np.sign(np.cos(tn))
    if cross.any():
        idx = np.nonzero(cross)[0]
        c0, c1 = np.cos(tt[idx]), np.cos(tn[idx])
        f = c0 / (c0 - c1)
        rq = rr[idx] + f * (rn[idx] - rr[idx])
        pq = pp[idx] + f * (pn[idx] - pp[idx])
        ok = (rq >= R_IN) & (rq <= R_OUT)
        g = active[idx[ok]]
        rq, pq = rq[ok], pq[ok]
        slot = nhit[g]
        room = slot < MAXHIT
        g, rq, pq, slot = g[room], rq[room], pq[room], slot[room]
        hit_r[g, slot] = rq
        hit_phi[g, slot] = pq
        nhit[g] += 1

    r[active], th[active], phi[active], pr[active], pth[active] = rn, tn, pn, qrn, qhn
    cap = rn < R_H * 1.01
    esc = (rn > R0 * 1.05) & (qrn > 0)
    full = nhit[active] >= MAXHIT
    bad = ~np.isfinite(rn)
    captured[active[cap | bad]] = True
    active = active[~(cap | esc | full | bad)]
    step += 1
    if step % 250 == 0:
        print(f"step {step} active {active.size} {time.time() - t0:.0f}s", flush=True)
print("integration done", step, f"{time.time() - t0:.0f}s", flush=True)

# Redshift of a circular prograde emitter at the hit radius.
rh = np.where(hit_r > 0, hit_r, 10.0)
om = 1 / (rh ** 1.5 + A)
g_tt = -(1 - 2 / rh)
g_tp = -2 * A / rh
g_pp = rh * rh + A * A + 2 * A * A / rh
ut = 1 / np.sqrt(np.maximum(-(g_tt + 2 * g_tp * om + g_pp * om * om), 1e-9))
gfac = 1 / (ut * (1 - om * L_phys[:, None]))
flag = (hit_r > 0).astype(np.float64)

G_LO, G_HI = 0.2, 1.8


def to8(v):
    return np.clip(np.round(v * 255), 0, 255).astype(np.uint8)


def plane(k):
    rn = (hit_r[:, k] - R_IN) / (R_OUT - R_IN)
    c = (np.cos(hit_phi[:, k]) + 1) / 2
    s = (np.sin(hit_phi[:, k]) + 1) / 2
    f = flag[:, k]
    return np.stack([to8(rn * f), to8(c * f), to8(s * f), to8(f)], 1).reshape(H, W, 4)


gn = (gfac - G_LO) / (G_HI - G_LO)
aux = np.stack([to8(gn[:, 0] * flag[:, 0]), to8(gn[:, 1] * flag[:, 1]), to8(captured.astype(float)), np.full(N, 255, np.uint8)], 1).reshape(H, W, 4)
np.savez_compressed(OUT + '.npz', W=W, H=H, halfWidthM=HALF_W, a=A, rIn=R_IN, rOut=R_OUT,
                    hit_r=np.where(flag > 0, hit_r, np.nan).astype(np.float32), hit_phi=hit_phi.astype(np.float32),
                    g=gfac.astype(np.float32), captured=captured)
Image.fromarray(plane(0), 'RGBA').save(OUT + '-hit1.png', optimize=True)
Image.fromarray(plane(1), 'RGBA').save(OUT + '-hit2.png', optimize=True)
Image.fromarray(aux, 'RGBA').save(OUT + '-aux.png', optimize=True)
json.dump({'W': W, 'H': H, 'halfWidthM': HALF_W, 'a': A, 'inclinationDeg': INC_DEG, 'rIn': R_IN, 'rOut': R_OUT,
           'rHorizon': R_H, 'gLo': G_LO, 'gHi': G_HI}, open(OUT + '.json', 'w'), indent=1)
left = gfac[(alpha < -5) & (flag[:, 0] > 0), 0].mean()
right = gfac[(alpha > 5) & (flag[:, 0] > 0), 0].mean()
cap_rows = captured.reshape(H, W)[H // 2]
xs = np.nonzero(cap_rows)[0]
print(f"mean g left {left:.3f} right {right:.3f}; shadow on the midline from alpha {(xs.min() + .5 - W / 2) * scale:.2f} to {(xs.max() + .5 - W / 2) * scale:.2f}", flush=True)
print("saved", f"{time.time() - t0:.0f}s")
