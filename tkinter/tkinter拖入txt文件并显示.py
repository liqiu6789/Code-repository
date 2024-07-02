import tkinter as tk
from tkinter import scrolledtext
from tkinterdnd2 import DND_FILES, TkinterDnD

def drop(event):
    file_path = event.data.strip('{}')
    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            text_area.delete('1.0', tk.END)
            text_area.insert(tk.INSERT, content)
    else:
        text_area.delete('1.0', tk.END)
        text_area.insert(tk.INSERT, "请拖入一个 .txt 文件。")

# 创建主窗口
root = TkinterDnD.Tk()
root.title("拖入TXT文件并显示")
root.geometry("600x400")

# 添加滚动文本框
text_area = scrolledtext.ScrolledText(root, width=70, height=30)
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# 绑定拖放事件
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

# 运行主循环
root.mainloop()
