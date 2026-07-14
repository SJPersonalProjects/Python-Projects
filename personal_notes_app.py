# Perosnal Notes App
# Continuously add notes to a file using append mode.

print("=== Personal Notes App ===")
print("Type 'exit' to stop adding notes.\n")

# Open the fiile in append mode.
# If the file doesn't exist. Python will create it.
file = open("notes.txt", "a")

while True:
    # Ask the user to enter a note.
    note = input("Enter a note: ")

    # Stop the program if the user types 'exit'
    if note.lower() == 'exit':
        break

    # Write the note to the file on a new line.
    file.write(note + "\n")


file.close()

print("\nYour notes have been saved successfully.")