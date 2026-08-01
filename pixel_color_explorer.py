# Pixel Color Explorer.

from PIL import Image

# Get image filename.
filename = input("Enter image filename: ")

# Open image.
image = Image.open(filename)

print(f"Image size: {image.width} x {image.height}")

# Get pixel coordinates.
x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

# Get pixel color.
color = image.getpixel((x, y))

# Display results.
print(f"\nPixel at ({x}, {y})")
print("Color: ", color)