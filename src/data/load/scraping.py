""" Scrape from the webpage bitcoin.com get data from 04-16-2022
from: https://github.com/Shreyav29/WebScrapingBitcoin.com/blob/main/Scraping%20Bitcoin.com%20.ipynb"""

import json
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
import os
import requests


def slenium_bitocin_page():
    """
    Usless cause it needs the driver and in production it has a spensive cost
    """
    driver = webdriver.Chrome("/opt/homebrew/bin/chromedriver")
    driver.get("https://charts.bitcoin.com/btc/chart/price#5moc")

    # Getting the names of the features that we want to download

    for name in names:
        driver.find_element_by_id("sidebar-list-btn").click()
        class_name = driver.find_element_by_id(
            "sidebar"
        ).find_element_by_id("directory")
        class_name.find_element_by_partial_link_text(name).click()
        time.sleep(3)
        driver.find_element_by_id("sidebar-tools-btn").click()

        driver.find_element_by_id("data-download").click()
        time.sleep(3)

    input_files = os.listdir('data')
