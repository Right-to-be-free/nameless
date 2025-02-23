import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import csv

def setup_driver():
    options = uc.ChromeOptions()
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-blink-features=AutomationControlled')
    
    driver = uc.Chrome(options=options)
    return driver

def wait_for_page_load(driver):
    """Wait for the page to be fully loaded"""
    time.sleep(5)  # Initial wait
    try:
        WebDriverWait(driver, 20).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete'
        )
    except:
        print("Page load wait timeout")

def scrape_naukri_jobs():
    driver = None
    try:
        print("Setting up browser...")
        driver = setup_driver()
        wait = WebDriverWait(driver, 20)  # Increased timeout
        
        print("Opening Naukri.com...")
        driver.get("https://www.naukri.com/ml-engineer-jobs-in-hyderabad")
        wait_for_page_load(driver)
        
        # Handle popup if it exists
        try:
            popup_close = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "crossIcon")))
            popup_close.click()
            print("Closed popup")
        except:
            print("No popup found or unable to close")
        
        job_data = []
        page_count = 0
        max_pages = 5
        
        print("Starting to scrape job listings...")
        while page_count < max_pages:
            try:
                # Wait for job cards to load
                print(f"Scanning page {page_count + 1}...")
                wait_for_page_load(driver)
                
                # Scroll down gradually to load all content
                for i in range(5):  # Increased scroll iterations
                    driver.execute_script(f"window.scrollTo(0, {i * 500});")  # Scroll in smaller increments
                    time.sleep(1)
                
                # Try different selectors for job cards
                selectors = [
                    "article.jobTuple",
                    "div.job-card",  # Alternative selector
                    "div[data-job-id]"  # Another alternative
                ]
                
                job_cards = None
                for selector in selectors:
                    try:
                        job_cards = wait.until(EC.presence_of_all_elements_located(
                            (By.CSS_SELECTOR, selector)))
                        if job_cards:
                            print(f"Found job cards using selector: {selector}")
                            break
                    except:
                        continue
                
                if not job_cards:
                    print("Could not find job cards with any selector")
                    # Save page source for debugging
                    with open(f'page_source_{page_count + 1}.html', 'w', encoding='utf-8') as f:
                        f.write(driver.page_source)
                    break
                
                print(f"Found {len(job_cards)} jobs on page {page_count + 1}")
                
                for card in job_cards:
                    try:
                        # Extract job details with multiple selector attempts
                        title = card.find_element(By.CSS_SELECTOR, "a.title, .job-title, h2").text.strip()
                        company = card.find_element(By.CSS_SELECTOR, "a.subTitle, .company-name, .company").text.strip()
                        location = card.find_element(By.CSS_SELECTOR, "li[class*='location'], .location").text.strip()
                        
                        try:
                            description = card.find_element(By.CSS_SELECTOR, "div.job-description, .description").text.strip()
                        except:
                            description = "Description not available"
                        
                        job_data.append({
                            "Title": title,
                            "Company": company,
                            "Location": location,
                            "Description": description
                        })
                        print(f"Scraped: {title} at {company}")
                        
                    except NoSuchElementException as e:
                        print(f"Error scraping a job card: {str(e)}")
                        continue
                
                # Try to go to next page
                try:
                    next_button = wait.until(EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, "a.fright[title='Next'], .next-page, button.next")))
                    driver.execute_script("arguments[0].click();", next_button)
                    page_count += 1
                    time.sleep(3)
                except:
                    print("No more pages available or couldn't click next")
                    break
                
            except TimeoutException as e:
                print(f"Timeout on page {page_count + 1}: {str(e)}")
                # Save page source for debugging
                with open(f'timeout_page_source_{page_count + 1}.html', 'w', encoding='utf-8') as f:
                    f.write(driver.page_source)
                break
                
        # Save results to CSV
        if job_data:
            try:
                filename = f'naukri_ml_jobs_{time.strftime("%Y%m%d_%H%M%S")}.csv'
                with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                    fieldnames = ['Title', 'Company', 'Location', 'Description']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(job_data)
                print(f"Successfully saved {len(job_data)} jobs to {filename}")
            except Exception as e:
                print(f"Error saving to CSV: {str(e)}")
        else:
            print("No job data collected")
            
    except Exception as e:
        print(f"Critical error: {str(e)}")
        
    finally:
        if driver:
            try:
                driver.quit()
                print("Browser closed successfully")
            except Exception as e:
                print(f"Error closing browser: {str(e)}")

if __name__ == "__main__":
    print("Starting the scraping process...")
    scrape_naukri_jobs()