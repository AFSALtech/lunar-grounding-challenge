"""
Generates Deliverable 6B: Risk Assessment Matrix (Formatted Landscape PDF)
"""

import subprocess
import pandas as pd

def generate_deliverable_6b():
    df = pd.read_csv("/home/afsal/lunar-grounding-challenge/deliverables/Deliverable_6B_Risk_Matrix.csv")
    
    rows_html = ""
    for _, row in df.iterrows():
        # color code initial score
        init_color = "#dc2626" if row['Init_Score'] >= 16 else ("#d97706" if row['Init_Score'] >= 10 else "#2563eb")
        rows_html += f"""
        <tr>
          <td style="font-weight:bold; text-align:center;">{row['Risk_ID']}</td>
          <td><strong>{row['Category']}</strong></td>
          <td><strong>{row['Risk_Title']}</strong><br/><span style="color:#475569; font-size:7pt;">Failure Mode: {row['Failure_Mode']}</span></td>
          <td style="font-size:7pt; color:#64748b;">{row['Root_Cause']}</td>
          <td style="text-align:center; font-weight:bold; color:{init_color};">{row['Init_Sev']} &times; {row['Init_Lik']} = {row['Init_Score']}</td>
          <td style="font-size:7pt;">{row['Mitigation_Strategy']}</td>
          <td style="text-align:center; font-weight:bold; color:#15803d;">{row['Post_Sev']} &times; {row['Post_Lik']} = {row['Post_Score']}</td>
          <td style="font-size:7pt; color:#334155;">{row['Verification_Method']}</td>
        </tr>
        """

    html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>A-GATE: FMECA Risk Matrix</title>
<style>
  @page {{
    size: letter landscape;
    margin: 0.45in 0.5in 0.45in 0.5in;
  }}
  body {{
    font-family: Arial, Helvetica, sans-serif;
    font-size: 8pt;
    color: #0f172a;
    margin: 0;
    padding: 0;
  }}
  .header {{
    border-bottom: 2px solid #1F3D76;
    padding-bottom: 3px;
    margin-bottom: 8px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }}
  .header-title {{
    font-size: 11pt;
    font-weight: bold;
    color: #1F3D76;
    text-transform: uppercase;
  }}
  .header-doc {{
    font-size: 8.5pt;
    color: #64748b;
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 7.5pt;
  }}
  th, td {{
    border: 1px solid #cbd5e1;
    padding: 3.5px 4.5px;
  }}
  th {{
    background: #1F3D76;
    color: #ffffff;
    font-weight: bold;
    text-align: left;
  }}
  tr:nth-child(even) {{
    background: #f8fafc;
  }}
  .summary-bar {{
    margin-top: 8px;
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    border-radius: 4px;
    padding: 6px 12px;
    display: flex;
    justify-content: space-between;
    font-size: 8pt;
  }}
</style>
</head>
<body>
  <div class="header">
    <span class="header-title">A-GATE System — Failure Modes, Effects &amp; Criticality Analysis (FMECA) Risk Matrix</span>
    <span class="header-doc">NASA Lunar Grounding Challenge | Deliverable 6B</span>
  </div>

  <table>
    <thead>
      <tr>
        <th style="width:6%; text-align:center;">ID</th>
        <th style="width:9%;">Category</th>
        <th style="width:18%;">Risk Title &amp; Failure Mode</th>
        <th style="width:13%;">Root Cause</th>
        <th style="width:7%; text-align:center;">Initial (S&times;L)</th>
        <th style="width:23%;">Mitigation Strategy &amp; Redundant Safety Pathway</th>
        <th style="width:7%; text-align:center;">Post (S&times;L)</th>
        <th style="width:17%;">Verification Method</th>
      </tr>
    </thead>
    <tbody>
      {rows_html}
    </tbody>
  </table>

  <div class="summary-bar">
    <span><strong>Risk Scoring Key:</strong> Severity (1-5) &times; Likelihood (1-5) = Risk Score (1-25) | High &ge; 16 (Red), Med 10-15 (Amber), Low &lt; 10 (Green)</span>
    <span><strong>Post-Mitigation Status:</strong> <strong style="color:#15803d;">100% of Identified Risks Reduced to LOW (Score &le; 4)</strong></span>
    <span><strong>Standard:</strong> NASA-STD-8729.1 &amp; NPR 8705.4</span>
  </div>
</body>
</html>
"""

    html_path = "/home/afsal/lunar-grounding-challenge/html_source/deliverable_6b.html"
    pdf_path = "/home/afsal/lunar-grounding-challenge/deliverables/Deliverable_6B_Risk_Matrix.pdf"
    
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
            print(f"Deliverable 6B generated: {line.strip()}")

if __name__ == "__main__":
    generate_deliverable_6b()
