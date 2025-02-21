from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Configure Selenium (Headless Mode)
options = Options()
options.add_argument("--headless")  # No browser UI
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Start WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# URL of WuxiaWorld
url = "https://www.wuxiaworld.com/"
driver.get(url)

time.sleep(3)  # Allow the page to load

# Scraping Novel Details
novels = []
try:
    # Wait until the novel list loads
    wait = WebDriverWait(driver, 10)
    novel_elements = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, '//div[@class="novel-list-item"]'))
    )

    for novel in novel_elements:
        title = novel.find_element(By.XPATH, './/h4').text
        novel_url = novel.find_element(By.XPATH, './/a').get_attribute("href")
        try:
            description = novel.find_element(By.XPATH, './/p').text
        except:
            description = "No description available."

        novels.append({"Title": title, "Description": description, "URL": novel_url})

        print(f"Title: {title}")
        print(f"URL: {novel_url}")
        print(f"Description: {description[:100]}...\n")

except Exception as e:
    print(f"Error scraping WuxiaWorld: {e}")

finally:
    driver.quit()

# Save to CSV
df = pd.DataFrame(novels)
df.to_csv("wuxiaworld_novels.pdf", index=False)
print("Data saved to wuxiaworld_novels.pdf")
