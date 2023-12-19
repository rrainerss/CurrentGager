import mysql.connector

def queries_0003_191223(config):
    # Connect to database
    mydb = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        autocommit=True
    )
    # Create a cursor
    cursor = mydb.cursor()

    cursor.execute('''
        DROP DATABASE IF EXISTS electricity_prices;
    ''')

    cursor.execute('''
        CREATE DATABASE IF NOT EXISTS electricity_prices;
    ''')

    cursor.execute('''
        USE electricity_prices
    ''')

    cursor.execute('''
        CREATE TABLE price_data(
            id INT AUTO_INCREMENT PRIMARY KEY,
            date DATE NOT NULL,
            price_list JSON NOT NULL
        );
    ''')

    # Commit changes and close connections
    mydb.commit()
    cursor.close()
    mydb.close()