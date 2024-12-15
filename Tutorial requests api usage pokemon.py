import requests


base_url="https://pokeapi.co/api/v2"

def get_pokemon(name):
    url=f"{base_url}/pokemon/{name}"
    response=requests.get(url)
    

    if response.status_code==200:
        pokemon_data=response.json()
        print(f"{pokemon_data['name']} and {name}")
    else:
        print(f"not found,{response.status_code}")

pokemans='pichu'

get_pokemon=get_pokemon(pokemans) 

#### number 2 

import requests
base_url="https://pokeapi.co/api/v2"

def get_pokemon(name):
    url=f"{base_url}/pokemon/{name}"
    response=requests.get(url)

    if response.status_code==200:
        pokemon_data=response.json()
        return pokemon_data
    else:
        print("not found")

pokemans='pikachu'

get_pokemon=get_pokemon(pokemans)


if get_pokemon:
   
   print(f"{get_pokemon['name']}")
   print(f"{get_pokemon['id']}")
   print(f"{get_pokemon['height']}")


