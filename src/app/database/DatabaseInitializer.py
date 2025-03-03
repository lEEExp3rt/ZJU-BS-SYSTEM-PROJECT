"""
This module is used to initialize the database.
"""

from app import db

import os
import pymysql


db_initializer = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'configs', 'DBInitializer.sql')

def init_db():
    """
    Initialize the database and clear all the existing data.
    """

    try:
        with open(db_initializer, 'r') as f:
            script = f.read()

            # Connect to the database.
            if not db.is_connected:
                db.connect(database='')

            # Execute the SQL script.
            sqls = script.split(';')
            for sql in sqls:
                if sql.strip():
                    db.execute(sql)

    except FileNotFoundError:
        raise FileNotFoundError(f"Database initializer script {db_initializer} not found.")
    except pymysql.MySQLError as e:
        raise e
