"""
This module is used to establish a connection to the database.

:version: 0.8.0

Use `get_conn()` and `close_conn()` to get a database connection and release the resources rather than creating a new instance every time.

:version: 0.7.0

First load the configuration of the database when constructing, then use `connect()` to establish a connection to the database.

After connection, you can use the `conn` to interact with the database.

And don't forget to close the connection using `close()` to release the resources!

"""

import pymysql.cursors
import pymysql
from flask import g, current_app


class DatabaseConnector:
    """
    Database connector.

    Use this class to establish a connection to the database and do operations on the database.
    """

    cursorType = pymysql.cursors.Cursor

    def __init__(self, config):

        self.__config = config
        self.__conn: pymysql.Connection = None

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
                host=self.__config['DB_HOST'],
                user=self.__config['DB_USER'],
                password=self.__config['DB_PASSWORD'],
                database=self.__config['DB_DATABASE'],
                port=self.__config['DB_PORT'],
                charset=self.__config['DB_CHARSET'],
                cursorclass=self.cursorType
            )

    def close(self) -> None:
        """
        Close the connection to the database.
        """

        if self.__conn is not None:
            self.__conn.close()
            self.__conn = None


def get_conn() -> pymysql.Connection:
    """
    Get one database connection.

    If the database connection is not established, establish a new connection, otherwise return the existing connection.

    :return: The database connection.
    """

    if 'db' not in g:
        db = DatabaseConnector(current_app.config)
        db.connect()
        g.db = db.conn

    return g.db

def close_conn(e=None) -> None:
    """
    Close the database connection.

    This function comes from Flask.
    """

    db = g.pop('db', None)
    if db is not None:
        db.close()


""" New Version """

class databaseconnector():
    """
    Database connector.

    Use this class to establish a connection to the database and do operations on the database.
    """

    def __init__(self):

        self.__conn: pymysql.Connection = None



# db = databaseconnector()
