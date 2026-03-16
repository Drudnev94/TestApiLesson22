from api.base_api import BaseApi
from test.data.json_for_authorization import JsonForAuthorization


class ApiAuthorization(BaseApi):
    ENDPOINT = "/api/login"

    def autorization_user(self,login = "dimaru123@example.su",password = "q1w232e3"):
        data_json =  JsonForAuthorization().get_data_autorization(login, password)
        response_autorization = self._request(method="POST", json=data_json)
        return response_autorization


    def get_token(self):
        token_data = self.autorization_user()
        return token_data.json()["token"]
