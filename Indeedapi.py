import requests

API_KEY = "your_indeed_api_key"
BASE_URL = "https://api.indeed.com/v2/jobsearch"

params = {
    "q": "Data Scientist",
    "l": "New York",
    "radius": 50,
    "start": 0,
    "limit": 10,
    "userip": "1.2.3.4",  # Replace with actual IP
    "useragent": "Mozilla/5.0",
    "format": "json",
    "publisher": API_KEY  # Required API key
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    print(response.json())  # Print job listings
else:
    print(f"Error: {response.status_code}, {response.text}")
