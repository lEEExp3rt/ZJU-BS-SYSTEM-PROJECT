"""
This file defines the `Product` entity model.
"""

from utils.Configs import Platform

class Product:
    """
    `Product` entity model.
    """

    def __init__(self, id: int = None, name: str = None, category: str = None, description: str = None, scale: str = None, image: str = None, platform: Platform = None):
        """
        Constructor of `Product` entity model.

        :param id: product id.
        :param name: product name.
        :param category: product category.
        :param description: product description.
        :param scale: product scale.
        :param image: product image URL.
        :param platform: product platform.
        """

        self.__id = id
        self.__name = name
        self.__category = category
        self.__description = description
        self.__scale = scale
        self.__image = image
        self.__platform = platform
    
    def __str__(self):
        """
        String representation of `Product` entity model.

        :return: string representation of `Product` entity model.
        """

        return f"Product [id = {self.__id}, name = {self.__name}, category = {self.__category}, description = {self.__description}, scale = {self.__scale}, image = {self.__image}, platform = {self.__platform}]"

    def __eq__(self, other: object) -> bool:
        """
        Equality of `Product` entity model.

        :param other: another `Product` entity model.
        :return: `True` if two `Product` entity models are equal, otherwise `False`.
        """

        if not isinstance(other, Product):
            return False

        return self.__id == other.__id and self.__name == other.__name and self.__category == other.__category and self.__description == other.__description and self.__scale == other.__scale and self.__image == other.__image and self.__platform == other.__platform

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
    def category(self) -> str:
        """
        Product category.
        """

        return self.__category

    @property
    def description(self) -> str:
        """
        Product description.
        """

        return self.__description

    @property
    def scale(self) -> str:
        """
        Product scale.
        """

        return self.__scale

    @property
    def image(self) -> str:
        """
        Product image URL.
        """

        return self.__image

    @property
    def platform(self) -> Platform:
        """
        Product platform.
        """
    
        return self.__platform
    
    @id.setter
    def id(self, id: int):
        """
        Set product id.
        """

        self.__id = id

    @name.setter
    def name(self, name: str):
        """
        Set product name.
        """

        self.__name = name

    @category.setter
    def category(self, category: str):
        """
        Set product category.
        """

        self.__category = category

    @description.setter
    def description(self, description: str):
        """
        Set product description.
        """

        self.__description = description

    @scale.setter
    def scale(self, scale: str):
        """
        Set product scale.
        """

        self.__scale = scale

    @image.setter
    def image(self, image: str):
        """
        Set product image URL.
        """

        self.__image = image

    @platform.setter
    def platform(self, platform: Platform):
        """
        Set product platform.
        """

        self.__platform = platform
