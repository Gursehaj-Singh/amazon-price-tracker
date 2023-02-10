# Apple AirPods (3rd Generation) with Lightning Charging Case

import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.ca/Apple-AirPods-3rd-Generation-Lightning-Charging/dp/B0BDHB9Y8H/ref=sr_1_2_sspa?crid=" \
      "2BWTPNX2T3NV3&keywords=airpods&qid=1673738882&sprefix=airpod%2Caps%2C176&sr=8-2-spons&psc=1&spLa=ZW5jcnlw" \
      "dGVkUXVhbGlmaWVyPUEzUEYxQ1hFNjhYSzlUJmVuY3J5cHRlZElkPUEwNzkwMjc4QTZKQk1JRTMxRVVNJmVuY3J5cHRlZEFkSWQ9QTA2N" \
      "DkyMjkzNEhYUEsyNkxQVVNMJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/102.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,fr;q=0.8,te;q=0.7"
}

response = requests.get(URL, headers=header)  # , headers=header
page = response.text

soup = BeautifulSoup(page, "html.parser")
rough_price = soup.find(class_="a-price-whole").text
price = rough_price.split(".")[0]
final_price = f"${price}"
print(final_price)
