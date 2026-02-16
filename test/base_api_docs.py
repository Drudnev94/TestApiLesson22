import random
import requests


class BaseApiDocs:
    """ "Constants for user"""

    BASE_URL = "http://185.240.103.201:8000"
    ENDPOINT_REGISTER = "/api/register"
    ENDPOINT_LOGIN = "/api/login"
    HEADERS = {"Content-Type": "application/json"}
    PAYLOAD_CREATE = {
        "email": "dimaru123@example.su",
        "password": "q1w232e3",
        "username": "DIMAR123",
    }
    PAYLOAD_FOR_TOKEN = {"email": "dimaru123@example.su", "password": "q1w232e3"}
    """"Constants for docs"""
    # BASE_URL_DOCS = BASE_URL
    ENDPOINT_DOCS = "/api/notes"
    HEADERS_DOCS = {"Content-Type": "application/json"}
    HEADERS_DOCS1 = {"accept": "application/json"}
    BODY_DOCS_POST = {"content": "Заметка про заметки", "title": "Заметка № 1"}


# heders= self.HEADERS_DOCS | HEADERS_DOCS1 , f'Bearer {token}'
