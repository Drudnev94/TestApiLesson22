class TestGetBanner:

    def test_api_get_banner_id(self, api_get_banner):
        response = api_get_banner.api_get_banner_id(55)
        response = response.json()
        print(response)

    def test_api_get_all_banner(self, api_get_banner):
        response = api_get_banner.api_get_all_banner()
        response = response.json()
        print(response)