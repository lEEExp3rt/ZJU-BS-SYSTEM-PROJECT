"""
This module is used to initialize the Flask app.
"""

from backend.database.DatabaseInitializer import init_db_command
from backend.database.DatabaseConnector import close_db
from flask import Flask


def init_app(app: Flask) -> None:
    """
    Initializes the Flask app.
    """

    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
