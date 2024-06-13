import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Tkinter 文本对齐示例")

    # 创建一个Text控件
    text = tk.Text(root, width=40, height=10)
    text.pack()

    # 插入左对齐文本
    text.insert(tk.END, "这是左对齐的文本。\n", "left")
    # 配置左对齐标签
    text.tag_configure("left", justify='left')

    # 插入居中对齐文本
    text.insert(tk.END, "这是居中对齐的文本。\n", "center")
    # 配置居中对齐标签
    text.tag_configure("center", justify='center')

    # 插入右对齐文本
    text.insert(tk.END, "这是右对齐的文本。\n", "right")
    # 配置右对齐标签
    text.tag_configure("right", justify='right')

    # 插入更多示例文本以便展示效果
    text.insert(tk.END, "\n额外的左对齐文本。\n", "left")
    text.insert(tk.END, "额外的居中对齐文本。\n", "center")
    text.insert(tk.END, "额外的右对齐文本。\n", "right")

    root.mainloop()

if __name__ == "__main__":
    main()
