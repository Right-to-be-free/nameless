from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

# Path to your ChromeDriver executable
driver_path = "C:\\chromedriver\\chromedriver.exe"  # Update this path

# Initialize the WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# URL of the website
base_url = "https://www.telangana.gov.in/government/chief-minister"

# List to store scraped data
data = []

try:
    # Open the website
    driver.get(base_url)
    time.sleep(3)  # Wait for the page to load

    # Scrape data from the current page
    name = driver.find_element(By.ID, "NameorTittle").text.strip()
    designation = driver.find_element(By.ID, "Designation").text.strip()

    # Extract details from the table
    table = driver.find_element(By.ID, "footable_28890")
    rows = table.find_elements(By.TAG_NAME, "tr")
    details = {}
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if len(cells) == 2:
            key = cells[0].text.strip()
            value = cells[1].text.strip()
            details[key] = value

    # Append the data to the list
    data.append({
        "Name": name,
        "Designation": designation,
        **details  # Unpack the details dictionary
    })

finally:
    # Close the WebDriver
    driver.quit()

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("chief_minister_data.csv", index=False)

print("Data saved to chief_minister_data.csv")