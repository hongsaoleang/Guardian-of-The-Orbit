
battery_level = 18.2
time_remaining = 24.5
dist_to_goal = 1.1

if time_remaining < 30:
    print("[CRITICAL] Low time remaining -> Abort to Goal Checkpoint")
elif battery_level < 20.0:
    print("[WARNING] Low Battery -> Transition to conservation velocity")
else:
    print("[NOMINAL] Proceed to next inspection checkpoint.")
