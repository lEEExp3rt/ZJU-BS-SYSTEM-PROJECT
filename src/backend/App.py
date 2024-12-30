"""
This module defines the Budget Bee Application class.

This is a wrapper class.
"""

from backend import configs, db, email_manager
from backend.database.DatabaseConnector import close_db
from backend.database.DatabaseInitializer import init_db

import os
from flask import Flask


class APP:
    """
    Budget Bee Application class.
    """

    def __init__(self):
        """
        Load all the configurations.
        """

        self.__app = Flask(
            import_name=configs.app_name,
            instance_path=os.path.abspath(configs.instance_path),
            template_folder=os.path.abspath("src/backend/templates"),
            static_folder=os.path.abspath("src/backend/static")
        )

        # Set the configuration for the Flask app.
        self.__app.config.from_mapping(
            SECRET_KEY="dev"
        )

        # Initialize the application.
        self.__app.teardown_appcontext(close_db)

        # Register the blueprints.
        from .views import authentication
        self.__app.register_blueprint(authentication.auth)
    
    def init_app(self):
        """
        Initialize the application.

        Database will be initialized here.
        """

        init_db()

    def run(self, debug=False):
        """
        Run the Flask app.

        :param debug: Whether to run in debug mode.
        """

        self.__app.run(debug=debug)
