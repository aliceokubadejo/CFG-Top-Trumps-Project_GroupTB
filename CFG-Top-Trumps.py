import random
import requests
def user_pokemon():
    pokemon_card_number = random.randint(1,51)
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_card_number}/'
    response = requests.get(url)
    pokemon = response.json()


    return {
    'name': pokemon['name'],
    'id': pokemon['id'],
    'height': pokemon['height'],
    'weight': pokemon['weight'],
     }
