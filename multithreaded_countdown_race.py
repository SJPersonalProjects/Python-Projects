# Multithreaded Countdown Race.

import threading
import time

# Store the winner.
winner = None

# Countdown function.
def countdown(name, seconds):
    global winner

    for remaining in range(seconds, 0, -1):
        print(f"{name}: {remaining}")
        time.sleep(1)

    print(f"{name} finished!")

    # Record the first thread to finish.
    if winner is None:
        winner = name
    

# Create threads
thread1 = threading.Thread(target=countdown, args=("Timer 1", 5))
thread2 = threading.Thread(target=countdown, args=("Timer 2", 8))
thread3 = threading.Thread(target=countdown, args=("Timer 3", 3))

# Start threads
thread1.start()
thread2.start()
thread3.start()

# Wait for all the threads to finish.
thread1.join()
thread2.join()
thread3.join()

# Display the winner.
print("\nRace Finished!")
print(f"The winner is {winner}")