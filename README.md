# 📈 Web Scraping Stock Prices using Python

This project scrapes **real-time stock data** from [Groww.in](https://groww.in) using Python. It automates the extraction of key stock information such as **Company Name**, **Current Price**, **Change (%)**, **Volume**, and **Stock URL**.

---

## 🚀 Features

- ✅ Scrapes stock data from multiple company pages (US + Indian Stocks)
- ✅ Extracts:
  - Company Name
  - Current Stock Price
  - Price Change (%)
  - Volume
  - Stock URL
- ✅ Displays clean, structured output
- ✅ Handles missing or unavailable data gracefully
- ✅ Easy to extend to new stock URLs

---

## 🧠 Tech Stack Used

- **Python**
- **Requests** – for HTTP requests
- **BeautifulSoup (bs4)** – for parsing HTML
- **Pandas** (used optionally for future data processing)
- **Groww.in** as the source website

---

## 🔍 Sample Output

```bash
{'Company': 'Nike Inc', 'Price': '$58.59', 'Change': 'N/A', 'Volume': 'N/A', 'URL': 'https://groww.in/us-stocks/nke'}
--------------------------------------------------
{'Company': 'Apple Inc', 'Price': '$205.35', 'Change': 'N/A', 'Volume': 'N/A', 'URL': 'https://groww.in/us-stocks/aapl'}
--------------------------------------------------
...
