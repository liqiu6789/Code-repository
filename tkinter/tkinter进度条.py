import tkinter as tk
from tkinter import ttk


def start_progress():
    progress['value'] = 0
    max_value = 100
    step = 10

    for i in range(0, max_value, step):
        progress['value'] += step
        root.update_idletasks()
        root.after(500)  # 模拟一些处理时间


root = tk.Tk()
root.title("进度条示例")

# 创建一个进度条
progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=20)

# 创建一个按钮，点击后开始进度
start_button = tk.Button(root, text="开始", command=start_progress)
start_button.pack(pady=10)

root.mainloop()
