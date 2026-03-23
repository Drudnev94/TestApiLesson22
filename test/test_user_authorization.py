from test.conftest import api_authorization


class TestUserAuthorization:
    def test_user_authorization(self, api_authorization, token):
        """Возможно указать кастомные данные для регистрации: email, password"""
        response = api_authorization.autorization_user()
        data = response.json()
        assert response.status_code == 200
        assert isinstance(data, dict)
        assert data["token"] is not None
        assert len(data["token"]) == 125
        assert "token" in data, "ERROR: token is not data"
