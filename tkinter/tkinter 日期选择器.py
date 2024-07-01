import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

def show_selected_date():
    selected_date = cal.get_date()
    date_label.config(text=f"选中的日期: {selected_date}")

root = tk.Tk()
root.title("日期选择器示例")

# 创建日期选择器
cal = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
cal.pack(pady=20)

# 创建显示选中日期的按钮
show_date_button = tk.Button(root, text="显示选中日期", command=show_selected_date)
show_date_button.pack(pady=10)

# 创建一个标签用于显示选中的日期
date_label = tk.Label(root, text="未选择日期")
date_label.pack(pady=20)

root.mainloop()
