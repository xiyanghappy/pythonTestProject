from service.api.http_api import HttpApi


class FeiShu(HttpApi):
    token: str = None

    def __init__(self):
        self.token: str = None
        self.app_id = 'cli_a1ab480158f8d00c'
        self.app_secret = 'dY8NAoGZGij9QSUQKopN4diuurBVkTzj'

    def get_token(self):
        url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal'

        if self.token is None:
            j = self.request(
                url=url,
                method='post',
                json={
                    'app_id': self.app_id,
                    'app_secret': self.app_secret
                }
            )
            self.token = j['tenant_access_token']
        return self.token
