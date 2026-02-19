import requests
from test.payload_generator import PayloadGenerator
from test.checks_api import Checks_Api


class TestCreateUser(PayloadGenerator):
    def test_register_user(self):
        response = requests.post(
            f"{self.BASE_URL}{self.ENDPOINT_REGISTER}",
            headers=self.HEADERS,
            json=self.PAYLOAD_CREATE,
        )
        status_code = response.status_code
        Checks_Api().assert_create_user(response, status_code, 201)

    def test_add_token_user(self):
        response = requests.post(
            f"{self.BASE_URL}{self.ENDPOINT_LOGIN}",
            headers=self.HEADERS,
            json=self.PAYLOAD_FOR_TOKEN,
        )
        response_data = response.json()
        status_code = response.status_code
        Checks_Api().assert_add_token_user(response, status_code, 200)
        print(f" Получен: {response_data}")

    def test_create_docs(self, token):  # мы передали сюда фиксутру  token
        headers = (
            self.HEADERS_DOCS
            | self.HEADERS_DOCS1
            | {"Authorization": f"Bearer {token}"}
        )  # Добовляем токен в хедеры
        response = requests.post(
            f"{self.BASE_URL}{self.ENDPOINT_DOCS}",
            headers=headers,
            json=self.BODY_DOCS_POST,
        )
        Checks_Api().assert_create_docs(response, response.status_code, 201)
        response_data = response.json()
        print(f"Body: : {response_data}")

    def test_get_docs(self, token, create_and_cleaen_docs):
        id_docs = create_and_cleaen_docs
        headers = self.HEADERS_DOCS1 | {"Authorization": f"Bearer {token}"}
        response = requests.get(f"{self.BASE_URL}{self.ENDPOINT_DOCS}", headers=headers)
        response_data = response.json()
        Checks_Api.assert_get_docs(response, 200)
        print(f"Boby: {response_data}")

    def test_delete_docs(self, token, get_id_docs):
        headers = self.HEADERS_DOCS1 | {"Authorization": f"Bearer {token}"}
        id = f"/{get_id_docs}"
        print(id)
        response = requests.delete(
            f"{self.BASE_URL}{self.ENDPOINT_DOCS}{id}", headers=headers
        )
        response_data = response.json()
        Checks_Api.assert_deelete_docs(response, 200)
        print(response_data)
