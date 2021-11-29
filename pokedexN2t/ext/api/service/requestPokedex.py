import requests

def request_pokemon(pokemon: str)-> dict:
    try:
        request = requests.get(
                                f'https://pokeapi.co/api/v2/pokemon/{pokemon}/'
                                )
        response = request.json()
        gif_pokemon = get_gif(response)
        print(gif_pokemon)
        id_pokemon = get_id(response)
        name_pokemon = get_name(response)
        type_pokemon = get_type(response)

        pokemon_object = {}
        pokemon_object['gif'],pokemon_object['id'],pokemon_object['name'], pokemon_object['type'] = gif_pokemon, id_pokemon,name_pokemon, type_pokemon

        return pokemon_object 
    except Exception as e:
        return e

def get_gif(payload_pokemon: dict)-> str:
    gif_pokemon = payload_pokemon['sprites']['versions']['generation-v']['black-white']['animated']['front_default']
    return gif_pokemon

def get_id(payload_pokemon: dict)->str:
    return payload_pokemon['id']

def get_name(payload_pokemon: dict)->str:
    return payload_pokemon['name']

def get_type(payload_pokemon: dict)->str:
    return payload_pokemon['types'][0]['type']['name']