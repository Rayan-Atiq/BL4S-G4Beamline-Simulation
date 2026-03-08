incident_particles = 0

with open("det1.txt", "r") as file:
    for line in file:
        if line.startswith("#"):
            continue
        
        data = line.split()
        parent_id = int(data[10])
        
        if parent_id == 0:
            incident_particles += 1

print("Total number of incident particles:", incident_particles)