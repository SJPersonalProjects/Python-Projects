# Digital Clock.

from datetime import datetime
import time

print("Press Ctrl+C to stop the clock.\n")

try:
    while True:
        # Get the current date and time.
        current_time = datetime.now()

        # Format the date and time.
        formatted_time = current_time.strftime("%d-%m-%Y %H:%M:%S")

        # Display the clock.
        print(formatted_time, end="\r")

        # Wait for 1 second.
        time.sleep(1)

except KeyboardInterrupt:
    print("\nClock stopped.")