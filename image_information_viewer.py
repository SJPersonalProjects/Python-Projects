# Image Information Viewer.

from PIL import Image
import os

# Ask user for image path.
image_path = input("Enter image filename: ")

# Check if image exists.
if os.path.exists(image_path):

    # Open image.
    image = Image.open(image_path)

    # Display information.
    print("\nImage Information")
    print("-" * 30)

    print("Filename :", image.filename)
    print("Format   :", image.format)
    print("Width    :", image.width, " pixels")
    print("Height   :", image.height, " pixels")

    # Get file size.
    file_size = os.path.getsize(image_path)

    print("Size :", file_size, " bytes")

else:
    print("Image file not found.")