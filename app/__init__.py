
from flask import Flask

from .blueprints.shop import shop #Aquí importamos el blueprint 



def create_app():

    app = Flask(__name__)

    app.register_blueprint(shop)

    return app