# Word splitter.

sentence = input("Enter sentence: ")

words = sentence.split()

counter = 0

# Loop to count the words.
for word in words:
    counter += 1

print(f"Total words: {counter}")