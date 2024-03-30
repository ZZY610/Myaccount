import tkinter as tk
from functions import dictionary_management as dm
from functions import currents_management as cm
from tkinter import ttk
# 创建表格
tree=None
def create_table(container, columns, data):
    global tree
    if tree:
        tree.destroy()

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
    return 0

# 流水查询tab页创建
def add_query_currents_tab(notebook):
    tab1 = tk.Frame(notebook)
    notebook.add(tab1, text='流水查询')
    label0 = tk.Frame(tab1)
    label0.pack()

    # listbox = tk.Listbox(tab1, font=('微软雅黑', 10))
    # listbox.pack(side="left",fill='both',expand='True')

    # 标签内容
    labels = ["流水ID", "用户ID", "流水类型", "收支类型", "发生金额", "备注", "创建时间"]
    for label_text in labels:
        label = tk.Label(label0, text=label_text, font=('微软雅黑', 10), relief="solid", width=9)
        label.pack(side="left", padx=1, pady=1)

    # 纵向滚动条
    # scrollbar1 = tk.Scrollbar(tab1, orient="vertical", command=listbox.yview)
    # scrollbar1.pack(side="right", fill="y")
    # listbox.config(yscrollcommand=scrollbar1.set)
    #
    # # 横向滚动条
    # xscrollbar = tk.Scrollbar(tab1, orient="horizontal", command=listbox.xview)
    # xscrollbar.pack(side="bottom", fill="x")
    # listbox.config(xscrollcommand=xscrollbar.set)

    Button1 = tk.Button(tab1, text='查询数据', font=('微软雅黑', 10), width=6,
                        command=lambda: create_table(tab1,labels,cm.query_currents()))
    Button1.pack(side="top")
    Button2 = tk.Button(tab1, text='退出', font=('微软雅黑', 10), width=6,
                        command=notebook.quit)
    Button2.pack(side="bottom")


# 新增流水tab页创建
def add_add_currents_tabs(notebook):
    tab2 = tk.Frame(notebook)
    notebook.add(tab2, text='新增流水')

    label_income_expense = ttk.Label(tab2, text='收支类型:', style='TLabel')  # 使用 ttk.Label
    label_currents_type = ttk.Label(tab2, text='流水类型:', style='TLabel')
    label_amount = ttk.Label(tab2, text='发生金额:', style='TLabel')

    options_income_expense = ['收入', '支出']
    options_currents_type = ['类型1', '类型2', '类型3']


    income_expense_var = tk.StringVar()
    transaction_type_var = tk.StringVar()
    amount_var = tk.DoubleVar()

    dropdown_income_expense = ttk.Combobox(tab2, textvariable=income_expense_var,
                                           values=options_income_expense, style='TCombobox')  # 使用 ttk.Combobox
    dropdown_transaction_type = ttk.Combobox(tab2, textvariable=transaction_type_var,
                                             values=options_currents_type, style='TCombobox')
    entry_amount = ttk.Entry(tab2, textvariable=amount_var, style='TEntry')  # 使用 ttk.Entry

    button_add = ttk.Button(tab2, text='新增', command=lambda:cm.add_currents(user_id=1,
                                                                              transaction_type=transaction_type_var.get(),
                                                                              tcurrent_type=income_expense_var.get(),
                                                                              amount=amount_var.get(),
                                                                              ),
                            style='TButton')  # 使用 ttk.Button
    button_exit = ttk.Button(tab2, text='退出', command=notebook.quit, style='TButton')

    label_income_expense.grid(row=0, column=0, padx=10, pady=10)
    label_currents_type.grid(row=1, column=0, padx=10, pady=10)
    label_amount.grid(row=2, column=0, padx=10, pady=10)

    dropdown_income_expense.grid(row=0, column=1, padx=10, pady=10)
    dropdown_transaction_type.grid(row=1, column=1, padx=10, pady=10)
    entry_amount.grid(row=2, column=1, padx=10, pady=10)

    button_add.grid(row=3, column=0, columnspan=2, pady=10)
    button_exit.grid(row=4, column=0, columnspan=2, pady=10)
# 数据字典tab页创建
def add_dictionary_tab(notebook):
    tab3 = tk.Frame(notebook)
    notebook.add(tab3, text='数据字典管理')

    # 在新的选项卡页面中放置相关的组件和功能按钮
    add_button = tk.Button(tab3, text='添加', command=dm.add_dictionary_item)
    add_button.pack()

    edit_button = tk.Button(tab3, text='编辑', command=dm.edit_dictionary_item)
    edit_button.pack()

    delete_button = tk.Button(tab3, text='删除', command=dm.delete_dictionary_item)
    delete_button.pack()


