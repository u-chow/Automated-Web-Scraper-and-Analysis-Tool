import requests
from bs4 import BeautifulSoup
import random
import pandas as pd

def fetch_custom_website(url):
    headers = {
        'User-Agent': random.choice([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
            'Mozilla/5.0 (X11; Linux x86_64)'
        ])
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        data = []
        # Detect if the website is an e-commerce site (for shoes) or news
        if 'product' in url or 'shop' in url:
            products = soup.find_all(['div', 'li'], class_=['product', 'item'])
            for product in products:
                name = product.find(['h2', 'span', 'p']).get_text(strip=True) if product.find(['h2', 'span', 'p']) else 'N/A'
                price = product.find(['span', 'div'], class_=['price', 'amount']).get_text(strip=True) if product.find(['span', 'div'], class_=['price', 'amount']) else 'N/A'
                data.append({'Product Name': name, 'Price': price})
        else:
            articles = soup.find_all('h2')
            for article in articles:
                title = article.get_text(strip=True)
                link = article.find('a')['href'] if article.find('a') else url
                data.append({'Title': title, 'Link': link})
        df = pd.DataFrame(data)
        df.to_csv('data/custom_scraped_data.csv', index=False)
        print("Website data has been saved.")
    else:
        print(f"Failed to fetch data. Status Code: {response.status_code}")
