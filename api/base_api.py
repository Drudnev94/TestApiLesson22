import requests


class BaseApi:
    base_url = "http://185.240.103.201:8000"
    token = " "
    ENDPOINT = " "

    def headers(self, need_token: bool):
        """Определяем тип хедера в зависимости от необходимости токена"""
        if need_token:
            return {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.token}",
            }
        else:
            return {
                "Accept": "application/json",
                "Content-Type": "application/json",
            }

    def _request(self, method: str, not_id=None, need_token=False, json=None):
        """Генерация Url в зависимости от heders"""
        if not_id:
            url = f"{self.base_url}{self.ENDPOINT}/{not_id}"
        else:
            url = f"{self.base_url}{self.ENDPOINT}"
        response = requests.request(
            method, url, headers=self.headers(need_token), json=json
        )

        return response
