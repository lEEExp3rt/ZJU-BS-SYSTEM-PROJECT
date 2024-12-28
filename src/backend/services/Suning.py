"""
This module defines the spider used to crawl from Suning.
"""

from backend.services.Spider import Spider
from backend.models.Product import Product
from backend.models.Price import Price
from backend.utils.Configs import Platform
import time
import re
import mmh3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from typing import List, Tuple

class Suning(Spider):
    """
    [Suning](https://www.suning.com/) spider.
    """

    def __init__(self, driver: webdriver.Chrome):

        super().__init__(driver, Platform.SUNING)

    def crawl(self, keyword, pages = 1) -> List[Tuple[Product, Price]]:

        try:
            # Open the site.
            self.driver.get(self.platform.value)

            # Find the search box and input the keyword.
            search_box = self.driver.find_element(By.ID, "searchKeywords")
            search_box.send_keys(keyword)
            search_box.send_keys(Keys.ENTER)

            # Get the products.
            price_format = re.compile(r"\d+\.\d{2}")
            result = []
            wait = WebDriverWait(self.driver, self.wait_time)
            checkpoint = int(time.time())
            for page in range(pages):
                self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
                products = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-box")))

                # Parse each product.
                for product in products:
                    name = product.find_element(By.CLASS_NAME, "title-selling-point").text
                    try:
                        description = product.find_element(By.CLASS_NAME, "title-selling-point").find_element(By.TAG_NAME, "em").get_attribute("innerText")
                    except NoSuchElementException:
                        description = None
                    url = product.find_element(By.CLASS_NAME, "title-selling-point").find_element(By.TAG_NAME, "a").get_attribute("href")
                    image_url = product.find_element(By.CLASS_NAME, "sellPoint").find_element(By.TAG_NAME, "img").get_attribute("src")
                    category = None # TODO
                    scale = None # TODO
                    id = mmh3.hash(key=url, signed=False)
                    try:
                        shop = product.find_element(By.CLASS_NAME, "store-name").text
                    except NoSuchElementException:
                        shop = None
                    price = float(price_format.search(product.find_element(By.CLASS_NAME, "def-price").text).group())
                    result.append((
                        Product(
                            id=id,
                            name=name,
                            description=description,
                            url=url,
                            image=image_url,
                            category=category,
                            scale=scale,
                            shop=shop,
                            checkpoint=checkpoint,
                            platform=self.platform
                        ),
                        Price(
                            id=id,
                            price=price,
                            checkpoint=checkpoint
                        )
                    ))

                try:
                    next_page = wait.until(EC.presence_of_element_located((By.ID, "nextPage")))
                except TimeoutException:
                    break
                else:
                    self.driver.get(next_page.get_attribute("href"))

        except Exception as e:
            raise e
        
        else:
            return result

        finally:
            self.driver.quit()
