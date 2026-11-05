import math 
flight_path1 = []
flight_path2 = []
flight_path3 = []

def calculate_3d_distance(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    dz = p2[2] - p1[2]
    return math.sqrt(dx**2 + dy**2 + dz**2)

flight_path1.append([10.71, -1.90, 4.85])
flight_path2.append([11.25, -1.50, 5.00])
flight_path3.append([12.10, -0.80, 4.95])


print('Result: ')
print(calculate_3d_distance(flight_path1, flight_path2))
print(calculate_3d_distance(flight_path3, flight_path1))