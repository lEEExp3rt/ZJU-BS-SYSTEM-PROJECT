"""
This file is used to establish a connection to the database.
"""

from ConnectConfig import ConnectConfig
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

        self.__config = config
        self.__conn = None
    
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
    
    def getCursor(self) -> pymysql.cursors.Cursor:
        """
        Get a cursor to the connected database.
        """

        return self.__conn.cursor(self.cursorType)
    
    def connect(self) -> None:
        """
        Connect to the database.
        """

        if self.__conn is None:
            try:
                self.__conn = pymysql.connect(host=self.__config.host,
                                              user=self.__config.user,
                                              password=self.__config.password,
                                              database=self.__config.database,
                                              port=self.__config.port,
                                              charset=self.__config.charset,
                                              cursorclass=self.cursorType)
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
    
    def commit(self):
        raise NotImplementedError()

if __name__ == '__main__':
    db = DatabaseConnector(ConnectConfig())
    db.connect()
    cursor = db.getCursor()
    cursor.execute("select version()")
    print(cursor.fetchone())
    db.close()