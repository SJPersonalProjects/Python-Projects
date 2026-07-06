# Palindrome Checker

text = input("Enter text: ")

text = text.lower()

reversed_text = ""

for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]

if text == reversed_text:
    print("It's a palindrome")
else:
    print("it's not a palindrome")