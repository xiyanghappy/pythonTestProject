import requests as requests

from service.api.log import log


class HttpApi:
    def request(self, method, url, *args, **kwargs):
        log.debug({
            'method':method,
            'url': url,
            **kwargs
        })
        r = requests.request(
            method=method,
            url=url,
            **kwargs
        )
        log.info(r.status_code)
        log.debug((r.json()))
        return r.json()
