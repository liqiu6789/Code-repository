import tkinter as tk
from PIL import Image, ImageTk

# 创建主窗口
root = tk.Tk()
root.title("按钮背景图片示例")

# 加载图片
image = Image.open("new.png")
photo = ImageTk.PhotoImage(image)

# 创建按钮并设置背景图片
button = tk.Button(root, image=photo)
button.pack()

# 运行主循环
root.mainloop()
