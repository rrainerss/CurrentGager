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
    print(f"--- Here is the price table for {date.today()}")
    print()

    print("--- {:<6} {:<6}".format('Hour','Price'))
    for key, value in data.items():
        print("--- {:<6} {:<6}".format(key, value))