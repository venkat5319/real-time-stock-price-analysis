import requests
import json

API_KEY = 'RAPYLKXSA74MNQVB'  # Replace with your actual API key
STOCK_SYMBOL = 'AAPL'
BASE_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK_SYMBOL}&interval=1min&apikey={API_KEY}'

def fetch_stock_data():
    response = requests.get(BASE_URL)
    data = response.json()
    return data

# if __name__ == "__main__":

def fetch_data():
    stock_data = fetch_stock_data()
    with open("stock_data.json","w",encoding='utf-8') as f:
        json.dump(stock_data,f,ensure_ascii=False,indent=4)
    return "Success"
