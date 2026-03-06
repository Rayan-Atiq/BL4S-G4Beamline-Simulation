import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# 1. FORCE THE FOLDER PATH (Using the path from your screenshot)
folder = r"C:\Users\rayan\Desktop\simulation"
os.chdir(folder) # This moves Python to your desktop folder

# 2. FIND THE FILE (Check for det3 or det3.txt)
file_name = "det3.txt" if os.path.exists("det3.txt") else "det3"

if not os.path.exists(file_name):
    print(f"CRITICAL ERROR: Still can't find {file_name} in {folder}")
    print("Files I actually see:", os.listdir())
else:
    print(f"Success! Found {file_name}. Starting analysis...")
    try:
        # 3. LOAD DATA (on_bad_lines handles the 'Exceptions' text from your screenshot)
        df = pd.read_csv(file_name, sep=r'\s+', comment='#', header=None, on_bad_lines='skip')

        # 4. CALCULATE MOMENTUM (Using **2 for squaring - fixes your SyntaxError)
        # We use .iloc to grab columns by POSITION (3, 4, 5) to fix the KeyError
        px = df.iloc[:, 3]
        py = df.iloc[:, 4]
        pz = df.iloc[:, 5]
        pdg = df.iloc[:, 7] # Particle ID column
        
        P = np.sqrt(px**2 + py**2 + pz**2)

        # 5. FILTER FOR NEUTRONS (The green tracks in your image)
        # Neutron ID = 2112
        neutrons = P[pdg == 2112]

        # 6. PLOT AND EXPORT
        plt.figure(figsize=(10, 6))
        plt.hist(neutrons, bins=100, color='forestgreen', alpha=0.7)
        plt.yscale('log')
        plt.title(f"Physics Results: Neutron Momentum ({file_name})")
        plt.xlabel("Momentum (MeV/c)")
        plt.ylabel("Count")
        
        # Saves the graph so you can use it in your report
        output_name = "final_physics_graph.png"
        plt.savefig(output_name, dpi=300)
        print(f"COMPLETE: Graph saved as {output_name}")
        
        plt.show()

    except Exception as e:
        print(f"Analysis failed: {e}")