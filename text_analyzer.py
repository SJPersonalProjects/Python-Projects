# Text Analyzer.

text = input("Enter some text: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
symbols = 0

for character in text:
    if character.lower() in 'aeiou':
        vowels += 1
    
    elif character.isalpha():
        consonants += 1
    
    elif character.isdigit():
        digits += 1
    
    elif character.isspace():
        spaces += 1
    
    else:
        symbols += 1
    
print("Text Analyzer".center(25, "="))
print(f"Vowels : {vowels}")
print(f"Consonants : {consonants}")
print(f"Digits : {digits}")
print(f"Spaces : {spaces}")
print(f"Symbols : {symbols}")