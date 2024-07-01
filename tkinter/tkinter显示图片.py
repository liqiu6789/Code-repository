import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename(title="选择图片", filetypes=(("PNG文件", "*.png"), ("JPEG文件", "*.jpg;*.jpeg"), ("所有文件", "*.*")))
    if file_path:
        img = Image.open(file_path)
        img = img.resize((300, 300), Image.Resampling.LANCZOS)  # 调整图片大小
        img_tk = ImageTk.PhotoImage(img)
        img_label.config(image=img_tk)
        img_label.image = img_tk  # 防止垃圾回收

root = tk.Tk()
root.title("图片显示示例")

open_button = tk.Button(root, text="打开图片", command=open_image)
open_button.pack(pady=20)

img_label = tk.Label(root)
img_label.pack(pady=20)

root.mainloop()
