import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import csv

def setup_driver():
    options = uc.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-blink-features=AutomationControlled')
    return uc.Chrome(options=options)

def wait_for_user(message="Press Enter after completing the action..."):
    input(message)

def scrape_indeed_jobs():
    driver = None
    try:
        print("Starting browser...")
        driver = setup_driver()
        wait = WebDriverWait(driver, 20)
        
        # Go to Indeed
        print("Opening Indeed.com...")
        driver.get("https://www.indeed.com")
        time.sleep(5)
        
        # Wait for user to handle any verification
        print("Please complete any verification if present.")
        wait_for_user()
        
        # Find and fill search fields
        print("Entering search criteria...")
        what_field = wait.until(EC.presence_of_element_located((By.ID, "text-input-what")))
        where_field = wait.until(EC.presence_of_element_located((By.ID, "text-input-where")))
        
        what_field.send_keys("ML Engineer")
        where_field.clear()
        where_field.send_keys("Hyderabad")
        where_field.send_keys(Keys.RETURN)
        
        time.sleep(5)
        print("Search completed. Please verify results are visible.")
        wait_for_user()
        
        jobs_data = []
        pages = 0
        max_pages = 5
        
        while pages < max_pages:
            print(f"\nScraping page {pages + 1}")
            
            # Wait for job cards to load
            job_cards = wait.until(EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "job_seen_beacon")))
            
            print(f"Found {len(job_cards)} jobs on this page")
            
            # Process each job card
            for card in job_cards:
                try:
                    title = card.find_element(By.CLASS_NAME, "jobTitle").text
                    company = card.find_element(By.CLASS_NAME, "companyName").text
                    location = card.find_element(By.CLASS_NAME, "companyLocation").text
                    
                    jobs_data.append({
                        "Title": title,
                        "Company": company,
                        "Location": location
                    })
                    print(f"Scraped: {title} at {company}")
                    
                except Exception as e:
                    print(f"Error scraping a job: {str(e)}")
                    continue
            
            # Try to go to next page
            try:
                next_button = driver.find_element(By.CSS_SELECTOR, '[aria-label="Next Page"]')
                if not next_button.is_enabled():
                    print("Reached last page")
                    break
                    
                next_button.click()
                pages += 1
                time.sleep(5)
                print("Moving to next page...")
                wait_for_user("Press Enter after page loads...")
                
            except Exception as e:
                print("No more pages available")
                break
        
        # Save the results
        if jobs_data:
            filename = f'indeed_jobs_{time.strftime("%Y%m%d_%H%M%S")}.csv'
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=["Title", "Company", "Location"])
                writer.writeheader()
                writer.writerows(jobs_data)
            print(f"\nSaved {len(jobs_data)} jobs to {filename}")
        else:
            print("\nNo jobs were collected")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
    finally:
        if driver:
            driver.quit()
            print("Browser closed")

if __name__ == "__main__":
    print("Starting Indeed job scraper...")
    scrape_indeed_jobs()
