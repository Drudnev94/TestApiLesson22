
class TestGetNotes:

    def test_get_notes(self, api_get_notes,setup_teardown_note):
        response = api_get_notes.get_all_note()
        assert response.status_code == 200



