"""
This file defines the base spider class.
"""

from models.Product import Product
from utils.Configs import Platform
from selenium import webdriver
from abc import ABC, abstractmethod

class Spider(ABC):
    """
    Spider interface.
    """

    wait_time = 5

    def __init__(self, driver: webdriver.Chrome, platform: Platform):
        """
        Constructor.

        :param driver: The webdriver to use.
        :param platform: The platform to crawl.
        """

        self.__driver = driver
        self.__platform = platform
    
    @abstractmethod
    def crawl(self, keyword: str, pages: int) -> list[Product]:
        """
        Crawl the site for the given keyword.

        :param keyword: The keyword to search for.
        :param pages: The number of pages to crawl.
        """

        pass

    @property
    def driver(self) -> webdriver.Chrome:
        """
        Get the webdriver.
        """

        return self.__driver

    @property
    def platform(self) -> Platform:
        """
        Get the platform.
        """

        return self.__platform