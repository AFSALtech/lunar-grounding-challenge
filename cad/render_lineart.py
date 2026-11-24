#!/usr/bin/env python3
"""Orthographic technical line drawing: all mesh edges, z-buffer hidden-line removal."""
import struct
import sys
import numpy as np
from PIL import Image, ImageDraw


def load_stl(path):
    with open(path, "rb") as f:
        f.read(80)
        n = struct.unpack("<I", f.read(4))[0]
        data = np.frombuffer(f.read(n * 50), dtype=np.uint8).reshape(n, 50)
    floats = data[:, :48].copy().view("<f4").reshape(n, 4, 3)
    tris = floats[:, 1:, :].astype(np.float64)
    return tris


def rot_x(deg):
    a = np.radians(deg); c, s = np.cos(a), np.sin(a)
    return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])


def rot_z(deg):
    a = np.radians(deg); c, s = np.cos(a), np.sin(a)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])


def line_art(tris, R, size=1800, ss=2, line=(15, 15, 15), bg=(255, 255, 255),
             zoom=None, center=None, edge_filter=True):
    S = size * ss
    tris_r = tris @ R.T
    v0, v1, v2 = tris_r[:, 0], tris_r[:, 1], tris_r[:, 2]
    fn = np.cross(v1 - v0, v2 - v0)
    flen = np.linalg.norm(fn, axis=1, keepdims=True)
    fn = np.divide(fn, flen, out=np.zeros_like(fn), where=flen > 1e-12)

    pts = tris_r.reshape(-1, 3)
    if center is None:
        center = (pts.min(0) + pts.max(0)) / 2
    if zoom is None:
        extent = float((pts.max(0) - pts.min(0)).max())
        zoom = 0.92 * S / max(extent, 1e-6)

    px = (tris_r[..., 0] - center[0]) * zoom + S / 2
    py = -(tris_r[..., 1] - center[1]) * zoom + S / 2
    pz = tris_r[..., 2]

    # z-buffer from faces
    zbuf = np.full((S, S), -1e30)
    for i in range(len(tris_r)):
        x0, y0, z0 = px[i, 0], py[i, 0], pz[i, 0]
        x1, y1, z1 = px[i, 1], py[i, 1], pz[i, 1]
        x2, y2, z2 = px[i, 2], py[i, 2], pz[i, 2]
        minx = int(max(0, np.floor(min(x0, x1, x2))))
        maxx = int(min(S - 1, np.ceil(max(x0, x1, x2))))
        miny = int(max(0, np.floor(min(y0, y1, y2))))
        maxy = int(min(S - 1, np.ceil(max(y0, y1, y2))))
        if minx > maxx or miny > maxy:
            continue
        xs = np.arange(minx, maxx + 1) + 0.5
        ys = np.arange(miny, maxy + 1) + 0.5
        gx, gy = np.meshgrid(xs, ys)
        den = (y1 - y2) * (x0 - x2) + (x2 - x1) * (y0 - y2)
        if abs(den) < 1e-12:
            continue
        w0 = ((y1 - y2) * (gx - x2) + (x2 - x1) * (gy - y2)) / den
        w1 = ((y2 - y0) * (gx - x2) + (x0 - x2) * (gy - y2)) / den
        w2 = 1 - w0 - w1
        mask = (w0 >= 0) & (w1 >= 0) & (w2 >= 0)
        if not mask.any():
            continue
        z = w0 * z0 + w1 * z1 + w2 * z2
        yi, xi = np.where(mask)
        zz = z[yi, xi]
        sub = zbuf[miny + yi, minx + xi]
        upd = zz > sub
        zbuf[miny + yi[upd], minx + xi[upd]] = zz[upd]

    # unique edges
    V = tris_r.reshape(-1, 3)
    q = np.round(V, 4)
    uniq, inv = np.unique(q, axis=0, return_inverse=True)
    faces = inv.reshape(-1, 3)
    edge_faces = {}
    for fi, (a, b, c) in enumerate(faces):
        for e in ((a, b), (b, c), (c, a)):
            key = (e[0], e[1]) if e[0] < e[1] else (e[1], e[0])
            edge_faces.setdefault(key, []).append(fi)

    front = fn[:, 2] > 1e-9
    drawable = []
    for key, flist in edge_faces.items():
        if len(flist) == 1:
            drawable.append(key)  # boundary
        elif len(flist) == 2:
            f0, f1 = flist
            if front[f0] != front[f1]:
                drawable.append(key)  # silhouette
            else:
                dot = float(np.clip(fn[f0] @ fn[f1], -1, 1))
                ang = np.degrees(np.arccos(dot))
                if ang > 35.0:
                    drawable.append(key)  # sharp feature
                # else smooth — skip to reduce noise (cylinder facets)
        else:
            # non-manifold: keep as feature
            drawable.append(key)

    def edge_visible(p0, p1):
        t = np.linspace(0, 1, 20)
        pe = p0[None, :] * (1 - t[:, None]) + p1[None, :] * t[:, None]
        ex = (pe[:, 0] - center[0]) * zoom + S / 2
        ey = -(pe[:, 1] - center[1]) * zoom + S / 2
        ez = pe[:, 2]
        xi = np.clip(ex, 0, S - 1).astype(int)
        yi = np.clip(ey, 0, S - 1).astype(int)
        zb = zbuf[yi, xi]
        tol = 2.0 / zoom + 1.5
        vis = ez >= (zb - tol)
        return vis.mean() > 0.20

    img = Image.new("RGB", (S, S), bg)
    draw = ImageDraw.Draw(img)
    lw = max(2, ss)

    for a, b in drawable:
        p0, p1 = uniq[a], uniq[b]
        if not edge_visible(p0, p1):
            continue
        x0 = (p0[0] - center[0]) * zoom + S / 2
        y0 = -(p0[1] - center[1]) * zoom + S / 2
        x1 = (p1[0] - center[0]) * zoom + S / 2
        y1 = -(p1[1] - center[1]) * zoom + S / 2
        draw.line([(float(x0), float(y0)), (float(x1), float(y1))],
                  fill=line, width=lw)

    return np.array(img.resize((size, size), Image.LANCZOS))


def main():
    stl = sys.argv[1] if len(sys.argv) > 1 else "/home/afsal/lunar-grounding-challenge/cad/assembly.stl"
    out = sys.argv[2] if len(sys.argv) > 2 else "/home/afsal/lunar-grounding-challenge/cad/line"
    tris = load_stl(stl)
    print(f"{len(tris)} tris")
    cen = tris.mean(1)
    subsets = [
        (tris, "full"),
        (tris[cen[:, 2] < 295], "rec"),
        (tris[cen[:, 2] >= 300], "wand"),
    ]
    views = [
        (rot_x(-90), "front"),
        (rot_x(-90) @ rot_z(90), "side"),
        (np.eye(3), "top"),
        (rot_x(-28) @ rot_z(45), "iso"),
    ]
    for tset, tag in subsets:
        if len(tset) < 10:
            continue
        for R, vname in views:
            img = line_art(tset, R, size=1600, ss=2)
            path = f"{out}_{tag}_{vname}.png"
            Image.fromarray(img).save(path, optimize=True)
            print("PNG ->", path)


if __name__ == "__main__":
    main()
