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
def api_get_notes(token):
    return ApiGetNotes(token)

@pytest.fixture
def api_delete_notes(token):
     return ApiDeleteNotes(token)

@pytest.fixture
def token(api_authorization):
     return api_authorization.get_token()


@pytest.fixture
def api_get_id_notes(api_get_notes,api_post_notes,api_create_notes):
    body = api_post_notes.return_body_notes()
    title = body["title"]
    return api_get_notes.get_id_notes(title=title)

"""Создание заметки перед тестом"""
@pytest.fixture
def api_create_notes(api_post_notes):
    return  api_post_notes.create_notes()

"""Удаление созданной заметки после теста"""
@pytest.fixture
def cleaning_after_creation(api_delete_notes,api_get_notes):
    id = (api_get_notes.get_id_notes("Заметка"))
    yield api_delete_notes.delete_notes(id)



"""Создания - перед / удаление - после"""
@pytest.fixture
def setup_teardown_note(api_post_notes,api_delete_notes,api_get_id_notes):
    api_post_notes.create_notes()
    yield (
        api_delete_notes.delete_notes(api_get_id_notes))











