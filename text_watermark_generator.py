# Text Watermark Generator.

from PIL import Image, ImageDraw

# Get image filename.
filename = input("Enter image filename: ")

# Open image.
image = Image.open(filename)

# Create a drawing object.
draw = ImageDraw.Draw(image)

# Get watermark text.
watermark = input("Enter watermark text: ")

# Position near the bottom-right corner.
x = image.width - 220
y = image.height - 40

# Draw watermark.
draw.text(
    (x, y),
    watermark,
    fill="white"
)

# Save image.
image.save("watermarked_image.png")

print("Watermaked image saved as watermarked_image.png")