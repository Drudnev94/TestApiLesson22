
class Test_User_Registration:

    def test_user_registration(self, api_registration):
        response = api_registration.register_user()
        data_response = response.json()
        assert response.status_code == 201
        assert data_response is not None
        assert data_response == {'message': 'Успешная регистрация!'}
