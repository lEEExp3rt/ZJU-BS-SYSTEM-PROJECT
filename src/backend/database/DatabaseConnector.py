"""
This file is used to establish a connection to the database.

First load the configuration of the database when constructing, then use `connect()` to establish a connection to the database.

After connection, you can use the `conn` to interact with the database.

And don't forget to close the connection using `close()` to release the resources!
"""

from backend.database.ConnectConfig import ConnectConfig
import pymysql.cursors
import pymysql

class DatabaseConnector:
    """
    Database connector.
    """

    cursorType = pymysql.cursors.Cursor

    def __init__(self, config: ConnectConfig):
        """
        Constructor.

        :param config: The configuration of the database.
        """

        self.__config: ConnectConfig = config
        self.__conn: pymysql.Connection = None
    
    def __del__(self):
        """
        Destructor.
        """

        self.close()
    
    @property
    def config(self) -> ConnectConfig:
        """
        Get the configuration of the database.
        """

        return self.__config

    @property
    def conn(self) -> pymysql.Connection:
        """
        Get the connection to the database.
        """

        return self.__conn 
    
    def connect(self) -> None:
        """
        Connect to the database.
        """

        if self.__conn is None:
            try:
                self.__conn = pymysql.connect(
                    host=self.__config.host,
                    user=self.__config.user,
                    password=self.__config.password,
                    database=self.__config.database,
                    port=self.__config.port,
                    charset=self.__config.charset,
                    cursorclass=self.cursorType
                )
            except Exception as e:
                raise e
    
    def close(self) -> None:
        """
        Close the connection to the database.
        """

        if self.__conn is not None:
            try:
                self.__conn.close()
                self.__conn = None
            except Exception as e:
                raise e