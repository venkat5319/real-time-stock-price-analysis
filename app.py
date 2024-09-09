from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error
from fetch_stock_data import fetch_data
from process_data import processed_data
from database_setup import setup_database
from store_data import stored_data

app = Flask(__name__)

def get_stock_data():
    try:
        if fetch_data() == "Success":
            if processed_data() == "Success":
                if setup_database() == "Success":
                    if stored_data() == "Success":
                        
                        connection = mysql.connector.connect(
                            host='localhost',
                            user='root',
                            password='Venkataramana1998*',
                            database='stock_data_db'
                        )
                        if connection.is_connected():
                            cursor = connection.cursor(dictionary=True)
                            cursor.execute('SELECT * FROM stock_data')
                            rows = cursor.fetchall()
                            return rows
    except Error as e:
        print(f"Error: {e}")
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/stocks', methods=['GET'])
def stocks():
    data = get_stock_data()
    return jsonify(data)

@app.route("/", methods = ['GET'])
def home():
    return "Welcome to the home page please type '/stocks' in the existing url to see the processed stocks data"

if __name__ == "__main__":
    app.run(debug=True)
    
from flask import Flask, jsonify

app = Flask(__name__)

# Existing route for /stocks
@app.route('/stocks', methods=['GET'])
def get_stocks():
    # Logic to return all stocks
    return jsonify({"stocks": [{"symbol": "AAPL", "price": 150.25}, {"symbol": "GOOG", "price": 2800.50}]})

# New route for /stocks/<symbol>
@app.route('/stocks/<symbol>', methods=['GET'])
def get_stock_by_symbol(symbol):
    # Your logic to retrieve stock by symbol
    # Example logic:
    stocks = {
        "AAPL": 150.25,
        "GOOG": 2800.50,
        "MSFT": 299.15
    }
    price = stocks.get(symbol.upper(), "Stock not found")
    return jsonify({"symbol": symbol, "price": price})

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/stocks/<symbol>', methods=['GET'])
def get_stock_by_symbol(symbol):
    # Example logic
    stocks = {
        "AAPL": 150.25,
        "GOOG": 2800.50,
        "MSFT": 299.15
    }
    price = stocks.get(symbol.upper(), "Stock not found")
    return jsonify({"symbol": symbol, "price": price})

