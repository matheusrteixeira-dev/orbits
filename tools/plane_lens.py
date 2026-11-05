"""Exact light paths from the orbital plane to the camera, for the Orbits homepage.

The planets, their orbit lines and the asteroid belt all lie in the hole's
equatorial plane, between r = 26 M and r = 52 M. This script traces null
geodesics of the Kerr metric (a = 0.9, G = c = M = 1) backwards from the same
camera as tools/kerr.py (600 M away, 72 degrees from the spin axis) and records
where each ray crosses the equatorial plane, and how long the light took.

Inverting those crossings gives, for every point (r, phi) of the plane, where
its light lands on the screen and when:

  image 0: the direct image (first crossing of the backward ray)
  image 1: the secondary image, whose light first passes round the hole
           (second crossing), seen as a thin arc just outside the shadow

For each image the table holds alpha, beta (screen coordinates, in M at the
hole, Bardeen's convention) and the light travel time T to the camera, minus
the camera distance. phi is measured from the camera's azimuth, in the sense
of the hole's rotation, as in the browser code (0 = nearest point, 90 = right).

Output: src/assets/bh/plane.json (parameters, and the table as base64 little-endian Int16).
Usage: python3 tools/plane_lens.py [workers]
"""
import base64
import json
import sys
import time
from multiprocessing import Pool

import numpy as np
from scipy.interpolate import griddata

A = 0.9
INC = np.radians(72.0)
R0 = 600.0
R_H = 1 + np.sqrt(1 - A * A)
R_MIN, R_MAX, DR = 25.0, 53.0, 1.0          # table radii (M)
NPHI = 120                                   # table azimuths (3 degrees)
SCALE_XY, SCALE_T = 500.0, 50.0              # Int16 quantisation: 0.002 M and 0.02 M


def inv_metric(r, th):
    s2 = np.maximum(np.sin(th) ** 2, 1e-10)
    c2 = np.cos(th) ** 2
    sig = r * r + A * A * c2
    dl = r * r - 2 * r + A * A
    gtt = -((r * r + A * A) ** 2 - A * A * dl * s2) / (sig * dl)
    gtp = -2 * A * r / (sig * dl)
    gpp = (dl - A * A * s2) / (sig * dl * s2)
    return gtt, gtp, gpp, dl / sig, 1 / sig


def ham(r, th, pr, ph, Lz):
    gtt, gtp, gpp, grr, ghh = inv_metric(r, th)
    return 0.5 * (gtt + 2 * gtp * Lz + gpp * Lz * Lz + grr * pr * pr + ghh * ph * ph)


def rhs(r, th, pr, ph, Lz):
    """Hamilton's equations for the traced (time-reversed) photon, p_t = +1, plus dt/dlambda."""
    gtt, gtp, gpp, grr, ghh = inv_metric(r, th)
    er, eh = 1e-6 * r, 1e-6
    dHdr = (ham(r + er, th, pr, ph, Lz) - ham(r - er, th, pr, ph, Lz)) / (2 * er)
    dHdh = (ham(r, th + eh, pr, ph, Lz) - ham(r, th - eh, pr, ph, Lz)) / (2 * eh)
    return grr * pr, ghh * ph, gtp + gpp * Lz, -dHdr, -dHdh, gtt + gtp * Lz


def trace(args):
    """Trace rays for image-plane points (alpha, beta); return the first two equatorial crossings."""
    alpha, beta = args
    N = alpha.size
    L = alpha * np.sin(INC)                  # traced photon: L_t = alpha sin(i)
    r, th, phi, t = np.full(N, R0), np.full(N, INC), np.zeros(N), np.zeros(N)
    pth = -beta.copy()
    gtt, gtp, gpp, grr, ghh = inv_metric(r, th)
    pr = -np.sqrt(np.maximum(-(gtt + 2 * gtp * L + gpp * L * L + ghh * pth * pth), 0) / grr)
    hr, hp, ht = np.full((N, 2), np.nan), np.full((N, 2), np.nan), np.full((N, 2), np.nan)
    nh = np.zeros(N, np.int8)
    act = np.arange(N)
    for _ in range(6000):
        if not act.size:
            break
        rr, tt, pp, ti, qr, qh, Lz = r[act], th[act], phi[act], t[act], pr[act], pth[act], L[act]
        h = np.clip(0.02 * (rr - R_H), 0.002, 15.0)
        s = (rr, tt, qr, qh)
        k1 = rhs(*s, Lz)
        k2 = rhs(rr + h / 2 * k1[0], tt + h / 2 * k1[1], qr + h / 2 * k1[3], qh + h / 2 * k1[4], Lz)
        k3 = rhs(rr + h / 2 * k2[0], tt + h / 2 * k2[1], qr + h / 2 * k2[3], qh + h / 2 * k2[4], Lz)
        k4 = rhs(rr + h * k3[0], tt + h * k3[1], qr + h * k3[3], qh + h * k3[4], Lz)
        u = [h / 6 * (a + 2 * b + 2 * c + d) for a, b, c, d in zip(k1, k2, k3, k4)]
        rn, tn, pn, qrn, qhn, tin = rr + u[0], tt + u[1], pp + u[2], qr + u[3], qh + u[4], ti + u[5]
        cr = np.nonzero(np.sign(np.cos(tt)) != np.sign(np.cos(tn)))[0]
        if cr.size:
            c0, c1 = np.cos(tt[cr]), np.cos(tn[cr])
            f = c0 / (c0 - c1)
            g = act[cr]
            k = nh[g]
            room = k < 2
            g, k, cr, f = g[room], k[room], cr[room], f[room]
            hr[g, k] = rr[cr] + f * (rn[cr] - rr[cr])
            hp[g, k] = pp[cr] + f * (pn[cr] - pp[cr])
            ht[g, k] = -(ti[cr] + f * (tin[cr] - ti[cr]))    # travel time (the traced photon runs back in time)
            nh[g] += 1
        r[act], th[act], phi[act], t[act], pr[act], pth[act] = rn, tn, pn, tin, qrn, qhn
        done = (rn < R_H * 1.01) | ((rn > R0 * 1.05) & (qrn > 0)) | (nh[act] >= 2) | ~np.isfinite(rn)
        act = act[~done]
    return hr, hp, ht


def grid(a0, a1, b0, b1, d):
    a, b = np.meshgrid(np.arange(a0, a1 + 1e-9, d), np.arange(b0, b1 + 1e-9, d))
    return a.ravel(), b.ravel()


if __name__ == '__main__':
    workers = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    t0 = time.time()
    # Wide field for the direct images, fine field round the shadow for the secondary ones.
    parts = [grid(-62, 62, -34, 34, 0.15), grid(-9, 9, -9, 9, 0.025)]
    alpha = np.concatenate([p[0] for p in parts])
    beta = np.concatenate([p[1] for p in parts])
    # Rays with little angular momentum (|alpha| < 0.35 M) pass close to the pole, where the
    # Boyer-Lindquist integration loses accuracy; drop that thin column and let the interpolation bridge it.
    keep = np.abs(alpha) > 0.35
    alpha, beta = alpha[keep], beta[keep]
    chunks = np.array_split(np.arange(alpha.size), workers * 8)
    with Pool(workers) as pool:
        out = pool.map(trace, [(alpha[c], beta[c]) for c in chunks])
    hr = np.concatenate([o[0] for o in out])
    hp = np.concatenate([o[1] for o in out])
    ht = np.concatenate([o[2] for o in out])
    print(f"traced {alpha.size} rays in {time.time() - t0:.0f}s", flush=True)

    T0 = R0                                   # light-time reference: the camera distance
    rq = np.arange(R_MIN, R_MAX + 1e-9, DR)
    pq = np.arange(NPHI) * 2 * np.pi / NPHI
    RQ, PQ = np.meshgrid(rq, pq, indexing='ij')
    tab = np.zeros((2, 3, rq.size, NPHI))
    for k in range(2):
        ok = np.isfinite(hr[:, k]) & (hr[:, k] > R_MIN - 3) & (hr[:, k] < R_MAX + 3)
        x, y = hr[ok, k] * np.cos(hp[ok, k]), hr[ok, k] * np.sin(hp[ok, k])
        q = np.stack([RQ.ravel() * np.cos(PQ.ravel()), RQ.ravel() * np.sin(PQ.ravel())], 1)
        for j, v in enumerate([alpha[ok], beta[ok], ht[ok, k] - T0]):
            tab[k, j] = griddata(np.stack([x, y], 1), v, q, method='linear').reshape(RQ.shape)
        print(f"image {k}: {ok.sum()} crossings, missing cells {np.isnan(tab[k, 0]).sum()}", flush=True)
    # Check every entry by tracing its ray forward: the k-th crossing must land on the cell's own
    # (r, phi). Entries that miss (where the secondary image is squeezed too thin to sample) are
    # dropped; the browser then draws no image there.
    for k in range(2):
        a_, b_ = tab[k, 0].ravel(), tab[k, 1].ravel()
        ok = np.isfinite(a_) & (np.abs(a_) > 0.35)
        idx = np.nonzero(ok)[0]
        cs = np.array_split(idx, workers * 4)
        with Pool(workers) as pool:
            res = pool.map(trace, [(a_[c], b_[c]) for c in cs])
        cr = np.concatenate([o[0][:, k] for o in res])
        cp = np.concatenate([o[1][:, k] for o in res])
        rt, pt = RQ.ravel()[idx], PQ.ravel()[idx]
        dphi = np.angle(np.exp(1j * (cp - pt)))
        good = (np.abs(cr - rt) < 0.3) & (np.abs(dphi) * rt < 0.6)
        kill = np.zeros(a_.size, bool)        # rays near the pole (|alpha| <= 0.35) cannot be checked; kept
        kill[idx[~good]] = True
        kill[~np.isfinite(a_)] = True
        if k == 1:
            kill[np.abs(a_) <= 0.35] = True    # a secondary image needs the check; drop what cannot be checked
        print(f"image {k}: median miss {np.median(np.abs(cr - rt)[good]):.3f} M in r", flush=True)
        for j in range(3):
            v = tab[k, j].ravel()
            v[kill] = np.nan
            tab[k, j] = v.reshape(RQ.shape)
        print(f"image {k}: {good.sum()} of {a_.size} entries verified by forward tracing", flush=True)
    bad = ~np.isfinite(tab)
    q16 = np.where(bad, -32768, np.round(tab * np.array([SCALE_XY, SCALE_XY, SCALE_T])[None, :, None, None])).astype('<i2')
    json.dump({'rMin': R_MIN, 'dr': DR, 'nr': int(rq.size), 'nphi': NPHI, 'scaleXY': SCALE_XY, 'scaleT': SCALE_T,
               'layout': 'int16[image 0..1][alpha, beta, T - R0][r][phi], little-endian, base64; -32768 = no image',
               'a': A, 'inclinationDeg': 72.0, 'camera': R0,
               'data': base64.b64encode(q16.tobytes()).decode()}, open('src/assets/bh/plane.json', 'w'), separators=(',', ':'))
    # Sanity: compare with the flat-space projection and the weak-field lens at a few points.
    for r_, f_ in [(28, 0), (28, 90), (28, 180), (44, 180), (44, 270)]:
        i, j = int(round((r_ - R_MIN) / DR)), int(round(f_ / 3))
        print(f"r {r_} phi {f_}: image0 ({tab[0, 0, i, j]:.2f}, {tab[0, 1, i, j]:.2f}) T {tab[0, 2, i, j]:.1f};"
              f" flat ({r_ * np.sin(np.radians(f_)):.2f}, {-r_ * np.cos(np.radians(f_)) * np.cos(INC):.2f});"
              f" image1 ({tab[1, 0, i, j]:.2f}, {tab[1, 1, i, j]:.2f})")
    print(f"saved in {time.time() - t0:.0f}s")
