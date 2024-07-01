import tkinter as tk
from time import strftime

def time():
    string = strftime('%Y-%m-%d %H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)  # 每秒更新一次时间

root = tk.Tk()
root.title("电子时钟")

label = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
label.pack(anchor='center')

time()  # 初始化时钟

root.mainloop()
