# Automatic Image Watermark System.

import os
from PIL import Image

# Get folder and logo paths.
input_folder = input("Enter image folder: ")
logo_path = input("Enter logo image: ")

# Open logo.
logo = Image.open(logo_path).convert("RGBA")

# Resize logo.
logo.thumbnail((120, 120))

# Craete output folder.
output_folder = os.path.join(input_folder, "Processed Images")
os.makedirs(output_folder, exist_ok=True)

# Supported image formats.
image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".webp")

# Process each image.
for filename in os.listdir(input_folder):

    if not filename.lower().endswith(image_extensions):
        continue

    
    image_path = os.path.join(input_folder, filename)

    image = Image.open(image_path).convert("RGBA")

    # Resize large images.
    if image.width > 1200 or image.height > 1200:
        image.thumbnail((1200, 1200))

    # Position logo at bottom-right
    x = image.width - logo.width - 20
    y = image.height - logo.height - 20

    # Paste logo using its transparency.
    image.paste(logo, (x, y), logo)

    # Convert JPEG images back to RGB
    if filename.lower().endswith((".jpg", ".jpeg")):
        image = image.convert("RGB")

    output_path = os.path.join(output_folder, filename)

    image.save(output_path)

    print(f"Processed: {filename}")

print("\nAll images processed successfully!")