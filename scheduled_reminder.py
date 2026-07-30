
import time
import os

# Ask the user for the reminder details.
delay = int(input("Enter the delay in seconds: "))
message = input("Enter the reminder message: ")

print(f"\nReminder set for {delay} seconds...")
time.sleep(delay)

print("\nReminder!")
print(message)

# Create a reminder file.
filename = "reminder.txt"

with open(filename, "w") as file:
    file.write(message)

print("\nReminder saved to '{filename}'.")
os.system(f'xdg-open "{filename}"')