# Basic Drawing Generator.

from PIL import Image, ImageDraw

# Create a blank image.
image = Image.new("RGB", (800, 600), "white")

# Create a drawing object.
draw = ImageDraw.Draw(image)

# Draw a line.
draw.line((50, 50, 300, 50), fill="black", width=3)

# Draw a rectangle.
draw.rectangle((50, 100, 250, 250), outline="blue", width=3)

# Draw a filled rectangle
draw.rectangle((300, 100, 500, 250), fill="yellow", outline="black")

# Draw a circle.
draw.ellipse((50, 300, 250, 500), outline="red", width=3)

# Draw a filled circle.
draw.ellipse((300, 300, 500, 500), fill="green", outline="black")

# Draw a polygon (triangle)
draw.polygon(
    [(600, 100), (700, 250), (500, 250)],
    fill="orange",
    outline="black"
)

# Save image.
image.save("drawing.png")

print("Drawing saved as drawing.png")