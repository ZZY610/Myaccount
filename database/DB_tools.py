import sqlite3 as sq

# 连接数据库和创建游标，返回游标对象
def connect_database():
    con = sq.connect('F:\SQLite\database\my_account.db')
    if con:
        print('数据库连接成功')

    return con.cursor()

