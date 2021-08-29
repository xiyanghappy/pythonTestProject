import requests


class TestTask:
    """
    测试任务的接口测试用例
    """

    def setup_class(self):
        self.base_url = "http://192.168.3.155:9091/task"

    def test_get_task(self):
        """
        获取任务列表的测试用例
        :return:
        """
        r = requests.get(self.base_url)
        assert r.status_code == 200

    def test_post_task(self):
        """
        新增测试任务的测试用例
        :return:
        """
        # 用例的信息
        data = {"nodeid": "yang.py"}
        r = requests.post(self.base_url, json=data)
        assert r.status_code == 200
