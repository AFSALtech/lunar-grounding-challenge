"""
NASA Lunar Grounding Challenge: Electrical Performance Simulation
Model: Suited Astronaut Discharge through A-GATE 1.0 Gigaohm Dissipation Network
Capacitance: C = 200 pF, V_astronaut = -100 kV, V_lander = +100 V
"""

import numpy as np
import pandas as pd
import math

def run_simulation():
    # Parameters
    C = 200e-12        # Farads (200 pF)
    V0 = -100000.0     # Volts (-100 kV)
    VL = 100.0         # Volts (+100 V Lander)
    delta_V0 = V0 - VL # -100,100 V
    R_nom = 1.0e9      # Ohms (1.0 Gigaohm)
    
    # Time constants
    tau = R_nom * C    # 0.200 seconds
    t_end = 3.0        # seconds (well within 30 s limit)
    num_pts = 3001     # 1 ms resolution
    
    t = np.linspace(0, t_end, num_pts)
    
    # Analytical expressions for overdamped RC network
    # Potential of the suit relative to lunar lander:
    V_suit = VL + (V0 - VL) * np.exp(-t / tau)
    # Voltage difference across the dissipation network:
    delta_V = V_suit - VL # Volts
    # Discharge current (from lander to suit):
    # Conventional positive current flowing to neutralize negative charge
    I_current = np.abs(delta_V) / R_nom # Amperes
    I_current_mA = I_current * 1e3     # milliAmperes
    # Power dissipated in resistor network:
    P_watt = (I_current ** 2) * R_nom  # Watts
    # Cumulative energy dissipated:
    E_total_nominal = 0.5 * C * (delta_V0 ** 2) # Joules (~1.002 J)
    E_dissipated = E_total_nominal * (1.0 - np.exp(-2 * t / tau)) # Joules
    
    # Create DataFrame
    df = pd.DataFrame({
        'Time_s': np.round(t, 4),
        'Suit_Potential_kV': np.round(V_suit / 1e3, 4),
        'Potential_Diff_kV': np.round(np.abs(delta_V) / 1e3, 4),
        'Discharge_Current_mA': np.round(I_current_mA, 6),
        'Instantaneous_Power_W': np.round(P_watt, 4),
        'Energy_Dissipated_J': np.round(E_dissipated, 6),
        'Residual_Voltage_V': np.round(np.abs(delta_V), 4)
    })
    
    # Save full CSV data deliverable
    csv_path = "/home/afsal/lunar-grounding-challenge/deliverables/Deliverable_5B_Electrical_Discharge_Data.csv"
    df.to_csv(csv_path, index=False)
    print(f"Saved dataset with {len(df)} rows to {csv_path}")
    
    # Print key milestones
    milestones = [0.0, 0.1, 0.2, 0.4, 0.6, 1.0, 1.5, 2.0, 3.0]
    print("\n--- Key Discharge Milestones ---")
    for tm in milestones:
        row = df.iloc[(df['Time_s'] - tm).abs().argmin()]
        print(f"t = {row['Time_s']:.2f} s | V_suit = {row['Suit_Potential_kV']:.2f} kV | I = {row['Discharge_Current_mA']:.5f} mA | V_res = {row['Residual_Voltage_V']:.2f} V | E = {row['Energy_Dissipated_J']:.4f} J")
        
    return df

if __name__ == "__main__":
    run_simulation()
