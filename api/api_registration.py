from api.base_api import BaseApi
from test.helper import Helper

class ApiRegistretion(BaseApi):
    ENDPOINT = "/api/register"

    def register_user(self,email= Helper.email(),password= Helper.password(), username= Helper.username()):
        data_json = JsonForRegistration().data_for_registration(email,password,username)
        respose_registration = self._request(method="POST", json=data_json)
        return respose_registration
