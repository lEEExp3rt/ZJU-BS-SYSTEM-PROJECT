"""
This module stores the application's configurations.
"""

import os
import yaml
from enum import Enum, unique


config_file = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "Appication.yml")

class DatabaseConfig:
    """
    Database configuration.
    """

    def __init__(self, config_file: str = config_file):
        """
        Open the configuration file and load the database configuration.
        """

        self.__host: str = None
        self.__port: int = None
        self.__user: str = None
        self.__password: str = None
        self.__database: str = None
        self.__charset: str = None

        try:
            with open(config_file, "r", encoding="utf-8") as f:
                config = yaml.safe_load(f)
                self.__host = config['host']
                self.__port = config['port']
                self.__user = config['user']
                self.__password = config['password']
                self.__database = config['database']
                self.__charset = config['charset']
        except FileNotFoundError:
            raise FileNotFoundError("Database configuration file not found.")
        except yaml.YAMLError:
            raise yaml.YAMLError("Error while loading database configuration file.")

    @property
    def host(self) -> str:
        """
        Get the host to connect to the database.
        """

        return self.__host

    @property
    def port(self) -> int:
        """
        Get the port to connect to the database.
        """

        return self.__port

    @property
    def user(self) -> str:
        """
        Get the user to connect to the database.
        """

        return self.__user

    @property
    def password(self) -> str:
        """
        Get the password to connect to the database.
        """

        return self.__password

    @property
    def database(self) -> str:
        """
        Get the name of the database to connect to.
        """

        return self.__database

    @property
    def charset(self) -> str:
        """
        Get the charset of the database.
        """

        return self.__charset


@unique
class Platform(Enum):
    """
    Supported platforms.
    """

    SUNING = "https://www.suning.com/"
    DANGDANG = "https://www.dangdang.com/"
