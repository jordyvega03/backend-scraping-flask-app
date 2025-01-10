from flask import Flask
from .routes import api_routes

def create_app():
    app = Flask(__name__)

    # Cargar configuraciones desde config.py
    app.config.from_object("config.Config")

    # Registrar rutas
    app.register_blueprint(api_routes, url_prefix="/api")

    return app
