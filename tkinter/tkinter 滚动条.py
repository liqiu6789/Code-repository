import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("Tkinter滚动条")

    # 创建一个Text控件
    text = tk.Text(root, wrap='none', width=40, height=10)
    text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # 创建一个垂直滚动条并将其与Text控件关联
    v_scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
    v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text.configure(yscrollcommand=v_scrollbar.set)

    # 创建一个水平滚动条并将其与Text控件关联
    h_scrollbar = ttk.Scrollbar(root, orient='horizontal', command=text.xview)
    h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
    text.configure(xscrollcommand=h_scrollbar.set)

    # 向Text控件中插入一些文本以便演示滚动功能
    for i in range(1, 51):
        text.insert(tk.END, f"This is line number {i}\n")

    root.mainloop()

if __name__ == "__main__":
    main()
