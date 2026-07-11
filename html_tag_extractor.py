# HTML Tag Extractor
# Extract all HTML tags using greedy and non-greedy matching.

import re

# Asks for html code as input.
html = input("Enter HTML: ")

# Greedy pattern.
# .* tries to match as much text as possible.
greedy_pattern = r"<.*>"

# Non-greedy pattern.
# .*? matches as little text as possible.
non_greedy_pattern = r"<.*?>"

# Find matches.
greedy_matches = re.findall(greedy_pattern, html)
non_greedy_matches = re.findall(non_greedy_pattern, html)

print("Greedy Match: ")
print(greedy_matches)

print("\nNon-Greedy Matches: ")
print(non_greedy_matches)