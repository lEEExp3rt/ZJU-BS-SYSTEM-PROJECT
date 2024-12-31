"""
This module is used to establish a connection to the database.

:version: 0.11.0

Wrap all the database operations in this module to make it easier to maintain and use.

:version: 0.8.0

Use `get_conn()` and `close_conn()` to get a database connection and release the resources rather than creating a new instance every time.

:version: 0.7.0

First load the configuration of the database when constructing, then use `connect()` to establish a connection to the database.

After connection, you can use the `conn` to interact with the database.

And don't forget to close the connection using `close()` to release the resources!

"""

import pymysql


class DatabaseConnector():
    """
    Database connector.

    Use this class to establish a connection to the database and do operations on the database.
    """

    def __init__(self, host: str, port: int, user: str, password: str, database: str, charset: str):

        self.__host: str = host
        self.__port: int = port
        self.__user: str = user
        self.__password: str = password
        self.__database: str = database
        self.__charset: str = charset
        self.__conn: pymysql.Connection = None

    @property
    def is_connected(self) -> bool:
        """
        If the database is connected.
        """

        return self.__conn is not None

    def connect(self, host: str = None, port: int = None, user: str = None, password: str = None, database: str = None, charset: str = None) -> None:
        """
        Connect to the database.

        If the parameters are not provided, use the parameters loaded from the configuration.
        """

        if not self.is_connected:
            self.__conn = pymysql.connect(
                host=self.__host if host is None else host,
                user=self.__user if user is None else user,
                password=self.__password if password is None else password,
                database=self.__database if database is None else database,
                port=self.__port if port is None else port,
                charset=self.__charset if charset is None else charset,
                autocommit=False
            )

    def close(self) -> None:
        """
        Close the connection to the database.
        """

        if self.is_connected:
            try:
                self.__conn.close()
                self.__conn = None
            except pymysql.err.Error:
                pass
    
    def execute(self, sql: str, params: tuple = None):
        """
        Execute the sql statement with the given parameters.

        Please make sure that the database is connected before calling this function.

        :param sql: The sql statement to be executed.
        :param params: The parameters to be used in the sql statement.

        :return: The result of the sql statement. If the sql statement is a SELECT statement, return the result set. Otherwise, return the number of affected rows.
        """

        is_select = sql.strip().upper().startswith("SELECT") == True
        with self.__conn.cursor() as cursor:
            try:
                cursor.execute(sql, params)

                if is_select:
                    return cursor.fetchall()
                else:
                    self.__conn.commit()
                    return cursor.rowcount
            except pymysql.MySQLError as e:
                if not is_select:
                    self.__conn.rollback()
                raise e

def close_db(e=None) -> None:
    """
    Close the database connection.

    This function comes from Flask.
    """

    from backend import db
    db.close()
