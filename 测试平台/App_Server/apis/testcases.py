from flask import request
from flask_restful import Resource
from backend.models.testcases import Testcase
from backend.server import app, db


class TestCaseService(Resource):
    """
    测试用例服务
    """

    # 方法名，对应app.route中的methods
    def get(self):
        case_data = Testcase.query.all()
        data = [{'id': i.id, 'nodeid': i.nodeid, 'remark': i.remark} for i in case_data]
        app.logger.info(data)
        return {'error': 0, 'msg': {'data': data}}

    def post(self):
        # 增加一条用例
        case_data = request.json
        app.logger.info(case_data)
        # 从接口拿到的字典数据进行解包，使用关键字传参传入testcase
        testcase = Testcase(**case_data)
        db.session.add(testcase)
        db.session.commit()
        return {'error': 0, 'msg': 'post success'}

    def put(self):
        case_id = request.json.get('id')
        case = Testcase.query.filter_by(id=case_id). \
            update(request.json)
        db.session.commit()
        app.logger.info(case)
        return {'error': 0, 'msg': 'put success'}

    def delete(self):
        case_id = request.args.get('id')
        if not case_id:
            return {'error': 40001, 'msg': 'delete case_id cant null'}
        else:
            Testcase.query.filter_by(id=case_id).delete()
            db.session.commit()
            return {'error': 0, 'msg': 'delete success'}

