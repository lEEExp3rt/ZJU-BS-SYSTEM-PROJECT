"""
This module stores the application's configurations.
"""

import os
import yaml


class Config:
    """
    The configuration of the application.
    """

    config_file = os.path.join(os.path.dirname(__file__), os.pardir, "configs", "Application.yml")

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
        self.__app_name: str = None
        self.__app_instance_path: str = None
        self.__email_smtp: str = None
        self.__emial_port: int = None
        self.__email_sendername: str = None
        self.__email_senderemail: str = None
        self.__email_senderpassword: str = None

        try:
            with open(config_file, "r", encoding="utf-8") as f:
                config = yaml.safe_load(f)
                self.__db_host = config['Database']['host']
                self.__db_port = config['Database']['port']
                self.__db_user = config['Database']['user']
                self.__db_password = config['Database']['password']
                self.__db_database = config['Database']['database']
                self.__db_charset = config['Database']['charset']
                self.__app_name = config['Build']['name']
                self.__app_instance_path = config['Build']['instance_path']
                self.__email_smtp = config['Email']['smtp']
                self.__emial_port = config['Email']['port']
                self.__email_sendername = config['Email']['sendername']
                self.__email_senderemail = config['Email']['senderemail']
                self.__email_senderpassword = config['Email']['senderpassword']
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
    def app_name(self) -> str:
        """
        Get the name of the application.
        """

        return self.__app_name

    @property
    def instance_path(self) -> str:
        """
        Get the path to the instance directory.
        """

        return self.__app_instance_path
    
    @property
    def email_smtp(self) -> str:
        """
        Get the SMTP server address.
        """

        return self.__email_smtp

    @property
    def email_port(self) -> int:
        """
        Get the SMTP server port.
        """

        return self.__emial_port

    @property
    def email_sendername(self) -> str:
        """
        Get the sender's name.
        """

        return self.__email_sendername

    @property
    def email_senderemail(self) -> str:
        """
        Get the sender's email address.
        """

        return self.__email_senderemail

    @property
    def email_senderpassword(self) -> str:
        """
        Get the sender's password.
        """

        return self.__email_senderpassword


""" Global instance of the Config class. """
configs = Config()
