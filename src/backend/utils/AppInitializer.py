"""
This module is used to initialize the Flask app.

:DeprecationWarning:
    This module is deprecated and will be removed in the future.
"""

from backend.database.DatabaseInitializer import init_db_command
from backend.database.DatabaseConnector import close_conn
from flask import Flask
import os


def init_app(app: Flask) -> None:
    """
    Initializes the Flask app.
    """

    app.teardown_appcontext(close_conn)
    app.cli.add_command(init_db_command)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
