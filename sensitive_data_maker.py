# Sensitive Data Maker.
# Mask phone numbers and email addresses in a text.

import re


# Ask the user to enter some text.
text = input("Enter some text: ")

# Pattern for phone numbers. (123-456-7890)
phone_pattern = r"(\d{3})-(\d{3})-(\d{4})"

# Pattern for email addresses.
email_pattern = r"([a-zA-Z])[a-zA-Z0-9._%+-]*@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"

# Function to mask phone numbers.
def mask_phone(match):
    # match.group(3) contains the last four digits.
    return "***-***-" + match.group(3)


# Funtion to mask email addresses.
def mask_email(match):
    # Keep only the first letter of the username.
    # Keep the complete domains.
    return match.group(1) + "***@" + match.group(2)


# Replace phone numbers.
text = re.sub(phone_pattern, mask_phone, text)

# Replace email addresses.
text = re.sub(email_pattern, mask_email, text)

# Disxplay the masked text.
print("\nMasked Text: ")
print(text)