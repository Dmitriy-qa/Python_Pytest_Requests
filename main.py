import requests
token = 'edece32d80d32185b21cd3c487529e94'
response = requests.post('https://api.pokemonbattle.me:9104/pokemons', json = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers={'Content-Type': 'application/json',
            'trainer_token': token})
print(response.text)

response2 = requests.put('https://api.pokemonbattle.me:9104/pokemons', json = {
    "pokemon_id": "11214",
    "name": "New Name1",
    "photo": "https://dolnikov.ru/pokemons/albums/007.png"
}, headers={'Content-Type': 'application/json',
            'trainer_token': token})
print(response2.text)

response3 = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball', json = {
    "pokemon_id": "11214"
}, headers={'Content-Type': 'application/json',
            'trainer_token': token})
print(response3.text)

print(response.status_code)