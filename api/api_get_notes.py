from api.base_api import BaseApi


class ApiGetNotes(BaseApi):
    ENDPOINT = "/api/notes"

    def __init__(self, token):
        self.token = token

    def get_all_note(self):
        get_notes = self._request(method="GET", need_token=True)
        return get_notes

    def get_id_notes(self, title):
        all_note = self.get_all_note().json()
        for note in all_note:
            if note["title"] == title:
                return note["id"]
