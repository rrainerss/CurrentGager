from scraper import scrapeData
from datetime import date
import os

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