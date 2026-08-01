# Simple Image Cropper.

from PIL import Image

# Get image filename.
filename = input("Enter image filename: ")

# Open image.
image = Image.open(filename)

print("Image size:")
print("Width:", image.width)
print("Height:", image.height)

# Get crop coordinates.
left = int(input("Left coordinate: "))
top = int(input("Top coordinate: "))
right = int(input("Right coordinate: "))
bottom = int(input("Bottom coordinate: "))

# Crop image.
cropped_image = image.crop(
    (left, top, right, bottom)
)

# Save cropped image.
cropped_image.save("cropped_image.png")

print("Image cropped successfully!")
print("Saved as cropped_image.png")