""" 
This file is used to store the database connection configurations.
"""

import yaml
import os

class ConnectConfig:
    """
    Database connection configuration class.
    """

    configFile = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'config', 'application.yml')

    def __init__(self):
        """
        Constructor of the connect config class.
        """

        self.__host: str = None
        self.__port: int = None
        self.__user: str = None
        self.__password: str = None
        self.__database: str = None
        self.__charset: str = None

        try:
            with open(self.configFile, 'r', encoding='utf-8') as f:
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
    
    def __str__(self):
        """
        String representation of the connect config class.
        """

        return (f"utils.ConnectConfig: ["
                 "Host: {self.__host},"
                 "Port: {self.__port},"
                 "User: {self.__user},"
                 "Password: {self.__password},"
                 "Database: {self.__database},"
                 "Charset: {self.__charset}"
                 "]")

    @property
    def host(self) -> str:
        """
        Get the host of the database.
        """

        return self.__host

    @property
    def port(self) -> int:
        """
        Get the port of the database.
        """

        return self.__port

    @property
    def user(self) -> str:
        """
        Get the user of the database.
        """

        return self.__user

    @property
    def password(self) -> str:
        """
        Get the password of the database.
        """

        return self.__password

    @property
    def database(self) -> str:
        """
        Get the name of the database.
        """

        return self.__database

    @property
    def charset(self) -> str:
        """
        Get the charset of the database.
        """

        return self.__charset