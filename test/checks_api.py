class Checks_Api:

    def assert_create_user(self, response, status_code, expected_code=201):
        assert response.status_code == expected_code, (
            f"Ожидался статус  201, получен статус {status_code}, "
            f"Body: {response.json()}"
        )

    def assert_add_token_user(self, response, status_code, expected_code=200):
        assert response.status_code == expected_code, (
            f"Ожидался код 200 . Получен {status_code}, " f"Body: {response.json()}"
        )

    def assert_create_docs(self, response, status_code, expected_code=201):
        assert response.status_code == expected_code, (
            f"Ожидался код 201, получен код {status_code}, " f"Body: {response.json()}"
        )

    @staticmethod
    def assert_get_docs(response, expected_code=200):
        assert response.status_code == expected_code, (
            f"Ожижадся код 200, получен код {response.status_code}, "
            f"Body: {response.json()}"
        )

    @staticmethod
    def assert_deelete_docs(response, expected_code=200):
        assert response.status_code == expected_code, (
            f"Ожижадся код 200, получен код {response.status_code}, "
            f"Body: {response.json()}"
        )
