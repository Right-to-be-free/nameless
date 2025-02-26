from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open YouTube video
url = "https://www.youtube.com/watch?v=KTKVWnp0BW0"
driver.get(url)

# Scroll to load comments
time.sleep(5)  # Wait for page to load

# Scroll multiple times to load more comments
for _ in range(15):  # Increase for more comments
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(3)

# Extract comments
comments = driver.find_elements(By.XPATH, '//*[@id="content-text"]')

# Store comments in a list
data = []
for i, comment in enumerate(comments):
    data.append([i + 1, comment.text])

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Comment Number", "Comment Text"])

# Save to Excel
df.to_excel("youtube_comments.xlsx", index=False)

# Close browser
driver.quit()

print("Comments saved to youtube_comments.xlsx")
