from api.base_api import BaseApi


class ApiDeleteNotes(BaseApi):
    ENDPOINT = "/api/notes"

    def __init__(self, token):
        self.token = token

    def delete_notes(self, note_id):
        """Удаление заметки"""
        response_delete = self._request(
            method="DELETE", not_id=note_id, need_token=True
        )
        return response_delete
