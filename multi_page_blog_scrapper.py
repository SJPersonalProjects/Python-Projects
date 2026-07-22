# Multi-Page Blog Scrapper.
# Scrape article titles from multiple pages and save them.

import requests
from bs4 import BeautifulSoup

base_url = "https://blog.python.org"
current_url = base_url

all_titles = []
pages_to_scrape = 3

try:
    for page in range(pages_to_scrape):

        print(f"Scrapping page {page + 1}...")

        # Download page.
        response = requests.get(current_url)
        response.raise_for_status()

        # Parse HTML.
        soup = BeautifulSoup(response.text, "html.parser")

        # Find article titles.
        titles = soup.select("h3.post-title")

        for title in titles:
            article_title = title.get_text(strip=True)
            all_titles.append(article_title)

        # Find next page link.
        next_button = soup.find("a", text="Next")

        if next_button:
            next_url = next_button.get("href")
            current_url = next_url

        else:
            print("No more pages found.")
            break
    
    # Save titles to file.
    with open("blog_titles.txt", "w", encoding="utf-8") as file:
        for number, title in enumerate(all_titles, start=1):
            file.write(f"{number}. {title}\n")

    print("Done! Titles saved to blog_titles.txt")

except requests.exceptions.RequestException as error:
    print("Error downloading webpage:")
    print(error)