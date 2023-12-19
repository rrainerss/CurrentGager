from datetime import date
import os
import json
import mysql.connector

# Clear console output for either Linux or Windows
def clearConsole():
    try:
        os.system("clear")
    except:
        os.system("clr")

# Print dictionary data in a readable way
def printNewData(config, data):   
    clearConsole()
    print(f"--- Here is the electricity price table for {date.today()}")
    print()
    print("--- {:<6} {:<10}".format('Hour','Price(eur)'))
    for key, value in data.items():
        print("--- {:<6} {:<10}".format(key, value))
    
    try:
        saveToDatabase(config, data)
    except Exception as e:
        print(e)

# Save passed data to the database
def saveToDatabase(config, data):
    cursor, mydb = connectToDatabase(config)

    # Assign only the values to a list
    json_prices = json.dumps(list(data.values()))

    # Insert the data
    query = '''
        INSERT INTO price_data (date, price_list) VALUES (%s, %s)
    '''

    # Execute the INSERT query with the values_list
    cursor.execute(query, (date.today(), json_prices))

    mydb.commit()
    cursor.close()
    mydb.close()

# Connect to the database
def connectToDatabase(config):
    mydb = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"]
    )

    cursor = mydb.cursor()
    return cursor, mydb

def getExistingData(config):
    cursor, mydb = connectToDatabase(config)

    query = "SELECT price_list FROM price_data WHERE date = %s"
    cursor.execute(query, (date.today(),))
    data = cursor.fetchone()

    hours = []

    for hour in range(24):
        next_hour = (hour + 1) % 24
        hours.append(f"{hour:02d}-{next_hour:02d}")

    if data:
        data_dictionary = {}
        json_data = data[0]
        data_list = json.loads(json_data)
        for hour, price in zip(hours, data_list):
            data_dictionary[hour] = price
        return data_dictionary
    else:
        return False
        
