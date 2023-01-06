import json
from http import HTTPStatus

from Framework.API_Colections.users_api import Users
from Framework.data_classes.user import User


def test_get_user_by_id():
    responce = Users().get_user_by_id(2)
    assert responce.status_code == HTTPStatus.OK


def test_invalid_user_id():
    response = Users().get_user_by_id(1222222)
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user():
    responce = Users().delete_user(1)
    assert responce.status_code == HTTPStatus.NO_CONTENT


def test_create_user():
    response = Users().create_user({"name": "morpheus", "job": "leader"})
    assert response.status_code == HTTPStatus.CREATED


def test_user_data(create_user):
    expected_user = create_user
    response = Users().get_user_by_id(3)
    user_data = json.loads(response.text)
    actual_user = User.from_json(**user_data)
    assert actual_user == expected_user


def test_user_page():
    response = Users().get_users_page(2)
    assert response.status_code == HTTPStatus.OK


def test_update_user_data():
    response = Users().put_user_data(2, {"name": "morpheus", "job": "zion resident"})
    assert response.status_code == HTTPStatus.OK
