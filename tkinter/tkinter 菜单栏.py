import tkinter as tk
from tkinter import messagebox

# 创建主窗口
root = tk.Tk()
root.title("Tkinter Menu 示例")
root.geometry("400x300")

# 创建主菜单
menu_bar = tk.Menu(root)

# 创建"文件"菜单
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="新建", command=lambda: messagebox.showinfo("信息", "新建文件"))
file_menu.add_command(label="打开", command=lambda: messagebox.showinfo("信息", "打开文件"))
file_menu.add_command(label="保存", command=lambda: messagebox.showinfo("信息", "保存文件"))
file_menu.add_separator()
file_menu.add_command(label="退出", command=root.quit)

# 将"文件"菜单添加到菜单栏
menu_bar.add_cascade(label="文件", menu=file_menu)

# 创建"帮助"菜单
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="关于", command=lambda: messagebox.showinfo("关于", "这是一个 Tkinter Menu 示例"))

# 将"帮助"菜单添加到菜单栏
menu_bar.add_cascade(label="帮助", menu=help_menu)

# 将菜单栏绑定到窗口
root.config(menu=menu_bar)

# 运行主循环
root.mainloop()
