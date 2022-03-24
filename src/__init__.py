from flask import Flask
from src.services.customer_service import ct_service
from src.services.booking_service import booking_service
from src.services.admin_service import admin_service
from src.services.demo_service import demo_service
from src.services.seat_service import seat_service

def create_app():
    app = Flask(__name__)
    app.register_blueprint(ct_service)
    app.register_blueprint(booking_service)
    app.register_blueprint(admin_service)
    app.register_blueprint(demo_service)
    app.register_blueprint(seat_service)
    
    return app
    