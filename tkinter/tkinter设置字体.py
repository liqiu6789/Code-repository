import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("文本编辑框字体设置示例")

# 创建文本编辑框并设置字体为微软雅黑
text_box = tk.Text(root, font=("Microsoft YaHei", 14, "italic"))
text_box.pack(expand=True, fill='both')

# 运行主循环
root.mainloop()
