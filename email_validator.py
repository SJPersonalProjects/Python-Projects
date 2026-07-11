# Email validator.
# Check whether the entered email address is valid using regular expression.

import re

# Ask the user to enter an email address.
email = input("Enter an email address: ")

# Regular expression pattern for a simple email validation.
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Checks if the email matches the pattern.
match = re.fullmatch(pattern, email)


if match:
    print("Valid email address")
else:
    print("Invalid email address.")