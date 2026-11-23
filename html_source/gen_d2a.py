"""
Generates Deliverable 2A: Technical Representation Deliverable - 2D Engineering Drawings & Schematics
Format: Multi-sheet 11x8.5 landscape or portrait engineering drawing format with ANSI title blocks.
"""

import subprocess

def generate_deliverable_2a():
    html_content = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>A-GATE: 2D Engineering Drawings &amp; Schematics</title>
<style>
  @page {
    size: letter landscape;
    margin: 0.4in;
  }
  body {
    font-family: Arial, Helvetica, sans-serif;
    color: #0f172a;
    margin: 0;
    padding: 0;
    background: #ffffff;
  }
  .sheet {
    break-after: page;
    box-sizing: border-box;
    width: 10.2in;
    height: 7.6in;
    max-height: 7.6in;
    overflow: hidden;
    position: relative;
    border: 2px solid #0f172a;
    padding: 8px;
  }
  .sheet:last-child {
    break-after: avoid;
  }
  /* ANSI Title Block */
  .title-block {
    position: absolute;
    bottom: 8px;
    right: 8px;
    width: 4.8in;
    border: 1.5px solid #0f172a;
    background: #f8fafc;
    display: grid;
    grid-template-columns: 2fr 1fr 1fr;
    font-size: 8pt;
  }
  .tb-cell {
    border: 0.5px solid #0f172a;
    padding: 2px 4px;
  }
  .tb-header {
    font-size: 6.5pt;
    text-transform: uppercase;
    color: #475569;
    font-weight: bold;
  }
  .tb-val {
    font-size: 8.5pt;
    font-weight: bold;
    color: #0f172a;
  }
  .drawing-title {
    font-size: 13pt;
    font-weight: bold;
    color: #1F3D76;
    margin-bottom: 2px;
  }
  .notes-block {
    position: absolute;
    top: 10px;
    left: 10px;
    width: 3.2in;
    background: #f8fafc;
    border: 1px solid #94a3b8;
    padding: 6px 8px;
    font-size: 7.5pt;
    line-height: 1.25;
  }
  .notes-title {
    font-weight: bold;
    text-transform: uppercase;
    color: #1F3D76;
    margin-bottom: 3px;
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 1px;
  }
  .view-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    width: 100%;
  }
</style>
</head>
<body>

  <!-- ==================== SHEET 1 ==================== -->
  <div class="sheet">
    <div class="notes-block">
      <div class="notes-title">General Engineering Notes</div>
      <ol style="margin:0; padding-left:14px;">
        <li>ALL DIMENSIONS ARE IN MILLIMETERS [INCHES].</li>
        <li>TOLERANCES UNLESS OTHERWISE SPECIFIED:<br/>
            .X = ±0.5 mm [±0.020 in]<br/>
            .XX = ±0.15 mm [±0.006 in]<br/>
            ANGLES = ±0.5°</li>
        <li>SURFACE FINISH: 32 µin Ra MAX ON SEALING SURFACES.</li>
        <li>MATERIALS:<br/>
            HOUSING: AL 6061-T6 MIL-A-8625 TYPE III HARD COAT.<br/>
            INSULATOR: 99.5% ALUMINA CERAMIC (Al2O3).<br/>
            FARADAY CAGE: OFHC COPPER C10100 NI-PLATED.<br/>
            SEALS: VIRGIN PTFE W/ ELGILOY CANTILEVER SPRINGS.</li>
        <li>COATING: DRY FILM LUBRICANT MoS2 PER MIL-PRF-81329 ON SLIDING SURFACES.</li>
        <li>DIELECTRIC WITHSTAND: 150 kV DC VACUUM VOLTAGE PROOF.</li>
      </ol>
    </div>

    <div class="view-container" style="padding-left:1.8in; padding-bottom:1.2in;">
      <img src="schematic_mechanical.svg" style="width:78%; max-height:5.2in;" alt="A-GATE Mechanical Assembly"/>
    </div>

    <!-- Title Block -->
    <div class="title-block">
      <div class="tb-cell" style="grid-column: 1 / span 3; background:#eff6ff;">
        <span class="tb-header">PROGRAM / SPONSOR</span>
        <div class="tb-val" style="color:#1F3D76;">NASA TOURNAMENT LAB / CROWDPLAT — LUNAR GROUNDING CHALLENGE</div>
      </div>
      <div class="tb-cell" style="grid-column: 1 / span 2;">
        <span class="tb-header">DRAWING TITLE</span>
        <div class="tb-val">A-GATE SYSTEM ASSEMBLY &amp; CROSS-SECTION</div>
      </div>
      <div class="tb-cell">
        <span class="tb-header">CAGE CODE</span>
        <div class="tb-val">AG001</div>
      </div>
      <div class="tb-cell">
        <span class="tb-header">DRAWING NUMBER</span>
        <div class="tb-val">DWG-AG-1001-A</div>
      </div>
      <div class="tb-cell">
        <span class="tb-header">REV</span>
        <div class="tb-val">B.1</div>
      </div>
      <div class="tb-cell">
        <span class="tb-header">SHEET</span>
        <div class="tb-val">1 OF 3</div>
      </div>
      <div class="tb-cell">
        <span class="tb-header">SCALE</span>
        <div class="tb-val">1:2 [METRIC]</div>
      </div>
      <div class="tb-cell" style="grid-column: 2 / span 2;">
        <span class="tb-header">STATUS</span>
        <div class="tb-val" style="color:#15803d;">RELEASED FOR FLIGHT CONCEPT</div>
      </div>
    </div>
  </div>

  <!-- ==================== SHEET 2 ==================== -->
  <div class="sheet">
    <div class="notes-block">
      <div class="notes-title">Electrical System Notes</div>
      <ol style="margin:0; padding-left:14px;">
        <li>R_TOTAL = 1.00 GΩ ±1% OVER -40°C TO +40°C (HEATED CORE).</li>
        <li>R1 = 900 MΩ HIGH VOLTAGE THICK-FILM CERMET STRING (3x 300 MΩ).</li>
        <li>R2 = 100 MΩ KELVIN CURRENT MONITOR SHUNT (1.0 V / 10 µA SCALE).</li>
        <li>FARADAY SHIELD BONDED TO LANDER STRUCTURE (< 0.010 Ω DC BONDING RESISTANCE PER MIL-B-5087B CLASS R).</li>
        <li>OPTICAL STATUS LED RING POWERED BY LANDER 28V DC BUS (1.5 W MAX ACTIVE).</li>
        <li>PASSIVE FAIL-SAFE: DISCHARGE OCCURS ENTIRELY VIA PASSIVE RESISTOR NETWORK WITHOUT ACTIVE POWER.</li>
      </ol>
    </div>

    <div class="view-container" style="padding-left:1.8in; padding-bottom:1.2in;">
      <img src="schematic_circuit.svg" style="width:82%; max-height:5.2in;" alt="A-GATE Electrical Schematic"/>
    </div>

    <!-- Title Block -->
    <div class="title-block">
      <div class="tb-cell" style="grid-column: 1 / span 3; background:#eff6ff;">
        <span class="tb-header">PROGRAM / SPONSOR</span>
        <div class="tb-val" style="color:#1F3D76;">NASA TOURNAMENT LAB / CROWDPLAT — LUNAR GROUNDING CHALLENGE</div>
      </div>
      <div class="tb-cell" style="grid-column: 1 / span 2;">
        <span class="tb-header">DRAWING TITLE</span>
        <div class="tb-val">ELECTRICAL SCHEMATIC &amp; WIRING ARCHITECTURE</div>
      </div>
      <div class="tb-cell">
        <span class="tb-header">CAGE CODE</span>
        <div class="tb-val">AG001</div>
      </div>
      <div class="tb-cell">
        <span class="tb-header">DRAWING NUMBER</span>
        <div class="tb-val">DWG-AG-2001-E</div>
      </div>
      <div class="tb-cell">
        <span class="tb-header">REV</span>
        <div class="tb-val">B.1</div>
      </div>
      <div class="tb-cell">
        <span class="tb-header">SHEET</span>
        <div class="tb-val">2 OF 3</div>
      </div>
      <div class="tb-cell">
        <span class="tb-header">SCALE</span>
        <div class="tb-val">NONE</div>
      </div>
      <div class="tb-cell" style="grid-column: 2 / span 2;">
        <span class="tb-header">STATUS</span>
        <div class="tb-val" style="color:#15803d;">RELEASED FOR FLIGHT CONCEPT</div>
      </div>
    </div>
  </div>

  <!-- ==================== SHEET 3 ==================== -->
  <div class="sheet">
    <div class="notes-block">
      <div class="notes-title">Interlock &amp; Interface Notes</div>
      <ol style="margin:0; padding-left:14px;">
        <li>INSERTION STROKE: TOTAL 50.0 mm TRAVEL.<br/>
            0-45 mm: SEALING &amp; MAGNETIC SCAVENGING (CIRCUIT OPEN).<br/>
            45-50 mm: CAM ACTUATION ENGAGES ZERO-GAP CONTACT.</li>
        <li>NORMAL CONTACT FORCE: 12.0 N PRELOADED BY BeCu WIPERS.</li>
        <li>DETENT RETENTION FORCE: 35.0 N PULL-OUT RESISTANCE.</li>
        <li>WAND HANDLE: PEEK 450G DIELECTRIC HOUSING (VOLUME RESISTIVITY > 10^16 Ω-cm).</li>
        <li>GROUNDING CABLE: 1.8 m GORE EXPANDED PTFE COAXIAL TETHER RATED TO 120 kV PULSE.</li>
      </ol>
    </div>

    <div class="view-container" style="padding-left:1.8in; padding-bottom:1.2in;">
      <img src="plot_discharge_current.svg" style="width:78%; max-height:5.2in;" alt="A-GATE Discharge Curves"/>
    </div>

    <!-- Title Block -->
    <div class="title-block">
      <div class="tb-cell" style="grid-column: 1 / span 3; background:#eff6ff;">
        <span class="tb-header">PROGRAM / SPONSOR</span>
        <div class="tb-val" style="color:#1F3D76;">NASA TOURNAMENT LAB / CROWDPLAT — LUNAR GROUNDING CHALLENGE</div>
      </div>
      <div class="tb-cell" style="grid-column: 1 / span 2;">
        <span class="tb-header">DRAWING TITLE</span>
        <div class="tb-val">PERFORMANCE ENVELOPE &amp; TRANSIENT VERIFICATION</div>
      </div>
      <div class="tb-cell">
        <span class="tb-header">CAGE CODE</span>
        <div class="tb-val">AG001</div>
      </div>
      <div class="tb-cell">
        <span class="tb-header">DRAWING NUMBER</span>
        <div class="tb-val">DWG-AG-3001-P</div>
      </div>
      <div class="tb-cell">
        <span class="tb-header">REV</span>
        <div class="tb-val">B.1</div>
      </div>
      <div class="tb-cell">
        <span class="tb-header">SHEET</span>
        <div class="tb-val">3 OF 3</div>
      </div>
      <div class="tb-cell">
        <span class="tb-header">SCALE</span>
        <div class="tb-val">NONE</div>
      </div>
      <div class="tb-cell" style="grid-column: 2 / span 2;">
        <span class="tb-header">STATUS</span>
        <div class="tb-val" style="color:#15803d;">RELEASED FOR FLIGHT CONCEPT</div>
      </div>
    </div>
  </div>

</body>
</html>
"""

    html_path = "/home/afsal/lunar-grounding-challenge/html_source/deliverable_2a.html"
    pdf_path = "/home/afsal/lunar-grounding-challenge/deliverables/Deliverable_2A_Drawings_Schematics.pdf"
    
    with open(html_path, "w") as f:
        f.write(html_content)
        
    cmd = [
        "google-chrome",
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    subprocess.run(cmd, check=True)
    
    out = subprocess.check_output(["pdfinfo", pdf_path]).decode()
    for line in out.splitlines():
        if "Pages:" in line:
            print(f"Deliverable 2A generated: {line.strip()}")

if __name__ == "__main__":
    generate_deliverable_2a()
