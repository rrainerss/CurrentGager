import os
import sys
from dataInputOutput import printNewData

# Clear console output for either Linux or Windows
def clearConsole():
    try:
        os.system("clear")
    except:
        os.system("clr")

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
