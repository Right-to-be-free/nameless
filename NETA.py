import requests
from bs4 import BeautifulSoup
import csv
import datetime

# URL of the website
url = "https://www.telangana.gov.in/government/chief-minister"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the Chief Minister's name
    name = soup.find('h2', id='NameorTittle').text.strip()
    
    # Extract the Chief Minister's designation
    designation = soup.find('h3', id='Designation').text.strip()
    
    # Extract the Chief Minister's details from the table
    details = {}
    table = soup.find('table', id='footable_28890')
    rows = table.find_all('tr')
    
    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 2:
            key = cells[0].text.strip()
            value = cells[1].text.strip()
            details[key] = value
    
    # Print the extracted data
    print(f"Name: {name}")
    print(f"Designation: {designation}")
    for key, value in details.items():
        print(f"{key}: {value}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    # Save data to CSV
    

   
      