import requests


class TestCase:
    def setup_class(self):
        self.base_url = 'http://192.168.3.155:9091/testcase'

    def test_get(self):
        r = requests.get(self.base_url)
        print(r.json())
        assert r.status_code == 200

    def test_post(self):
        # data = {'id':1,'nodeid':'node111','remark':'测试'}
        data = {'id': 3, 'nodeid': 'node222', 'remark': '试验'}
        r = requests.post(self.base_url, json=data)
        assert r.status_code == 200

    def test_put(self):
        data = {'id': 2, 'nodeid': 'node222', 'remark': 'bbbbbbbbb'}
        r = requests.put(self.base_url, json=data)
        assert r.status_code == 200

    def test_delete(self):
        r = requests.delete(self.base_url)
        assert r.json()['error'] == 40001
        r = requests.delete(self.base_url, params={'id': 1})
        assert r.status_code == 200
