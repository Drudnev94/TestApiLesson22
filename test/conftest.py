import requests
import pytest
from test.base_api_docs import BaseApiDocs


# Импорт базового класса
@pytest.fixture
def api_user():
    return BaseApiDocs()


# Получение токена
@pytest.fixture
def token(api_user):
    response = requests.post(
        f"{api_user.BASE_URL}{api_user.ENDPOINT_LOGIN}",
        headers=api_user.HEADERS,
        json=api_user.PAYLOAD_FOR_TOKEN,
    )
    response_json = response.json()
    token = response_json["token"]
    return token


# Получаем первый id  в списке заметок
@pytest.fixture
def get_id_docs(api_user, token):
    headers = api_user.HEADERS_DOCS1 | {"Authorization": f"Bearer {token}"}
    response = requests.get(
        f"{api_user.BASE_URL}{api_user.ENDPOINT_DOCS}", headers=headers
    )
    response_data = response.json()
    id_docs = response_data[0]["id"]
    return id_docs
