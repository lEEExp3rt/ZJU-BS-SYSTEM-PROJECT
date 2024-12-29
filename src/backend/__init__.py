"""
This file builds the Flask app instance and sets up the configuration.
"""

from . import Configs
from flask import Flask
import os


def create_app() -> Flask:
    """
    Get the whole app instance.

    :return: The Flask app instance.
    """

    # Load the configuration.
    config = Configs.Config()

    # Create the Flask app instance
    app = Flask(
        import_name="BudgetBEE",
        instance_path=os.path.abspath(config.instance_path),
        template_folder=os.path.abspath("src/backend/templates"),
        static_folder=os.path.abspath("src/backend/static")
    )

    app.config.from_mapping(
        SECRET_KEY='dev'
    )
    app.config.from_object(config)

    # Initialize the app.
    from .utils import AppInitializer
    AppInitializer.init_app(app)

    # Register the blueprints.
    from .views import authentication
    app.register_blueprint(authentication.auth)

    @app.route('/')
    def index():
        return "Hello, World!"

    return app
