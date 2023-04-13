import json.decoder

import requests



base_url = "https://petfriends.skillfactory.ru/"

def get_login(user, password):
    headers = {
        'email' : user,
        'password': password
    }

    response = requests.get(base_url + 'api/key', headers=headers)
    status_code = response.status_code
    token = {'key':'value'}
    try:
        token = response.json()
    except json.decoder.JSONDecodeError:
        token = response.text
    for key,value in token.items():
        token = value
    return status_code, token

def get_login_with_bad_request(user, password):
    headers = {
        'email' : user,
        'password': password
    }

    response = requests.get(base_url + 'api/key', headers=headers)
    status_code = response.status_code
    token = {'key':'value'}
    try:
        token = response.json()
    except json.decoder.JSONDecodeError:
        token = response.text
    return status_code, token

def post_create_pet_simple(token, name, type, y_old):
    headers = {
        'auth_key' : token
    }
    body = {
        'name' : name,
        'animal_type' : type,
        'age' : y_old
    }

    response = requests.post(base_url+'api/create_pet_simple', headers=headers, json=body)
    status_code = response.status_code
    try:
        result = response.json()
    except json.decoder.JSONDecodeError:
        result = response.text
    return status_code, result

def get_all_pets(token, filter):
    headers = {
        'auth_key': token
    }

    filter = {
        'filter': filter
    }

    response = requests.get(base_url + '/api/pets', headers=headers, params=filter)
    status_code = response.status_code
    try:
        result = response.text
    except json.decoder.JSONDecodeError:
        result = response.json()
    return status_code, result