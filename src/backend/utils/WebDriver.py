"""
This file gets a webdriver instance for spiders.

The webdriver is Chrome.
"""

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

driver_path = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "resources", "chromedriver")

def get_webdriver(headless: bool = True) -> webdriver.Chrome:
    """
    Get a webdriver instance for spiders.
    """

    options = Options()
    if headless:
        options.add_argument("--headless")
    return webdriver.Chrome(
        options=options,
        service=ChromeService(executable_path=driver_path)
    )