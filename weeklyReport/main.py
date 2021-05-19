import os
import time
from datetime import datetime
from calendar import monthrange

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup

# ============= HEROKU CONFIGURATION ==============
# Heroku required Chrome web browser and chrome driver to be installed into their cloud
# system via Buildpacks and paths directed to it using environment variable.
#
# Buildpacks:
# https://github.com/heroku/heroku-buil...
# https://github.com/heroku/heroku-buil...
#
# Environment Variables Paths:
# CHROMEDRIVER_PATH = /app/.chromedriver/bin/chromedriver
# GOOGLE_CHROME_BIN = /app/.apt/usr/bin/google-chrome

