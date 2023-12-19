import sys
from dataInputOutput import clearConsole
from dataInputOutput import getExistingData
from dataInputOutput import printNewData
from runMigrations import migrate
from scraper import scrapeData
import logging

logging.basicConfig(
    filename='info.log',
    level=logging.INFO,
    filemode='w',
    format='%(message)s'
)
logging.info('-')
logging.info('Program was run')

clearConsole()
config = {}

# Try opening the config file
try:
    file = open('config.txt', 'r')
    lines = file.readlines()
    for line in lines:
        key, value = line.strip().split("=")
        config[key] = value
except:
    print("No configuration file found!")
    sys.exit()

print("--- Welcome to CurrentGager")

# Uncomment when running for the first time - migrates database structure
# Can also be used to manually test both use cases for program - scraping data and fetching from db
# migrate(config)

getExistingData(config)

# Checks if data already exists
if getExistingData(config):
    input("--- Previous price records found! Press enter to show ...")
    data = getExistingData(config)
    logging.info('Records were found')
else:
    input("--- No previous price records found. Press Enter to gather new data ...")
    data = scrapeData(config)
    logging.info('No records found')

printNewData(config, data)
logging.shutdown()

