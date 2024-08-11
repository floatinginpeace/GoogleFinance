import requests
from lxml import html

ticker = input("Type NASDAQ Ticker. Do not include $:")

# Construct the URL
url = f"https://www.google.com/finance/quote/{ticker}:NASDAQ?hl=en"

# Set a User-Agent to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Send a GET request to the URL
response = requests.get(url, headers=headers)

# Parse the HTML content
tree = html.fromstring(response.content)

# Use XPath to find the company name
# This XPath targets the div containing the company name
company_name = tree.xpath('//div[contains(@class, "zzDege")]')

if company_name:
    print("Company Name:", company_name[0].text_content().strip())
else:
    print("Company name not found")

# Use XPath to find the stock price
stock_price = tree.xpath('//div[contains(@class, "YMlKec fxKbKc")]')

if stock_price:
    print("Stock Price:", stock_price[0].text_content().strip())
else:
    print("Stock price not found")


