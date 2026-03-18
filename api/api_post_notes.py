from wsgiref import headers

from api.base_api import BaseApi
from test.data.json_for_post_notes import Jsonforpostnotes


class ApiPostNotes(BaseApi):
    ENDPOINT = "/api/notes"


    def __init__(self, token):
        self.token = token
        self.last_body = None


    def create_notes(self,content = "Заметка№_1", title = "Заметка"):
        body= Jsonforpostnotes().body(content,title)
        self.last_body = body
        post_create_notes = self._request(
            method="POST",
            need_token=True,
            json=body,
        )
        return post_create_notes
        """Возврат boby для api_get_id_notes """
    def return_body_notes(self,body= None):
        if body is None:
            return self.last_body

