import tkinter as tk
from tkinter import ttk, colorchooser, filedialog, messagebox, font
import os

def create_toolbar_button(parent, image_path, row, column, command=None):
    icon = tk.PhotoImage(file=image_path)
    btn = ttk.Button(parent, image=icon, command=command)
    btn.image = icon  # 保持引用，防止图像被垃圾回收
    btn.grid(row=row, column=column, padx=5)
    return btn

def create_menu_command(menu, label, icon, accelerator, command):
    menu.add_command(label=label, image=icon, compound=tk.LEFT, accelerator=accelerator, command=command)

main_application = tk.Tk()
main_application.geometry('1200x600')
main_application.title("基于Python开发的文本编辑器")

main_menu = tk.Menu()
file = tk.Menu(main_menu, tearoff=False)
edit = tk.Menu(main_menu, tearoff=False)
view = tk.Menu(main_menu, tearoff=False)
color_theme = tk.Menu(main_menu, tearoff=False)

main_menu.add_cascade(label="文件", menu=file)
main_menu.add_cascade(label="编辑", menu=edit)
main_menu.add_cascade(label="视图", menu=view)
main_menu.add_cascade(label="主题", menu=color_theme)

icon_paths = [
    "icon/new.png", "icon/open.png", "icon/save.png", "icon/save_as.png", "icon/exit.png",
    "icon/copy.png", "icon/paste.png", "icon/cut.png", "icon/clear_all.png", "icon/find.png",
    "icon/tool_bar.png", "icon/status_bar.png", "icon/light_default.png", "icon/light_plus.png",
    "icon/dark.png", "icon/red.png", "icon/monokai.png", "icon/night_blue.png"
]

icons = [tk.PhotoImage(file=path) for path in icon_paths]

(
    new_icon, open_icon, save_icon, save_as_icon, exit_icon,
    copy_icon, paste_icon, cut_icon, clear_all_icon, find_icon,
    tool_bar_icon, status_bar_icon, light_default_icon, light_plus_icon,
    dark_icon, red_icon, monokai_icon, night_blue_icon
) = icons

color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)
theme_choice = tk.StringVar()

color_dict = {
    "Light Default": ("#000000", "#ffffff"),
    "Light Plus": ("#474747", "#e0e0e0"),
    "Dark": ("#c4c4c4", "#2d2d2d"),
    "Red": ("#2d2d2d", "#ffe8e8"),
    "Monokai": ("#d3b774", "#474747"),
    "Night Blue": ("#ededed", "#6b9dc2")
}

tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)

font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state="readonly")
font_box["values"] = font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0, column=0, padx=5)

size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=14, textvariable=size_var, state="readonly")
font_size["values"] = tuple(range(8, 80, 2))
font_size.current(3)
font_size.grid(row=0, column=1, padx=5)

button_configs = [
    ("icon/bold.png", 0, 2, None),
    ("icon/italic.png", 0, 3, None),
    ("icon/underline.png", 0, 4, None),
    ("icon/font_color.png", 0, 5, None),
    ("icon/align_left.png", 0, 6, None),
    ("icon/align_center.png", 0, 7, None),
    ("icon/align_right.png", 0, 8, None)
]

buttons = [create_toolbar_button(tool_bar, *config) for config in button_configs]

text_editor = tk.Text(main_application, wrap="word", relief=tk.FLAT)
text_editor.pack(fill=tk.BOTH, expand=True)

scroll_bar = tk.Scrollbar(main_application)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

current_font_family = "Arial"
current_font_size = 12

def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))

def change_font_size(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))

font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_font_size)

def change_bold():
    text_property = tk.font.Font(font=text_editor["font"])
    if text_property.actual()["weight"] == "normal":
        text_editor.config(font=(current_font_family, current_font_size, "bold"))
    elif text_property.actual()["weight"] == "bold":
        text_editor.config(font=(current_font_family, current_font_size, "normal"))

buttons[0].configure(command=change_bold)

def change_italic():
    text_property = tk.font.Font(font=text_editor["font"])
    if text_property.actual()["slant"] == "roman":
        text_editor.config(font=(current_font_family, current_font_size, "italic"))
    elif text_property.actual()["slant"] == "italic":
        text_editor.config(font=(current_font_family, current_font_size, "normal"))

buttons[1].configure(command=change_italic)

def change_underline():
    text_property = tk.font.Font(font=text_editor["font"])
    if text_property.actual()["underline"] == 0:
        text_editor.config(font=(current_font_family, current_font_size, "underline"))
    elif text_property.actual()["underline"] == 1:
        text_editor.config(font=(current_font_family, current_font_size, "normal"))

buttons[2].configure(command=change_underline)

def change_font_color():
    color_var = tk.colorchooser.askcolor()[1]
    if color_var:
        text_editor.configure(fg=color_var)

buttons[3].configure(command=change_font_color)

def align_text(align):
    text_content = text_editor.get(1.0, "end")
    text_editor.tag_config(align, justify=align)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, align)

buttons[4].configure(command=lambda: align_text(tk.LEFT))
buttons[5].configure(command=lambda: align_text(tk.CENTER))
buttons[6].configure(command=lambda: align_text(tk.RIGHT))

text_editor.configure(font=("Arial", 12))

status_bar = ttk.Label(main_application, text="状态栏")
status_bar.pack(side=tk.BOTTOM)

text_changed = False

def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, "end-1c").split())
        characters = len(text_editor.get(1.0, "end-1c"))
        status_bar.config(text=f'字符数: {characters} 词数: {words}')
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>", changed)

url = ""

def new_file(event=None):
    global url
    url = ""
    text_editor.delete(1.0, tk.END)

def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title="选择文件", filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
    try:
        with open(url, "r") as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except Exception as e:
        messagebox.showerror("错误", f"无法打开文件: {e}")
    main_application.title(os.path.basename(url))

def save_file(event=None):
    global url
    try:
        if url:
            content = text_editor.get(1.0, tk.END)
            with open(url, "w", encoding="utf-8") as fw:
                fw.write(content)
        else:
            save_as()
    except Exception as e:
        messagebox.showerror("错误", f"无法保存文件: {e}")

def save_as(event=None):
    global url
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text File", "*.txt"), ("All Files", "*.*")])
        if url:
            with open(url, "w", encoding="utf-8") as fw:
                fw.write(content)
    except Exception as e:
        messagebox.showerror("错误", f"无法保存文件: {e}")

def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel("请稍等！", "您要保存文件吗？")
            if mbox:
                save_file()
            if mbox is not None:
                main_application.destroy()
        else:
            main_application.destroy()
    except Exception as e:
        messagebox.showerror("错误", f"无法退出: {e}")

create_menu_command(file, "新建", new_icon, "Ctrl+N", new_file)
create_menu_command(file, "打开", open_icon, "Ctrl+O", open_file)
create_menu_command(file, "保存", save_icon, "Ctrl+S", save_file)
create_menu_command(file, "另存为", save_as_icon, "Ctrl+Alt+S", save_as)
create_menu_command(file, "退出", exit_icon, "Ctrl+Q", exit_func)

def find_func(event=None):
    def find():
        word = find_input.get()
        text_editor.tag_remove('match', "1.0", tk.END)
        matches = 0
        if word:
            start_pos = "1.0"
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                text_editor.tag_add("match", start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config("match", foreground="yellow", background="green")

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry("375x250+500+200")
    find_dialogue.title("查找")
    find_dialogue.resizable(0, 0)

    find_frame = ttk.LabelFrame(find_dialogue, text="查找/替换")
    find_frame.pack(pady=20)

    text_find_label = ttk.Label(find_frame, text="查找: ")
    text_replace_label = ttk.Label(find_frame, text="替换:")

    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    find_button = ttk.Button(find_frame, text="查找", command=find)
    replace_button = ttk.Button(find_frame, text="替换", command=replace)

    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=2, padx=8, pady=4)

    find_dialogue.mainloop()

create_menu_command(edit, "复制", copy_icon, "Ctrl+C", lambda: text_editor.event_generate("<Control c>"))
create_menu_command(edit, "粘贴", paste_icon, "Ctrl+V", lambda: text_editor.event_generate("<Control v>"))
create_menu_command(edit, "剪切", cut_icon, "Ctrl+X", lambda: text_editor.event_generate("<Control x>"))
create_menu_command(edit, "清空", clear_all_icon, "Ctrl+Alt+X", lambda: text_editor.delete(1.0, tk.END))
create_menu_command(edit, "查找", find_icon, "Ctrl+F", find_func)

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)

show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def toggle_widget(widget, var):
    if var.get():
        widget.pack(side=tk.BOTTOM if widget == status_bar else tk.TOP, fill=tk.X)
    else:
        widget.pack_forget()

view.add_checkbutton(label="工具栏", onvalue=True, offvalue=False, variable=show_toolbar, image=tool_bar_icon, compound=tk.LEFT, command=lambda: toggle_widget(tool_bar, show_toolbar))
view.add_checkbutton(label="状态栏", onvalue=True, offvalue=False, variable=show_statusbar, image=status_bar_icon, compound=tk.LEFT, command=lambda: toggle_widget(status_bar, show_statusbar))

def change_theme():
    chosen_theme = theme_choice.get()
    fg_color, bg_color = color_dict[chosen_theme]
    text_editor.config(background=bg_color, fg=fg_color)

for count, (theme_name, colors) in enumerate(color_dict.items()):
    color_theme.add_radiobutton(label=theme_name, image=color_icons[count], variable=theme_choice, compound=tk.LEFT, command=change_theme)

main_application.config(menu=main_menu)

main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-n>", new_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Alt-s>", save_as)
main_application.bind("<Control-q>", exit_func)
main_application.bind("<Control-f>", find_func)

main_application.mainloop()
