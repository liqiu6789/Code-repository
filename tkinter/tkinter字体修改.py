import tkinter as tk
from tkinter import ttk, font

# 创建主窗口
root = tk.Tk()
root.title("字体选择器")
root.geometry("800x600")

# 创建文本编辑框
text_editor = tk.Text(root, wrap='word', relief=tk.FLAT)
text_editor.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# 获取所有可用字体
available_fonts = list(font.families())

# 当前选择的字体和大小
current_font_family = tk.StringVar(value="Arial")
current_font_size = tk.IntVar(value=12)

# 字体选择器
font_label = ttk.Label(root, text="选择字体:")
font_label.pack(side=tk.LEFT, padx=(10, 5))
font_family_box = ttk.Combobox(root, textvariable=current_font_family, state='readonly', values=available_fonts)
font_family_box.pack(side=tk.LEFT, padx=(0, 10))

# 字体大小选择器
font_size_label = ttk.Label(root, text="选择大小:")
font_size_label.pack(side=tk.LEFT, padx=(10, 5))
font_size_box = ttk.Combobox(root, textvariable=current_font_size, state='readonly', values=tuple(range(8, 72, 2)))
font_size_box.pack(side=tk.LEFT, padx=(0, 10))

# 应用字体变化的函数
def apply_font_changes(event=None):
    selected_font_family = current_font_family.get()
    selected_font_size = current_font_size.get()
    text_editor.config(font=(selected_font_family, selected_font_size))

# 绑定选择事件
font_family_box.bind("<<ComboboxSelected>>", apply_font_changes)
font_size_box.bind("<<ComboboxSelected>>", apply_font_changes)

# 初始设置字体
apply_font_changes()

# 运行主循环
root.mainloop()
