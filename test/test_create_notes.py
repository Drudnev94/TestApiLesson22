from test.data.json_for_post_notes import data_for_notes


class TestCreateNote:
    def test_create_notes(self, api_post_notes, cleaning_after_creation):
        response = api_post_notes.create_notes(
            data_for_notes["content"], data_for_notes["title"]
        )
        data = response.json()
        assert response.status_code == 201
        assert response.json().get("message") == "Заметка создана!"
        assert isinstance(data, dict)
        assert len(data) > 0
        assert "message" in data, "ERROR: id is not data"

    def test_create_notes_invalid_token(self, api_post_notes_invalid_token):
        response = api_post_notes_invalid_token.create_notes(
            data_for_notes["content"], data_for_notes["title"]
        )
        data = response.json()
        assert response.status_code == 403
        assert data["message"] == "Token is invalid or expired!"
        assert isinstance(data, dict)

    def test_create_notes_without_token(self, api_post_notes_without_token):
        response = api_post_notes_without_token.create_notes(
            data_for_notes["content"], data_for_notes["title"]
        )
        data = response.json()
        print(data)
        assert response.status_code == 401
        assert data["message"] == "Token is missing!"
        assert isinstance(data, dict)
