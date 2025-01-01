"""
This module defines the Budget Bee Application class.

This is a wrapper class.
"""

from app import configs
from app.database.DatabaseConnector import close_db
from app.database.DatabaseInitializer import init_db

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
            template_folder=configs.app_template_path,
            static_folder=configs.app_static_path
        )

        # Set the configuration for the Flask app.
        self.__app.config.from_mapping(
            SECRET_KEY="dev"
        )

        # Initialize the application.
        self.__app.teardown_appcontext(close_db)

        # Register the blueprints.
        from .views import index, authentication, home
        self.__app.register_blueprint(index.index_bp)
        self.__app.register_blueprint(authentication.auth)
        self.__app.register_blueprint(home.home_bp)
    
    def init_app(self):
        """
        Initialize the application.

        Database will be initialized here.
        """

        init_db()

    def run(self, host: str = configs.runtime_host, port: int = configs.runtime_port, debug=False):
        """
        Run the Flask app.

        :param host: The host to run the app on. If not specified, it will use the default value loaded from the config.
        :param port: The port to run the app on. If not specified, it will use the default value loaded from the config.
        :param debug: Whether to run in debug mode. Default is False.
        """

        self.__app.run( host=host, port=port, debug=debug)
