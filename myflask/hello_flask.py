from flask import Flask, url_for
from db.db_operate_select import *

# 创建Flask对象
app = Flask(__name__)


# 视图函数
@app.route('/')
def hello_world():
    return f'hello world! zwj'


@app.route('/g1/userInfo')
def get_user_info():
    return select_data()


with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('get_user_info'))


if __name__ == '__main__':
    my_host = '0.0.0.0'
    app.run(my_host)
    # app.run(host=my_host, debug=True)



