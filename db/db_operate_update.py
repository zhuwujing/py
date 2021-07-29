# 导入pymysql
import pymysql

# 建立链接connection
conn = pymysql.connect(
    host='120.24.149.135',  # 数据库所在的服务器地址
    port=3306,  # 数据库所在的服务器端口
    user='root',  # 连接的用户名
    password='jkcclean123',  # 连接
    database='commercial_clean',  # 数据库的
    charset='utf8')

# 获取游标
cursor = conn.cursor()

# 需要执行的sql语句
user_table = 'tbl_user'
sql = f'insert into {user_table} values (0,"hello","1234","",1,"86");'
# sql = f'update {user_table} set username = "猴子" where user_id=3'
# sql = f'delete from {user_table}  where user_id=2'

# 执行sql语句
row_count = cursor.execute(sql)
print(f'影响的行数{row_count}')

# 提交数据到数据库
# conn.commit()

# 回滚数据到什么都不做的状态，也就是撤销刚刚的修改
conn.rollback()

# 获取执行结果,类型是元组
result = cursor.fetchall()
print(f'执行结果{result}')   # (('123', 'zwj', 1, '', 1, '86'),)

# 关闭cursor
cursor.close()

# 关闭connection
conn.close()
