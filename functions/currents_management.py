import tkinter as tk
import sqlite3 as sq
from database import DB_tools

cur=DB_tools.connect_database()

# 查询流水
def query_currents():
    con = sq.connect('F:\SQLite\database\my_account.db')
    if con:
        print('ok')
    cur = con.cursor()
    result = cur.execute('select case when '
                         't.transaction_type =1 then "支出" else "收入" end as "收支类型",t.*'
                         ' from tcurrents t')
    rows=result.fetchall()
    result_list = [list(row) for row in rows]

    # tree.delete(*tree.get_children())

    return result_list
    # listbox.delete(0,tk.END)
    # for row in result.fetchall():
    #     listbox.insert(tk.END,row)
    # return 0

# 插入流水
def add_currents(user_id,transaction_type,tcurrent_type,amount):
    con = sq.connect('F:\SQLite\database\my_account.db')
    if con:
        print('ok')
    cur = con.cursor()
    cur.execute("INSERT INTO tcurrents (user_id,transaction_Type, tcurrent_Type, amount) VALUES (?, ?, ?,?)",
                (1, transaction_type,tcurrent_type,amount))

    con.commit()
    con.close()
    print("数据插入成功")
    return 0