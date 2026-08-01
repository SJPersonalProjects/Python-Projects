# Image Rotation and Flip Tool.

from PIL import Image

# Get image filename.
filename = input("Enter image filename: ")

# Open image.
image = Image.open(filename)

# Display menu.
print("\nImage Editing Menu")
print("1. Rotate 90°")
print("2. Rotate 180°")
print("3. Rotate 270°")
print("4. Flip Horizontally")
print("5. Flip Vertically")

choice = input("Choose an option: ")

# Perform operation.
if choice == "1":
    edited_image = image.rotate(90, expand=True)

elif choice == "2":
    edited_image = image.rotate(180, expand=True)

elif choice == "3":
    edited_image = image.rotate(270, expand=True)

elif choice == "4":
    edited_image = image.transpose(Image.FLIP_LEFT_RIGHT)

elif choice == "5":
    edited_image = image.transpose(Image.FLIP_TOP_BOTTOM)

else:
    print("Invalid choice.")
    exit()

# Save edited image.
edited_image.save("edited_image.png")

print("Image saved as edited_image.png")