from flask import Flask

from pokedexN2t.ext import api
from pokedexN2t.ext import site

def create_app():
    app = Flask(__name__)

    api.init_app(app)
    site.init_app(app)
    
    return app