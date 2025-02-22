import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/AAPL"

# Add headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find the stock price (update this selector if needed)
price_element = soup.find("fin-streamer", {"data-field": "regularMarketPrice"})

# Check if the element exists
if price_element:
    print("Apple Stock Price:", price_element.text)
else:
    print("Stock price not found. Yahoo Finance may have changed the HTML structure.")
