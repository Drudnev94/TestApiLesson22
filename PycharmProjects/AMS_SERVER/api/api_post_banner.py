import json
from test.data.json_for_post_baner import json_for_post_baner
from api.base_api import BaseAPI


class PostBaner(BaseAPI):
    ENDPOINT = "/api/v1/image_switch_banners"

    def api_post_banner(self):
        image_path = json_for_post_baner['image_path']
        params = {k: v for k, v in json_for_post_baner.items() if k != 'image_path'}

        with open(image_path, 'rb') as image_file:
            files = { 'image': ('red_forest_16_9.jpg', image_file, 'image/jpeg')}
            data = {'params': json.dumps(params)}
            response_post_banner = self._request(method="POST", files=files, data=data, )
        return response_post_banner
