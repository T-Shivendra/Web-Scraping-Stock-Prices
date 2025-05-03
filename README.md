# 📈 Stock Data Scraper (Groww.in)

This Python script scrapes financial data of US and Indian companies from [Groww.in](https://groww.in) using `requests` and `BeautifulSoup`. The data is structured into a Pandas DataFrame and saved as a CSV file.

---

## 🔧 Features

- Scrapes:
  - Company name
  - Current stock price
  - Daily change %
  - Market Cap
  - P/E Ratio
  - EPS
  - Dividend Yield
  - ROE, P/B, Face Value, Volume, and more

- Supports both US and Indian stocks listed on Groww.in
- Outputs data as a table and also saves it as `stock_data.csv`

---

## 🧰 Requirements

Install required Python packages:

```bash
pip install requests beautifulsoup4 pandas
