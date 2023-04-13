import requests

import result_json
import urls
import api
import dict_algoritm
import pytest
import parametrize

headers = {
    "email": "qwertyuiop@mail.ru",
    "password":"qwertyuiop"
}

email = "qwertyuiop@mail.ru"
password = "qwertyuiop"

class Test_api:
    def test_get_login(self):
        response = requests.get(urls.urls_get_login, headers=headers)
        print(response)
        assert response.status_code == 200


    def test_get_method(self):
        code, token = api.get_login(email,password)
        assert code == 200
        assert token is not None
        dict_algoritm.token_without_json(token)
        print(token)


    def test_get_method_is_not_true(self):
        code, token = api.get_login_with_bad_request(email, None)
        assert code == 403
        assert "This user wasn&#x27" in token

    @pytest.mark.parametrize('namess, typess, years_oldss', parametrize.dog_parametrize)
    def test_post_add_new_animal_without_photo(self, namess, typess, years_oldss):
        code, result = api.post_create_pet_simple(result_json.token_clear, namess, typess, years_oldss )
        assert code == 200
        assert 'id' in result

    def test_get_all_pets(self):
        code, result = api.get_all_pets(result_json.token_clear, 'my_pets')
        assert code == 200
        assert 'pets' in result




