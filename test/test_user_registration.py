class Test_User_Registration:

    def test_user_registration(self, api_registration):
        response = api_registration.register_user()
        """Возможно указать кастомные данные для регистрации: email,password,username"""
        data = response.json()
        assert response.status_code == 201
        assert isinstance(data, dict)
        assert len(data) > 0
        assert data is not None
        assert data == {"message": "Успешная регистрация!"}
        assert "message" in data, "ERROR: id is not data"
