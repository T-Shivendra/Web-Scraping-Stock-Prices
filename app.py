import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from urllib3.util import url

headers = {'user agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.2035442 Safari/537.36'}

urls =[
    'https://groww.in/us-stocks/nke',
    'https://groww.in/us-stocks/ko',
    'https://groww.in/us-stocks/msft',
    'https://groww.in/stocks/m-india-ltd',
    'https://groww.in/us-stocks/axp',
    'https://groww.in/us-stocks/amgn',
    'https://groww.in/us-stocks/aapl',
    'https://groww.in/us-stocks/ba',
    'https://groww.in/us-stocks/csco',
    'https://groww.in/us-stocks/gs',
    'https://groww.in/us-stocks/ibm',
    'https://groww.in/us-stocks/intc',
    'https://groww.in/us-stocks/jpm',
    'https://groww.in/us-stocks/mcd',
    'https://groww.in/us-stocks/crm',
    'https://groww.in/us-stocks/vz',
    'https://groww.in/us-stocks/v',
    'https://groww.in/us-stocks/wmt',
    'https://groww.in/us-stocks/dis'
    ]

def get_stock_data(url):
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')

        # Company name
        company = soup.find('h1', {'class': 'usph14Head displaySmall'})
        if company:
            company = company.text.strip()
        else:
            company = "N/A"

         # Price (handle duplicate class)
        price_tags = soup.find_all('span', {'class': 'uht141Pri contentPrimary displayBase'})
        price = price_tags[0].text.strip() if price_tags else "N/A"

        # Change (%)
        change_tags = soup.find_all('span', {'class': 'uht141Day bodyBaseHeavy contentNegative'})
        if not change_tags:
            # Try positive class
            change_tags = soup.find_all('span', {'class': 'uht141Day bodyBaseHeavy contentPositive'})
            change = change_tags[0].text.strip() if change_tags else "N/A"

            # Volume
            volume_table = soup.find('table', {'class': 'tb10Table col 15'})
            volume = volume_table.find_all('td')[1].text.strip() if volume_table else "N/A"

            # Initialize metrics
            metrics = {
                'Market Cap': 'N/A',
                'P/E Ratio': 'N/A',
                'Dividend Yield': 'N/A',
                '52W High': 'N/A',
                '52W Low': 'N/A',
                'EPS': 'N/A',
                'ROE': 'N/A',
                'P/B Ratio': 'N/A',
                'Debt to Equity': 'N/A',
                'Face Value': 'N/A',
                'Volume' : 'N/A',
            }

            # Parse tables for financial metrics
            tables = soup.find_all('table')
            for table in tables:
                rows = table.find_all('tr')
                for row in rows:
                    cols = row.find_all('td')
                    if len(cols) >= 2:
                        label = cols[0].text.strip()
                        value = cols[1].text.strip()
                        for key in metrics.keys():
                            if key.lower() in label.lower():
                                metrics[key] = value

        return{
            'Company': company,
            'Price': price,
            'Change': change,
            **metrics,
            'URL': url
            }

    except Exception as e:
            print(f"Error scrapping {url}: {e}")
            return None

all_data = []
# Loop through URLs
for url in urls:
    print(f"Scraping: {url}")
    stock_data = get_stock_data(url)
    if stock_data:
     all_data.append(stock_data)
    time.sleep(2)  # polite delay

# Create and display the DataFrame
df = pd.DataFrame(all_data)

print("\nScraped Stock Data:\n")
print(df.to_string(index=False))
# Create and display the DataFrame
df = pd.DataFrame(all_data)

print("\nScraped Stock Data:\n")
print(df.to_string(index=False))
