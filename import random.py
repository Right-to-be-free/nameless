import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent

# 🛠️ 1️⃣ Configure Selenium (Headless, Proxies, Random User-Agent)
options = Options()
options.add_argument("--headless")  # Run without opening a browser
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# **Use Random User-Agent to avoid detection**
ua = UserAgent()
options.add_argument(f"user-agent={ua.random}")

# **Set Up Rotating Proxies**
proxy_list = [
    "http://username:password@proxy1.com:8080",
    "http://username:password@proxy2.com:8080",
    "http://username:password@proxy3.com:8080"
]
random_proxy = random.choice(proxy_list)
options.add_argument(f"--proxy-server={random_proxy}")

# Start WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# WuxiaWorld URL
url = "https://www.wuxiaworld.com/"
driver.get(url)

# ⏳ **Wait for page to load properly**
time.sleep(random.uniform(3, 6))  # Random sleep to mimic human behavior

novels = []
try:
    # ✅ **Wait until the novel list loads**
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

        print(f"✅ Title: {title}")
        print(f"🔗 URL: {novel_url}")
        print(f"📜 Description: {description[:100]}...\n")

except Exception as e:
    print(f"❌ Error scraping WuxiaWorld: {e}")

finally:
    driver.quit()

print("✅ Scraping Completed Successfully!")
