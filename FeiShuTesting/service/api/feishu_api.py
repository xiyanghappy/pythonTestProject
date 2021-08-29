import requests as requests

from service.api.http_api import HttpApi


class FeiShuApi(HttpApi):
    def get_token(self):
        pass

    def request(self, method, url, *args, **kwargs):
        print(kwargs)
        print(method)
        print(url)
        r = requests.request(
            method=method,
            url=url,
            headers={
                'Authorization': f'Bearer {self.get_token()}'
            },
            **kwargs
        )
        print(r.status_code)
        print(r.json())
        return r.json()
