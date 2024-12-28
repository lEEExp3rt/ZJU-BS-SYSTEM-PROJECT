"""
This module is used to establish a connection to the database.

First load the configuration of the database when constructing, then use `connect()` to establish a connection to the database.

After connection, you can use the `conn` to interact with the database.

And don't forget to close the connection using `close()` to release the resources!

You can also use `get_db()` and `close_db()` to get a database connection and release the resources, respectively.
"""

from backend.utils.Configs import DatabaseConfig
import pymysql.cursors
import pymysql
from flask import g


class DatabaseConnector:
    """
    Database connector.

    Use this class to establish a connection to the database and do operations on the database.
    """

    cursorType = pymysql.cursors.Cursor

    def __init__(self):

        self.__config: DatabaseConfig = DatabaseConfig()
        self.__conn: pymysql.Connection = None

    def __del__(self):

        self.close()

    @property
    def conn(self) -> pymysql.Connection:
        """
        Get the connection to the database.
        """

        return self.__conn 

    @property
    def cursor(self) -> cursorType:
        """
        Get the cursor to the database.
        """

        return self.__conn.cursor() if self.__conn is not None else None

    def connect(self) -> None:
        """
        Connect to the database.

        :param use_db: Whether to use the database specified in the configuration.
        """

        if self.__conn is None:
            self.__conn = pymysql.connect(
                host=self.__config.host,
                user=self.__config.user,
                password=self.__config.password,
                database=self.__config.database,
                port=self.__config.port,
                charset=self.__config.charset,
                cursorclass=self.cursorType
            )

    def close(self) -> None:
        """
        Close the connection to the database.
        """

        if self.__conn is not None:
            self.__conn.close()
            self.__conn = None


def get_db() -> pymysql.Connection:
    """
    Get one database connection.

    This function comes from Flask.

    :return: The database connection.
    """

    if 'db' not in g:
        db = DatabaseConnector()
        db.connect()
        g.db = db.conn

    return g.db

def close_db() -> None:
    """
    Close the database connection.

    This function comes from Flask.
    """

    db = g.pop('db', None)
    if db is not None:
        db.close()
