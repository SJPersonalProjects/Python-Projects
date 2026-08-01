# Image Resizer Tool.

from PIL import Image

# Get image filename
filename = input("Enter image filename: ")

# Open the image.
image = Image.open(filename)

# Get new dimensions.
width = int(input("Enter new width: "))
height = int(input("Enter new height: "))

# Resize image.
resized_image = image.resize(
    (width, height)
)

# Saved resized image.
resized_image.save("resized_image.png")

print("Image resized successfully!")
print("Saved as resized_image.png")