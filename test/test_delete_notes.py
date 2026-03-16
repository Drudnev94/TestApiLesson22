
class TestDeleteNotes:

     def test_delete_notes(self, api_delete_notes,api_get_id_notes,api_create_notes):
        response = api_delete_notes.delete_notes(api_get_id_notes)
        assert response.status_code == 200
        assert len(response.json()) > 0
        assert response.json()["message"] == "Note deleted!"



