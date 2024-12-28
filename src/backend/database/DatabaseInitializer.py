"""
This module is used to initialize the database.
"""

from backend.utils.Configs import DatabaseConfig
import os
import pymysql
import click


db_initializer = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'DBInitializer.sql')

def init_db():
    """
    Initialize the database.

    Remember to call this function when first using the database, or any time you want to reset the database.
    """

    try:
        with open(db_initializer, 'r') as f:
            script = f.read()

            # Connect to the database.
            config = DatabaseConfig()
            conn = pymysql.connect(
                host=config.host,
                user=config.user,
                password=config.password,
                database=config.database,
                charset=config.charset
            )

            # Execute the SQL script.
            with conn.cursor() as cursor:
                sqls = script.split(';')
                for sql in sqls:
                    if sql.strip():
                        cursor.execute(sql)
                conn.commit()

    except FileNotFoundError:
        conn.rollback()
        raise FileNotFoundError(f"Database initializer script {db_initializer} not found.")
    except pymysql.MySQLError as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

@click.command('init-db')
def init_db_command():
    """
    Initialize the database in CLI.
    """

    init_db()
    click.echo('Database initialized.')
