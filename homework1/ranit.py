import random

battery = 100.0

def battery_status(level):
    if level < 75:
        return "EMERGENCY RETURN"
    elif level < 80:
        return "CAUTION: LOW BATTERY"
    return "SAFE"
waypoint = 1

while waypoint <= 10:
    loss = random.uniform(1.5, 3.5)
    battery -= loss
    print(f"Waypoint {waypoint}: Battery = {battery:.2f}%")
    status = battery_status(battery)
    print(status)
    if status == "EMERGENCY RETURN":
        break
    waypoint += 1
