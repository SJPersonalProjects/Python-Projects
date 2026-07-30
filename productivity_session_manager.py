# Productivity Session Manager

import time
import subprocess
from datetime import datetime

# Countdown timer.
def countdown(seconds, session_name):
    while seconds > 0:
        minutes = seconds // 60
        remaining_seconds = seconds % 60

        print(
            f"\r{session_name}: "
            f"{minutes:02}:{remaining_seconds:02}",
            end=""
        )

        time.sleep(1)
        seconds -= 1
    
    print(f"\n{session_name} finished!")


# Save completed session to a log file.
def log_session(session_type):
    with open("session_log.txt", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{session_type} completed {timestamp}\n")


# Launch Calculator
def launch_program():
    choice = input("\nOpen Calculator? (y/n): ").lower()

    if choice == 'y':
        subprocess.Popen(["gnome-calculator"])


# Main program.
work_minutes = int(input("Work duration (minutes): "))
break_minutes = int(input("Break duration (minutes): "))

print("\nStarting work session...")
countdown(work_minutes * 60, "Work Session")
log_session("Work Session")
launch_program

print("\nStarting break...")
countdown(break_minutes * 60, "Break Session")
log_session("Break Session")
launch_program()
print("\nProductivity session completed!")