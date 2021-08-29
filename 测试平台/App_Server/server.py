import logging

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app, supports_credentials=True)
api = Api(app)
username = "root"
pwd = "123456"
ip = "127.0.0.1"
port = "3306"
database = "test_yang"
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.logger.setLevel(logging.DEBUG)
db = SQLAlchemy(app)


def router():
    """
    路由管理
    :return:
    """
    from backend.apis.testcases import TestCaseService
    api.add_resource(TestCaseService, "/testcase")
    from backend.apis.task import TaskService
    api.add_resource(TaskService, "/task")


if __name__ == "__main__":
    router()
    app.run(port=9091, debug=True, host='0.0.0.0')
