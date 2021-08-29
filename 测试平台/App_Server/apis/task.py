from flask import request
from flask_restful import Resource

from backend.models.task import Task
from backend.server import app, db
from backend.utils.execute_tools import ExecuteTools


class TaskService(Resource):
    def post(self):
        """
               1. 调用jenkins执行用例
               2. 执行用例之后，写入执行记录到数据库
               :return:
               """
        data = request.json
        nodeids = [i['nodeid'] for i in data]
        nodeids = " ".join(nodeids)
        app.logger.info(f"执行的用例为{nodeids}")
        report = ExecuteTools.invoke(nodeids)
        app.logger.info(f"添加一条task，报告为{report}，执行用例为{nodeids}")
        task = Task(remark=nodeids, report=report)
        db.session.add(task)
        db.session.commit()
        db.session.close()
        return {"error": 0, "msg": "ok"}

    def get(self):
        """
                获取任务列表
                :return:
                """
        # 查询task所有的数据
        tasks = Task.query.all()
        for task in tasks:
            task_info = task.as_dict()
            print(task_info)
        # as dict 把对象转为python 字典格式，后面flask好解析
        tasks_data = [task.as_dict() for task in tasks]
        app.logger.info(f"获取到的任务列表为{tasks_data}")
        # 接口的响应数据
        return {"error": 0, "msg": {"data": tasks_data}}
