from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Set up WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Base URL
base_url = "https://www.indeed.com/jobs?q=data+scientist&l=remote"

# Storage for scraped data
job_listings = []

# Loop through the first 10 pages
for page in range(0, 10):
    url = f"{base_url}&start={page * 10}"  # Adjust for pagination
    driver.get(url)
    time.sleep(3)  # Wait for page to load
    
    # Find all job elements
    jobs = driver.find_elements(By.CLASS_NAME, "job_seen_beacon")
    
    for job in jobs:
        try:
            title = job.find_element(By.CLASS_NAME, "jobTitle").text
            company = job.find_element(By.CLASS_NAME, "companyName").text
            location = job.find_element(By.CLASS_NAME, "companyLocation").text
            job_listings.append({"Title": title, "Company": company, "Location": location})
        except:
            continue  # Skip if any error occurs

# Close the browser
driver.quit()

# Save data to CSV
df = pd.DataFrame(job_listings)
df.to_csv("indeed_jobs.pdf", index=False)
print("Scraping completed! Data saved to 'indeed_jobs.pdf'.")
