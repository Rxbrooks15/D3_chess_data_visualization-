import numpy as np
import pandas as pd
import bs4
from bs4 import BeautifulSoup
import requests
import csv
import datetime
import time
import hashlib
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
now = datetime.datetime.now()

USERNAME = "rainebrookshire"
PASSWORD = "God12345"
GAMES_URL = "https://www.chess.com/games/archive/rainebrookshire?gameType=recent&gameTypeslive%5B0%5D=rapid&gameOwner=my_game&gameTypes%5B0%5D=blitz&gameTypes%5B1%5D=standard&gameTypes%5B2%5D=lightning&gameTypes%5B3%5D=bullet&gameTypes%5B4%5D=daily&gameTypes%5B5%5D=rapid&page=1" + \
            USERNAME + \
            "&gameType=live&gameResult=&opponent=&opening=&color=&gameTourTeam=&" + \
            "timeSort=desc&rated=rated&startDate%5Bdate%5D=08%2F01%2F2013&endDate%5Bdate%5D=" + \
            str(now.month) + "%2F" + str(now.day) + "%2F" + str(now.year) + \
            "&ratingFrom=&ratingTo=&page="
LOGIN_URL = "https://www.chess.com/login"
#https://www.chess.com/games/archive?gameOwner=other_game&username=


driver = webdriver.Chrome("chromedriver.exe", options=options)
driver.get(LOGIN_URL)
driver.find_element(By.ID, "username").send_keys(USERNAME)
driver.find_element(By.ID, "password").send_keys(PASSWORD)
#driver.find_element_by_xpath("//button[contains(text(), 'Log In')]").click()
driver.find_element(By.ID,"login").click()
time.sleep(5)

tables = []
game_links = []

for page_number in range(1):
    driver.get(GAMES_URL + str(page_number + 1))
    time.sleep(5)
    tables.append(
        pd.read_html(
            driver.page_source,
            attrs={'class': 'table-component table-hover archive-games-table'}
        )[0]
    )

    table_user_cells = driver.find_elements(By.CLASS_NAME, 'archive-games-user-cell')
    for cell in table_user_cells:
        link = cell.find_elements(By.TAG_NAME, 'a')[0]
        game_links.append(link.get_attribute('href'))

driver.close()

# Print the extracted game links
for link in game_links:
    print(link)

with open('game_links.txt', 'w') as file:
    for link in game_links:
        file.write(link + '\n')

games = pd.concat(tables)

games.to_csv('collected_data.csv', index=False)
tables

identifier = pd.Series(
    games['Players'] + str(games['Result']) + str(games['Moves']) + games['Date']
).apply(lambda x: x.replace(" ", ""))

games.insert(
    0,
    'GameId',
    identifier.apply(lambda x: hashlib.sha1(x.encode("utf-8")).hexdigest())
)

print(games.head(3))