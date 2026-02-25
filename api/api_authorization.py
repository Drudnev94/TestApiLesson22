from api.base_api import BaseApi
from test.data.json_for_authorization import JsonForAuthorization


class ApiAuthorization(BaseApi):
    ENDPOINT = "/api/login"


    def autorization_user(self):
        response_autorization = self.metod_request(method="POST", json=JsonForAuthorization.data_authorization)
        return response_autorization


    def get_token(self):
        token_data = self.autorization_user()
        return token_data.json()["token"]

