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
    print(os.path.abspath(config.instance_path))
    app = Flask(__name__, instance_path=os.path.abspath(config.instance_path))
    app.config.from_object(config)

    from .utils import AppInitializer
    AppInitializer.init_app(app)

    # Register the blueprints
    # TODO
    #from .routes.authentication import Authenticator
    #app.register_blueprint(Authenticator.auth)

    @app.route('/')
    def index():
        return "Hello, World!"

    return app
