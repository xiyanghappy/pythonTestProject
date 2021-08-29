import datetime

from backend.server import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    remark = db.Column(db.String(120))
    report = db.Column(db.String(120))
    create_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def as_dict(self):
        return {"id": self.id,
                "remark": self.remark,
                "report": self.report,
                # 强转为字符串的格式
                "create_at": str(self.create_at)}
if __name__ == '__main__':
    db.create_all()

