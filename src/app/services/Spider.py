"""
This module defines the base spider class.
"""

from app.models.Product import Product
from app.models.Price import Price
from app.utils.Platforms import Platform
from app.services import Dangdang, Suning
from app.utils.WebDriver import get_webdriver
from typing import List, Tuple

class SpiderManager:
    """
    Spider manager to handle crawling data.
    """

    def __init__(self, wait_time: int = 2):
        """
        Initializer.

        :param wait_time: The waiting time for each crawler.
        """

        self.__wait_time = wait_time
    
    def crawl(self, platform: Platform, keyword: str, pages: int = 1) -> List[Tuple[Product, Price]]:
        """
        Crawl the site for the given keyword.

        :param platform: The platform to crawl.
        :param keyword: The keyword to search for.
        :param pages: The number of pages to crawl.
        """

        results = []
        match platform:
            case Platform.DANGDANG:
                results = Dangdang.crawl(get_webdriver(), keyword, self.__wait_time, pages)
            case Platform.SUNING:
                results = Suning.crawl(get_webdriver(), keyword, self.__wait_time, pages)
            case _:
                raise ValueError("Invalid platform.")

        return results
