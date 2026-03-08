neutrons = 0
incident_pions = 0

with open("det2.txt", "r") as file:
    for line in file:
        if line.startswith("#"):
            continue
        
        data = line.split()
        
        pdg = int(data[7])
        parent = int(data[10])
        
        if pdg == 2112:
            neutrons += 1
        
        if (pdg == 211 or pdg == -211) and parent == 0:
            incident_pions += 1

print("Total neutrons produced:", neutrons)
print("Incident pion particles:", incident_pions)