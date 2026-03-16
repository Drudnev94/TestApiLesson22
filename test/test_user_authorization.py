from test.conftest import api_authorization

class TestUserAuthorization:
    def test_user_authorization(self, api_authorization, token):
        response = api_authorization.autorization_user()
        data_json = response.json()
        assert response.status_code == 200
        assert len(data_json["token"]) == 125