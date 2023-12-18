from scraper import scrapeData
from datetime import date

def printNewData(url):   
    data = scrapeData(url)

    print(date.today())
    print(data)
