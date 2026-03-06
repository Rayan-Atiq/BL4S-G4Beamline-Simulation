import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# 1. FORCE THE PATH (This fixes the 'cannot see' error)
# We tell Python exactly where your 'simulation' folder is
target_folder = r"C:\Users\rayan\Desktop\simulation"

try:
    os.chdir(target_folder)
    print(f"Successfully moved to: {target_folder}")
except Exception as e:
    print(f"Error: Could not find the folder {target_folder}. Check the path.")

# 2. FIND THE FILE (Check for det2.txt or det2)
file_name = "det2.txt" if os.path.exists("det2.txt") else "det2"

if not os.path.exists(file_name):
    print(f"CRITICAL ERROR: Still can't find {file_name} in {target_folder}")
    print("Files actually in your simulation folder:", os.listdir())
else:
    print(f"Found it! Analyzing {file_name}...")
    try:
        # 3. LOAD DATA (1,313 KB file)
        df = pd.read_csv(file_name, sep=r'\s+', comment='#', header=None, on_bad_lines='skip')

        # 4. CALCULATE MOMENTUM (Fixes your math syntax error)
        px, py, pz = df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5]
        momentum = np.sqrt(px**2 + py**2 + pz**2)

        # 5. PLOT RESULTS FOR DET2 (Post-Carbon Target)
        plt.figure(figsize=(10, 6))
        plt.hist(momentum, bins=100, color='darkorange', alpha=0.7, edgecolor='black')
        plt.yscale('log')
        plt.title(f"Momentum Distribution: Post-Carbon Target ({file_name})")
        plt.xlabel("Momentum (MeV/c)")
        plt.ylabel("Count (Log Scale)")
        plt.grid(True, alpha=0.2)

        # 6. EXPORT
        plt.savefig("carbon_target_results_det2.png", dpi=300)
        plt.show()
        print("Success! Graph saved as 'carbon_target_results_det2.png'")

    except Exception as e:
        print(f"Analysis failed: {e}")