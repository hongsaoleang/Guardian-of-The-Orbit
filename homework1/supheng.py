import random

# Initialize battery percentage
battery = 100.0

# Loop through 10 navigation waypoints
for waypoint in range(1, 11):
    print(f"Approaching waypoint {waypoint}...")
    
    # Reduce battery by a simulated random float between 1.5 and 3.5
    drain = random.uniform(1.5, 3.5)
    battery -= drain
    print(f"Current Battery: {battery:.2f}%")
    
    # Check battery thresholds
    if battery < 75.0:
        print("[EMERGENCY RETURN TRIGGERED]")
        break
    elif battery < 80.0:
        print("Caution: Battery has dropped below 80%!")

