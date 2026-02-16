import requests
from test.base_api_docs import BaseApiDocs
from test.payload_generator import PayloadGenerator

class TestCreateDocs(PayloadGenerator):
    def test_register_user(self):
        self.payload = PayloadGenerator().get_user_paylod()
        responce = requests.post(f"{self.BASE_URL}{self.ENDPOINT_REGISTER}",
        headers=self.HEADERS,
        json= self.payload)
        print(responce.json())
        assert responce.status_code == 201
