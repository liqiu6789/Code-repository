import tkinter as tk
from tkinter import colorchooser

# 创建主窗口
main_application = tk.Tk()
main_application.geometry('800x600')
main_application.title("颜色选择器示例")

# 创建一个文本编辑器
text_editor = tk.Text(main_application, wrap='word', relief=tk.FLAT)
text_editor.pack(fill=tk.BOTH, expand=True)

# 定义更改背景颜色的函数
def change_bg_color():
    color = colorchooser.askcolor()[1]  # 获取选中的颜色
    if color:
        text_editor.config(bg=color)  # 更改文本编辑器的背景颜色

# 创建一个按钮来调用颜色选择器并放在中间
color_button = tk.Button(main_application, text='选择背景颜色', command=change_bg_color)
color_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# 运行主循环
main_application.mainloop()
