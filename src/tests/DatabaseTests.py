"""
This is the test suite for the database module.
"""

from backend.database.DatabaseConnector import db

def test_db():
    """
    Test the database functionalities.
    """

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