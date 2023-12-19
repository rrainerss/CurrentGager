# This file will run the program and automatically re-create the database
# each time, not requiring code modifications

from runMigrations import migrate
import main
import sys

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

# Force database migration/creation
migrate(config)