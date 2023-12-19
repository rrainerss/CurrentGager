import requests
from bs4 import BeautifulSoup
from dataInputOutput import printNewData

def scrapeData(config):
    # Get response, extract code, parse into HTML
    response = requests.get(config["url"])
    htmlCode = response.content
    soup = BeautifulSoup(htmlCode, "html.parser")

    # Find the table with time intervals
    time_intervals_HTML = soup.find_all("tr", attrs={"data-hours": True})
    time_intervals_values = {}

    # Assign time intervals and the corresponding price data to a dictionary
    for time_interval in time_intervals_HTML:
        time_intervals_values[
            time_interval.find("th").get_text()
            ] = time_interval.find("th").find_next().get_text()

    return time_intervals_values