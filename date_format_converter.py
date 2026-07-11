# Date Format Converter.
# Convert dates like MM/DD/YYYY or MM-DD-YYYY
# Into the format YYYY-MM-DD

import re

# Asks user input.
text = input("Enter a sentence: ")

# Pattern.
pattern = r"(\d{2})[/-](\d{2})[/-](\d{4})"

converted = re.sub(pattern, r"\3-\1-\2", text)

print("Converter text: ")
print(converted)