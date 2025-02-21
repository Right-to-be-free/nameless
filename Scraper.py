from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the website
driver.get('https://www.indeed.com/')

# Find the main content element
main_content = driver.find_element(By.ID, 'main')

# Extract text from the main content
content_text = main_content.text

# Print the extracted text
print(content_text)

# Close the webdriver
driver.quit()
