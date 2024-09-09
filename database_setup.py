import mysql.connector
from mysql.connector import Error

def setup_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your MySQL server hostname
            port="3306",
            user='root',       # Replace with your MySQL username
            password='Venkataramana1998*'  # Replace with your MySQL password
        )
        if connection.is_connected():
            print('Connected to MySQL server')

            cursor = connection.cursor()

            # Create a new database
            cursor.execute('CREATE DATABASE IF NOT EXISTS stock_data_db')
            print('Database created or already exists')

            # Select the database
            cursor.execute('USE stock_data_db')

            # Create a table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS stock_data (
                    time VARCHAR(255) PRIMARY KEY,
                    open DECIMAL(10, 2),
                    high DECIMAL(10, 2),
                    low DECIMAL(10, 2),
                    close DECIMAL(10, 2),
                    volume INT
                )
            ''')
            print('Table created or already exists')
            return "Success"

            connection.commit()

    except Error as e:
        print(f"Error: {e}")
        return e

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection closed')

if __name__ == "__main__":
    setup_database()
    
