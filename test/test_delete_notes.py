class TestDeleteNotes:

    def test_delete_notes(self, api_delete_notes, api_get_id_notes):
        """Удаление с валидным токеном"""
        response = api_delete_notes.delete_notes(api_get_id_notes)
        data = response.json()
        assert response.status_code == 200
        assert data["message"] == "Note deleted!"
        assert isinstance(data, dict)

    def test_delete_notes_with_invalid_token(
        self, api_delete_notes_invalid_token, api_get_id_notes
    ):
        """Удаление с невалидным токеном"""
        response = api_delete_notes_invalid_token.delete_notes(api_get_id_notes)
        data = response.json()
        assert response.status_code == 403
        assert data["message"] == "Token is invalid or expired!"
        assert isinstance(data, dict)
