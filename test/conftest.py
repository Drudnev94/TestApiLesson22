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


@pytest.fixture
def create_and_cleaen_docs(api_user, token):
    """Создаю новую заметку"""
    headers_post = (
        api_user.HEADERS_DOCS
        | api_user.HEADERS_DOCS1
        | {"Authorization": f"Bearer {token}"}
    )
    response_post = requests.post(
        url=f"{api_user.BASE_URL}{api_user.ENDPOINT_DOCS}",
        headers=headers_post,
        json=api_user.BODY_DOCS_POST,
    )
    response_post.raise_for_status()
    body_post = response_post.json()
    print(f"Создана Заметка {body_post} ")

    """Получаю ее id через гет запрос"""

    headers_get = api_user.HEADERS_DOCS1 | {"Authorization": f"Bearer {token}"}
    response_get = requests.get(
        f"{api_user.BASE_URL}{api_user.ENDPOINT_DOCS}", headers=headers_get
    )
    response_get.raise_for_status()

    data_id = response_get.json()
    id_docs = data_id[0]["id"]
    print(f"ID заметки получен: {id_docs}")

    """Удяляю созданную заметку"""
    yield id_docs

    headers_del = api_user.HEADERS_DOCS1 | {"Authorization": f"Bearer {token}"}
    response_del = requests.delete(
        f"{api_user.BASE_URL}{api_user.ENDPOINT_DOCS}{id_docs}", headers=headers_del
    )
    print(f"Заметка c ID {id_docs} удалена")
