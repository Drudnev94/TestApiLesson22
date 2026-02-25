from test.data.conftest import api_authorization


class Test_Api:

    def test_user_registration(self,api_registration):
        response = api_registration.register_user()
        data_response = response.json()
        print(data_response)
        print(response.status_code)
        assert response.status_code == 201

    def test_user_authorization(self,api_authorization,token):
        response = api_authorization.autorization_user()
        data_response = response.json()
        print(data_response)
        assert response.status_code == 200


    def test_create_notes(self,api_post_notes):
        response = api_post_notes.create_notes()
        data_response = response.json()
        print(data_response)
        assert response.status_code == 201

    def test_get_notes(self,api_get_notes):
        response = api_get_notes.get_all_note()
        data_response = response.json()
        print(data_response)
        assert response.status_code == 200

    def test_get_notes_witsh_invalid_token(self,invalid_token):
         response = invalid_token.get_all_note()
         data_response = response.json()
         print(data_response)
         assert response.status_code == 403

    def test_delete_notes(self,api_delete_notes):
        response = api_delete_notes.delete_notes()
        data_response = response.json()
        print(data_response)
        assert response.status_code == 200



