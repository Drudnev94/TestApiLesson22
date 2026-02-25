from test.data.json_for_registration import JsonForRegistration
from api.base_api import BaseApi


class ApiRegistretion(BaseApi):
    ENDPOINT = "/api/register"

    def register_user(self):
        respose_registration = self.metod_request(
            method="POST", json=JsonForRegistration.data_for_registration
        )
        return respose_registration
