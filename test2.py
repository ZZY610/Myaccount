import tkinter as tk
from tkinter import ttk

def create_table(container, columns, data):
    # 创建 Treeview 组件
    tree = ttk.Treeview(container, columns=columns, show="headings")
    # 添加表头
    for col in columns:
        tree.heading(col, text=col)
    # 插入数据
    for row in data:
        tree.insert("", "end", values=row)
    # 设置布局
    tree.pack(fill="both", expand=True)
    return tree
# 测试数据
columns = ["列1", "列2", "列3"]
data = [("行1数据1", "行1数据2", "行1数据3"),
        ("行2数据1", "行2数据2", "行2数据3")]

root = tk.Tk()
root.geometry("400x300")

# 创建表格
create_table(root, columns, data)

root.mainloop()
