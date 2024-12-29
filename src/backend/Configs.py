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

        self.__db_host: str = None
        self.__db_port: int = None
        self.__db_user: str = None
        self.__db_password: str = None
        self.__db_database: str = None
        self.__db_charset: str = None
        self.__app_instance_path: str = None

        try:
            with open(config_file, "r", encoding="utf-8") as f:
                config = yaml.safe_load(f)
                self.__db_host = config['Database']['host']
                self.__db_port = config['Database']['port']
                self.__db_user = config['Database']['user']
                self.__db_password = config['Database']['password']
                self.__db_database = config['Database']['database']
                self.__db_charset = config['Database']['charset']
                self.__app_instance_path = config['Build']['instance_path']
        except FileNotFoundError:
            raise FileNotFoundError("Application configuration file not found.")
        except yaml.YAMLError:
            raise yaml.YAMLError("Error while loading application configuration file.")

    @property
    def DB_HOST(self) -> str:
        """
        Get the host to connect to the database.
        """

        return self.__db_host

    @property
    def DB_PORT(self) -> int:
        """
        Get the port to connect to the database.
        """

        return self.__db_port

    @property
    def DB_USER(self) -> str:
        """
        Get the user to connect to the database.
        """

        return self.__db_user

    @property
    def DB_PASSWORD(self) -> str:
        """
        Get the password to connect to the database.
        """

        return self.__db_password

    @property
    def DB_DATABASE(self) -> str:
        """
        Get the name of the database to connect to.
        """

        return self.__db_database

    @property
    def DB_CHARSET(self) -> str:
        """
        Get the charset of the database.
        """

        return self.__db_charset

    @property
    def instance_path(self) -> str:
        """
        Get the path to the instance directory.
        """

        return self.__app_instance_path
