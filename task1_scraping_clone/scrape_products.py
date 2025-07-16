import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
import json


BASE_URL = "https://scrapeme.live/shop/"

# Set up headless browser
options = Options()
options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get(BASE_URL)
time.sleep(5)  # Wait for JS to load

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

product_cards = soup.select("li.product")

print(f"[DEBUG] Found {len(product_cards)} products")

data = []
os.makedirs('task1_scraping_clone/output/images', exist_ok=True)

for product in product_cards:
    try:
        name = product.select_one("h2").text.strip()
        price = product.select_one("span.price").text.strip() if product.select_one("span.price") else "N/A"
        img_url = product.select_one("img")["src"]
        product_url = product.select_one("a")["href"]
        image_filename = f"{name.replace(' ', '_')}.jpg"

        img_data = requests.get(img_url).content
        with open(f'task1_scraping_clone/output/images/{image_filename}', 'wb') as handler:
            handler.write(img_data)

        data.append({
            "name": name,
            "price": price,
            "image_filename": image_filename,
            "product_url": product_url
        })
        print(f"[+] Scraped: {name}")
    except Exception as e:
        print(f"[!] Error scraping product: {e}")

driver.quit()

# Save to CSV/JSON
df = pd.DataFrame(data)
df.to_csv('task1_scraping_clone/output/products.csv', index=False)
with open('task1_scraping_clone/output/products.json', 'w') as f:
    json.dump(data, f, indent=4)

print("[✅] Done scraping with Selenium.")
