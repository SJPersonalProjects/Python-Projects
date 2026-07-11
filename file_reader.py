# File Reader.
# Read the contents of a text file and display them.

# Open the file in read mode.
file = open("welcome.txt", "r")

# Read the entire contents of the file.
content = file.read()

# Display the contents
print("File Contents:\n")
print(content)

# Close the file.
file.close()