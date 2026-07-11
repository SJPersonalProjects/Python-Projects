# Phone number finder.
# Search a paragraph and print the first phone number.
# In the format 123-456-7890.

import re

# User enters a paragraph.
paragraph = input("Enter a paragraph: ")


# 3 digits first then - then 3 digits then - then 4 digits.
pattern = r"\d{3}-\d{3}-\d{4}"

match = re.search(pattern, paragraph)

if match:
    print("Phone number found: ", match.group())
else:
    print("No phone number found.")

