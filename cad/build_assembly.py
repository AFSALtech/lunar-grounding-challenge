"""
A-GATE Detailed Flight Assembly — build123d / OpenCascade
Exports: STEP (named+colored assembly), STL (render), SVG HLR projections (drawings)
Computes: per-part volume, mass (real densities), assembly CG.
Units: millimeters, kg.
"""
import numpy as np
from build123d import (
    Box, Cylinder, Cone, RegularPolygon, Pos, Rot, Axis, Color,
    Compound, Location, Align, ExportSVG, Unit, export_step, export_stl,
    Rotation, extrude,
)

C = Align.CENTER
MIN = Align.MIN

# densities kg/mm^3
DENS = {
    "AL": 2.700e-6, "TI": 4.430e-6, "CU": 8.960e-6, "AL2O3": 3.950e-6,
    "PTFE": 2.200e-6, "PEEK": 1.320e-6, "STEEL": 7.850e-6, "NDFEB": 7.500e-6,
    "SIL": 1.100e-6, "G10": 1.850e-6, "BE": 1.850e-6, "MYLAR": 1.390e-6,
}
PARTS = []  # (name, shape, density, material, group)


def add(name, shape, mat, group, color=None, label=None):
    shape.label = label or name
    if color is not None:
        shape.color = color
    PARTS.append((name, shape, DENS[mat], mat, group))
    return shape


def cyl_between(p1, p2, r):
    p1 = np.asarray(p1, float); p2 = np.asarray(p2, float)
    d = p2 - p1; h = float(np.linalg.norm(d)); d = d / h
    z = np.array([0.0, 0.0, 1.0])
    c = float(np.dot(z, d))
    if abs(c) > 0.99999:
        rot = None if c > 0 else Rot(Y=180)
    else:
        v = np.cross(z, d)
        ang = np.degrees(np.arccos(np.clip(c, -1, 1)))
        rot = Rotation(Axis((0, 0, 0), v), ang)
    cyl = Cylinder(r, h, align=(C, C, MIN))  # from origin along +Z
    oriented = rot * cyl if rot is not None else cyl
    return Pos(*p1) * oriented  # then translate start to p1




# ============================================================
# 1. LANDER RECEPTACLE HOUSING (Al 6061-T6, hard anodized)
#    flange O160x12, body O110, funnel flare to O160 (60deg half-angle)
#    bores: O101 sleeve zone, O92 cage zone, O48 wiring, O84 canister pass
# ============================================================
outer = (
    Cylinder(80, 12, align=(C, C, MIN))                          # flange z0..12
    .fuse(Pos(0, 0, 12) * Cylinder(55, 258, align=(C, C, MIN)))  # body z12..270
    .fuse(Pos(0, 0, 270) * Cone(55, 80, 15, align=(C, C, MIN)))  # funnel z270..285
)
housing = (
    outer
    .cut(Pos(0, 0, 145) * Cylinder(50.5, 140, align=(C, C, MIN)))  # sleeve bore
    .cut(Pos(0, 0, 45) * Cylinder(46, 100, align=(C, C, MIN)))     # cage bore
    .cut(Pos(0, 0, 12) * Cylinder(24, 33, align=(C, C, MIN)))      # wiring bore
    .cut(Pos(0, 0, 0) * Cylinder(42, 12, align=(C, C, MIN)))       # canister hole
)
add("Housing", housing, "AL", "1. Lander Receptacle", Color(0.62, 0.65, 0.68))

# ============================================================
# 2. ALUMINA CERAMIC SLEEVE (99.5% Al2O3) z145..245
# ============================================================
sleeve = Pos(0, 0, 145) * Cylinder(50, 100, align=(C, C, MIN))
sleeve = sleeve.cut(Pos(0, 0, 145) * Cylinder(20, 100, align=(C, C, MIN)))
add("CeramicSleeve", sleeve, "AL2O3", "1. Lander Receptacle", Color(0.95, 0.95, 0.92))

# ============================================================
# 3. DUAL PTFE SPRING-ENERGIZED WIPER SEALS z247..255, z256..264
# ============================================================
for i, z in enumerate((247, 256)):
    seal = Pos(0, 0, z) * Cylinder(50, 8, align=(C, C, MIN))
    seal = seal.cut(Pos(0, 0, z) * Cylinder(15.5, 8, align=(C, C, MIN)))
    add(f"Seal_{i+1}", seal, "PTFE", "2. Dust Exclusion", Color(0.93, 0.93, 0.88))

# ============================================================
# 4. MAGNETIC REGOLITH TRAP RING z266..278 (NdFeB segments in Ti cage)
# ============================================================
mag = Pos(0, 0, 266) * Cylinder(50, 12, align=(C, C, MIN))
mag = mag.cut(Pos(0, 0, 266) * Cylinder(21, 12, align=(C, C, MIN)))
# segment cuts (8 radial slots)
for k in range(8):
    ang = k * 45
    slot = Rot(Z=ang) * Pos(0, 0, 266) * Box(6, 130, 13, align=(C, C, MIN))
    mag = mag.cut(slot)
add("MagneticRing", mag, "NDFEB", "2. Dust Exclusion", Color(0.25, 0.25, 0.28))

# ============================================================
# 5. FARADAY ARC CONTAINMENT CAGE (Ni-plated OFHC Cu) z51..129
# ============================================================
cage = Pos(0, 0, 51) * Cylinder(45, 78, align=(C, C, MIN))
cage = cage.cut(Pos(0, 0, 55) * Cylinder(41, 74, align=(C, C, MIN)))
add("FaradayCage", cage, "CU", "3. Arc Containment", Color(0.72, 0.45, 0.30))

# ============================================================
# 6. SEQUENCED MECHANICAL INTERLOCK SWITCH z74..96 + cam + pushrod
# ============================================================
sw = Pos(0, 0, 74) * Box(40, 30, 22, align=(C, C, MIN))
sw = sw.fuse(Pos(0, 0, 96) * Cylinder(6, 18, align=(C, C, MIN)))          # pushrod
sw = sw.fuse(Pos(0, -18, 104) * Box(8, 36, 6, align=(C, C, MIN)))         # lever
sw = sw.fuse(Pos(0, 0, 114) * Cylinder(8, 8, align=(C, C, MIN)))          # cam boss
sw = sw.fuse(Pos(0, 0, 70) * Cylinder(14, 6, align=(C, C, MIN)))          # contact pad
add("InterlockSwitch", sw, "BE", "3. Arc Containment", Color(0.20, 0.22, 0.25))

# contact pin (BeCu, gold plated) reaches to docking plane z145
pin = Pos(0, 0, 122) * Cylinder(5, 55, align=(C, C, MIN))
pin = pin.fuse(Pos(0, 0, 177) * Cone(5, 0.5, 8, align=(C, C, MIN)))  # conical contact tip
add("ContactPin", pin, "BE", "3. Arc Containment", Color(0.85, 0.68, 0.20))

# ============================================================
# 7. POTTED RESISTOR CANISTER (1.0 G ohm string + silicone) z-95..0
# ============================================================
can = Cylinder(40, 95, align=(C, C, MIN))  # z-95..0
can = can.fuse(Pos(0, 0, -98) * Cylinder(8, 6, align=(C, C, MIN)))  # connector boss
# potting bands (visual)
band1 = Pos(0, 0, -70) * Cylinder(41.5, 6, align=(C, C, MIN))
band2 = Pos(0, 0, -35) * Cylinder(41.5, 6, align=(C, C, MIN))
add("ResistorCanister", can, "SIL", "4. Resistor Core", Color(0.16, 0.18, 0.22))
add("CanisterBand1", band1, "AL", "4. Resistor Core", Color(0.30, 0.45, 0.75))
add("CanisterBand2", band2, "AL", "4. Resistor Core", Color(0.30, 0.45, 0.75))

# ============================================================
# 8. TITANIUM LADDER MOUNT BRACKET: base plate + posts + back plate
# ============================================================
base = Pos(0, 0, -8) * Box(160, 140, 8, align=(C, C, MIN))
base = base.cut(Pos(0, 0, -8) * Cylinder(42, 8, align=(C, C, MIN)))
for k in range(6):
    a = np.radians(k * 60)
    x, y = 65 * np.cos(a), 65 * np.sin(a)
    base = base.cut(Pos(x, y, -8) * Cylinder(3.3, 8, align=(C, C, MIN)))
for sx in (-1, 1):
    for sy in (-1, 1):
        base = base.fuse(Pos(sx * 60, sy * 50, -40) * Cylinder(6, 32, align=(C, C, MIN)))
back = Pos(0, 0, -48) * Box(160, 140, 8, align=(C, C, MIN))
for sx in (-1, 1):
    for sy in (-1, 1):
        back = back.cut(Pos(sx * 65, sy * 55, -48) * Cylinder(3.5, 8, align=(C, C, MIN)))
bracket = base.fuse(back)
add("Bracket", bracket, "TI", "6. Thermal & Bracket", Color(0.55, 0.56, 0.58))

# ============================================================
# 9. FASTENER KIT: 6x M6 SHCS through flange+bracket
# ============================================================
fasteners = None
for k in range(6):
    a = np.radians(k * 60)
    x, y = 65 * np.cos(a), 65 * np.sin(a)
    shank = Pos(x, y, -8) * Cylinder(3, 20, align=(C, C, MIN))     # z-8..12
    head = Pos(x, y, 12) * Cylinder(5, 6, align=(C, C, MIN))       # z12..18
    hexcut = Pos(x, y, 12.5) * extrude(RegularPolygon(2.887, 6), amount=5.5)
    bolt = shank.fuse(head).cut(hexcut)
    fasteners = bolt if fasteners is None else fasteners.fuse(bolt)
add("Fasteners", fasteners, "STEEL", "1. Lander Receptacle", Color(0.45, 0.46, 0.50))

# ============================================================
# 10. OPTICAL STATUS LED BEZEL z285..290 + 8 LEDs
# ============================================================
bezel = Pos(0, 0, 285) * Cylinder(90, 5, align=(C, C, MIN))
bezel = bezel.cut(Pos(0, 0, 284) * Cylinder(60, 7, align=(C, C, MIN)))
add("LEDBezel", bezel, "AL", "7. Avionics", Color(0.20, 0.22, 0.25))
leds = None
for k in range(8):
    a = np.radians(k * 45 + 22.5)
    x, y = 70 * np.cos(a), 70 * np.sin(a)
    led = Pos(x, y, 290) * Cylinder(3.5, 3, align=(C, C, MIN))
    leds = led if leds is None else leds.fuse(led)
add("LEDs", leds, "SIL", "7. Avionics", Color(0.10, 0.85, 0.35))

# ============================================================
# 11. THERMAL: 15-layer MLI blanket shell over body + heater strips
# ============================================================
mli = Pos(0, 0, 30) * Cylinder(58, 240, align=(C, C, MIN))
mli = mli.cut(Pos(0, 0, 29) * Cylinder(55, 242, align=(C, C, MIN)))  # shell 3mm
add("MLIBlanket", mli, "MYLAR", "6. Thermal & Bracket", Color(0.85, 0.75, 0.35))
heater = Pos(0, 0, 60) * Cylinder(56.5, 60, align=(C, C, MIN))
heater = heater.cut(Pos(0, 0, 59) * Cylinder(55, 62, align=(C, C, MIN)))
add("HeaterFoil", heater, "SIL", "6. Thermal & Bracket", Color(0.75, 0.25, 0.20))

# ============================================================
# 12. EVA GROUNDING WAND (positioned above receptacle, tip down)
#     tip docking plane z145 -> wand tip shown at z310 (standoff pose)
# ============================================================
tip = Pos(0, 0, 310) * Cylinder(7, 42, align=(C, C, MIN))
tip = tip.fuse(Pos(0, 0, 302) * Cone(1.5, 7, 8, align=(C, C, MIN)))  # tip points down
add("WandTip", tip, "BE", "5. EVA Wand", Color(0.85, 0.68, 0.20))
shaft = Pos(0, 0, 352) * Cylinder(15, 110, align=(C, C, MIN))
add("WandShaft", shaft, "PEEK", "5. EVA Wand", Color(0.88, 0.88, 0.86))
collar = Pos(0, 0, 462) * Cylinder(22, 12, align=(C, C, MIN))
collar = collar.fuse(Pos(19, 0, 464) * Cylinder(4, 8, align=(C, C, C)))  # detent bump
add("WandCollar", collar, "STEEL", "5. EVA Wand", Color(0.55, 0.57, 0.60))
grip = Pos(0, 0, 474) * Cylinder(19, 90, align=(C, C, MIN))
grip = grip.fuse(Pos(0, 0, 564) * Cylinder(26, 6, align=(C, C, MIN)))  # end flange
grip = grip.fuse(Pos(0, -16, 510) * Box(20, 14, 40, align=(C, C, C)))  # thumb rest
add("WandGrip", grip, "PEEK", "5. EVA Wand", Color(0.12, 0.13, 0.15))
reel = Pos(70, 0, 530) * (Rot(Y=90) * Cylinder(30, 36, align=(MIN, C, C)))
add("TetherReel", reel, "AL", "5. EVA Wand", Color(0.50, 0.52, 0.55))
cable = cyl_between((0, 0, 570), (70, 0, 530), 4)
add("TetherCable", cable, "CU", "5. EVA Wand", Color(0.15, 0.15, 0.17))

# ============================================================
# MASS PROPERTIES (computed from real geometry)
# ============================================================
rows = []
tot_m = 0.0
tot_v = 0.0
cg = np.zeros(3)
for name, shp, dens, mat, grp in PARTS:
    v = float(shp.volume)
    m = v * dens
    try:
        com = np.array(tuple(shp.center()), float)
    except Exception:
        com = np.zeros(3)
    rows.append((name, grp, mat, v, m, com))
    tot_m += m
    tot_v += v
    cg += m * com

cg = cg / tot_m if tot_m else cg
print(f"{'PART':<22}{'GROUP':<26}{'MAT':<8}{'VOL mm^3':>12}{'MASS kg':>10}")
print("-" * 80)
for name, grp, mat, v, m, com in rows:
    print(f"{name:<22}{grp:<26}{mat:<8}{v:>12.1f}{m:>10.4f}")
print("-" * 80)
print(f"{'TOTAL':<22}{'':<26}{'':<8}{tot_v:>12.1f}{tot_m:>10.4f}")
print(f"Assembly CG (x,y,z) mm: ({cg[0]:.1f}, {cg[1]:.1f}, {cg[2]:.1f})")
print(f"Mass margin vs 20 kg: {(20 - tot_m) / 20 * 100:.1f}%  ({20 - tot_m:.3f} kg reserve)")

# ============================================================
# EXPORTS
# ============================================================
shapes = [s for _, s, _, _, _ in PARTS]
compound = Compound(children=shapes)
compound.label = "A-GATE Assembly"

out_step = "/home/afsal/lunar-grounding-challenge/deliverables/Deliverable_2A_A_GATE_System.step"
export_step(compound, out_step)
print("STEP ->", out_step)

out_stl = "/home/afsal/lunar-grounding-challenge/cad/assembly.stl"
export_stl(compound, out_stl, tolerance=0.08)
print("STL ->", out_stl)

# HLR SVG projections for engineering drawings (patched ExportSVG for full circles)
from build123d import ExportSVG
from build123d.exporters import ExportSVG as _ES
import math as _math
from OCP.gp import gp_Dir as _gp_Dir
import svgpathtools.path as _sp


def _fixed_circle_segments(self, edge, reverse):
    """Like ExportSVG._circle_segments but splits full circles (start==end)."""
    if edge.length < 1e-6:
        return []
    curve = edge.geom_adaptor()
    circle = curve.Circle()
    radius = circle.Radius()
    x_axis = circle.XAxis().Direction()
    z_axis = circle.Axis().Direction()
    fp = curve.FirstParameter()
    lp = curve.LastParameter()
    du = lp - fp
    large_arc = (du < -_math.pi) or (du > _math.pi)
    sweep = (z_axis.Z() > 0) ^ reverse
    u0, u1 = (lp, fp) if reverse else (fp, lp)
    start = self._path_point(curve.Value(u0))
    end = self._path_point(curve.Value(u1))
    radius_c = complex(radius, radius)
    rotation = _math.degrees(_gp_Dir(1, 0, 0).AngleWithRef(x_axis, _gp_Dir(0, 0, 1)))
    if curve.IsClosed() or start == end:
        mid_u = u0 + (u1 - u0) / 2 if abs(u1 - u0) > 1e-12 else u0 + _math.pi
        # for full circle u1-u0 may be 0 or 2pi; pick geometric midpoint
        if abs(u1 - u0) < 1e-12 or abs(abs(u1 - u0) - 2 * _math.pi) < 1e-6:
            mid_u = u0 + _math.pi
        midway = self._path_point(curve.Value(mid_u))
        if midway == start:
            # fallback: offset along tangent
            midway = complex(start.real + radius, start.imag)
        result = [
            _sp.Arc(start, radius_c, rotation, False, sweep, midway),
            _sp.Arc(midway, radius_c, rotation, False, sweep, end if end != start else start),
        ]
        if result[1].end == result[1].start:
            result = result[:1]
    else:
        result = [_sp.Arc(start, radius_c, rotation, large_arc, sweep, end)]
    return result


_ES._circle_segments = _fixed_circle_segments
# _SEGMENT_LOOKUP captured original functions at class-body time — patch the dict
from build123d.build_enums import GeomType as _GT
_ES._SEGMENT_LOOKUP[_GT.CIRCLE] = _fixed_circle_segments


def _fixed_ellipse_segments(self, edge, reverse):
    if edge.length < 1e-6:
        return []
    curve = edge.geom_adaptor()
    ellipse = curve.Ellipse()
    minor_radius = ellipse.MinorRadius()
    major_radius = ellipse.MajorRadius()
    x_axis = ellipse.XAxis().Direction()
    z_axis = ellipse.Axis().Direction()
    fp = curve.FirstParameter()
    lp = curve.LastParameter()
    du = lp - fp
    large_arc = (du < -_math.pi) or (du > _math.pi)
    sweep = (z_axis.Z() > 0) ^ reverse
    u0, u1 = (lp, fp) if reverse else (fp, lp)
    start = self._path_point(curve.Value(u0))
    end = self._path_point(curve.Value(u1))
    radius_c = complex(major_radius, minor_radius)
    rotation = _math.degrees(_gp_Dir(1, 0, 0).AngleWithRef(x_axis, _gp_Dir(0, 0, 1)))
    if curve.IsClosed() or start == end:
        if abs(u1 - u0) < 1e-12 or abs(abs(u1 - u0) - 2 * _math.pi) < 1e-6:
            mid_u = u0 + _math.pi
        else:
            mid_u = u0 + (u1 - u0) / 2
        midway = self._path_point(curve.Value(mid_u))
        result = [
            _sp.Arc(start, radius_c, rotation, False, sweep, midway),
            _sp.Arc(midway, radius_c, rotation, False, sweep, end),
        ]
    else:
        result = [_sp.Arc(start, radius_c, rotation, large_arc, sweep, end)]
    return result


_ES._ellipse_segments = _fixed_ellipse_segments
_ES._SEGMENT_LOOKUP[_GT.ELLIPSE] = _fixed_ellipse_segments
# _circle_element / _ellipse_element also call self._*_segments — already patched on class


def project(shape, rot, path, scale=1.0, margin=5.0):
    """HLR-project shape to black-on-white SVG via ExportSVG."""
    try:
        svg = ExportSVG(unit=Unit.MM, scale=scale, margin=margin)
        svg.add_shape(rot * shape)
        svg.write(path)
        print("SVG ->", path)
        return True
    except Exception as e:
        print(f"FAIL {path}: {type(e).__name__}: {e}")
        return False

# receptacle only (cut away wand for clarity): use receptacle subset
rec_shapes = [s for _, s, _, _, grp in PARTS if grp != "5. EVA Wand"]
rec = Compound(children=rec_shapes)
rec.label = "Receptacle"

# front view (section): cut x>0 half to expose internals
half = Pos(200, 0, 120) * Box(400, 400, 500, align=(C, C, C))
rec_sec = rec.cut(half)
project(rec, Rot(X=-90), "/home/afsal/lunar-grounding-challenge/cad/proj_front.svg")
project(rec_sec, Rot(X=-90), "/home/afsal/lunar-grounding-challenge/cad/proj_section.svg")
project(rec, Rot(X=-90, Z=90), "/home/afsal/lunar-grounding-challenge/cad/proj_side.svg")
project(rec, Rot(X=0), "/home/afsal/lunar-grounding-challenge/cad/proj_top.svg")
project(compound, Rot(X=-90), "/home/afsal/lunar-grounding-challenge/cad/proj_wand_front.svg")
# housing-only section as fallback for drawing sheet
hous_only = Compound(children=[housing])
project(hous_only.cut(half), Rot(X=-90), "/home/afsal/lunar-grounding-challenge/cad/proj_housing_section.svg")
# wand-only views for detail sheet
wand_shapes = [s for _, s, _, _, grp in PARTS if grp == "5. EVA Wand"]
wand = Compound(children=wand_shapes)
wand.label = "Wand"
project(wand, Rot(X=-90), "/home/afsal/lunar-grounding-challenge/cad/proj_wand_only.svg")
project(wand, Rot(X=0), "/home/afsal/lunar-grounding-challenge/cad/proj_wand_top.svg")

# write mass table for downstream documents
with open("/home/afsal/lunar-grounding-challenge/cad/mass_table.txt", "w") as f:
    f.write(f"{'PART':<22}{'GROUP':<26}{'MAT':<8}{'VOL mm^3':>12}{'MASS kg':>10}\n")
    for name, grp, mat, v, m, com in rows:
        f.write(f"{name:<22}{grp:<26}{mat:<8}{v:>12.1f}{m:>10.4f}\n")
    f.write(f"TOTAL {tot_m:.4f} kg | CG ({cg[0]:.1f},{cg[1]:.1f},{cg[2]:.1f}) mm\n")
print("done")
