"""
This file defines the `Subscription` entity model.
"""

class Subscription:
    """
    `Subscription` entity model.
    """

    def __init__(self, sid: int = None, pid: int = None, uid: int = None, timer: str = None, enable: bool = None):
        """
        Constructor of `Subscription` entity model.

        :param sid: subscription id.
        :param pid: product id.
        :param uid: user id.
        :param timer: subscription timer.
        :param enable: subscription enable status.
        """

        self.__sid = sid
        self.__pid = pid
        self.__uid = uid
        self.__timer = timer
        self.__enable = enable

    def __str__(self):
        """
        String representation of `Subscription` entity model.

        :return: string representation of `Subscription` entity model.
        """

        return f"Subscription [sid = {self.__sid}, pid = {self.__pid}, uid = {self.__uid}, timer = {self.__timer}, enable = {self.__enable}]"
    
    def __eq__(self, other: object) -> bool:
        """
        Equality of `Subscription` entity model.

        :param other: another `Subscription` entity model.
        :return: True if two `Subscription` entity models are equal, False otherwise.
        """

        if not isinstance(other, Subscription):
            return False
        return self.__sid == other.__sid and self.__pid == other.__pid and self.__uid == other.__uid and self.__timer == other.__timer and self.__enable == other.__enable

    @property
    def sid(self) -> int:
        """
        Subscription id.
        """

        return self.__sid

    @property
    def pid(self) -> int:
        """
        Product id of the subscription.
        """

        return self.__pid
    
    @property
    def uid(self) -> int:
        """
        User id of the subscription.
        """

        return self.__uid

    @property
    def timer(self) -> str:
        """
        Subscription timer.
        """

        return self.__timer

    @property
    def enable(self) -> bool:
        """
        Subscription enable status.
        """

        return self.__enable

    @sid.setter
    def sid(self, sid: int) -> None:
        """
        Set subscription id.
        """

        self.__sid = sid

    @pid.setter
    def pid(self, pid: int) -> None:
        """
        Set product id of the subscription.
        """

        self.__pid = pid

    @uid.setter
    def uid(self, uid: int) -> None:
        """
        Set user id of the subscription.
        """

        self.__uid = uid

    @timer.setter
    def timer(self, timer: str) -> None:
        """
        Set subscription timer.
        """

        self.__timer = timer

    @enable.setter
    def enable(self, enable: bool) -> None:
        """
        Set subscription enable status.
        """

        self.__enable = enable