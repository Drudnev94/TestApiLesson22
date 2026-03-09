
class TestGetNotes:

    def test_get_notes(self, api_get_notes,setup_teardown_note):
        response = api_get_notes.get_all_note()
        data_response = response.json()
        print(data_response)
        assert response.status_code == 200
        assert len(data_response) > 0


    def test_get_notes_witsh_invalid_token(self, invalid_token):
        response = invalid_token.get_all_note()
        data_response = response.json()
        print(data_response)
        assert response.status_code == 403