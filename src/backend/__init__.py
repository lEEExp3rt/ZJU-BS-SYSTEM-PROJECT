"""
This file builds the Flask app instance and sets up the configuration.
"""

from flask import Flask


def create_app() -> Flask:
    """
    Get the whole app instance.

    :return: The Flask app instance.
    """

    # Create the Flask app instance
    app = Flask(__name__)

    # Load the configuration
    app.config.from_object() # TODO

    # TODO
    #from .utils.AppInitializer import init_app
    #init_app(app)

    # Register the blueprints
    # TODO
    from .routes.authentication import Authenticator
    app.register_blueprint(Authenticator.auth)

    return app
