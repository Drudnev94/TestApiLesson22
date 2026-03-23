from api.base_api import BaseApi
from test.data.json_for_registration import data_for_registration


class ApiRegistretion(BaseApi):
    ENDPOINT = "/api/register"
    data_user = data_for_registration

    def register_user(
        self,
        email=data_user["email"],
        password=data_user["password"],
        username=data_user["username"],
    ):
        """Данные для регистрации по умолчанию из data_for_registration"""
        data_json = {
            "email": email,
            "password": password,
            "username": username,
        }
        respose_registration = self._request(method="POST", json=data_json)
        return respose_registration
