import pytest

URL = "/auth/register"


def test_register(not_auth_test_client):
    data = {
        "email": "example1@example.com",
        "password": "exampleexampleexample",
    }
    response = not_auth_test_client.post(URL, json=data)
    assert (
        response.status_code == 201
    ), "При регистрации с валидными данными ожидается ответ со статусом 201"


@pytest.mark.parametrize(
    "email, password",
    [
        ("qwe@qwe.ru", ""),
        ("qwe1@qwe.ru", "q"),
        ("qwe1@qwe.ru", "q2"),
    ],
)
def test_len_password(test_client, email, password):
    data = {
        "email": email,
        "password": password,
    }
    response = test_client.post(URL, json=data)
    assert (
        response.status_code == 400
    ), "Убедитесь , что пароль не может быть короче 3 символов или пустым"


@pytest.mark.parametrize(
    "email, password",
    [
        ("qwe@qwe.ru", "qwe@qwe.ru"),
    ],
)
def test_login_password(test_client, email, password):
    data = {
        "email": email,
        "password": password,
    }
    response = test_client.post(URL, json=data)
    assert (
        response.status_code == 400
    ), "Убедитесь , что пароль не может содержать логин"
