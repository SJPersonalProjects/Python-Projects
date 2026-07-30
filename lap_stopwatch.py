# Lap Stopwatch.

import time

print("Press Enter to record a lap.")
print("Press Ctrl+C to stop the stopwatch.\n")

lap_times = []

start_time = time.time()
last_lap_time = start_time
lap_number = 1

try:
    while True:
        # Wait for the enter.
        input()

        current_time = time.time()

        total_time = current_time - start_time
        lap_time = current_time - last_lap_time

        lap_times.append(lap_time)

        print(
            f"Lap {lap_number}: "
            f"Lap Time = {lap_time:.2f} sec | "
            f"Total Time = {total_time:.2f} sec"
        )

        last_lap_time = current_time
        lap_number += 1

except KeyboardInterrupt:
    print("\n\nStopwatch stopped.")

    print("\nLap Summary")
    print("-" * 30)

    if lap_times:
        for i, lap in enumerate(lap_times, start=1):
            print(f"Lap {i}: {lap:.2f} seconds")
        
        print("-" * 30)
        print(f"Total Laps: {len(lap_times)}")
        print(f"Total Time: {sum(lap_times):.2f} seconds")

    else:
        print("No laps were recorded.")