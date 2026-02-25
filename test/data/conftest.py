from api.api_registration import ApiRegistretion
from api.api_authorization import ApiAuthorization
from api.api_post_notes import ApiPostNotes
from api.api_get_notes import ApiGetNotes
from api.api_delete_notes import ApiDeleteNotes
from test.data.json_for_post_notes import Jsonforpostnotes

import pytest


@pytest.fixture
def api_registration():
    return ApiRegistretion()


@pytest.fixture
def api_authorization():
    return ApiAuthorization()


@pytest.fixture
def api_post_notes(token):
    return ApiPostNotes(token)


@pytest.fixture
def token():
    api_auth = ApiAuthorization()  # Создаём экземпляр
    return api_auth.get_token()


@pytest.fixture
def api_get_notes(token):
    return ApiGetNotes(token)


@pytest.fixture
def api_get_id_notes(api_get_notes):
    title = Jsonforpostnotes.data_post_notes["title"]
    return api_get_notes.get_id_notes(title=title)


@pytest.fixture
def api_delete_notes(token, api_get_id_notes):
    print(api_get_id_notes)
    return ApiDeleteNotes(token, api_get_id_notes)


@pytest.fixture
def invalid_token(token):
    aut_token = ApiGetNotes(token)
    aut_token.token = token + "_invalid_suffix"
    return aut_token
