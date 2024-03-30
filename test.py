import tkinter as tk
from tkinter import ttk

# 创建主窗口
root = tk.Tk()
root.geometry("600x400")
root.title("容器组件层级示例")

# 创建菜单栏目
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# 添加菜单项
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# 创建 Frame 1
frame1 = tk.Frame(root, bg="lightblue", bd=5, relief="sunken")
frame1.pack(side="top", fill="both", expand=True)

# Label 1 在 Frame 1 内
label1 = tk.Label(frame1, text="Frame 1", bg="lightblue", font=("Arial", 12, "bold"))
label1.pack(side="top", fill="x")

# 创建 Frame 2，位于 Frame 1 内
frame2 = tk.Frame(frame1, bg="lightgreen", bd=5, relief="ridge")
frame2.pack(side="left", fill="both", expand=True)

# Label 2 在 Frame 2 内
label2 = tk.Label(frame2, text="Frame 2", bg="lightgreen", font=("Arial", 12, "bold"))
label2.pack(side="top", fill="x")

# 创建 Notebook，位于 Frame 2 内
notebook = ttk.Notebook(frame2)
notebook.pack(side="left", fill="both", expand=True)

# Tab 1 在 Notebook 内
tab1 = tk.Frame(notebook)
notebook.add(tab1, text="Tab 1")

# Label 3 在 Tab 1 内
label3 = tk.Label(tab1, text="Tab 1 Content", font=("Arial", 12))
label3.pack(side="top", pady=10)

# 创建 Frame 3，位于 Frame 2 内
frame3 = tk.Frame(frame2, bg="lightyellow", bd=5, relief="raised")
frame3.pack(side="right", fill="both", expand=True)

# Label 4 在 Frame 3 内
label4 = tk.Label(frame3, text="Frame 3", bg="lightyellow", font=("Arial", 12, "bold"))
label4.pack(side="top", fill="x")

# 创建 Button，位于 Frame 3 内
button1 = tk.Button(frame3, text="Button 1", width=10)
button1.pack(side="top", pady=10)

# 创建 Frame 4，位于 Frame 1 的右侧
frame4 = tk.Frame(frame1, bg="lightcoral", bd=5, relief="groove")
frame4.pack(side="right", fill="both", expand=True)

# Label 5 在 Frame 4 内
label5 = tk.Label(frame4, text="Frame 4", bg="lightcoral", font=("Arial", 12, "bold"))
label5.pack(side="top", fill="x")

# 创建 Notebook，位于 Frame 4 内
notebook2 = ttk.Notebook(frame4)
notebook2.pack(fill="both", expand=True)

# Tab 2 在 Notebook2 内
tab2 = tk.Frame(notebook2)
notebook2.add(tab2, text="Tab 2")

# Label 6 在 Tab 2 内
label6 = tk.Label(tab2, text="Tab 2 Content", font=("Arial", 12))
label6.pack(side="top", pady=10)

# 创建下拉框，位于 Frame 4 内
options = ["Option 1", "Option 2", "Option 3"]
combo = ttk.Combobox(frame4, values=options)
combo.pack(side="top", pady=10)

# 创建列表框，位于 Frame 4 内
listbox = tk.Listbox(frame4)
for i in range(20):
    listbox.insert(tk.END, f"Item {i+1}")
listbox.pack(side="top", fill="both", expand=True)

# 创建滚动条，位于 Frame 4 内
scrollbar = tk.Scrollbar(frame4, orient="vertical", command=listbox.yview)
scrollbar.pack(side="right", fill="y")

# 关联滚动条和列表框
listbox.config(yscrollcommand=scrollbar.set)

root.mainloop()
