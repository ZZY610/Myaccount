import tkinter as tk
from ttkbootstrap import Style  # 导入 Style 类
import datetime
from tkinter import ttk
from gui import tab_create
help(Style)
# man! what can i say, mamba out
# 男人，什么罐头我说，树眼镜蛇出去

root=tk.Tk()
root.title('记账程序')
# root.geometry('400x400+100+100')
# style = Style(theme='flatly')


# 创建tab页
tabs = ttk.Notebook(root)
# tabs.grid(row=0, column=0, padx=50, pady=50, sticky='ew')
tabs.pack(side='left',fill="both", expand=True)

## 填充
tabs.pack(fill='both',expand=True)
tab_create.add_query_currents_tab(tabs)
tab_create.add_add_currents_tabs(tabs)
tab_create.add_dictionary_tab(tabs)

# listbox.grid(row=0, column=0, columnspan=3, pady=10)
root.mainloop()
