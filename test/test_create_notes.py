
class TestCreateNote:
    def test_create_notes(self, api_post_notes,cleaning_after_creation, api_get_id_notes):
        response = api_post_notes.create_notes()
        assert response.status_code == 201
        assert response.json().get("message") == "Заметка создана!"
        assert len(response.json())  == 1