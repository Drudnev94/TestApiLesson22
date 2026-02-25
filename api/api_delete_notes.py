from samba.dcerpc.dcerpc import response

from api.base_api import BaseApi


class ApiDeleteNotes(BaseApi):
    ENDPOINT = "/api/notes"

    def __init__(self, token, note_id):
        self.token = token
        self.note_id = note_id

    def delete_notes(self):
        response_delete = self.metod_request(
            method="DELETE", not_id=self.note_id, need_token=True
        )
        return response_delete
