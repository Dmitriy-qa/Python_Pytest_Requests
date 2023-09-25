import requests
import pytest
token = 'edece32d80d32185b21cd3c487529e94'

def test_status_code():
    response = requests.get('https://api.pokemonbattle.me:9104/trainers',
    headers={'Content-Type': 'application/json',
                'trainer_token': token})
    assert response.status_code == 200
    print(response.text)

def test_traineer():
    response = requests.get('https://api.pokemonbattle.me:9104/trainers?trainer_id=2075',
    headers={'Content-Type': 'application/json',
                'trainer_token': token})
    assert response.json()['id'] == '2075'