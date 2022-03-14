from flask import Flask
from src.DataController.customerService import ct_service




def create_app():
    app = Flask(__name__)
    app.register_blueprint(ct_service)
    return app
    