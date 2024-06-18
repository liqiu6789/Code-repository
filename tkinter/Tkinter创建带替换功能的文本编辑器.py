import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

class TextEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("带查找和替换功能的文本编辑器")
        self.geometry("800x600")

        self.text_area = tk.Text(self, wrap='word')
        self.text_area.pack(expand=1, fill='both')

        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="文件", menu=self.file_menu)
        self.file_menu.add_command(label="新建", command=self.new_file)
        self.file_menu.add_command(label="打开", command=self.open_file)
        self.file_menu.add_command(label="保存", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="退出", command=self.exit_app)

        self.edit_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="编辑", menu=self.edit_menu)
        self.edit_menu.add_command(label="查找", command=self.find_text)
        self.edit_menu.add_command(label="替换", command=self.replace_text)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                                  filetypes=[("所有文件", "*.*"), ("文本文件", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                    filetypes=[("所有文件", "*.*"), ("文本文件", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))

    def exit_app(self):
        self.quit()

    def find_text(self):
        search_string = simpledialog.askstring("查找", "输入要查找的文本:")
        if search_string:
            start_pos = '1.0'
            while True:
                start_pos = self.text_area.search(search_string, start_pos, stopindex=tk.END)
                if not start_pos:
                    messagebox.showinfo("查找", "未找到更多结果。")
                    break
                end_pos = f"{start_pos}+{len(search_string)}c"
                self.text_area.tag_add("highlight", start_pos, end_pos)
                self.text_area.tag_config("highlight", background="yellow")
                start_pos = end_pos

    def replace_text(self):
        find_string = simpledialog.askstring("查找", "输入要查找的文本:")
        replace_string = simpledialog.askstring("替换", "输入替换文本:")
        if find_string and replace_string:
            start_pos = '1.0'
            while True:
                start_pos = self.text_area.search(find_string, start_pos, stopindex=tk.END)
                if not start_pos:
                    messagebox.showinfo("替换", "未找到更多结果。")
                    break
                end_pos = f"{start_pos}+{len(find_string)}c"
                self.text_area.delete(start_pos, end_pos)
                self.text_area.insert(start_pos, replace_string)
                start_pos = f"{start_pos}+{len(replace_string)}c"

if __name__ == "__main__":
    app = TextEditor()
    app.mainloop()
