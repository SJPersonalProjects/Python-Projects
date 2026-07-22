# Image Downloader.

import os
import requests

from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Website to scrape
URL = "https://python.org"

# Folder to save images.
IMAGE_FOLDER = "downloaded_images"

# Create folder if it doesn't exist.
if not os.path.exists(IMAGE_FOLDER):
    os.mkdir(IMAGE_FOLDER)

def download_image(image_url, count):
    try:
        # Download image data.
        response = requests.get(image_url, timeout=10)

        response.raise_for_status()

        # Get file extension.
        extension = image_url.split(".")[-1]

        # Create filename.
        filename = f"image_{count}.{extension}"

        filePath = os.path.join(IMAGE_FOLDER, filename)

        # Save image.
        with open(filePath, "wb") as file:
            file.write(response.content)

        print(f"Downloaded: {filename}")

    except Exception as error:
        print("Failed to download")
        print(image_url)
        print(error)


def scrape_images(url):

    try:

        # Get webpage.
        response = requests.get(url, timeout=10)

        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all images.
        images = soup.find_all("img")

        print(f"Found {len(images)} images")

        count = 1

        for image in images:
            image_source = image.get("src")

            if image_source:

                # Convert relative URL to absolute URL
                image_url = urljoin(url, image_source)

                download_image(image_url, count)

                count += 1
    
    except Exception as error:

        print(f"Website error: {error}")


# Run program.
scrape_images(URL)

print("\nFinished downloading images.")