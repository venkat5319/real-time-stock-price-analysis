import mysql.connector
import json
from mysql.connector import Error

def store_data(processed_data):
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Venkataramana1998*',
            database='stock_data_db'
        )

        if connection.is_connected():
            print('Connected to MySQL server')

            cursor = connection.cursor()

            # Insert or replace data into the table
            for time, metrics in processed_data.items():
                cursor.execute('''
                    INSERT INTO stock_data (time, open, high, low, close, volume)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                    open = VALUES(open),
                    high = VALUES(high),
                    low = VALUES(low),
                    close = VALUES(close),
                    volume = VALUES(volume)
                ''', (time, metrics['open'], metrics['high'], metrics['low'], metrics['close'], metrics['volume']))
            
            connection.commit()
            print('Data stored in database')

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection closed')

#if __name__ == "__main__":
def stored_data():
    # Load processed data from a file or another source
    with open('processed_data.json', 'r') as file:
        processed_data = json.load(file)
    store_data(processed_data)
    return "Success"
