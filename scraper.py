import os
import requests
from bs4 import BeautifulSoup

def scrapeData(url):
    # Get response, extract code, parse into HTML
    response = requests.get(url)
    htmlCode = response.content
    soup = BeautifulSoup(htmlCode, "html.parser")

    # print(soup.prettify())

    dates = soup.find_all("span", class_="help")
    date_today = dates[0].get_text()

    print(date_today)

    time_intervals_HTML = soup.find_all("tr", attrs={"data-hours": True})
    time_intervals_values = {}

    for time_interval in time_intervals_HTML:
        time_intervals_values[time_interval.find("th").get_text()] = time_interval.find("th").find_next().get_text()

    return time_intervals_values