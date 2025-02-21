# indeed.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import time

# Configure Selenium with Headless Mode & Random User-Agent
options = Options()
options.add_argument("--headless")  # Run without opening a browser
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Use a fake User-Agent to bypass bot detection
ua = UserAgent()
options.add_argument(f"user-agent={ua.random}")

# Start WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Job URL
job_url = "https://www.indeed.com/?advn=7817571209469162&vjk=bd752a94b462cbe2"
driver.get(job_url)

try:
    # Wait for the job title to load
    wait = WebDriverWait(driver, 10)

    job_title = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1"))).text

    # Try different methods to locate Company Name
    try:
        company_name = wait.until(
            EC.presence_of_element_located((By.XPATH, '//div[@data-testid="inlineHeader-companyName"]'))
        ).text
    except:
        company_name = "Not Found"

    # Get Job Location
    try:
        location = driver.find_element(By.XPATH, '//div[@data-testid="inlineHeader-companyLocation"]').text
    except:
        location = "Not Found"

    # Get Salary (if available)
    try:
        salary = driver.find_element(By.XPATH, '//div[contains(@class, "salary-snippet")]').text
    except:
        salary = "Not Provided"

    # Get Job Description
    job_description = driver.find_element(By.XPATH, '//div[@id="jobDescriptionText"]').text

    print(f"Title: {job_title}")
    print(f"Company: {company_name}")
    print(f"Location: {location}")
    print(f"Salary: {salary}")
    print(f"Description: {job_description[:200]}...")  # Print first 200 chars

    # Save job details to a PDF
    pdf_filename = "job_details.pdf"
    pdf = canvas.Canvas(pdf_filename, pagesize=letter)
    pdf.setTitle("Indeed Job Details")

    width, height = letter
    y_position = height - 50  # Start position for text

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, y_position, "Job Details from Indeed")
    y_position -= 30

    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, y_position, f"Title: {job_title}")
    y_position -= 20
    pdf.drawString(50, y_position, f"Company: {company_name}")
    y_position -= 20
    pdf.drawString(50, y_position, f"Location: {location}")
    y_position -= 20
    pdf.drawString(50, y_position, f"Salary: {salary}")
    y_position -= 30

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, y_position, "Job Description:")
    y_position -= 20
    pdf.setFont("Helvetica", 10)

    # Split description into multiple lines
    lines = job_description.split("\n")
    for line in lines:
        if y_position < 50:
            pdf.showPage()
            pdf.setFont("Helvetica", 10)
            y_position = height - 50
        pdf.drawString(50, y_position, line)
        y_position -= 15

    pdf.save()
    print(f"Job details saved to {pdf_filename}")

except Exception as e:
    print(f"Error scraping job details: {e}")

finally:
    driver.quit()  # Close browser