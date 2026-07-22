# Image Downloader.

import requests

url = input("Enter image URL: ")

filename = "downloaded_image.jpg"

try:
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, "wb") as file:
        for chunk in response.iter_content(100000):
            file.write(chunk)

    print("Image downloaded successfully!")

except Exception as error:
    print("Error downloading Image: ", error)