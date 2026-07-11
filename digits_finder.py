# Digit Finder.
# Find the first number in a sentence using regular expression.

import re

# Asks user input.
sentence = input("Enter a sentence: ")


# Search any digit 0 - 9 and one or more digits.
match = re.search("\d+", sentence)


# Checks if a number was found.
if match:
    print("First number found: ", match.group())
else:
    print("No number found in the sentence.")
