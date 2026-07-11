# Vowels and Consonants Matcher.
# Find and count all the vowels and consonants in a sentence.

import re

# Asks for a sentence.
sentence = input("Enter a sentence: ")

# Regex pattern for vowels both uppercase and lowercase.
vowels_pattern = r"[aeiouAEIOU]"

# Regex pattern for consonants both lowercase and uppercase.
consonants_pattern = r"[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]"

# Find all vowels and consonants.
vowels = re.findall(vowels_pattern, sentence)
consonants = re.findall(consonants_pattern, sentence)

print("Vowels: ", vowels)
print("Number of vowels: ", len(vowels))

print("Consonants: ", consonants)
print("Number of consonants: ", len(consonants))