# Image Format Converter.

from PIL import Image
import os

# Get image details.
input_file = input("Enter image filename: ")
output_file = input("Enter new filename with extension: ")

try:
    # Open image.
    image = Image.open(input_file)

    # Save with new format.
    image.save(output_file)

    print("Image converted successfully!")
    print("Saved as:", output_file)

except FileNotFoundError:
    print("Image file not found.")
except Exception as error:
    print("Error: ", error)