#!/usr/bin/env python
"""
This is the main file for the application server.
"""


def create_app():
    """
    Create the application instance.

    Returns:
                Flask: The Flask application instance.
    """
    from flask import Flask
    from app.routes import api

    app = Flask(__name__)
    app.register_blueprint(api, url_prefix="/api")
    app.url_map.strict_slashes = False

    return app
