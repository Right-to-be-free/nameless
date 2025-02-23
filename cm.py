from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
from webdriver_manager.chrome import ChromeDriverManager

def get_random_delay():
    return random.uniform(2, 5)  # Random delay to avoid detection

def scrape_telangana_gov():
    url = "https://www.telangana.gov.in/government/chief-minister/"
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    time.sleep(get_random_delay())
    
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    # Extract Chief Minister’s Information
    cm_info = {}
    cm_section = soup.find("div", class_="cm-profile")
    if cm_section:
        cm_info["Name"] = cm_section.find("h2").text.strip() if cm_section.find("h2") else "N/A"
        cm_info["Designation"] = cm_section.find("h3").text.strip() if cm_section.find("h3") else "N/A"
        cm_info["Tenure"] = cm_section.find("p").text.strip() if cm_section.find("p") else "N/A"
    
    # Extract News and Announcements
    news_list = []
    news_section = soup.find("div", class_="news-list")
    if news_section:
        news_items = news_section.find_all("li")
        for news in news_items:
            title = news.text.strip()
            link = news.find("a")["href"] if news.find("a") else "N/A"
            news_list.append({"Title": title, "Link": link})
    
    # Extract Government Officials/Departments
    officials_list = []
    officials_section = soup.find("div", class_="officials-list")
    if officials_section:
        officials = officials_section.find_all("li")
        for official in officials:
            name = official.text.strip()
            officials_list.append({"Name": name})
    
    # Save results to CSV files
    if cm_info:
        pd.DataFrame([cm_info]).to_csv("chief_minister_info.csv", index=False)
    if news_list:
        pd.DataFrame(news_list).to_csv("news_announcements.csv", index=False)
    if officials_list:
        pd.DataFrame(officials_list).to_csv("government_officials.csv", index=False)
    
    print("Scraping completed and data saved successfully!")
    driver.quit()

if __name__ == "__main__":
    scrape_telangana_gov()
    # Convert CSV files to PDF
    def convert_to_pdf():
        try:
            # Read CSV files
            cm_df = pd.read_csv("chief_minister_info.csv")
            news_df = pd.read_csv("news_announcements.csv") 
            officials_df = pd.read_csv("government_officials.csv")
            
            # Create PDF filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            pdf_filename = f"telangana_gov_data_{timestamp}.pdf"
            
            # Initialize PDF document
            from fpdf import FPDF
            pdf = FPDF()
            
            # Add CM Info page
            pdf.add_page()
            pdf.set_font('Arial', 'B', 16)
            pdf.cell(0, 10, "Chief Minister Information", ln=True, align='C')
            pdf.set_font('Arial', '', 12)
            for col in cm_df.columns:
                pdf.cell(0, 10, f"{col}: {cm_df[col].iloc[0]}", ln=True)
                
            # Add News page    
            pdf.add_page()
            pdf.set_font('Arial', 'B', 16)
            pdf.cell(0, 10, "News and Announcements", ln=True, align='C')
            pdf.set_font('Arial', '', 12)
            for _, row in news_df.iterrows():
                pdf.cell(0, 10, f"Title: {row['Title']}", ln=True)
                pdf.cell(0, 10, f"Link: {row['Link']}", ln=True)
                pdf.cell(0, 5, "", ln=True)
                
            # Add Officials page
            pdf.add_page()
            pdf.set_font('Arial', 'B', 16)
            pdf.cell(0, 10, "Government Officials", ln=True, align='C')
            pdf.set_font('Arial', '', 12)
            for _, row in officials_df.iterrows():
                pdf.cell(0, 10, f"Name: {row['Name']}", ln=True)
            
            # Save PDF
            pdf.output(pdf_filename)
            print(f"📄 Data converted and saved to {pdf_filename}")
            
        except Exception as e:
            print(f"❌ Error converting to PDF: {e}")
    
    # Call the conversion function
    convert_to_pdf()
