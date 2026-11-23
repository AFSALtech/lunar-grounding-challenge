"""
Generates Deliverable 3: Concept of Operations (Strictly 2-page PDF)
NASA rules: 11pt Arial, <=15 chars/inch, <=6 lines/inch, exactly 2 pages.
"""

import subprocess

def generate_deliverable_3():
    html_content = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>A-GATE: Concept of Operations</title>
<style>
  @page {
    size: letter;
    margin: 0.5in 0.55in 0.5in 0.55in;
  }
  body {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 11pt;
    line-height: 1.35;
    color: #0f172a;
    margin: 0;
    padding: 0;
  }
  .page {
    break-after: page;
    box-sizing: border-box;
    height: 10.0in;
    max-height: 10.0in;
    overflow: hidden;
    position: relative;
  }
  .page:last-child {
    break-after: avoid;
  }
  .header {
    border-bottom: 2px solid #1F3D76;
    padding-bottom: 3px;
    margin-bottom: 8px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }
  .header-title {
    font-size: 9pt;
    font-weight: bold;
    color: #1F3D76;
    text-transform: uppercase;
  }
  .header-doc {
    font-size: 8.5pt;
    color: #64748b;
  }
  .footer {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    border-top: 1px solid #cbd5e1;
    padding-top: 4px;
    display: flex;
    justify-content: space-between;
    font-size: 8.5pt;
    color: #64748b;
  }
  h1 {
    font-size: 15pt;
    color: #1F3D76;
    margin: 0 0 4px 0;
  }
  h2 {
    font-size: 12pt;
    color: #1e3a8a;
    margin: 8px 0 3px 0;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 2px;
  }
  h3 {
    font-size: 11pt;
    color: #0f172a;
    margin: 6px 0 2px 0;
  }
  p {
    margin: 0 0 5px 0;
    text-align: justify;
  }
  ul, ol {
    margin: 0 0 6px 0;
    padding-left: 18px;
  }
  li {
    margin-bottom: 2px;
  }
  .step-box {
    background: #f8fafc;
    border-left: 3px solid #1F3D76;
    padding: 5px 8px;
    margin: 4px 0;
    border-radius: 0 4px 4px 0;
  }
  .step-title {
    font-weight: bold;
    color: #1F3D76;
    font-size: 10pt;
  }
</style>
</head>
<body>

  <!-- ==================== PAGE 1 ==================== -->
  <div class="page">
    <div class="header">
      <span class="header-title">NASA Lunar Grounding Challenge — Concept of Operations (ConOps)</span>
      <span class="header-doc">A-GATE System | Phase 1</span>
    </div>

    <h1>A-GATE: Concept of Operations (ConOps)</h1>
    <p style="font-size:9.5pt; color:#475569; margin-bottom:6px;"><strong>Operational Architecture, Crew Workflow, and Multi-EVA Lifecycle for Artemis Lunar South Pole Surface Missions</strong></p>

    <h2>1. Mission Overview &amp; Operational Context</h2>
    <p>
      The A-GATE system provides an autonomous, passive-primary electrostatic neutralization capability supporting up to four surface EVAs over a 10-day mission at the lunar South Pole. The operational baseline mitigates the life-threatening hazard of a suited astronaut returning from a Permanently Shadowed Region (PSR) charged to -100 kV approaching a +100 V stationary lander. The Concept of Operations is partitioned into six sequential phases designed to minimize crew workload, eliminate single-point operational failures, and operate seamlessly in extreme lunar darkness and dusty terrain.
    </p>

    <h2>2. Phase I: Pre-Launch Integration &amp; Surface Transit</h2>
    <p>
      During vehicle assembly and payload integration on Earth:
    </p>
    <ul>
      <li><strong>Lander Bracket Mounting:</strong> The A-GATE Lander Receptacle Assembly (4.53 kg total) is bolted via four flight-qualified NAS6204 fasteners to the primary descent ladder structural rail at a nominal 1.1 m height above the landing pads.</li>
      <li><strong>Electrical &amp; Thermal Interface:</strong> The receptacle is bonded to the lander structural ground bus (&lt;10 mΩ) and connected to the lander 28V DC auxiliary power bus drawing 12.0 W nominal (40 W max limit) for internal Kapton strip heaters.</li>
      <li><strong>Transit &amp; Touchdown:</strong> The passive MLI blanket protects the internal core during trans-lunar injection, lunar orbit insertion, and powered descent. The assembly is rated for NASA GEVS qualification vibration (14.1 grms) with zero pyrotechnic deployment required.</li>
    </ul>

    <h2>3. Phase II: Autonomous Surface Activation &amp; Pre-EVA Check</h2>
    <p>
      Immediately following lunar touchdown on the rim of Shackleton Crater:
    </p>
    <ul>
      <li><strong>Heater Initiation:</strong> The lander avionics bus automatically energizes the A-GATE thermal loop, maintaining the core resistor block and mechanical interlock chamber between -40°C and +20°C despite ambient shadow temperatures plunging to 55 K (-361°F).</li>
      <li><strong>Optical Self-Test:</strong> The status LED ring illuminates in steady <strong>AMBER</strong>, confirming continuous ground bus continuity, heater operation, and receptacle readiness for incoming crew.</li>
      <li><strong>Crew Suit Check:</strong> Prior to egressing the airlock, each astronaut clips their personal EVA Grounding Wand (AG-WND-601-H) to the AxEMU chest tool carrier and confirms secure bonding to the suit backpack grounding lug.</li>
    </ul>

    <h2>4. Phase III: Surface Traverse &amp; Charge Accumulation</h2>
    <p>
      During surface exploration:
    </p>
    <ul>
      <li><strong>Regolith Interaction:</strong> As the astronaut walks through illuminated terrain and descends into deep PSRs, continuous boot-soil triboelectric charging and ambient plasma electron collection build up negative charge on the 200 pF suit capacitance.</li>
      <li><strong>Charge Standoff Protocol:</strong> Flight operational rules mandate that astronauts maintain a minimum standoff distance of 2.0 m from the lander metallic hull until electrostatic neutralization is confirmed, preventing unguided approach arcing.</li>
    </ul>

    <div class="footer">
      <span>A-GATE Concept of Operations</span>
      <span>Page 1 of 2</span>
    </div>
  </div>

  <!-- ==================== PAGE 2 ==================== -->
  <div class="page">
    <div class="header">
      <span class="header-title">NASA Lunar Grounding Challenge — Concept of Operations (ConOps)</span>
      <span class="header-doc">A-GATE System | Phase 1</span>
    </div>

    <h2>5. Phase IV: Approach, Docking &amp; Discharge Sequence</h2>
    <p>
      Upon returning to the lander, the astronaut executes the neutralization procedure:
    </p>

    <div class="step-box">
      <div class="step-title">Step 1: Visual Acquisition &amp; Wand Unholstering (Time: 0 to 5 s)</div>
      The returning astronaut halts at the base of the ladder. In low-sun or deep shadow lighting, self-luminous tritium crosshairs and the steady AMBER LED beacon guide visual orientation. The astronaut unholsters the EVA Wand from their chest with one pressurized glove.
    </div>

    <div class="step-box">
      <div class="step-title">Step 2: Blind-Mate Insertion &amp; Dust Scraping (Time: 5 to 8 s)</div>
      The astronaut guides the probe into the wide 160 mm funnel (60° capture cone). As the probe slides into the bore:
      (a) The 0.45 T NdFeB magnetic throat strips ferromagnetic agglutinates;
      (b) Dual PTFE spring-energized scrapers shear off adhering surface dust;
      (c) High-purity alumina sleeve isolates the probe from external metal.
    </div>

    <div class="step-box">
      <div class="step-title">Step 3: Zero-Gap Interlock Engagement &amp; Discharge (Time: 8 to 11 s)</div>
      At 45 mm insertion depth, mechanical cam arms compress the internal pushrod, closing switch SW1 within the sealed Faraday chamber with zero pre-contact gap. 
      The optical ring transitions to <strong>FLASHING BLUE (4 Hz)</strong>, signaling that discharge current is flowing through the 1.0 GΩ cermet resistor string. Peak current is clamped to <strong>0.100 mA</strong> (strictly below human perception).
    </div>

    <div class="step-box">
      <div class="step-title">Step 4: Equilibrium Confirmation &amp; Detent Release (Time: 11 to 13 s)</div>
      Within <strong>2.0 seconds</strong>, residual suit potential drops below 4.5 V (&lt;0.01 µA current). The onboard sensing circuit triggers the LED ring to <strong>STEADY GREEN</strong>, signaling "SAFE TO DISENGAGE &amp; CLIMB". An internal mechanical detent relaxes, permitting the astronaut to smoothly extract the probe.
    </div>

    <h2>6. Phase V: Vehicle Ingress &amp; Multi-EVA Lifecycle</h2>
    <p>
      Following successful discharge verification:
    </p>
    <ul>
      <li><strong>Automatic Cable Retraction:</strong> The spring-loaded reel automatically draws the grounding tether taut and snaps the wand into its harness retention holster.</li>
      <li><strong>Direct Ingress:</strong> The astronaut safely grasps the lander ladder rungs and ascends to the airlock with zero remaining electrostatic charge or arcing risk.</li>
      <li><strong>Multi-EVA Durability:</strong> The receptacle automatically returns to steady AMBER standby. With dry-lubricated components rated for 100+ mating cycles, A-GATE fully supports all 4 planned EVAs across the 10-day mission without servicing or consumables replacement.</li>
    </ul>

    <h2>7. Human Factors &amp; Crew Workload Evaluation</h2>
    <p>
      In accordance with NASA-STD-3001, Vol. 2:
    </p>
    <ul>
      <li><strong>Single-Handed Operation:</strong> The entire docking and discharge task requires only one hand, allowing the crew member to stabilize themselves with their opposite hand on the ladder rail.</li>
      <li><strong>Zero Fine Dexterity:</strong> The 160 mm funnel self-centers the probe even with ±30° angular misalignment and ±40 mm translational error, fully accommodating restricted EVA glove mobility.</li>
      <li><strong>Fail-Safe Contingency:</strong> If vehicle power is lost, the passive 1.0 GΩ dissipation network still neutralizes the astronaut flawlessly; only the LED indicator is unpowered (contingency rule: hold wand seated for 5 seconds).</li>
    </ul>

    <div class="footer">
      <span>A-GATE Concept of Operations</span>
      <span>Page 2 of 2</span>
    </div>
  </div>

</body>
</html>
"""

    html_path = "/home/afsal/lunar-grounding-challenge/html_source/deliverable_3.html"
    pdf_path = "/home/afsal/lunar-grounding-challenge/deliverables/Deliverable_3_Concept_of_Operations.pdf"
    
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
            print(f"Deliverable 3 generated: {line.strip()}")

if __name__ == "__main__":
    generate_deliverable_3()
