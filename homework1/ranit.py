import math

# Coordinates
kibo_pos = [10.71, -1.90, 4.85]

print("Kibo Position:", kibo_pos)
# Waypoints
flight_path = []
flight_path.append([10.71, -1.90, 4.85])
flight_path.append([11.25, -1.50, 5.00])
flight_path.append([12.10, -0.80, 4.95])
print("Flight Path:", flight_path)
print("Total Waypoints:", len(flight_path))

# Calculate 3D Distance
def calculate_3d_distance(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    dz = p2[2] - p1[2]
    distance = math.sqrt(dx**2 + dy**2 + dz**2)
    return distance

# Test Distance
p1 = flight_path[0]
p2 = flight_path[1]
p3 = flight_path[2]
print("Distance 1:", calculate_3d_distance(p1, p2))
print("Distance 2:", calculate_3d_distance(p3, p1))
