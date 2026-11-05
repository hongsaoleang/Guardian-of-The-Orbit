import random

battery = 100.0
ran = 0

for b in range(1,11):
    battery -= random.uniform(1.5, 3.5)
    if battery < 80:
        print("[CUATION] Battery level is 80.0%") 
    elif battery < 70:
        print("EMEGENCY RETURN TRIGGERED")
    else:print("SAFE!")