
import random

battery = 100.0

for waypoint in range(1, 11):
    print(f"Approaching waypoint {waypoint}...")
    
    drain = random.uniform(1.5, 3.5)
    battery -= drain
    print(f"Current Battery: {battery:.2f}%")
    
    if battery < 75.0:
        print("[EMERGENCY RETURN TRIGGERED]")
        break
    elif battery < 80.0:
        print("Caution: Battery has dropped below 80%!")