
class Test_User_Registration:

    def test_user_registration(self, api_registration):
        response = api_registration.register_user()
        data_response = response.json()
        print(data_response)
        print(response.status_code)
        assert response.status_code == 201