# Converts seconds into minutes and hours.

seconds = float(input("Enter seconds: "))

minutes = seconds / 60
hours = minutes / 3600

print(f"We've {minutes} minutes and {hours} hours in {seconds} seconds.")