"""
Generates the comprehensive Bill of Materials (BOM) for the A-GATE system.
Covers: Lander Receptacle Assembly, EVA Probe Wand, Resistor Core,
Faraday Arc Chamber, Dust Labyrinths, Thermal Subsystem, and Avionics.
"""

import pandas as pd

def generate_bom():
    items = [
        {
            "Item_No": "1.1",
            "Subsystem": "Lander Receptacle",
            "Part_Name": "Guide Funnel & Docking Collar",
            "Part_Number": "AG-REC-101-A",
            "Manufacturer": "Moog Inc. / Space & Defense",
            "Material_Spec": "Aluminum 6061-T6 (MIL-A-8625 Type III Hard Anodize)",
            "Qty": 1,
            "Unit_Mass_kg": 0.850,
            "Total_Mass_kg": 0.850,
            "Assembly_Method": "Bolted via A286 high-strength fasteners to lander bracket",
            "TRL": 8,
            "Flight_Heritage": "Apollo/Orion docking collars"
        },
        {
            "Item_No": "1.2",
            "Subsystem": "Lander Receptacle",
            "Part_Name": "Dielectric Sleeve Liner",
            "Part_Number": "AG-ISO-201-B",
            "Manufacturer": "CoorsTek Inc.",
            "Material_Spec": "High-Purity Alumina Ceramic (99.5% Al2O3)",
            "Qty": 1,
            "Unit_Mass_kg": 0.420,
            "Total_Mass_kg": 0.420,
            "Assembly_Method": "Interference shrink-fit with ceramic retention ring",
            "TRL": 9,
            "Flight_Heritage": "ISS High Voltage Solar Array Isolators"
        },
        {
            "Item_No": "1.3",
            "Subsystem": "Dust Exclusion",
            "Part_Name": "Dual Spring-Energized Dust Seals",
            "Part_Number": "AG-SEA-301-D",
            "Manufacturer": "Trelleborg Sealing Solutions",
            "Material_Spec": "Virgin PTFE with Elgiloy Cantilever Spring",
            "Qty": 2,
            "Unit_Mass_kg": 0.045,
            "Total_Mass_kg": 0.090,
            "Assembly_Method": "Snap-retained internal groove assembly",
            "TRL": 8,
            "Flight_Heritage": "Mars Perseverance drill chuck seals"
        },
        {
            "Item_No": "1.4",
            "Subsystem": "Dust Exclusion",
            "Part_Name": "Magnetic Regolith Brush Ring",
            "Part_Number": "AG-MAG-302-A",
            "Manufacturer": "Dexter Magnetic Technologies",
            "Material_Spec": "Nickel-plated NdFeB N52 Magnets in Ti-6Al-4V Cage",
            "Qty": 1,
            "Unit_Mass_kg": 0.110,
            "Total_Mass_kg": 0.110,
            "Assembly_Method": "Press-fit and bonded with Master Bond EP21TCHT-1",
            "TRL": 6,
            "Flight_Heritage": "Mars Exploration Rover magnetic capture arrays"
        },
        {
            "Item_No": "1.5",
            "Subsystem": "Arc Containment",
            "Part_Name": "Faraday Chamber Shield Housing",
            "Part_Number": "AG-FAR-401-C",
            "Manufacturer": "EaglePicher / VACCO",
            "Material_Spec": "Oxygen-Free High Conductivity Copper (OFHC Cu C10100), Electroless Ni plated",
            "Qty": 1,
            "Unit_Mass_kg": 0.380,
            "Total_Mass_kg": 0.380,
            "Assembly_Method": "Electron-beam welded hermetic seam to mounting base",
            "TRL": 8,
            "Flight_Heritage": "Space Shuttle high-power EMI Faraday shields"
        },
        {
            "Item_No": "1.6",
            "Subsystem": "Arc Containment",
            "Part_Name": "Mechanical Zero-Gap Interlock Switch",
            "Part_Number": "AG-SWI-402-A",
            "Manufacturer": "Teledyne Relays / Leach",
            "Material_Spec": "Beryllium Copper (C17200) gold-plated blades, Alumina body",
            "Qty": 1,
            "Unit_Mass_kg": 0.220,
            "Total_Mass_kg": 0.220,
            "Assembly_Method": "Cam-actuated mechanical interlock tied to probe insertion depth",
            "TRL": 7,
            "Flight_Heritage": "Satellite payload umbilical blind-mate mechanisms"
        },
        {
            "Item_No": "2.1",
            "Subsystem": "Electrical Core",
            "Part_Name": "High-Voltage Cermet Resistor String (900 MΩ)",
            "Part_Number": "AG-RES-501-HV",
            "Manufacturer": "Ohmite Manufacturing / Vishay Dale",
            "Material_Spec": "Thick Film Cermet on 96% Alumina (Max 150 kV pulse, TCR < 50 ppm/K)",
            "Qty": 3,
            "Unit_Mass_kg": 0.180,
            "Total_Mass_kg": 0.540,
            "Assembly_Method": "Series solder-brazed with high-temperature Au-Sn eutectic",
            "TRL": 8,
            "Flight_Heritage": "JWST MIRI High Voltage Bias Divider"
        },
        {
            "Item_No": "2.2",
            "Subsystem": "Electrical Core",
            "Part_Name": "Current Monitoring Precision Shunt (100 MΩ)",
            "Part_Number": "AG-RES-502-SH",
            "Manufacturer": "Caddock Electronics",
            "Material_Spec": "Tetrinox Resistance Film, hermetically glass-passivated",
            "Qty": 1,
            "Unit_Mass_kg": 0.080,
            "Total_Mass_kg": 0.080,
            "Assembly_Method": "Direct terminal pin brazing",
            "TRL": 9,
            "Flight_Heritage": "Hubble Space Telescope electronics"
        },
        {
            "Item_No": "2.3",
            "Subsystem": "Electrical Core",
            "Part_Name": "High-Voltage Dielectric Potting Compound",
            "Part_Number": "AG-POT-503-E",
            "Manufacturer": "NuSil Technology LLC",
            "Material_Spec": "CV-1142 Low-Outgassing Controlled Volatility Silicone (CVCM < 0.01%)",
            "Qty": 1,
            "Unit_Mass_kg": 0.350,
            "Total_Mass_kg": 0.350,
            "Assembly_Method": "Vacuum de-aired centrifugal potting and thermal cure",
            "TRL": 9,
            "Flight_Heritage": "Orion spacecraft high-voltage harness potting"
        },
        {
            "Item_No": "3.1",
            "Subsystem": "EVA Wand & Harness",
            "Part_Name": "Ergonomic EVA Glove Grip Handle",
            "Part_Number": "AG-WND-601-H",
            "Manufacturer": "ILC Dover / Collins Aerospace",
            "Material_Spec": "PEEK (Polyetheretherketone) 450G with anti-static dissipative coating",
            "Qty": 1,
            "Unit_Mass_kg": 0.280,
            "Total_Mass_kg": 0.280,
            "Assembly_Method": "Modular latch to AxEMU harness tool clip",
            "TRL": 7,
            "Flight_Heritage": "EMU Pistol Grip Tool (PGT)"
        },
        {
            "Item_No": "3.2",
            "Subsystem": "EVA Wand & Harness",
            "Part_Name": "Spring-Loaded Coaxial Contact Pin",
            "Part_Number": "AG-PIN-602-C",
            "Manufacturer": "Amphenol Aerospace",
            "Material_Spec": "Beryllium Copper Alloy 25, 50 µin hard gold plating over nickel",
            "Qty": 1,
            "Unit_Mass_kg": 0.060,
            "Total_Mass_kg": 0.060,
            "Assembly_Method": "Threaded retaining nut with Belleville preload washers",
            "TRL": 8,
            "Flight_Heritage": "Artemis Gateway blind mate power connectors"
        },
        {
            "Item_No": "3.3",
            "Subsystem": "EVA Wand & Harness",
            "Part_Name": "Retractable High-Voltage Grounding Cable",
            "Part_Number": "AG-CAB-603-T",
            "Manufacturer": "W.L. Gore & Associates",
            "Material_Spec": "Silver-plated copper braid, expanded PTFE dielectric (rated 120 kV DC)",
            "Qty": 1,
            "Unit_Mass_kg": 0.360,
            "Total_Mass_kg": 0.360,
            "Assembly_Method": "Spring-reel canister attached to suit backpack bonding lug",
            "TRL": 8,
            "Flight_Heritage": "ISS EVA safety tethers"
        },
        {
            "Item_No": "4.1",
            "Subsystem": "Thermal & Enclosure",
            "Part_Name": "Multi-Layer Insulation (MLI) Blanket",
            "Part_Number": "AG-MLI-701-K",
            "Manufacturer": "Sheldahl Flexible Technologies",
            "Material_Spec": "15-Layer double-aluminized Mylar with Dacron netting & Kapton outer face",
            "Qty": 1,
            "Unit_Mass_kg": 0.160,
            "Total_Mass_kg": 0.160,
            "Assembly_Method": "Nomex hook-and-loop fasteners and transfer adhesive tape",
            "TRL": 9,
            "Flight_Heritage": "Standard space thermal blankets"
        },
        {
            "Item_No": "4.2",
            "Subsystem": "Thermal & Enclosure",
            "Part_Name": "Lander-Powered Patch Heaters",
            "Part_Number": "AG-HTR-702-M",
            "Manufacturer": "Minco Products, Inc.",
            "Material_Spec": "Kapton insulated etched-foil heaters (12W nominal, 28V DC bus)",
            "Qty": 2,
            "Unit_Mass_kg": 0.035,
            "Total_Mass_kg": 0.070,
            "Assembly_Method": "Pressure-sensitive acrylic adhesive layer to core aluminum body",
            "TRL": 9,
            "Flight_Heritage": "Curiosity & Perseverance rover robotic arm heaters"
        },
        {
            "Item_No": "4.3",
            "Subsystem": "Thermal & Enclosure",
            "Part_Name": "Lander Structural Mounting Bracket",
            "Part_Number": "AG-BKT-703-L",
            "Manufacturer": "General Dynamics / Honeybee Robotics",
            "Material_Spec": "Titanium Ti-6Al-4V (Grade 5 annealed)",
            "Qty": 1,
            "Unit_Mass_kg": 0.420,
            "Total_Mass_kg": 0.420,
            "Assembly_Method": "Four NAS6204 bolts to lander ladder descent rail",
            "TRL": 8,
            "Flight_Heritage": "Apollo Lunar Module egress platform brackets"
        },
        {
            "Item_No": "5.1",
            "Subsystem": "Avionics & Optical",
            "Part_Name": "Status Indicator Ring & Electronics",
            "Part_Number": "AG-AV-801-LED",
            "Manufacturer": "Broadcom Space Products / STMicroelectronics",
            "Material_Spec": "Radiation-hardened GaN LED cluster, sapphire diffuser window",
            "Qty": 1,
            "Unit_Mass_kg": 0.140,
            "Total_Mass_kg": 0.140,
            "Assembly_Method": "O-ring sealed bezel with Viton GLT extreme low-temp seal",
            "TRL": 8,
            "Flight_Heritage": "Dragon / Starliner external docking status indicators"
        }
    ]

    df = pd.DataFrame(items)
    
    # Calculate totals
    total_mass = df["Total_Mass_kg"].sum()
    print(f"Total BOM Components: {len(df)}")
    print(f"Total System Mass: {total_mass:.3f} kg (NASA limit is 20.0 kg - Margin: {(20.0 - total_mass)/20.0 * 100:.1f}%)")
    
    csv_path = "/home/afsal/lunar-grounding-challenge/deliverables/Deliverable_2B_Bill_of_Materials.csv"
    df.to_csv(csv_path, index=False)
    print(f"Saved Bill of Materials to {csv_path}")
    return df

if __name__ == "__main__":
    generate_bom()
