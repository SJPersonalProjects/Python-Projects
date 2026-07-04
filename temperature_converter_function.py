# Functions converts the temperature and returns value.

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


celsius = float(input("Enter celsius: "))
print(f"{celsius_to_fahrenheit(celsius)} Fahrenheits in {celsius} Celsius")
