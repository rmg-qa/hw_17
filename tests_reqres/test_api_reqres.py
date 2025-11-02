import requests
from jsonschema import validate
from schemas.shemas import create_users, login_users, register_successful, put_users
import helpers

"""
Часть № 1: Написать API-тесты на каждый из методов: GET, POST, PUT, DELETE
"""


def test_get_users():
    request = requests.get('https://reqres.in/api/users',
                           headers={"x-api-key": "reqres-free-v1"},
                           params={"page": 2})
    assert request.status_code == 200


def test_post_create_user():
    request = requests.post('https://reqres.in/api/users',
                            headers={"x-api-key": "reqres-free-v1"},
                            json={"name": helpers.fake_data_user()[0], "job": helpers.fake_data_user()[2]})
    body = request.json()
    assert request.status_code == 201
    validate(body, schema=create_users)


def test_put_user():
    request = requests.put('https://reqres.in/api/users/2',
                           headers={"x-api-key": "reqres-free-v1"},
                           json={"name": helpers.fake_data_user()[0], "job": helpers.fake_data_user()[2]})
    body = request.json()
    assert request.status_code == 200
    validate(body, schema=put_users)


def test_delete_user():
    request = requests.delete('https://reqres.in/api/users/2',
                              headers={"x-api-key": "reqres-free-v1"})
    assert request.status_code == 204


"""
Часть № 2: Позитивные/Негативные тесты на одну из ручек.
"""


## Создам только негативный тест, так как позитивный был сделан в 1 части задания.
## Этот тест по идеи должен упасть, так как ключ "name" back-end обычно валидирует только на передачу
# типа данных = str. В этом сервисе вообще нет валидаци на значения параметров, которые передаются в json


def test_negative_create_user():
    request = requests.post('https://reqres.in/api/users',
                            headers={"x-api-key": "reqres-free-v1"},
                            json={"name": 1, "job": helpers.fake_data_user()[2]})
    assert request.status_code == 400


"""
Часть № 3: Написать тесты на разные статус-коды 200/201/204/404/400
"""


## Тесты со статус-кодом: 200, 201, 204 есть в 1 части задания.


def test_error_404():
    request = requests.get('https://reqres.in/api/users/23',
                           headers={"x-api-key": "reqres-free-v1"})
    assert request.status_code == 404


def test_error_400():
    request = requests.post('https://reqres.in/api/register',
                            headers={"x-api-key": "reqres-free-v1"},
                            json={"email": helpers.fake_data_user()[1]})
    assert request.status_code == 400


"""
Часть № 4: Написать тесты на разные схемы (4-5 схем)
"""


## 2 теста со схемами есть в 1 части задания

def test_post_successful_register():
    request = requests.post('https://reqres.in/api/register',
                            headers={"x-api-key": "reqres-free-v1"},
                            json={"email": "eve.holt@reqres.in", "password": "pistol"})
    body = request.json()
    assert request.status_code == 200
    validate(body, schema=register_successful)


def test_successful_login():
    request = requests.post('https://reqres.in/api/login',
                            headers={"x-api-key": "reqres-free-v1"},
                            json={"email": "eve.holt@reqres.in", "password": "cityslicka"})
    body = request.json()
    assert request.status_code == 200
    validate(body, schema=login_users)


"""
Часть № 5: C ответом и без ответа
"""


## Тут насколько я понял, нужно написать тесты с телом ответа, и без тела ответа. С телом ответа есть в 1 части
## задания, добавлю только тест с пустым json


def test_empty_body_response_json():
    request = requests.get('https://reqres.in/api/users/23',
                           headers={"x-api-key": "reqres-free-v1"})
    assert request.json() == {}


"""
Часть №6: тест на бизнес-логику (заметить какую-то фичу и автоматизировать, как делали на уроке)
"""


## Автогенерируем name и job и проверяем в тесте, что это занчение нам и вернулось

def test_return_correct_fields_name_and_job():
    name = helpers.fake_data_user()[0]
    job = helpers.fake_data_user()[2]
    request = requests.post('https://reqres.in/api/users',
                            headers={"x-api-key": "reqres-free-v1"},
                            json={"name": name, "job": job})
    body = request.json()
    assert request.json()['name'] == name
    assert request.json()['job'] == job
    validate(body, schema=create_users)
