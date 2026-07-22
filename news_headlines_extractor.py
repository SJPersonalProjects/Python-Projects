# News Headlines Extractor.
# Fetch a news website and extracts headlines using Beautiful Soup

import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://news.ycombinator.com/"

try:
    # Downloads webpage.
    response = requests.get(url)

    # Checks for errors.
    response.raise_for_status()

    # Parse HTML.
    soup = BeautifulSoup(response.text, "html.parser")

    # Find headlines using CSS selector.
    headlines = soup.select(".titleline a")

    print("Latest Headlines:\n")

    # Display headlines.
    for number, headline in enumerate(headlines, start=1):
        print(f"{number}. {headline.get_text()}")

except requests.exceptions.RequestException as error:
    print("Error downloading webpage")
    print(error)



