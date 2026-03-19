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
        if all_note is None:
            return None

        for note in all_note:
            if note["title"] == "Заметка":
                return note["id"]

        return  None


