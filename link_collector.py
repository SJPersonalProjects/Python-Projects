# Link Collector.
# Scrape a webpage and collect every hyperlink (<a> tag)

import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

try:
    # Download webpage.
    response = requests.get(url)

    # Check for errors.
    response.raise_for_status()

    # Parse HTML.
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all hyperlinks.
    links = soup.find_all("a")

    print("Collected Links:\n")

    # Display link text and URL.
    for number, link in enumerate(links, start=1):
        text = link.get_text(strip=True)
        url = link.get("href")

        print(f"{number}. Text: {text}")
        print(f"    URL: {url}")
        print()

except requests.exceptions.RequestException as error:
    print("Error downloading webpage:")
    print(error)