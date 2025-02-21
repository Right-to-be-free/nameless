import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Scraping setup
base_url = "https://quotes.toscrape.com"
all_quotes = []
page_url = "/page/1/"  # Start with the first page

while page_url:
    response = requests.get(base_url + page_url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all('div', class_='quote')

    for quote in quotes:
        text = quote.find('span', class_='text').get_text(strip=True)
        author = quote.find('small', class_='author').get_text(strip=True)
        all_quotes.append(f'"{text}" - {author}')

    next_button = soup.find('li', class_='next')
    page_url = next_button.find('a')['href'] if next_button else None

# Creating a PDF
pdf_filename = "quotes.pdf"
pdf = canvas.Canvas(pdf_filename, pagesize=letter)
pdf.setTitle("Scraped Quotes")

# PDF Styling
width, height = letter
y_position = height - 40  # Start position for text

for quote in all_quotes:
    if y_position < 40:  # New page if space runs out
        pdf.showPage()
        y_position = height - 40  

    pdf.drawString(40, y_position, quote)
    y_position -= 30  # Move to the next line

pdf.save()
print(f"PDF saved as {pdf_filename}")
