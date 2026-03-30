from api.api_registration import ApiRegistration
from api.api_authorization import ApiAuthorization
from api.api_post_notes import ApiPostNotes
from api.api_get_notes import ApiGetNotes
from api.api_delete_notes import ApiDeleteNotes
from test.data.json_for_post_notes import data_for_notes

import pytest


@pytest.fixture
def api_registration():
    return ApiRegistration()


@pytest.fixture
def api_authorization():
    return ApiAuthorization()


@pytest.fixture
def api_post_notes(token):
    return ApiPostNotes(token)


@pytest.fixture
def api_post_notes_without_token():
    return ApiPostNotes(None)


@pytest.fixture
def api_post_notes_invalid_token(token):
    token = "121234dsafefegewgf"
    return ApiPostNotes(token)


@pytest.fixture
def api_get_notes(token):
    return ApiGetNotes(token)


@pytest.fixture
def api_get_notes_invalid_token(token):
    token = "121234dsafefegewgf"
    return ApiGetNotes(token)


@pytest.fixture
def api_delete_notes(token):
    return ApiDeleteNotes(token)


@pytest.fixture
def api_delete_notes_invalid_token(token):
    token = "121234dsafefegewgf"
    return ApiDeleteNotes(token)


@pytest.fixture
def token(api_authorization):
    return api_authorization.get_token()


@pytest.fixture
def api_get_id_notes(api_get_notes, api_create_notes):
    title = data_for_notes["title"]
    return api_get_notes.get_id_notes(title=title)


@pytest.fixture
def api_create_notes(api_post_notes):
    """Создание заметки перед тестом"""
    return api_post_notes.create_notes(
        data_for_notes["content"], data_for_notes["title"]
    )


@pytest.fixture
def cleaning_after_creation(api_delete_notes, api_get_notes):
    """Удаление созданной заметки после теста"""
    yield
    note_id = api_get_notes.get_id_notes()
    api_delete_notes.delete_notes(note_id)


@pytest.fixture
def setup_teardown_note(api_delete_notes, api_get_id_notes):
    """Создания - перед / удаление - после"""
    yield
    api_delete_notes.delete_notes(api_get_id_notes)
