from scraper import scrapeData
from datetime import date
import os
import mysql.connector

cursor = ""

def connectDatabase(configurationValues):
    mydb = mysql.connector.connect(
        host=configurationValues["host"],
        user=configurationValues["user"],
        password=configurationValues["password"]
    )

    cursor = mydb.cursor()
    cursor.execute("DROP DATABASE IF EXISTS electricity_prices")
    cursor.execute("CREATE DATABASE electricity_prices")


# Clear console output for either Linux or Windows
def clearConsole():
    try:
        os.system("clear")
    except:
        os.system("clr")

def printNewData(url):   
    data = scrapeData(url)

    clearConsole()
    print(f"--- Here is the electricity price table for {date.today()}")
    print()
    print("--- {:<6} {:<10}".format('Hour','Price(eur)'))
    for key, value in data.items():
        print("--- {:<6} {:<10}".format(key, value))
    
    saveToDatabase(data)

def saveToDatabase(data):
    print()