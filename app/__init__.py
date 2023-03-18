
from flask import Flask

from .blueprints.shop import shop #Aquí importamos el blueprint 

from .config import Config

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    app.register_blueprint(shop)

    return app