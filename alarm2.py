import time
from datetime import datetime
import os  # Use os.system for cross-platform sound

alarm_time = input("Set alarm (HH:MM:SS): ")

print(f"Alarm set for {alarm_time}")

while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    print(current_time, end="\r")

    if current_time == alarm_time:
        print("\nWake up! Alarm ringing...")
        # Cross-platform beep (works on Linux/macOS)
        os.system('echo -e "\a"')
        break

    time.sleep(1)