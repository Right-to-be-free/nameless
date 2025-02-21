#beautifulsoup

from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("https://quotes.toscrape.com/")

soup = BeautifulSoup(page_to_scrape.text, "html.parser")

quotes = soup.find_all('div', class_='quote')

for quote in quotes:
    text = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()
    print(f"Quote: {text}\nAuthor: {author}\n")



