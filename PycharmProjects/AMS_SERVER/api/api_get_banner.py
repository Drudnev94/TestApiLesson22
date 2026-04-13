from api.base_api import BaseAPI

class APIGetBanner(BaseAPI):
    ENDPOINT = "/api/v1/switch_banners"

    def api_get_banner_id(self, banner_id:int):
        responses = self._request(method= "GET",banner_id = banner_id)
        return responses

    def api_get_all_banner(self):
        responses = self._request(method= "GET")
        return responses
