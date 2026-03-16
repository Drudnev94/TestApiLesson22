import requests


class BaseApi:
    base_url = "http://185.240.103.201:8000"
    token = " "
    ENDPOINT = " "

    """Определаем тип хедера в зависиомти от необходимости токена"""

    def headers(self, need_token: bool):
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

    """Метод которырй генерирует нужный урл в зависимости от атрибутов переденных в него"""

    def _request(self, method: str, not_id=None, need_token=False, json=None):
        if not_id:
            url = f"{self.base_url}{self.ENDPOINT}/{not_id}"
        else:
            url = f"{self.base_url}{self.ENDPOINT}"
        response = requests.request(method, url, headers=self.headers(need_token), json=json)

        return response