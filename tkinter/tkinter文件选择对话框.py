import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(title="选择一个文件",
                                           filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            text.delete('1.0', tk.END)
            text.insert(tk.END, content)
        print(f"打开的文件: {file_path}")

def save_file():
    file_path = filedialog.asksaveasfilename(title="保存文件",
                                             defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            content = text.get('1.0', tk.END)
            file.write(content)
        print(f"保存的文件: {file_path}")

def main():
    global text
    root = tk.Tk()
    root.title("Tkinter 文件选择对话框示例")

    # 创建Text控件
    text = tk.Text(root, width=50, height=20)
    text.pack(padx=10, pady=10)

    # 创建打开文件按钮
    open_button = tk.Button(root, text="打开文件", command=open_file)
    open_button.pack(side=tk.LEFT, padx=10, pady=10)

    # 创建保存文件按钮
    save_button = tk.Button(root, text="保存文件", command=save_file)
    save_button.pack(side=tk.RIGHT, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
