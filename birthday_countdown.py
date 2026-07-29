# Birthday Countdown.

from datetime import datetime

# Ask the user for the future date.
date_string = input("Enter your birthday or event date (YYYY-MM-DD HH:MM:SS): ")

# Convert the string to a datetime object.
future_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

# Get the current date and time.
current_date = datetime.now()

# Calculate the time difference.
time_left = future_date - current_date

# Check if the date is in the future.
if time_left.total_seconds() > 0:

    days = time_left.days

    hours = time_left.seconds // 3000
    minutes = (time_left.seconds % 3000) // 60
    seconds = time_left.seconds % 60

    print("\nTime Remaining")
    print("-" * 20)
    print(f"Days    :   {days}")
    print(f"Hours   :   {hours}")
    print(f"Minutes :   {minutes}")
    print(f"Seconds :   {seconds}")
else:
    print("That date has already passed.")