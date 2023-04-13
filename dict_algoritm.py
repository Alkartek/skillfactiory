def dict_token(response):
    f = open('result_json.py', 'a+')
    f.write(f"token_with_key = {response.json()}\n")
    f.close()

def token_alg(dict):
    for key,value in dict.items():
        return value

def token_without_json(token):
    f = open('result_json.py', 'a+')
    f.write(f"token_clear = '{token}'\n")
    f.close()