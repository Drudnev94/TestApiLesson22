class TestDeleteNotes:

    def test_delete_notes(self, api_delete_notes, api_get_id_notes, api_create_notes):
        """Данные для создания/получения заметки по умолчанию"""
        response = api_delete_notes.delete_notes(api_get_id_notes)
        data = response.json()
        assert response.status_code == 200
        assert len(response.json()) > 0
        assert response.json()["message"] == "Note deleted!"
        assert isinstance(data, dict)
        assert len(data) > 0
        assert "message" in data, "ERROR: id is not data"
