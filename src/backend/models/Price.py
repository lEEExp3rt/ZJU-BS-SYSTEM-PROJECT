"""
This module defines the `Price` entity model.
"""

class Price:
    """
    `Price` entity model.
    """

    def __init__(self, id: int = None, price: float = None, checkpoint: int = None):
        """
        Initializer of `Price` entity model.

        :param id: product id.
        :param price: product price at the checkpoint.
        :param checkpoint: the checkpoint of the current price.
        """

        self.__id = id
        self.__price = price
        self.__checkpoint = checkpoint
    
    def __str__(self):
        """
        String representation of `Price` entity model.

        :return: string representation of `Price` entity model.
        """

        return f"Price [id = {self.__id}, price = {self.__price}, checkpoint = {self.__checkpoint}]"
    
    def __eq__(self, other: object) -> bool:
        """
        Equality comparison of `Price` entity model.

        :param other: the other `Price` entity model to be compared.
        :return: `True` if the two `Price` entity models are equal, `False` otherwise.
        """

        if not isinstance(other, Price):
            return False
        
        return self.__id == other.__id and self.__price == other.__price and self.__checkpoint == other.__checkpoint
    
    @property
    def id(self) -> int:
        """
        Product id of the price.
        """

        return self.__id
    
    @property
    def price(self) -> float:
        """
        Price of the product at the checkpoint.
        """

        return self.__price
    
    @property
    def checkpoint(self) -> int:
        """
        Checkpoint of the current price.
        """

        return self.__checkpoint
    
    @id.setter
    def id(self, id: int) -> None:
        """
        Set the product id of the price.
        """

        self.__id = id
    
    @price.setter
    def price(self, price: float) -> None:
        """
        Set the price of the product at the checkpoint.
        """

        self.__price = price
    
    @checkpoint.setter
    def checkpoint(self, checkpoint: int) -> None:
        """
        Set the checkpoint of the current price.
        """

        self.__checkpoint = checkpoint