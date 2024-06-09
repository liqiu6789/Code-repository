import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# 创建主窗口
root = tk.Tk()
root.title("Tkinter 工具栏示例")
root.geometry("800x600")

# 创建文本编辑框
text_editor = tk.Text(root, wrap='word', relief=tk.FLAT)
text_editor.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# 当前文件路径
current_file = None

# 工具栏回调函数
def new_file():
    global current_file
    current_file = None
    text_editor.delete(1.0, tk.END)

def open_file():
    global current_file
    current_file = filedialog.askopenfilename(defaultextension=".txt",
                                              filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if current_file:
        text_editor.delete(1.0, tk.END)
        with open(current_file, "r", encoding="utf-8") as file:
            text_editor.insert(1.0, file.read())

def save_file():
    global current_file
    if current_file:
        with open(current_file, "w", encoding="utf-8") as file:
            file.write(text_editor.get(1.0, tk.END))
    else:
        save_as_file()

def save_as_file():
    global current_file
    current_file = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if current_file:
        with open(current_file, "w", encoding="utf-8") as file:
            file.write(text_editor.get(1.0, tk.END))

def cut_text():
    text_editor.event_generate("<<Cut>>")

def copy_text():
    text_editor.event_generate("<<Copy>>")

def paste_text():
    text_editor.event_generate("<<Paste>>")

# 创建工具栏
toolbar = ttk.Frame(root)
toolbar.pack(side=tk.TOP, fill=tk.X)

# 添加工具栏按钮
new_button = ttk.Button(toolbar, text="新建", command=new_file)
new_button.pack(side=tk.LEFT, padx=2, pady=2)

open_button = ttk.Button(toolbar, text="打开", command=open_file)
open_button.pack(side=tk.LEFT, padx=2, pady=2)

save_button = ttk.Button(toolbar, text="保存", command=save_file)
save_button.pack(side=tk.LEFT, padx=2, pady=2)

cut_button = ttk.Button(toolbar, text="剪切", command=cut_text)
cut_button.pack(side=tk.LEFT, padx=2, pady=2)

copy_button = ttk.Button(toolbar, text="复制", command=copy_text)
copy_button.pack(side=tk.LEFT, padx=2, pady=2)

paste_button = ttk.Button(toolbar, text="粘贴", command=paste_text)
paste_button.pack(side=tk.LEFT, padx=2, pady=2)

# 运行主循环
root.mainloop()
