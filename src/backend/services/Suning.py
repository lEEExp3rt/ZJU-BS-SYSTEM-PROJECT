"""
This file defines the spiders used to crawl the website.
"""

import time
import re
import hashlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from .Spider import Spider
from models.Product import Product
from utils.Configs import Platform

class Suning(Spider):
    """
    [Suning](https://www.suning.com/) spider.
    """

    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver, Platform.SUNING)

    def crawl(self, keyword, pages) -> list[Product]:
        try:
            # Open the site.
            self.driver.get(self.platform.value)

            # Find the search box and input the keyword.
            search_box = self.driver.find_element(By.ID, "searchKeywords")
            search_box.send_keys(keyword)
            search_box.send_keys(Keys.ENTER)

            # Get the products.
            self.driver.implicitly_wait(self.wait_time)
            self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
            products = self.driver.find_elements(By.CLASS_NAME, "product-box")
            checkpoint = time.time()
            price_format = re.compile(r"\d+\.\d{2}")
            result = []

            # Parse each product.
            for product in products:
                name = product.find_element(By.CLASS_NAME, "title-selling-point").text
                description = None
                try:
                    description = product.find_element(By.CLASS_NAME, "title-selling-point").find_element(By.TAG_NAME, "em").get_attribute("innerText")
                except:
                    pass
                url = product.find_element(By.CLASS_NAME, "title-selling-point").find_element(By.TAG_NAME, "a").get_attribute("href")
                image_url = product.find_element(By.CLASS_NAME, "sellPoint").find_element(By.TAG_NAME, "img").get_attribute("src")
                category = None
                scale = None
                id = None
                price = float(price_format.search(product.find_element(By.CLASS_NAME, "def-price").text).group())
                print(f"Name: {name},\nDescription: {description},\nURL: {url},\nImage URL: {image_url},\nPrice: {price}")
                print()
                print()

        except Exception as e:
            raise e

        finally:
            self.driver.quit()
