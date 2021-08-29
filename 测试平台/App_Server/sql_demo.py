from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

username = "root"
pwd = "123456"
ip = "127.0.0.1"
port = "3306"
database = "test_yang"
# 设置mysql 链接方法是
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}?charset=utf8'
# 解决warning问题
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(120))
    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == '__main__':
    # 创建表
    #db.create_all()
    # 删除表
    # db.drop_all()
    #user1 = User(id=1,username='李四',email='s@q.com',gender='男')
    # user2 = User(id=2, username='李5', email='es@q.com', gender='男')
    # user3 = User(id=3, username='李6', email='ds@q.com', gender='男')
    # db.session.add_all([user2,user3])
    # db.session.commit()
    #res = User.query.all() # 查询所有
    # res = User.query.filter_by(gender='男').first()  # 条件查询
    # res = User.query.filter(User.id>2).all()
    # 删除操作
    # User.query.filter_by(id=2).delete()
    # db.session.commit()
    # 修改操作
    #第一种方法
    # res = User.query.filter_by(id=3).first()
    # res.gender = '女'
    # db.session.commit()
    res = User.query.filter_by(id=3).update({'email':'qqqq@q.com',
                                                     'gender':'未知'})
    db.session.commit()
