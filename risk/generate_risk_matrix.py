"""
Generates the comprehensive Failure Modes, Effects, and Criticality Analysis (FMECA)
and Risk Assessment Matrix for the A-GATE Lunar Grounding System.
"""

import pandas as pd

def generate_risk_matrix():
    risks = [
        {
            "Risk_ID": "RSK-E01",
            "Category": "Electrical",
            "Risk_Title": "Pre-Contact Vacuum Dust Arcing",
            "Failure_Mode": "High-voltage spark breakdown jumps across open gap between probe tip and lander before full mating.",
            "Root_Cause": "Suspended charged lunar regolith dust lowers dielectric breakdown threshold in lunar vacuum.",
            "Init_Sev": 5, "Init_Lik": 4, "Init_Score": 20,
            "Mitigation_Strategy": "Deeply recessed contact pin inside dielectric sleeve + mechanical sequence interlock switch. Circuit remains physically open during insertion stroke and only engages after full mechanical mating eliminates the open gap.",
            "Post_Sev": 2, "Post_Lik": 1, "Post_Score": 2,
            "Verification_Method": "High-voltage chamber test (120 kV, 10^-6 Torr) with JSC-1A lunar regolith simulant dust cloud."
        },
        {
            "Risk_ID": "RSK-E02",
            "Category": "Electrical",
            "Risk_Title": "Resistor String Dielectric Flashover",
            "Failure_Mode": "Surface flashover across 1.0 GΩ cermet resistor string body causes low-impedance short circuit.",
            "Root_Cause": "Thermal expansion mismatch micro-cracks or trapped gas voids in potting under deep vacuum.",
            "Init_Sev": 5, "Init_Lik": 3, "Init_Score": 15,
            "Mitigation_Strategy": "Segmented 3-resistor cermet string with ceramic creepage barriers; vacuum centrifugal centrifugal degassing and potting with space-grade NuSil CV-1142; rated to 150 kV pulse withstand (50% derating).",
            "Post_Sev": 3, "Post_Lik": 1, "Post_Score": 3,
            "Verification_Method": "Partial discharge testing (IEC 60270) and dielectric withstand test at 150 kV DC across thermal range."
        },
        {
            "Risk_ID": "RSK-M01",
            "Category": "Mechanical / Dust",
            "Risk_Title": "Regolith Jamming of Docking Funnel",
            "Failure_Mode": "Accumulated abrasive lunar dust inside guide sleeve binds or prevents full seating of EVA probe wand.",
            "Root_Cause": "Sub-micron regolith particles (0.02 - 10 µm) kicked up by boots entering open receptacle.",
            "Init_Sev": 4, "Init_Lik": 4, "Init_Score": 16,
            "Mitigation_Strategy": "Dual PTFE spring-energized scraper seals + high-gradient NdFeB magnetic dust collar at funnel throat to trap magnetic/agglutinate particles; 60° self-clearing funnel cone with MoS2 dry lubricant.",
            "Post_Sev": 2, "Post_Lik": 2, "Post_Score": 4,
            "Verification_Method": "Life cycle insertion test (50 cycles) in dirty vacuum chamber with sub-micron abrasive simulant."
        },
        {
            "Risk_ID": "RSK-T01",
            "Category": "Thermal",
            "Risk_Title": "Cryogenic Freezing in Lunar PSR",
            "Failure_Mode": "Extreme temperatures down to -361°F (55 K) cause embrittlement, contact stiffness, or excessive resistor TCR shift.",
            "Root_Cause": "Absence of solar radiation in permanently shadowed crater floors during Artemis IV EVAs.",
            "Init_Sev": 4, "Init_Lik": 3, "Init_Score": 12,
            "Mitigation_Strategy": "15-layer MLI blanket around resistor core; dual redundant 12W Kapton strip heaters drawing from lander 28V DC bus; core temperature maintained above -40°C; low TCR cermet (<50 ppm/K).",
            "Post_Sev": 2, "Post_Lik": 1, "Post_Score": 2,
            "Verification_Method": "Thermal vacuum chamber (TVAC) cycling test between 55 K and 300 K with active heater loop."
        },
        {
            "Risk_ID": "RSK-H01",
            "Category": "Human Factors",
            "Risk_Title": "Premature Disengagement by Crew",
            "Failure_Mode": "Astronaut pulls EVA wand out of receptacle before full charge dissipation (<2 seconds), causing residual shock.",
            "Root_Cause": "Crew hurry, fatigue, or low visibility in pitch-black shadow conditions.",
            "Init_Sev": 4, "Init_Lik": 3, "Init_Score": 12,
            "Mitigation_Strategy": "Spring-loaded mechanical capture detent requires deliberate 35 N unlatching pull force; high-contrast tri-color LED status ring with solid green 'SAFE TO DISENGAGE' visual confirmation.",
            "Post_Sev": 2, "Post_Lik": 1, "Post_Score": 2,
            "Verification_Method": "Human-in-the-loop pressurized suit glove ergonomic evaluation in NBL / simulated low-gravity mock-up."
        },
        {
            "Risk_ID": "RSK-O01",
            "Category": "Operational",
            "Risk_Title": "Cable Snag or Entanglement During Ingress",
            "Failure_Mode": "EVA grounding cable snags on lander ladder rungs, causing trip hazard or damaged cable.",
            "Root_Cause": "Slack in grounding tether during crew movement up the ladder.",
            "Init_Sev": 3, "Init_Lik": 3, "Init_Score": 9,
            "Mitigation_Strategy": "Spring-retracted cable reel mounted on suit harness keeps cable taut (<5 N tension); auto-stows wand into harness holster upon release with quick-breakaway safety link (45 N).",
            "Post_Sev": 2, "Post_Lik": 1, "Post_Score": 2,
            "Verification_Method": "Ladder ascent mobility trials with pressurized suit harness."
        },
        {
            "Risk_ID": "RSK-E03",
            "Category": "Electrical",
            "Risk_Title": "Arc Plasma Leakage to Exterior Environment",
            "Failure_Mode": "Internal micro-discharge vents plasma or UV photons that degrade outer suit garment.",
            "Root_Cause": "Contact bounce during mechanical switch closure inside chamber.",
            "Init_Sev": 5, "Init_Lik": 2, "Init_Score": 10,
            "Mitigation_Strategy": "Sealed OFHC Copper-Nickel Faraday cage surrounding switch contacts with tortuous optical labyrinth vents; located on lander ladder rail >1.5 m standoff distance from suit fabrics.",
            "Post_Sev": 1, "Post_Lik": 1, "Post_Score": 1,
            "Verification_Method": "Optical emission spectroscopy and streak camera imaging during 120 kV switch closure in vacuum."
        }
    ]

    df = pd.DataFrame(risks)
    csv_path = "/home/afsal/lunar-grounding-challenge/deliverables/Deliverable_6B_Risk_Matrix.csv"
    df.to_csv(csv_path, index=False)
    print(f"Saved Risk Matrix ({len(df)} risks) to {csv_path}")
    return df

if __name__ == "__main__":
    generate_risk_matrix()
