neutrons = 0

with open("det3.txt", "r") as file:
    for line in file:
        if line.startswith("#"):
            continue
        
        data = line.split()
        pdg = int(data[7])
        
        if pdg == 2112:
            neutrons += 1

print("Number of produced neutrons:", neutrons)