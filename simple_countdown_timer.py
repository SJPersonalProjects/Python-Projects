# Simple Countdown Timer.

import time

# Ask the user for the countdown time.
seconds = int(input("Enter the number of seconds: "))

# Countdown.
for remaining in range(seconds, 0, -1):
    print(f"Time Remaining: {remaining} seconds")
    time.sleep(1)

print("Time's Up!")