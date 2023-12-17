import os
import requests
from bs4 import BeautifulSoup

# Clear console output for either Linux or Windows
try:
    os.system("clear")
except:
    os.system("clr")

url = "https://www.nordpoolgroup.com/en/Market-data1/Dayahead/Area-Prices/ALL1/Hourly/?view=table"

response = requests.get(url)

htmlCode = response.content

parsedHtml = BeautifulSoup(htmlCode, "html.parser")

print(parsedHtml.prettify())