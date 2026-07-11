# Line Counter.
# Read a text file and count the total number of lines.

# Opens the file in read mode.
file = open("welcome.txt", "r")

# Read all the lines from a file into a list.
lines = file.readlines()

# Count the number of lines.
lines_count = len(lines)

print("Total number of lines: ", lines_count)

# Closes a file.
file.close()