
class TestPostBaner():

    def test_post_banner(self, post_banner_api):
        response = post_banner_api.api_post_banner()
        data = response.json()
        print(data)
