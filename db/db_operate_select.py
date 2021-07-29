# 导入pymysql
import pymysql
from flask import jsonify

# 建立链接connection
# 120.24.149.135 port:3306     root  jkcclean123   数据库名：commercial_clean
# sqlalchemy
conn = pymysql.connect(
    host='120.24.149.135',  # 数据库所在的服务器地址
    port=3306,  # 数据库所在的服务器端口
    user='root',  # 连接的用户名
    password='jkcclean123',  # 连接
    database='commercial_clean',  # 数据库的
    charset='utf8')

print(type(conn))  # Connection对象
# 获取游标
cursor = conn.cursor()


def select_data():

    # 需要执行的sql语句
    sql = 'select * from tbl_user;'

    # 执行sql语句
    row_count = cursor.execute(sql)
    print(f'影响的行数{row_count}')

    # 获取执行结果,类型是元组
    result = cursor.fetchall()
    print(f'执行结果{result}')  # (('123', 'zwj', 1, '', 1, '86'),)
    # 关闭cursor
    cursor.close()

    # 关闭connection
    conn.close()
    return jsonify(result)



