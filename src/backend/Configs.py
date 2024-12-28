"""
This module stores the application's configurations.
"""

import os
import yaml


config_file = os.path.join(os.path.dirname(__file__), os.pardir, "configs", "Application.yml")

class Config:
    """
    The configuration of the application.
    """

    def __init__(self, config_file: str = config_file):
        """
        Open the configuration file and load the application configuration.
        """

        self.__host: str = None
        self.__port: int = None
        self.__user: str = None
        self.__password: str = None
        self.__database: str = None
        self.__charset: str = None
        self.__instance_path: str = None

        try:
            with open(config_file, "r", encoding="utf-8") as f:
                config = yaml.safe_load(f)
                self.__host = config['Database']['host']
                self.__port = config['Database']['port']
                self.__user = config['Database']['user']
                self.__password = config['Database']['password']
                self.__database = config['Database']['database']
                self.__charset = config['Database']['charset']
                self.__instance_path = config['Build']['instance_path']
        except FileNotFoundError:
            raise FileNotFoundError("Application configuration file not found.")
        except yaml.YAMLError:
            raise yaml.YAMLError("Error while loading application configuration file.")

    @property
    def DB_HOST(self) -> str:
        """
        Get the host to connect to the database.
        """

        return self.__host

    @property
    def DB_PORT(self) -> int:
        """
        Get the port to connect to the database.
        """

        return self.__port

    @property
    def DB_USER(self) -> str:
        """
        Get the user to connect to the database.
        """

        return self.__user

    @property
    def DB_PASSWORD(self) -> str:
        """
        Get the password to connect to the database.
        """

        return self.__password

    @property
    def DB_DATABASE(self) -> str:
        """
        Get the name of the database to connect to.
        """

        return self.__database

    @property
    def DB_CHARSET(self) -> str:
        """
        Get the charset of the database.
        """

        return self.__charset

    @property
    def instance_path(self) -> str:
        """
        Get the path to the instance directory.
        """

        return self.__instance_path
