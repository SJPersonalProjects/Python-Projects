# Quote Scrapper.

import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"

try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text

        print("Quote: ", text)
        print("Author: ", author)
        print("-" * 40)

except Exception as error:
    print("Error: ", error)