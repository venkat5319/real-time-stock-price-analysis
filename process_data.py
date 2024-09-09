import json

def process_data(raw_data):
    # Example: Process the raw data to extract relevant information
    # This example assumes that `raw_data` is a dictionary with the stock data
    processed_data = {}
    
    try:
        time_series = raw_data.get('Time Series (1min)', {})
        for time, metrics in time_series.items():
            processed_data[time] = {
                'open': metrics.get('1. open'),
                'high': metrics.get('2. high'),
                'low': metrics.get('3. low'),
                'close': metrics.get('4. close'),
                'volume': metrics.get('5. volume')
            }
    except Exception as e:
        print(f"Error processing data: {e}")
    
    return processed_data

#if __name__ == "__main__":
def processed_data():
    with open('stock_data.json', 'r') as file:
        raw_data = json.load(file)
    processed_data = process_data(raw_data)
    with open("processed_data.json",'w', encoding='utf-8') as f:
        json.dump(processed_data,f,ensure_ascii=False,indent=4)
    return "Success"