
class Test_User_Registration:

    def test_user_registration(self, api_registration):
        response = api_registration.register_user()
        data_json = response.json()
        assert response.status_code == 201
        assert data_json is not None
        assert data_json == {'message': 'Успешная регистрация!'}
