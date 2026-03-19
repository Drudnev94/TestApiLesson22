
class TestGetNotes:

    def test_get_notes(self, api_get_notes,setup_teardown_note):
        response = api_get_notes.get_all_note()
        data = response.json()
        assert response.status_code == 200
        assert isinstance(data, list)
        """Проверка обязательных полей"""
        note = data[0]
        assert "content" in note,  "ERROR: content is not data"
        assert "date_posted" in note,  "ERROR: date posted is not data"
        assert  "id" in note, "ERROR: id is not data"
        assert "title" in note, "ERROR: title is not data"
        """Проверка типа данных"""
        assert isinstance(note, dict)
        assert isinstance(note["id"], int)
        assert isinstance(note["title"], str)
        assert isinstance(note["content"], str)
        assert isinstance(note["date_posted"], str)




