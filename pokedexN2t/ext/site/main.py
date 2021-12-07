from flask import Blueprint, request, render_template, current_app
from pokedexN2t.ext.api.service import request_pokemon
from pokedexN2t.ext.site.utils import TypePokemon


bp = Blueprint("site",__name__)

@bp.get('/')
def index():
    # faz mais sentido utilizar esse debbug
    object_pokemon = request_pokemon(request.args.get('nome', default='mudkip'))
    type_pokemon = object_pokemon['type']
    color_theme = TypePokemon[type_pokemon].value
    object_pokemon['color_theme'] = color_theme

    return render_template('index.html',object_pokemon=object_pokemon)

