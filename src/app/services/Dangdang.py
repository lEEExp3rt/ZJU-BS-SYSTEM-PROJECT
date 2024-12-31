"""
This module defines the spider used to crawl from Dangdang.
"""

from app.models.Product import Product
from app.models.Price import Price
from app.utils.Platforms import Platform
import re
import mmh3
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from typing import List, Tuple


def crawl(driver: webdriver.Chrome, keyword: str, wait_time: int, pages: int = 1 ) -> List[Tuple[Product, Price]]:
    """
    [Dangdang](https://www.dangdang.com/) crawler.
    """

    try:
        # Open the site.
        driver.get(Platform.DANGDANG.value)

        # Find the search box and input the keyword.
        search_box = driver.find_element(By.ID, "key_S")
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.ENTER)

        # Check if there are any results.
        try:
            driver.find_element(By.CLASS_NAME, "search_null_ts")
        except NoSuchElementException:
            pass
        else:
            return []

        # Get the products.
        price_format = re.compile(r"\d+\.\d{2}")
        result = []
        wait = WebDriverWait(driver, wait_time)
        checkpoint = datetime.now()
        for _ in range(pages):
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
            wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "li")))
            products = driver.find_element(By.CLASS_NAME, "bigimg").find_elements(By.TAG_NAME, "li")

            # Parse each product.
            for product in products:
                name = product.find_element(By.CLASS_NAME, "name").find_element(By.TAG_NAME, "a").get_attribute("title")
                description = name
                url = product.find_element(By.CLASS_NAME, "pic").get_attribute("href")
                image_url = product.find_element(By.TAG_NAME, "img").get_attribute("src")
                category = keyword
                scale = None # TODO
                id = mmh3.hash(key=url, signed=False)
                try:
                    shop = product.find_element(By.NAME, "itemlist-shop-name").text
                except NoSuchElementException:
                    shop = None
                try:
                    price = float(price_format.search(product.find_element(By.CLASS_NAME, "search_now_price").text).group())
                except NoSuchElementException:
                    price = float(price_format.search(product.find_element(By.CLASS_NAME, "price_n").text).group())
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
                        platform=Platform.DANGDANG
                    ),
                    Price(
                        id=id,
                        price=price,
                        checkpoint=checkpoint
                    )
                ))

            try:
                next_page = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "paging")))
                next_page = next_page.find_element(By.CLASS_NAME, "next").find_element(By.TAG_NAME, "a")
            except TimeoutException:
                break
            else:
                driver.get(next_page.get_attribute("href"))

    except Exception as e:
        raise e
    
    else:
        return result

    finally:
        driver.quit()
