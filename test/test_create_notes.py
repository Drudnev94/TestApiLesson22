
class TestCreateNote:
    def test_create_notes(self, api_post_notes,cleaning_after_creation):
        response = api_post_notes.create_notes()
        data_response = response.json()
        print(data_response)
        assert response.status_code == 201
        assert response.json().get("message") == "Заметка создана!"
        assert len(response.json())  == 1