"""
A basic Python script that scrapes data from a website.

PIP INSTALLATIONS:
pip install requests
pip install beautifulsoup4
pip install validators

"""

# Import necessary modules
import requests
from bs4 import BeautifulSoup
import validators

def scrape_quotes(url):
    """
    Scrapes quotes, authors, and tags from the given URL.
    """
    try:
        # Send a GET request to the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all quotes on the page
        quotes = soup.find_all("div", class_="quote")

        # Extract and print each quote
        for quote in quotes:
            text = quote.find("span", class_="text").get_text()
            author = quote.find("small", class_="author").get_text()
            tags = [tag.get_text() for tag in quote.find_all("a", class_="tag")]

            print(f"Quote: {text}")
            print(f"Author: {author}")
            print(f'Tags: {", ".join(tags)}')
            print("-" * 40)
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

def is_valid_url(url):
    """
    Validates the URL format.
    """
    return validators.url(url)
