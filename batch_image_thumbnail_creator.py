# Batch Image Thumbnail Creator.

from PIL import Image
import os

# Get folder path.
folder = input("Enter folder path: ")

# Create output folder.
thumbnail_folder = os.path.join(folder, "Thumbnails")
os.makedirs(thumbnail_folder, exist_ok=True)

# Supported image formats.
image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp")

# Process images.
for filename in os.listdir(folder):

    if filename.lower().endswith(image_extensions):
        image_path = os.path.join(folder, filename)

        image = Image.open(image_path)

        # Resize while keeping proportions.
        image.thumbnail((200, 200))

        output_path = os.path.join(
            thumbnail_folder,
            filename
        )

        image.save(output_path)

        print(f"Thumbnail created: {filename}")

print("\nAll thumbnails created successfully!")