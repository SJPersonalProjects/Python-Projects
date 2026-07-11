# All numbers extractor.
# Extract every number from a paragraph using findall().

import re

paragraph = input("Enter a paragraph: ")

pattern = r"\d+"

numbers = re.findall(pattern, paragraph)

if numbers:
    print("Numbers found: ", numbers)
else:
    print("No numbers found.")