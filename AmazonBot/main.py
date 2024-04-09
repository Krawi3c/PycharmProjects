from bs4 import BeautifulSoup
import requests
from email_management import EmailManagement

product_endpoint = "https://www.amazon.com/Instant-Pot-Electric-Sterilizer-Stainless/dp/B09MZTP44L/ref=sr_1_5?crid" \
                   "=5LYVWCT1ISMD&keywords=duo+evo+plus&qid=1678050781&sr=8-5"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 "
                  "Safari/537.36 OPR/95.0.0.0",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
}
response = requests.get(product_endpoint, headers=HEADERS)
amazon_page = response.text

soup = BeautifulSoup(amazon_page, "lxml")
print(soup)
price = "".join([symbol for symbol in soup.find(class_="a-price-whole").getText() if symbol != "."])
price_fraction = soup.find(class_="a-price-fraction").getText()
title = soup.find(id="productTitle").getText()

email = EmailManagement

if int(price) <= 130:
    email.send_email(price, price_fraction, title)
