import sys
from dataInputOutput import printNewData
from dataInputOutput import clearConsole
from dataInputOutput import checkExistingData
from runMigrations import migrate

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

checkExistingData(config)

input("--- No previous price records found. Press Enter to gather new data ...")

# Uncomment when running for the first time - migrates database structure
migrate(config)

# Connects to database and prints data
# printNewData(config["url"])
