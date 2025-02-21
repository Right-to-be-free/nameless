from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import time


# Set up Chrome WebDriver with User-Agent to bypass bot detection
options = Options()
options.add_argument("--headless")  
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Base URL for Indeed job search
base_url = "https://www.indeed.com/jobs?q=data+scientist&l=remote"

# Storage for scraped job listings
job_listings = []

# Loop through 10 pages
for page in range(0, 10):
    url = f"{base_url}&start={page * 10}"
    driver.get(url)
    time.sleep(3)  # Allow JavaScript to load

    # Scroll to load dynamic content
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    try:
        # Wait for job postings to be visible
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "job_seen_beacon")]'))
        )

        # Find all job elements
        jobs = driver.find_elements(By.XPATH, '//div[contains(@class, "job_seen_beacon")]')

        for job in jobs:
            try:
                title = job.find_element(By.XPATH, './/h2//span').text
                company = job.find_element(By.XPATH, './/span[@class="companyName"]').text
                location = job.find_element(By.XPATH, './/div[@class="companyLocation"]').text
                job_listings.append({"Title": title, "Company": company, "Location": location})
            except Exception as e:
                print(f"Skipping job due to error: {e}")
                continue

    except Exception as e:
        print(f"Error loading page {page + 1}: {e}")

# Close browser after scraping
driver.quit()

# Ensure job_listings is not empty before saving
if not job_listings:
    print("No job listings found. Exiting without creating a PDF.")
else:
    # Create a PDF file
    pdf_filename = "indeed_jobs.pdf"
    pdf = canvas.Canvas(pdf_filename, pagesize=letter)
    pdf.setTitle("Indeed Job Listings")

    # PDF Page Setup
    width, height = letter
    y_position = height - 50  # Start position for text

    pdf.setFont("Helvetica", 10)  # Set font size

    for job in job_listings:
        line = f"{job['Title']} - {job['Company']} ({job['Location']})"

        if y_position < 50:  # Move to new page if space runs out
            pdf.showPage()
            pdf.setFont("Helvetica", 10)
            y_position = height - 50  

        pdf.drawString(50, y_position, line)
        y_position -= 20  # Move text down

    pdf.save()
    print(f"Scraping completed! {len(job_listings)} job listings saved to '{pdf_filename}'.")
