from test.data.json_for_registration import data_for_registration


class Test_User_Registration:

    def test_user_registration(self, api_registration):
        """Регистрация пользователя"""
        response = api_registration.register_user(
            data_for_registration["email"],
            data_for_registration["password"],
            data_for_registration["username"],
        )
        data = response.json()
        assert response.status_code == 201
        assert isinstance(data, dict)
        assert data["message"] == "Успешная регистрация!"

    def test_user_re_registration(self, api_registration):
        """Повторная регистрация пользователя"""
        response = api_registration.register_user(
            data_for_registration["email"],
            data_for_registration["password"],
            data_for_registration["username"],
        )
        data = response.json()
        assert response.status_code == 409
        assert isinstance(data, dict)
        assert data["message"] == "Пользователь с таким email уже существует"

    def test_user_invalid_registration(self, api_registration):
        """Невалидные данные запроса"""
        response = api_registration.register_user(1, 2, 3)
        assert response.status_code == 500
