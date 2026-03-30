from test.data.json_for_authorization import json_for_autorization


class TestUserAuthorization:
    def test_user_authorization(self, api_authorization):
        response = api_authorization.autorization_user(
            json_for_autorization["email"], json_for_autorization["password"]
        )
        data_json = response.json()
        assert response.status_code == 200
        assert isinstance(data_json, dict)
        assert len(data_json["token"]) == 125

    def test_user_invalid_authorization(self, api_authorization):
        response = api_authorization.autorization_user("непочта", "непарль")
        data_json = response.json()
        assert response.status_code == 401
        assert isinstance(data_json, dict)
        assert (
            data_json["message"]
            == "Ошибка авторизации... Пожалуйста, проверь почту или пароль"
        )
