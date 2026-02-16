import unittest

import requests


class TestGetPet(BaseApiDocs):

    def test_getDocs(self):
        response = requests.get(url=f"{self.BASE_URL}{self.ENDPOINT}", headers=self.HEADERS)

