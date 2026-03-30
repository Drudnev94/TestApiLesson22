from api.base_api import BaseApi
from test.data.json_for_authorization import json_for_autorization


class ApiAuthorization(BaseApi):
    ENDPOINT = "/api/login"

    def autorization_user(self, login, password):
        """Авторизация пользователя с указанием данных, по умолчанию данные: json_for_autorization"""
        json = {"email": login, "password": password}
        response_autorization = self._request(method="POST", json=json)
        return response_autorization

    def get_token(self):
        """Получаем валидный токен,данные авторизации из json_for_autorization"""
        token_data = self.autorization_user(
            json_for_autorization["email"], json_for_autorization["password"]
        )
        return token_data.json()["token"]
