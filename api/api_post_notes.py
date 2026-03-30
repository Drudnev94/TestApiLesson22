from api.base_api import BaseApi
from test.data.json_for_post_notes import data_for_notes


class ApiPostNotes(BaseApi):
    ENDPOINT = "/api/notes"

    def __init__(self, token):
        self.token = token
        self.last_body = None

    def create_notes(self, content, title):
        json = {
            "content": content,
            "title": title,
        }
        post_create_notes = self._request(
            method="POST",
            need_token=True,
            json=json,
        )

        return post_create_notes
