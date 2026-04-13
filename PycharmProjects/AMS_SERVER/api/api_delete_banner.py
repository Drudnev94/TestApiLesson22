from api.base_api import BaseAPI

class ApiDeleteBanner(BaseAPI):
    ENDPOINT = "/api/v1/switch_banners"

    def api_delete_banner(self, banner_id:int):
        responses = self._request(method= "DELETE",banner_id = banner_id)
        return responses




