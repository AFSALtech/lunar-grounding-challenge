#!/usr/bin/env python3
"""Software rasterizer for binary STL -> shaded PNG (painter's algorithm)."""
import struct
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def load_stl(path):
    with open(path, "rb") as f:
        f.read(80)
        n = struct.unpack("<I", f.read(4))[0]
        data = np.frombuffer(f.read(n * 50), dtype=np.uint8).reshape(n, 50)
    floats = data[:, :48].copy().view("<f4").reshape(n, 4, 3)
    normals = floats[:, 0, :].astype(np.float64)
    tris = floats[:, 1:, :].astype(np.float64)
    return tris, normals


def rot_z(deg):
    a = np.radians(deg); c, s = np.cos(a), np.sin(a)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])


def rot_x(deg):
    a = np.radians(deg); c, s = np.cos(a), np.sin(a)
    return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])


def render(tris, normals, R, size=1600, ss=3, bg=(250, 250, 252),
           light_dir=(0.45, -0.55, 0.70), amb=0.32, spec=0.22,
           zoom=None, center=None, base_rgb=(0.62, 0.66, 0.70)):
    """Painter's-algorithm flat-shaded render. R: 3x3 model->view rotation."""
    S = size * ss
    tris_r = tris @ R.T
    nrm_r = normals @ R.T
    # recompute normals from winding (robust)
    v0, v1, v2 = tris_r[:, 0], tris_r[:, 1], tris_r[:, 2]
    fn = np.cross(v1 - v0, v2 - v0)
    flen = np.linalg.norm(fn, axis=1, keepdims=True)
    fn = np.divide(fn, flen, out=np.zeros_like(fn), where=flen > 1e-12)

    pts = tris_r.reshape(-1, 3)
    if center is None:
        center = (pts.min(0) + pts.max(0)) / 2
    if zoom is None:
        extent = float((pts.max(0) - pts.min(0)).max())
        zoom = 0.88 * S / max(extent, 1e-6)

    xy = (pts[:, :2] - center[:2]) * zoom
    sx = (xy[:, 0] + S / 2).reshape(-1, 3)
    sy = (-xy[:, 1] + S / 2).reshape(-1, 3)
    zc = tris_r[:, :, 2].mean(axis=1)  # centroid depth, larger = closer

    L = np.asarray(light_dir, float); L /= np.linalg.norm(L)
    ndl = np.clip(fn @ L, 0, 1)
    V = np.array([0.0, 0.0, 1.0])
    Hv = L + V; Hv /= np.linalg.norm(Hv)
    ndh = np.clip(fn @ Hv, 0, 1)
    shade = amb + (1.0 - amb) * ndl + spec * (ndh ** 24)
    # slight cool/warm tint by normal
    tint = np.stack([
        base_rgb[0] * (1.0 + 0.06 * (1 - ndl)),
        base_rgb[1] * (1.0 + 0.02 * (1 - ndl)),
        base_rgb[2] * (1.0 - 0.04 * (1 - ndl)),
    ], axis=1)
    colors = np.clip(tint * shade[:, None], 0, 1)

    # far to near
    order = np.argsort(zc)  # ascending: farthest first

    # supersampled canvas
    canvas = Image.new("RGB", (S, S), bg)
    draw = ImageDraw.Draw(canvas)

    for i in order:
        xs = sx[i]; ys = sy[i]
        if xs.max() < 0 or xs.min() >= S or ys.max() < 0 or ys.min() >= S:
            continue
        # skip tiny/degenerate
        area = abs((xs[1] - xs[0]) * (ys[2] - ys[0]) - (xs[2] - xs[0]) * (ys[1] - ys[0]))
        if area < 0.3:
            continue
        col = tuple(int(c * 255) for c in colors[i])
        pts_px = [(float(xs[k]), float(ys[k])) for k in range(3)]
        # fill + same-color stroke wider than 1 final px to close facet seams
        draw.polygon(pts_px, fill=col, outline=col)
        draw.line(pts_px + [pts_px[0]], fill=col, width=max(3, ss + 1), joint="curve")

    # downsample (box filter)
    img = np.asarray(canvas, dtype=np.float64)
    img = img.reshape(size, ss, size, ss, 3).mean(axis=(1, 3))
    return np.clip(img, 0, 255).astype(np.uint8)


def main():
    stl = sys.argv[1] if len(sys.argv) > 1 else "/home/afsal/lunar-grounding-challenge/cad/assembly.stl"
    out = sys.argv[2] if len(sys.argv) > 2 else "/home/afsal/lunar-grounding-challenge/cad/render"
    tris, normals = load_stl(stl)
    print(f"{len(tris)} triangles")

    R_iso = rot_x(-28) @ rot_z(45)
    R_front = rot_x(-90)   # wand on top, bracket at bottom
    R_side = rot_x(-90) @ rot_z(90)
    R_top = np.eye(3)

    for R, name in [
        (R_iso, "iso"),
        (R_front, "front"),
        (R_side, "side"),
        (R_top, "top"),
    ]:
        img = render(tris, normals, R, size=1400, ss=3)
        Image.fromarray(img).save(f"{out}_{name}.png", optimize=True)
        print("PNG ->", f"{out}_{name}.png")

    cen = tris.mean(1)
    for mask, name in [(cen[:, 2] < 295, "receptacle_iso"), (cen[:, 2] >= 300, "wand_iso")]:
        if mask.any():
            # rotate sub-assembly about its own center
            sub_t, sub_n = tris[mask], normals[mask]
            img = render(sub_t, sub_n, R_iso, size=1400, ss=3)
            Image.fromarray(img).save(f"{out}_{name}.png", optimize=True)
            print("PNG ->", f"{out}_{name}.png")


if __name__ == "__main__":
    main()
