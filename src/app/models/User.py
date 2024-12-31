"""
This module defines the `User` entity model.
"""

class User:
    """
    `User` entity model.
    """

    def __init__(self, id: int = None, name: str = None, password: str = None, email: str = None, create_time: str = None):
        """
        Initializer of `User` entity model.

        :param id: user id.
        :param name: user name.
        :param password: user password.
        :param email: user email.
        :param create_time: user create time.
        """

        self.__id = id
        self.__name = name
        self.__password = password
        self.__email = email
        self.__create_time = create_time
    
    def __str__(self):
        """
        String representation of `User` entity model.

        :return: string representation of `User` entity model.
        """

        return f"User [id = {self.__id}, name = {self.__name}, password = {self.__password}, email = {self.__email}, create_time = {self.__create_time}]"
    
    def __eq__(self, other: object) -> bool:
        """
        Equality of `User` entity model.

        :param other: another `User` entity model.
        :return: `True` if two `User` entity models are equal, otherwise `False`.
        """

        if not isinstance(other, User):
            return False
        
        return self.__id == other.__id and self.__name == other.__name and self.__password == other.__password and self.__email == other.__email and self.__create_time == other.__create_time
    
    @property
    def id(self) -> int:
        """
        User id.
        """

        return self.__id
    
    @property
    def name(self) -> str:
        """
        User name.
        """

        return self.__name
    
    @property
    def password(self) -> str:
        """
        User password.
        """

        return self.__password
    
    @property
    def email(self) -> str:
        """
        User email.
        """

        return self.__email
    
    @property
    def create_time(self) -> str:
        """
        User create time.
        """

        return self.__create_time
    
    @id.setter
    def id(self, id: int) -> None:
        """
        Set user id.
        """

        self.__id = id
    
    @name.setter
    def name(self, name: str) -> None:
        """
        Set user name.
        """

        self.__name = name
    
    @password.setter
    def password(self, password: str) -> None:
        """
        Set user password.
        """

        self.__password = password
    
    @email.setter
    def email(self, email: str) -> None:
        """
        Set user email.
        """

        self.__email = email
    
    @create_time.setter
    def create_time(self, create_time: str) -> None:
        """
        Set user create time.
        """

        self.__create_time = create_time