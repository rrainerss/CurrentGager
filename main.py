import sys
from dataInputOutput import printNewData
from dataInputOutput import clearConsole

clearConsole()

configurationValues = {}

try:
    file = open('config.txt', 'r')
    lines = file.readlines()
    for line in lines:
        key, value = line.strip().split("=")
        configurationValues[key] = value
except:
    print("No configuration file found!")
    sys.exit()

print("--- Welcome to CurrentGager")
input("--- No previous price records found. Press Enter to gather new data ...")

printNewData(configurationValues["url"])
