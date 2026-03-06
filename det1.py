import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# 1. DIRECTORY FIX: Moving to your simulation folder
target_folder = r"C:\Users\rayan\Desktop\simulation"

try:
    os.chdir(target_folder)
    print(f"Directory set to: {target_folder}")
except Exception as e:
    print(f"Path Error: {e}")

# 2. FILE FINDER: Looking for det1.txt (901 KB)
file_name = "det1.txt" if os.path.exists("det1.txt") else "det1"

if not os.path.exists(file_name):
    print(f"CRITICAL ERROR: Cannot find {file_name} in {target_folder}")
else:
    print(f"Analyzing Source Beam in: {file_name}")
    try:
        # 3. LOAD DATA
        df = pd.read_csv(file_name, sep=r'\s+', comment='#', header=None, on_bad_lines='skip')

        # 4. CALCULATE MOMENTUM (P = sqrt(Px^2 + Py^2 + Pz^2))
        px, py, pz = df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5]
        momentum = np.sqrt(px**2 + py**2 + pz**2)

        # 5. PLOT PRIMARY BEAM
        plt.figure(figsize=(10, 6))
        plt.hist(momentum, bins=100, color='royalblue', alpha=0.8, edgecolor='black')
        
        plt.title("Initial Pion Beam Momentum (Pre-Collision - det1)")
        plt.xlabel("Momentum (MeV/c)")
        plt.ylabel("Particle Count")
        plt.grid(True, alpha=0.2)

        # 6. EXPORT
        plt.savefig("primary_beam_det1.png", dpi=300)
        plt.show()
        print("Success! Graph saved as 'primary_beam_det1.png'")

    except Exception as e:
        print(f"Analysis failed: {e}")