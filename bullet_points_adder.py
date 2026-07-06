# Bullet Points Adder.

text = """Apples
Bananas
Oranges
Mangoes"""

lines = text.split("\n")

for line in lines:
    print("* " + line)