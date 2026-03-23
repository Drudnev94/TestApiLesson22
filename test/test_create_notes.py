class TestCreateNote:
    def test_create_notes(self, api_post_notes, cleaning_after_creation):
        """Возможно указать кастомные данные для создания: content, title.(требует изменений в api)"""
        response = api_post_notes.create_notes()
        data = response.json()
        assert response.status_code == 201
        assert response.json().get("message") == "Заметка создана!"
        assert isinstance(data, dict)
        assert len(data) > 0
        assert "message" in data, "ERROR: id is not data"
