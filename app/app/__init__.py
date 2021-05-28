"""
__init__.py: Flask server with Deep Learning model.
"""

__author__      = "pabloguinea"
__copyright__   = "Copyright 2021"


from flask import Flask, render_template

from config import config
from .model import init_model
from flask_cors import CORS, cross_origin
from flask import json
from .exceptions import InvalidRequest

def create_app(config_name="default"):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    with app.app_context():
        app.config["model"] = init_model(app.config["MODEL_PATH"])
        

    from .api import api
    app.register_blueprint(api, url_prefix="/model")

    #app.register_error_handler(InvalidRequest, handle_507)

    """
    @app.route("/dlflask", methods=["GET"])
    def dlflask():
        return render_template("dlflask.html")

    @app.route("/", methods=["GET"])
    def index():
        return "App"

    """

    return app


    