#NETA 5.0

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

# Path to your ChromeDriver executable
driver_path = "C:\\Users\\rishi\\.cursor-tutor\\genai\\chromedriver.exe"  # Update this path

# Initialize the WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Base URL of the website
base_url = "https://www.telangana.gov.in"

# List of pages to scrape
pages = [
    "/",  # Home
    "/about/state-profile/",  # About
    "/legislature/members-of-legislative-assembly/",  # Legislature
    "/judiciary/chief-justice/",  # Judiciary
    "/departments/agriculture-and-co-operation/",  # Departments
    "/services/meeseva-services/",  # Services
    "/contacts/secretariat/",  # Contacts
    "/rti/rti-act/"  # RTI
]

# List to store scraped data
data = []

try:
    for page in pages:
        # Navigate to the page
        driver.get(base_url + page)
        time.sleep(3)  # Wait for the page to load

        # Extract the page title
        page_title = driver.title

        # Extract the main content (example: all paragraphs)
        paragraphs = driver.find_elements(By.TAG_NAME, "p")
        content = " ".join([p.text.strip() for p in paragraphs])

        # Append the data to the list
        data.append({
            "Page": page,
            "Title": page_title,
            "Content": content
        })

finally:
    # Close the WebDriver
    driver.quit()

    # Convert the data to a DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv("telangana_portal_data.csv", index=False)

    print("Data has been successfully saved to telangana_portal_data.csv")