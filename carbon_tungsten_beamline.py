import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# 1. THE FILE FINDER: This checks every possible way the file could be named
possible_names = ["det3", "det3.txt", "DET3", "DET3.txt"]
file_to_open = None

for name in possible_names:
    if os.path.exists(name):
        file_to_open = name
        break

if file_to_open is None:
    print("CRITICAL ERROR: Python still cannot see the file.")
    print("I see these files in your folder:", os.listdir())
else:
    print(f"Success! Opening: {file_to_open}")
    try:
        # 2. LOAD DATA: 'on_bad_lines' fixes the ParserError from your screenshot
        df = pd.read_csv(file_to_open, sep=r'\s+', comment='#', header=None, on_bad_lines='skip')

        # 3. CALCULATE MOMENTUM: Using **2 (Fixes your SyntaxError)
        # Using .iloc handles the KeyError by using column position (3, 4, 5)
        px = df.iloc[:, 3]
        py = df.iloc[:, 4]
        pz = df.iloc[:, 5]
        pdg = df.iloc[:, 7]
        
        P = np.sqrt(px**2 + py**2 + pz**2)

        # 4. FILTER FOR NEUTRONS (The green cloud in your viewer)
        # Neutron PDG ID = 2112
        neutrons_P = P[pdg == 2112]

        # 5. CREATE AND EXPORT THE GRAPH
        plt.figure(figsize=(10, 6))
        plt.hist(neutrons_P, bins=60, color='forestgreen', alpha=0.7, edgecolor='black')
        plt.yscale('log')
        plt.title(f"Neutron Momentum Distribution from {file_to_open}")
        plt.xlabel("Momentum (MeV/c)")
        plt.ylabel("Count (Log Scale)")
        plt.grid(True, alpha=0.2)

        # Saves the image for your report
        plt.savefig("final_physics_report_graph.png", dpi=300)
        print("Success! Graph saved as 'final_physics_report_graph.png'")
        
        plt.show()

    except Exception as e:
        print(f"Analysis failed: {e}")