import requests


class BaseAPI:
    BASE_URL = "http://ams-server-rudnev.cas.sdd"
    ENDPOINT = ""

    headers = {"accept": "application/json",}

    def _request(self,method, json=None, files=None, data=None,banner_id=None):
        url = self.BASE_URL + f"{self.ENDPOINT}"
        if banner_id is not None:
            url += f"/{banner_id}"
            print(f"Запрос на {url}")

        if files:
            headers = self.headers.copy()
            if "Content-Type" in headers:
                del headers["Content-Type"]
        else:
            headers = self.headers.copy()

        response = requests.request(method, url, json=json, files=files, data=data, headers=headers)
        return response