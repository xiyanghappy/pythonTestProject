from service.api.event import Event
from service.api.feishu_api import FeiShuApi


class Calendar(FeiShuApi):
    feishu = None

    def get_token(self):
        return self.feishu.get_token()

    def set_token(self, feishu):
        self.feishu = feishu


    def create(self, summary,**kwargs):
        url = 'https://open.feishu.cn/open-apis/calendar/v4/calendars'
        kwargs['summary'] = summary
        j = self.request()
        return Calendar()

    def list(self, page_size=500, *args):
        url = 'https://open.feishu.cn/open-apis/calendar/v4/calendars'
        token = self.feishu.get_token()

        j = self.request(
            url=url,
            method='get'
        )
        return j

    def delete(self, *args):
        pass

    def update(self, *args):
        pass

    @classmethod
    def get(cls, *args):
        pass

    def subscribe(self):
        pass

    def unsubscribe(self):
        pass

    @classmethod
    def delete_all(cls, *args):
        pass

    def get_events(self):
        return list(Event())
