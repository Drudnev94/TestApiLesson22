from http.client import responses


class TestApiDeleteBanner:

    def test_delete_banner(self, delete_banner_api):
        responses = delete_banner_api.api_delete_banner(110)
        responses = responses.json()
        print(responses)
