import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import TkinterDnD, DND_FILES
import pandas as pd


class ExcelViewerApp(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.title("Excel Viewer")
        self.geometry("800x600")

        self.drop_label = ttk.Label(self, text="Drag and drop an Excel file here")
        self.drop_label.pack(pady=20)

        self.tree = ttk.Treeview(self)
        self.tree.pack(expand=True, fill='both')

        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', self.drop)

    def drop(self, event):
        file_path = event.data.strip('{}')
        if file_path.endswith(('.xls', '.xlsx')):
            self.show_excel(file_path)
        else:
            self.drop_label.config(text="Please drop a valid Excel file")

    def show_excel(self, file_path):
        df = pd.read_excel(file_path)
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = list(df.columns)
        self.tree["show"] = "headings"

        for column in self.tree["columns"]:
            self.tree.heading(column, text=column)

        for index, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))

        self.drop_label.config(text="Drag and drop an Excel file here")


if __name__ == "__main__":
    app = ExcelViewerApp()
    app.mainloop()
