# Web Page Downloader

import requests

print("Web Page Downloader")
print("-" * 30)

url = input("Enter a webpage URL to download: ")

try:
    # Download Webpage.
    response = requests.get(url)

    # Check for errors.
    response.raise_for_status()

    # Save HTML content.
    with open("downloaded_page.html", "w", encoding="utf-8") as file:
        file.write(response.text)

    print("Webpage downloaded successfully.")

except requests.exceptions.RequestException as error:
    print("Error downloading webpage:")
    print(error)