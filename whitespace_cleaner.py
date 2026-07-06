# Whitespace Cleaner.

text = input("Enter some text: ")

print("\nBefore:")
print(f"'{text}'")

cleaned_text = text.strip()

print("\nAfter:")
print(f"'{cleaned_text}'")