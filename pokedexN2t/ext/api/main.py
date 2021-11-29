from flask import Blueprint, jsonify, request, redirect, url_for
from .service import request_pokemon

bp = Blueprint("api", __name__)

@bp.get('/pokedex')
def index_pokedex():
    try:
        object_pokemon = request_pokemon('bulbasaur')
        
        return jsonify(object_pokemon), 201
    except Exception as e:
        return jsonify({'error':e}), 500