"""
This is the test suite for the database module.
"""

from backend.database.DatabaseConnector import DatabaseConnector
from backend.Configs import Config

def test_db():
    """
    Test the database functionalities.
    """

    config = Config()
    db = DatabaseConnector(
        host=config.db_host,
        port=config.db_port,
        user=config.db_user,
        password=config.db_password,
        database=config.db_database,
        charset=config.db_charset
    )

    db.connect()
    result = db.execute("SELECT * from users")
    for row in result:
        print(row)
    db.close()

    db.connect()
    db.execute(
        "insert into `users` (`user_name`, `password`, `email`, `create_time`) values (%s, %s, %s, now())",
        ("qqq", "123456", "<EMAIL>",)
    )
    db.close()

    db.connect()
    result = db.execute("SELECT * from users")
    for row in result:
        print(row)
    db.close()

    print("Database tests passed!")

if __name__ == '__main__':
    test_db()