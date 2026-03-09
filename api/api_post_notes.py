from api.base_api import BaseApi
from test.data.json_for_post_notes import Jsonforpostnotes


class ApiPostNotes(BaseApi):
    ENDPOINT = "/api/notes"

    def __init__(self, token):
        self.token = token

    def create_notes(self):
        post_create_notes = self._request(
            method="POST",
            need_token=True,
            json=Jsonforpostnotes.data_post_notes,
        )
        return post_create_notes
