import time
from datetime import datetime

alarm_time = input("Set alarm (HH:MM:SS): ")

print(f"Alarm set for {alarm_time}")

while True:
    current_time = datetime.now().strftime("%H:%M:%S")

    if current_time == alarm_time:
        print("\n⏰ ALARM! Wake up!")

        # Ring 10 times
        for _ in range(10):
            print("\a")
            time.sleep(1)

        break

    time.sleep(1)