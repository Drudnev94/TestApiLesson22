import requests

from api.base_api import BaseAPI


class ApiPatchBaner(BaseAPI):
    ENDPOINT = "/api/v1/switch_banners"

    def api_patch_banner(
            self,
            banner_id: int,
            name: str,
            show_duration: int,
            priority: int,
            max_show_times: int,
            platform_ids: tuple[int, ...]):
        json = {
            "name": name,
            "show_duration": show_duration,
            "priority": priority,
            "max_show_times": max_show_times,
            "platform_ids": list(platform_ids),
            "stb_model_ids": []
        }

        response = self._request(method="PATCH", json=json, banner_id=banner_id)
        return response
