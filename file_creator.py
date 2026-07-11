# File Creator.
# Create a new text file and write a welcome message.

file = open("welcome.txt", "w")

file.write("Welcome to Python File Handling!\n")
file.write("This is my first file created using Python.\n")
file.write("Happy Learning!")

file.close()

print("The file 'welcome.txt' is successfully created.")