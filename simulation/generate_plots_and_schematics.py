"""
Generates crisp, high-definition SVG figures and engineering schematics
for the A-GATE Lunar Grounding Challenge deliverables.
"""

import math

def generate_svgs():
    # 1. Electrical Schematic SVG
    circuit_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 360" width="100%" height="100%" style="background:#ffffff; font-family:Arial, sans-serif;">
  <defs>
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#f1f5f9" stroke-width="1"/>
    </pattern>
    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#1e293b"/>
    </marker>
  </defs>
  <rect width="100%" height="100%" fill="url(#grid)" />
  
  <!-- Boundary Boxes -->
  <!-- Suit Subsystem -->
  <rect x="30" y="40" width="220" height="280" rx="8" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5,5"/>
  <text x="45" y="65" font-size="13" font-weight="bold" fill="#0f172a">ASTRONAUT / AxEMU SUIT</text>
  <text x="45" y="85" font-size="11" fill="#64748b">Tribocharged Potential: -100 kV</text>
  
  <!-- Capacitance model -->
  <line x1="140" y1="110" x2="140" y2="150" stroke="#1e293b" stroke-width="2"/>
  <line x1="110" y1="150" x2="170" y2="150" stroke="#1e293b" stroke-width="3"/>
  <line x1="110" y1="160" x2="170" y2="160" stroke="#1e293b" stroke-width="3"/>
  <line x1="140" y1="160" x2="140" y2="200" stroke="#1e293b" stroke-width="2"/>
  <text x="180" y="158" font-size="11" font-weight="bold" fill="#0369a1">C_suit = 200 pF</text>
  <text x="180" y="173" font-size="10" fill="#64748b">E_stored = 1.00 J</text>
  
  <!-- Lunar surface ground reference for suit capacitor -->
  <line x1="120" y1="200" x2="160" y2="200" stroke="#64748b" stroke-width="2"/>
  <line x1="128" y1="205" x2="152" y2="205" stroke="#64748b" stroke-width="2"/>
  <line x1="135" y1="210" x2="145" y2="210" stroke="#64748b" stroke-width="2"/>
  <text x="110" y="230" font-size="10" fill="#64748b">Lunar Plasma / Regolith Ref</text>

  <!-- EVA Wand Connection Point -->
  <circle cx="210" cy="110" r="5" fill="#2563eb"/>
  <line x1="140" y1="110" x2="250" y2="110" stroke="#1e293b" stroke-width="2.5"/>
  <text x="145" y="103" font-size="10" font-weight="bold" fill="#1e293b">-100 kV Bus</text>

  <!-- A-GATE System Box -->
  <rect x="270" y="30" width="310" height="300" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
  <text x="285" y="55" font-size="14" font-weight="bold" fill="#1d4ed8">A-GATE INTERFACE ASSEMBLY</text>
  
  <!-- Mechanical Interlock Switch -->
  <text x="285" y="90" font-size="11" font-weight="bold" fill="#0f172a">Zero-Gap Mechanical Interlock (SW1)</text>
  <circle cx="310" cy="110" r="4" fill="#0f172a"/>
  <line x1="310" y1="110" x2="340" y2="95" stroke="#dc2626" stroke-width="2.5"/>
  <circle cx="345" cy="110" r="4" fill="#0f172a"/>
  <text x="290" y="130" font-size="9" fill="#dc2626">Engages ONLY after full mechanical seating</text>

  <!-- Faraday Shield & Spark Containment -->
  <rect x="370" y="80" width="190" height="180" rx="6" fill="#f8fafc" stroke="#475569" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="380" y="100" font-size="10" font-weight="bold" fill="#334155">FARADAY ARREST CHAMBER</text>

  <!-- Resistor String R1 -->
  <line x1="345" y1="110" x2="385" y2="110" stroke="#1e293b" stroke-width="2"/>
  <!-- Resistor zigzag -->
  <path d="M 385 110 L 392 100 L 402 120 L 412 100 L 422 120 L 432 100 L 442 120 L 452 100 L 460 110" fill="none" stroke="#2563eb" stroke-width="2.5"/>
  <text x="390" y="88" font-size="11" font-weight="bold" fill="#1e40af">R1 = 900 MΩ</text>
  <text x="390" y="135" font-size="9" fill="#64748b">Cermet Thick-Film (HV)</text>

  <!-- Resistor String R2 -->
  <path d="M 470 110 L 476 102 L 484 118 L 492 102 L 500 118 L 508 102 L 515 110" fill="none" stroke="#2563eb" stroke-width="2.5"/>
  <line x1="460" y1="110" x2="470" y2="110" stroke="#1e293b" stroke-width="2"/>
  <text x="470" y="88" font-size="11" font-weight="bold" fill="#1e40af">R2 = 100 MΩ</text>
  <text x="465" y="135" font-size="9" fill="#64748b">Current Monitor Shunt</text>

  <!-- Total R info -->
  <rect x="380" y="148" width="170" height="35" rx="4" fill="#e0f2fe" stroke="#0284c7" stroke-width="1"/>
  <text x="388" y="163" font-size="10" font-weight="bold" fill="#0369a1">R_total = 1.00 Gigaohm</text>
  <text x="388" y="176" font-size="9" fill="#0284c7">I_peak = 0.100 mA (Target ≤0.2 mA)</text>

  <!-- Optical / Visual Indicator Circuit -->
  <circle cx="492" cy="180" r="10" fill="#22c55e" stroke="#15803d" stroke-width="2"/>
  <text x="510" y="184" font-size="10" font-weight="bold" fill="#15803d">Status LED Ring</text>
  <text x="510" y="197" font-size="9" fill="#64748b">Green: Safe Equilibrium</text>

  <!-- Lander Subsystem -->
  <rect x="600" y="40" width="170" height="280" rx="8" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5,5"/>
  <text x="615" y="65" font-size="13" font-weight="bold" fill="#0f172a">LUNAR LANDER</text>
  <text x="615" y="85" font-size="11" fill="#64748b">Vehicle Potential: +100 V</text>

  <!-- Lander Ground Bus -->
  <line x1="515" y1="110" x2="650" y2="110" stroke="#1e293b" stroke-width="2.5"/>
  <circle cx="650" cy="110" r="5" fill="#e11d48"/>
  <line x1="650" y1="110" x2="650" y2="190" stroke="#1e293b" stroke-width="2"/>
  
  <!-- Lander Chassis Ground symbol -->
  <line x1="630" y1="190" x2="670" y2="190" stroke="#0f172a" stroke-width="3"/>
  <line x1="638" y1="196" x2="662" y2="196" stroke="#0f172a" stroke-width="2.5"/>
  <line x1="645" y1="202" x2="655" y2="202" stroke="#0f172a" stroke-width="2"/>
  <text x="620" y="222" font-size="10" font-weight="bold" fill="#0f172a">Lander Structure Ground</text>

  <!-- Heater Interface from Lander (40W max bus) -->
  <rect x="300" y="270" width="250" height="45" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="1.2"/>
  <text x="310" y="287" font-size="10" font-weight="bold" fill="#92400e">Thermal Regulation (Lander Bus)</text>
  <text x="310" y="302" font-size="9" fill="#b45309">12W Nominal (40W Max Limit) | MLI Blanket + Strip Heaters</text>

  <!-- Current flow arrow -->
  <path d="M 640 135 L 260 135" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow)" stroke-dasharray="6,4"/>
  <text x="400" y="130" font-size="10" font-weight="bold" fill="#0284c7">Neutralizing Electron Bleed Flow</text>
</svg>'''

    with open("/home/afsal/lunar-grounding-challenge/deliverables/schematic_circuit.svg", "w") as f:
        f.write(circuit_svg)

    # 2. Discharge Current Plot SVG
    # Sizing: 700x320
    # Data points: t=0..2.5 s, I(t) = 0.1001 * exp(-t/0.2)
    # Target line at 0.2 mA, Hard Limit at 1.0 mA
    pts = []
    w, h = 700, 320
    ox, oy = 80, 260
    pw, ph = 580, 210 # plot width, height
    
    # y-axis: 0.0 to 1.1 mA
    # x-axis: 0.0 to 2.5 s
    def t_to_x(t): return ox + (t / 2.5) * pw
    def i_to_y(i): return oy - (i / 1.1) * ph

    polyline_pts = []
    for step in range(251):
        t_val = step * 0.01
        i_val = 0.1001 * math.exp(-t_val / 0.2)
        polyline_pts.append(f"{t_to_x(t_val):.1f},{i_to_y(i_val):.1f}")
    polyline_str = " ".join(polyline_pts)

    current_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%" style="background:#ffffff; font-family:Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#ffffff" />
  <text x="{w/2}" y="28" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">Discharge Current vs. Time (A-GATE 1.0 GΩ System vs. NASA Limits)</text>
  
  <!-- Grid lines -->
  <line x1="{ox}" y1="{i_to_y(0.0)}" x2="{ox+pw}" y2="{i_to_y(0.0)}" stroke="#cbd5e1" stroke-width="1"/>
  <line x1="{ox}" y1="{i_to_y(0.2)}" x2="{ox+pw}" y2="{i_to_y(0.2)}" stroke="#fde047" stroke-width="1.5" stroke-dasharray="4,4"/>
  <line x1="{ox}" y1="{i_to_y(0.4)}" x2="{ox+pw}" y2="{i_to_y(0.4)}" stroke="#f1f5f9" stroke-width="1"/>
  <line x1="{ox}" y1="{i_to_y(0.6)}" x2="{ox+pw}" y2="{i_to_y(0.6)}" stroke="#f1f5f9" stroke-width="1"/>
  <line x1="{ox}" y1="{i_to_y(0.8)}" x2="{ox+pw}" y2="{i_to_y(0.8)}" stroke="#f1f5f9" stroke-width="1"/>
  <line x1="{ox}" y1="{i_to_y(1.0)}" x2="{ox+pw}" y2="{i_to_y(1.0)}" stroke="#fca5a5" stroke-width="1.5" stroke-dasharray="4,4"/>

  <!-- Vertical grid lines -->
  <line x1="{t_to_x(0.5)}" y1="{oy}" x2="{t_to_x(0.5)}" y2="{oy-ph}" stroke="#f1f5f9" stroke-width="1"/>
  <line x1="{t_to_x(1.0)}" y1="{oy}" x2="{t_to_x(1.0)}" y2="{oy-ph}" stroke="#f1f5f9" stroke-width="1"/>
  <line x1="{t_to_x(1.5)}" y1="{oy}" x2="{t_to_x(1.5)}" y2="{oy-ph}" stroke="#f1f5f9" stroke-width="1"/>
  <line x1="{t_to_x(2.0)}" y1="{oy}" x2="{t_to_x(2.0)}" y2="{oy-ph}" stroke="#f1f5f9" stroke-width="1"/>

  <!-- Axes -->
  <line x1="{ox}" y1="{oy}" x2="{ox+pw}" y2="{oy}" stroke="#334155" stroke-width="1.5"/>
  <line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy-ph}" stroke="#334155" stroke-width="1.5"/>

  <!-- Y Tick Labels -->
  <text x="{ox-8}" y="{i_to_y(0.0)+4}" font-size="10" fill="#64748b" text-anchor="end">0.0 mA</text>
  <text x="{ox-8}" y="{i_to_y(0.1)+4}" font-size="10" fill="#2563eb" font-weight="bold" text-anchor="end">0.10 mA (Peak)</text>
  <text x="{ox-8}" y="{i_to_y(0.2)+4}" font-size="10" fill="#b45309" font-weight="bold" text-anchor="end">0.20 mA</text>
  <text x="{ox-8}" y="{i_to_y(0.5)+4}" font-size="10" fill="#64748b" text-anchor="end">0.50 mA</text>
  <text x="{ox-8}" y="{i_to_y(1.0)+4}" font-size="10" fill="#dc2626" font-weight="bold" text-anchor="end">1.00 mA</text>

  <!-- X Tick Labels -->
  <text x="{t_to_x(0.0)}" y="{oy+18}" font-size="10" fill="#64748b" text-anchor="middle">0.0s</text>
  <text x="{t_to_x(0.2)}" y="{oy+18}" font-size="10" fill="#2563eb" text-anchor="middle">0.2s (τ)</text>
  <text x="{t_to_x(0.5)}" y="{oy+18}" font-size="10" fill="#64748b" text-anchor="middle">0.5s</text>
  <text x="{t_to_x(1.0)}" y="{oy+18}" font-size="10" fill="#64748b" text-anchor="middle">1.0s (5τ)</text>
  <text x="{t_to_x(1.5)}" y="{oy+18}" font-size="10" fill="#64748b" text-anchor="middle">1.5s</text>
  <text x="{t_to_x(2.0)}" y="{oy+18}" font-size="10" fill="#15803d" font-weight="bold" text-anchor="middle">2.0s (10τ)</text>
  <text x="{t_to_x(2.5)}" y="{oy+18}" font-size="10" fill="#64748b" text-anchor="middle">2.5s</text>

  <!-- Threshold Annotation Lines -->
  <!-- 1.0 mA Hard Limit -->
  <line x1="{ox}" y1="{i_to_y(1.0)}" x2="{ox+pw}" y2="{i_to_y(1.0)}" stroke="#dc2626" stroke-width="2" stroke-dasharray="6,4"/>
  <rect x="{ox+pw-230}" y="{i_to_y(1.0)-22}" width="225" height="18" fill="#fee2e2" rx="3"/>
  <text x="{ox+pw-118}" y="{i_to_y(1.0)-9}" font-size="10" font-weight="bold" fill="#b91c1c" text-anchor="middle">NASA Maximum Allowed Limit: 1.0 mA</text>

  <!-- 0.2 mA Human Perception Target -->
  <line x1="{ox}" y1="{i_to_y(0.2)}" x2="{ox+pw}" y2="{i_to_y(0.2)}" stroke="#d97706" stroke-width="2" stroke-dasharray="6,4"/>
  <rect x="{ox+pw-265}" y="{i_to_y(0.2)-22}" width="260" height="18" fill="#fef3c7" rx="3"/>
  <text x="{ox+pw-135}" y="{i_to_y(0.2)-9}" font-size="10" font-weight="bold" fill="#b45309" text-anchor="middle">NASA Human Perception Design Target: ≤0.2 mA</text>

  <!-- Curve -->
  <polyline points="{polyline_str}" fill="none" stroke="#2563eb" stroke-width="3"/>

  <!-- Shaded Area Below Curve -->
  <polygon points="{t_to_x(0.0)},{oy} {polyline_str} {t_to_x(2.5)},{oy}" fill="#3b82f6" fill-opacity="0.12"/>

  <!-- Callouts -->
  <!-- Initial Peak -->
  <circle cx="{t_to_x(0.0)}" cy="{i_to_y(0.1001)}" r="5" fill="#2563eb"/>
  <rect x="{t_to_x(0.0)+15}" y="{i_to_y(0.1001)-30}" width="180" height="28" rx="4" fill="#eff6ff" stroke="#3b82f6" stroke-width="1"/>
  <text x="{t_to_x(0.0)+20}" y="{i_to_y(0.1001)-17}" font-size="10" font-weight="bold" fill="#1d4ed8">Peak Current: 0.100 mA</text>
  <text x="{t_to_x(0.0)+20}" y="{i_to_y(0.1001)-5}" font-size="9" fill="#1e40af">50% Below Human Perception Target</text>

  <!-- Safe Point at 2.0s -->
  <circle cx="{t_to_x(2.0)}" cy="{i_to_y(0.00001)}" r="5" fill="#16a34a"/>
  <rect x="{t_to_x(2.0)-140}" y="{oy-65}" width="180" height="28" rx="4" fill="#f0fdf4" stroke="#22c55e" stroke-width="1"/>
  <text x="{t_to_x(2.0)-50}" y="{oy-52}" font-size="10" font-weight="bold" fill="#15803d" text-anchor="middle">At t = 2.0s: I = 0.01 µA</text>
  <text x="{t_to_x(2.0)-50}" y="{oy-40}" font-size="9" fill="#166534" text-anchor="middle">Residual Potential &lt; 4.5 V</text>

  <!-- Axis Titles -->
  <text x="{w/2}" y="{h-8}" font-size="11" font-weight="bold" fill="#334155" text-anchor="middle">Discharge Time (seconds)</text>
  <text transform="rotate(-90)" x="{-h/2}" y="22" font-size="11" font-weight="bold" fill="#334155" text-anchor="middle">Current (mA)</text>
</svg>'''

    with open("/home/afsal/lunar-grounding-challenge/deliverables/plot_discharge_current.svg", "w") as f:
        f.write(current_svg)

    # 3. Voltage Decay & Energy SVG
    v_poly = []
    e_poly = []
    for step in range(251):
        t_val = step * 0.01
        v_val = 100.1 * math.exp(-t_val / 0.2) # kV
        e_val = 1.002 * (1.0 - math.exp(-2 * t_val / 0.2)) # J
        v_poly.append(f"{t_to_x(t_val):.1f},{oy - (v_val/110.0)*ph:.1f}")
        e_poly.append(f"{t_to_x(t_val):.1f},{oy - (e_val/1.1)*ph:.1f}")

    voltage_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%" style="background:#ffffff; font-family:Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#ffffff" />
  <text x="{w/2}" y="28" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">Transient Potential Difference &amp; Energy Dissipated vs. Time</text>

  <!-- Grid -->
  <line x1="{ox}" y1="{oy}" x2="{ox+pw}" y2="{oy}" stroke="#334155" stroke-width="1.5"/>
  <line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy-ph}" stroke="#334155" stroke-width="1.5"/>
  <line x1="{ox+pw}" y1="{oy}" x2="{ox+pw}" y2="{oy-ph}" stroke="#334155" stroke-width="1.5"/>

  <!-- Ticks Left (Voltage) -->
  <text x="{ox-8}" y="{oy+4}" font-size="10" fill="#64748b" text-anchor="end">0 kV</text>
  <text x="{ox-8}" y="{oy-(25/110)*ph+4}" font-size="10" fill="#64748b" text-anchor="end">25 kV</text>
  <text x="{ox-8}" y="{oy-(50/110)*ph+4}" font-size="10" fill="#64748b" text-anchor="end">50 kV</text>
  <text x="{ox-8}" y="{oy-(75/110)*ph+4}" font-size="10" fill="#64748b" text-anchor="end">75 kV</text>
  <text x="{ox-8}" y="{oy-(100/110)*ph+4}" font-size="10" fill="#7c3aed" font-weight="bold" text-anchor="end">100 kV</text>

  <!-- Ticks Right (Energy) -->
  <text x="{ox+pw+8}" y="{oy+4}" font-size="10" fill="#64748b">0.0 J</text>
  <text x="{ox+pw+8}" y="{oy-(0.25/1.1)*ph+4}" font-size="10" fill="#64748b">0.25 J</text>
  <text x="{ox+pw+8}" y="{oy-(0.50/1.1)*ph+4}" font-size="10" fill="#64748b">0.50 J</text>
  <text x="{ox+pw+8}" y="{oy-(0.75/1.1)*ph+4}" font-size="10" fill="#64748b">0.75 J</text>
  <text x="{ox+pw+8}" y="{oy-(1.00/1.1)*ph+4}" font-size="10" fill="#059669" font-weight="bold">1.00 J (Total)</text>

  <!-- Voltage Curve (Purple) -->
  <polyline points="{' '.join(v_poly)}" fill="none" stroke="#7c3aed" stroke-width="3"/>

  <!-- Energy Curve (Emerald) -->
  <polyline points="{' '.join(e_poly)}" fill="none" stroke="#059669" stroke-width="3" stroke-dasharray="6,3"/>

  <!-- Legend -->
  <rect x="{ox+150}" y="45" width="280" height="34" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <line x1="{ox+165}" y1="56" x2="{ox+195}" y2="56" stroke="#7c3aed" stroke-width="3"/>
  <text x="{ox+202}" y="60" font-size="11" font-weight="bold" fill="#6d28d9">Potential Difference ΔV (kV)</text>

  <line x1="{ox+165}" y1="70" x2="{ox+195}" y2="70" stroke="#059669" stroke-width="3" stroke-dasharray="6,3"/>
  <text x="{ox+202}" y="74" font-size="11" font-weight="bold" fill="#047857">Dissipated Energy E (Joules)</text>

  <!-- X axis labels -->
  <text x="{t_to_x(0.0)}" y="{oy+18}" font-size="10" fill="#64748b" text-anchor="middle">0.0s</text>
  <text x="{t_to_x(0.5)}" y="{oy+18}" font-size="10" fill="#64748b" text-anchor="middle">0.5s</text>
  <text x="{t_to_x(1.0)}" y="{oy+18}" font-size="10" fill="#64748b" text-anchor="middle">1.0s</text>
  <text x="{t_to_x(1.5)}" y="{oy+18}" font-size="10" fill="#64748b" text-anchor="middle">1.5s</text>
  <text x="{t_to_x(2.0)}" y="{oy+18}" font-size="10" fill="#15803d" font-weight="bold" text-anchor="middle">2.0s</text>
  <text x="{t_to_x(2.5)}" y="{oy+18}" font-size="10" fill="#64748b" text-anchor="middle">2.5s</text>

  <text x="{w/2}" y="{h-8}" font-size="11" font-weight="bold" fill="#334155" text-anchor="middle">Discharge Time (seconds)</text>
  <text transform="rotate(-90)" x="{-h/2}" y="22" font-size="11" font-weight="bold" fill="#7c3aed" text-anchor="middle">Differential Voltage (kV)</text>
  <text transform="rotate(90)" x="{h/2}" y="{-w+22}" font-size="11" font-weight="bold" fill="#059669" text-anchor="middle">Energy Dissipated (Joules)</text>
</svg>'''

    with open("/home/afsal/lunar-grounding-challenge/deliverables/plot_voltage_energy.svg", "w") as f:
        f.write(voltage_svg)

    # 4. Mechanical 2D Cross Section SVG
    mech_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%" style="background:#ffffff; font-family:Arial, sans-serif;">
  <defs>
    <pattern id="diagHatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
      <line x1="0" y1="0" x2="0" y2="8" stroke="#cbd5e1" stroke-width="1.5" />
    </pattern>
  </defs>
  <text x="400" y="28" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">A-GATE Mechanical Docking Receptacle &amp; EVA Probe — Cross Sectional View</text>
  <text x="400" y="46" font-size="11" fill="#64748b" text-anchor="middle">Zero-Gap Hermetic Interlock, Multi-Stage Dust Exclusion Labyrinth, and Faraday Shield Core</text>

  <!-- Receptacle Outer Shell (Aluminum 6061-T6 hard anodized) -->
  <path d="M 120 100 L 260 180 L 580 180 L 580 320 L 260 320 L 120 400 L 80 400 L 80 100 Z" fill="url(#diagHatch)" stroke="#334155" stroke-width="2"/>
  <text x="150" y="140" font-size="10" font-weight="bold" fill="#475569">Guide Funnel (60° Half-Angle)</text>

  <!-- Ceramic Insulation Liner (Alumina 99.5% Al2O3) -->
  <path d="M 260 190 L 570 190 L 570 310 L 260 310 Z" fill="#f8fafc" stroke="#64748b" stroke-width="1.5"/>
  <text x="350" y="206" font-size="10" fill="#64748b">Alumina Dielectric Sleeve (150 kV Holdoff)</text>

  <!-- Dust Labyrinth & Magnetic Scraper Rings -->
  <rect x="270" y="215" width="16" height="70" fill="#cbd5e1" stroke="#475569" stroke-width="1"/>
  <rect x="295" y="215" width="16" height="70" fill="#93c5fd" stroke="#2563eb" stroke-width="1"/>
  <text x="260" y="340" font-size="9" fill="#1e40af">NdFeB Magnetic Dust Trap</text>
  <text x="260" y="352" font-size="9" fill="#475569">Dual PTFE Spring Seals</text>

  <!-- EVA Male Wand Probe (Advancing from Left) -->
  <g transform="translate(40, 20)">
    <!-- Insulated Grip Handle -->
    <rect x="30" y="195" width="110" height="70" rx="8" fill="#1e293b" stroke="#0f172a" stroke-width="2"/>
    <text x="85" y="235" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">EVA Glove Grip</text>
    <text x="85" y="248" font-size="8" fill="#94a3b8" text-anchor="middle">(75mm Palm Diameter)</text>

    <!-- Probe Shaft (PEEK High-Dielectric) -->
    <rect x="140" y="212" width="120" height="36" fill="#e2e8f0" stroke="#475569" stroke-width="1.5"/>
    <text x="200" y="233" font-size="9" fill="#475569" text-anchor="middle">PEEK Dielectric Body</text>

    <!-- Contact Pin Head (BeCu Gold-Plated) -->
    <path d="M 260 216 L 285 224 L 285 236 L 260 244 Z" fill="#f59e0b" stroke="#b45309" stroke-width="1.5"/>
  </g>

  <!-- Mechanical Vacuum Interlock Switch Core (Sealed Interior) -->
  <rect x="370" y="220" width="180" height="60" rx="4" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
  <text x="460" y="238" font-size="10" font-weight="bold" fill="#1e40af" text-anchor="middle">Vacuum Interlock Chamber</text>

  <!-- Contact Spring & Wiper -->
  <path d="M 370 240 L 390 232 L 400 248 L 410 232 L 420 248 L 430 240" fill="none" stroke="#b45309" stroke-width="2"/>
  <line x1="430" y1="240" x2="450" y2="240" stroke="#b45309" stroke-width="3"/>
  <circle cx="450" cy="240" r="5" fill="#f59e0b"/>
  <text x="440" y="265" font-size="9" fill="#b45309">Self-Wiping BeCu Terminal</text>

  <!-- Faraday Containment Enclosure (Nickel Plated Copper) -->
  <rect x="360" y="212" width="200" height="76" rx="6" fill="none" stroke="#059669" stroke-width="2" stroke-dasharray="4,2"/>
  <text x="460" y="300" font-size="9" font-weight="bold" fill="#047857" text-anchor="middle">Faraday Arc Containment Cage (1.0 mm Cu-Ni)</text>

  <!-- Resistor String Potted Assembly (Rear Block) -->
  <rect x="585" y="190" width="180" height="120" rx="6" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.5"/>
  <text x="675" y="212" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Potted Resistor Block</text>
  <rect x="600" y="225" width="150" height="20" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="1"/>
  <text x="675" y="239" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">1.0 GΩ Cermet Resistor String</text>
  <rect x="600" y="255" width="150" height="20" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="675" y="269" font-size="9" font-weight="bold" fill="#b45309" text-anchor="middle">12W Heaters + NuSil CV-1142</text>
  <text x="675" y="295" font-size="9" fill="#64748b" text-anchor="middle">To Lander Ground Bus (+100V)</text>

  <!-- Dimension Callouts -->
  <line x1="80" y1="90" x2="580" y2="90" stroke="#0284c7" stroke-width="1"/>
  <line x1="80" y1="85" x2="80" y2="95" stroke="#0284c7" stroke-width="1"/>
  <line x1="580" y1="85" x2="580" y2="95" stroke="#0284c7" stroke-width="1"/>
  <text x="330" y="82" font-size="10" font-weight="bold" fill="#0284c7" text-anchor="middle">Length: 285 mm</text>

  <line x1="60" y1="100" x2="60" y2="400" stroke="#0284c7" stroke-width="1"/>
  <line x1="55" y1="100" x2="65" y2="100" stroke="#0284c7" stroke-width="1"/>
  <line x1="55" y1="400" x2="65" y2="400" stroke="#0284c7" stroke-width="1"/>
  <text transform="rotate(-90)" x="-250" y="50" font-size="10" font-weight="bold" fill="#0284c7" text-anchor="middle">Outer Ø 160 mm</text>
</svg>'''

    with open("/home/afsal/lunar-grounding-challenge/deliverables/schematic_mechanical.svg", "w") as f:
        f.write(mech_svg)
    
    print("Generated all SVGs successfully.")

if __name__ == "__main__":
    generate_svgs()
