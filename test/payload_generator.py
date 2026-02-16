from test.base_api_docs import BaseApiDocs


class PayloadGenerator(BaseApiDocs):
    def get_user_paylod(self):
        return {
            "email": self.EMAIL,
            "password": self.PASSWORD,
            "username": self.USERNAME,
        }
