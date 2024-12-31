"""
This module defines the `Product` entity model.
"""

from app.utils.Platforms import Platform
from datetime import datetime
from typing import Tuple, overload

class Product:
    """
    `Product` entity model.
    """

    def __init__(
        self,
        id: int = None,
        name: str = None,
        description: str = None,
        url: str = None,
        image: str = None,
        category: str = None,
        scale: str = None,
        shop: str = None,
        checkpoint: datetime = None,
        platform: Platform = None
    ):
        """
        Initializer of `Product` entity model.

        :param id: product id.
        :param name: product name.
        :param description: product description.
        :param url: product URL.
        :param image: product image URL.
        :param category: product category.
        :param scale: product scale.
        :param shop: product shop name.
        :param checkpoint: product's latest checkpoint.
        :param platform: product platform.
        """

        self.__id = id
        self.__name = name
        self.__description = description
        self.__url = url
        self.__image = image
        self.__category = category
        self.__scale = scale
        self.__shop = shop
        self.__checkpoint = checkpoint
        self.__platform = platform
    
    def __str__(self):
        """
        String representation of `Product` entity model.

        :return: string representation of `Product` entity model.
        """

        return f"Product [" \
               f"id = {self.__id}, " \
               f"name = {self.__name}, " \
               f"description = {self.__description}, " \
               f"url = {self.__url}, " \
               f"image = {self.__image}, " \
               f"category = {self.__category}, " \
               f"scale = {self.__scale}, " \
               f"shop = {self.__shop}, " \
               f"checkpoint = {self.__checkpoint}, " \
               f"platform = {self.__platform}" \
               f"]"

    def __eq__(self, other: object) -> bool:
        """
        Equality of `Product` entity model.

        :param other: another `Product` entity model.
        :return: `True` if two `Product` entity models are equal, otherwise `False`.
        """

        if not isinstance(other, Product):
            return False

        return (
            self.__id == other.__id and
            self.__name == other.__name and
            self.__description == other.__description and
            self.__url == other.__url and
            self.__image == other.__image and
            self.__category == other.__category and
            self.__scale == other.__scale and
            self.__shop == other.__shop and
            self.__checkpoint == other.__checkpoint and
            self.__platform == other.__platform
        )

    def to_dict(self) -> dict:
        """
        Convert `Product` entity model to dictionary for display.

        :return: dictionary representation of `Product` entity model.
        """

        return {
            'id': self.__id,
            'name': self.__name,
            'description': self.__description if self.__description else '',
            'url': self.__url,
            'image': self.__image,
            'shop': self.__shop,
            'platform': self.__platform.value
        }
    
    @property
    def all(self) -> Tuple:
        """
        All attributes of `Product` entity model for database operations.
        """

        return (
            self.__id,
            self.__name,
            self.__description,
            self.__url,
            self.__image,
            self.__category,
            self.__scale,
            self.__shop,
            self.__checkpoint,
            self.__platform.name
        )

    @property
    def id(self) -> int:
        """
        Product id.
        """

        return self.__id

    @property
    def name(self) -> str:
        """
        Product name.
        """

        return self.__name

    @property
    def description(self) -> str:
        """
        Product description.
        """

        return self.__description

    @property
    def url(self) -> str:
        """
        Product URL.
        """

        return self.__url

    @property
    def image(self) -> str:
        """
        Product image URL.
        """

        return self.__image

    @property
    def category(self) -> str:
        """
        Product category.
        """

        return self.__category

    @property
    def scale(self) -> str:
        """
        Product scale.
        """

        return self.__scale

    @property
    def shop(self) -> str:
        """
        Product shop name.
        """

        return self.__shop
    
    @property
    def checkpoint(self) -> datetime:
        """
        Product's latest checkpoint.
        """

        return self.__checkpoint

    @property
    def platform(self) -> Platform:
        """
        Product platform.
        """

        return self.__platform

    @id.setter
    def id(self, id: int) -> None:
        """
        Set product id.
        """

        self.__id = id

    @name.setter
    def name(self, name: str) -> None:
        """
        Set product name.
        """

        self.__name = name

    @description.setter
    def description(self, description: str) -> None:
        """
        Set product description.
        """

        self.__description = description

    @url.setter
    def url(self, url: str) -> None:
        """
        Set product URL.
        """

        self.__url = url

    @image.setter
    def image(self, image: str) -> None:
        """
        Set product image URL.
        """

        self.__image = image

    @category.setter
    def category(self, category: str) -> None:
        """
        Set product category.
        """

        self.__category = category

    @scale.setter
    def scale(self, scale: str) -> None:
        """
        Set product scale.
        """

        self.__scale = scale

    @shop.setter
    def shop(self, shop: str) -> None:
        """
        Set product shop name.
        """

        self.__shop = shop
    
    @checkpoint.setter
    def checkpoint(self, checkpoint: datetime) -> None:
        """
        Set product's latest checkpoint.
        """

        self.__checkpoint = checkpoint

    @platform.setter
    def platform(self, platform: Platform) -> None:
        """
        Set product platform.
        """

        self.__platform = platform
