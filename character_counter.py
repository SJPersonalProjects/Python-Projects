# Character counter.

text = input("Enter a string: ")

character_count = {}

for character in text:
    if character in character_count:
        character_count[character] += 1
    else:
        character_count[character] = 1


print("\nCharacter Count:")

for character in character_count:
    print(f"{character}: {character_count[character]}")