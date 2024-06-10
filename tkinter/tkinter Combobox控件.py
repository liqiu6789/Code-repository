import tkinter as tk
from tkinter import ttk


def on_combobox_changed(event):
    selected_value = event.widget.get()
    print(f"你选择了: {selected_value}")


root = tk.Tk()
root.title("tkinter Combobox 示例")

# 创建一个 Combobox
combobox = ttk.Combobox(root, values=["选项1", "选项2", "选项3", "选项4"])
combobox.pack(pady=20)

# 当用户选择一个新的值时，触发回调函数
combobox.bind("<<ComboboxSelected>>", on_combobox_changed)

# 你可以设置默认值，如果不设置，则默认值为空
combobox.set("选项1")  # 设置默认值为 "选项1"

root.mainloop()