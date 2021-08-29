from jenkinsapi.jenkins import Jenkins


class ExecuteTools:
    BASE_URL = 'http://127.0.0.1:8080/'
    USERNAME = 'admin'
    PASSWORD = '11991cbb69ab8fc91889a474ef65783842'
    JOB_NAME = 'test_pingtai'

    @classmethod
    def get_job(cls):
        jenkins = Jenkins(cls.BASE_URL, cls.USERNAME, cls.PASSWORD)
        return jenkins.keys()

    @classmethod
    def invoke(cls, task):
        jenkins = Jenkins(cls.BASE_URL, cls.USERNAME, cls.PASSWORD)
        job_test_pingtai = jenkins.get_job(cls.JOB_NAME)
        job_test_pingtai.invoke(build_params={"task": task})
        last_build_number = job_test_pingtai.get_last_buildnumber()
        while True:
            build_number = job_test_pingtai.get_last_buildnumber()
            if last_build_number != build_number:
                report_path = f"{cls.BASE_URL}job/{cls.JOB_NAME}/{build_number}/allure/"
                return report_path

