# Program Execution Timer.

import time

print("Type some text and press Enter.")

# Record the start time.
start_time = time.time()

# Wait for the user input.
text = input("Enter text: ")

# Record the end time.
end_time = time.time()

# Calculate the elapsed time.
elapsed_time = end_time - start_time

# Display results.
print("\nYou entered:")
print(text)

print(f"Time taken: {round(elapsed_time, 2)} seconds")