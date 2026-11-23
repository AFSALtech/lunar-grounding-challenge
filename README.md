# A-GATE: Arc-Suppressed Grounding & Alignment Terminal for Lunar EVAs

> **NASA Tournament Lab — Lunar Grounding Challenge ($150,000 Prize Purse)**  
> *A Two-Stage Dissipative Mechanical-Interlock Discharge System for Artemis Lunar South Pole EVAs*

[![NASA Challenge](https://img.shields.io/badge/NASA-Tournament%20Lab-1F3D76.svg)](https://work.crowdplat.com/challenge/lunar-grounding-challenge)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Executive Summary

During lunar surface Extravehicular Activities (EVAs) at the lunar South Pole, suited astronauts traversing permanently shadowed regions (PSRs) accumulate extreme negative potentials up to **-100 kV**. When returning to the sunlit stationary lander (+100 V), the **>100 kV potential differential** creates an imminent risk of sudden, destructive vacuum flashover arcing mediated by suspended, charged lunar regolith dust (0.02–10 µm).

**A-GATE** solves this problem through a flight-ready, two-stage mechanical-dielectric terminal:
1. **Zero-Gap Sequenced Mechanical Interlock:** The contact switch remains mechanically open during probe approach and closure occurs only after complete mechanical seating inside a sealed chamber, physically eliminating pre-contact vacuum spark inception.
2. **Faraday Arc Containment Cage:** Contact mating is enclosed in an electroless nickel-plated OFHC copper Faraday cage (>60 dB EMI attenuation), situated >1.5 m away from suit textiles.
3. **1.0 GΩ Cermet Resistor String:** Clamps peak discharge current to **0.100 mA** (50% below NASA's 0.20 mA perception target) and equilibrates the astronaut (<4.5 V) in **2.0 seconds** (well within the 30-second requirement).

---

## Performance & Requirements Scorecard

| Parameter | NASA Challenge Requirement | A-GATE Performance | Safety Margin |
|---|---|---|---|
| **Peak Discharge Current** | $\le 1.0\text{ mA}$ (Target $\le 0.20\text{ mA}$) | **$0.100\text{ mA}$ ($100\ \mu\text{A}$)** | **50.0% below perception target** (90% below limit) |
| **Discharge Duration** | $\le 30\text{ seconds}$ | **$2.00\text{ seconds}$** ($\Delta V < 4.5\text{ V}$) | **93.3% time margin** |
| **Arc Contact with Suit** | No arcing to suit/astronaut | **100% physically contained in Faraday cage** | Complete elimination |
| **Total System Mass** | $< 20.0\text{ kg}$ | **$4.530\text{ kg}$** | **77.4% mass margin** (15.47 kg reserve) |
| **Power Consumption** | $\le 40.0\text{ W}$ Max | **$12.0\text{ W}$ nominal / $13.6\text{ W}$ peak** | **66.0% power margin** |
| **Multi-EVA Endurance** | 4 EVAs over 10 days | **100+ insertion cycles rated** | 25x mission lifecycle |
| **Operating Temperatures** | $-361^\circ\text{F}$ to $-31^\circ\text{F}$ (55 K to 238 K) | Core maintained $-40^\circ\text{C}$ to $+40^\circ\text{C}$ | Decoupled via 15-layer MLI + heaters |

---

## Deliverables in this Repository

* **`deliverables/Deliverable_1_Concept_Description.pdf`**: 5-page NASA-formatted technical concept narrative.
* **`deliverables/Deliverable_2A_Drawings_Schematics.pdf`**: 3 sheets of dimensioned ANSI mechanical & electrical engineering drawings.
* **`deliverables/Deliverable_2A_A_GATE_System.step`**: ISO 10303-21 AP214 CAD solid model of the entire docking assembly.
* **`deliverables/Deliverable_2B_Bill_of_Materials.csv` & `.pdf`**: 16 flight-qualified parts, CAGE codes, materials, masses, and TRL.
* **`deliverables/Deliverable_3_Concept_of_Operations.pdf`**: 2-page operational workflow for Artemis crew.
* **`deliverables/Deliverable_4_Physical_Properties_Estimate.pdf`**: 1-page structural mass, CG, and power budget breakdown.
* **`deliverables/Deliverable_5A_Electrical_Performance_Analysis.pdf`**: 5-page transient circuit and vacuum arc physics analysis.
* **`deliverables/Deliverable_5B_Electrical_Discharge_Data.csv`**: 3,001-row numerical ODE transient simulation time-series dataset.
* **`deliverables/Deliverable_6A_Risk_Assessment_Overview.pdf`**: 1-page NASA-STD-8729.1 FMECA risk overview.
* **`deliverables/Deliverable_6B_Risk_Matrix.csv` & `.pdf`**: Full 7-row failure mode and mitigation matrix.
