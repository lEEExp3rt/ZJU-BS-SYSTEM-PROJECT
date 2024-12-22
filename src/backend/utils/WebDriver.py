"""
This file gets a webdriver instance for spiders.

The webdriver is Chrome.
"""

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

driver_path = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "resources", "chromedriver")

def get_webdriver() -> webdriver.Chrome:
    """
    Get a webdriver instance for spiders.
    """

    return webdriver.Chrome(
        options=webdriver.ChromeOptions(),
        service=ChromeService(executable_path=driver_path)
    )