import tkinter as tk
from tkinter import Menu, PhotoImage

# 创建主窗口
root = tk.Tk()
root.title("Tkinter 菜单栏图标示例")
root.geometry("400x300")

# 加载图标
new_icon = PhotoImage(file="new.png")
open_icon = PhotoImage(file="open.png")
exit_icon = PhotoImage(file="exit.png")

# 创建菜单栏
menu_bar = Menu(root)
root.config(menu=menu_bar)

# 添加文件菜单
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="文件", menu=file_menu)

# 添加带图标的菜单项
file_menu.add_command(label="新建", image=new_icon, compound='left')
file_menu.add_command(label="打开", image=open_icon, compound='left')
file_menu.add_separator()
file_menu.add_command(label="退出", image=exit_icon, compound='left', command=root.quit)

# 运行主循环
root.mainloop()
