import os
import io
import sys
from PyQt5.QtGui import QIcon, QFontDatabase
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui
from PIL import Image, ImageDraw, ImageFont


class BirthdayCardGUI(QtWidgets.QWidget):
    def __init__(self):
        super(BirthdayCardGUI, self).__init__()
        self.initUI()

    def initUI(self):
        # 窗口设置
        self.setFixedSize(1200, 900)
        self.setWindowTitle('基于Python开发的生日祝福生成系统')
        self.setWindowIcon(QIcon('icon/icon.png'))

        # 一些全局变量
        self.card_image = None
        self.font_size = 35

        # 定义组件
        self.content_label = QLabel('选择内容:')
        self.bg_label = QLabel('背景图片:')
        self.font_label = QLabel('选择字体:')
        self.fontcolor_label = QLabel('字体颜色:')
        self.show_label = QLabel()
        self.show_label.setScaledContents(True)
        self.show_label.setFixedSize(1100, 600)  # 设置显示大小

        self.content_edit = QLineEdit()
        self.content_edit.setText('contents/birthday.txt')
        self.bg_edit = QLineEdit()
        self.bg_edit.setText('bgimages/1.png')
        self.font_combobox = QComboBox()  # 使用下拉列表选择字体

        self.choose_content_button = QPushButton('选择内容')
        self.choose_bg_button = QPushButton('选择背景')
        self.generate_button = QPushButton('生成祝福')
        self.save_button = QPushButton('保存祝福')

        self.font_color_combobox = QComboBox()
        colors = [
            'red', 'white', 'black', 'blue', 'yellow', 'green', 'purple', 'orange',
            'pink', 'brown', 'gray', 'cyan', 'magenta', 'lime', 'maroon',
            'navy', 'olive', 'teal', 'violet', 'gold'
        ]
        for color in colors:
            self.font_color_combobox.addItem(color)
        for item in (self.choose_content_button, self.choose_bg_button, self.generate_button, self.save_button):
            item.setFixedHeight(30)
        self.font_color_combobox.setFixedWidth(1100)
        self.font_combobox.setFixedWidth(1100)

        common_chinese_fonts = ["宋体", "新罗马", "仿宋", "微软雅黑","黑体","楷体"]
        for font in common_chinese_fonts:
            if font not in common_chinese_fonts:
                common_chinese_fonts.append(font)

        self.font_combobox.addItems(common_chinese_fonts)

        # 布局设置
        main_layout = QVBoxLayout()
        input_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        display_layout = QVBoxLayout()
        show_label_layout = QHBoxLayout()

        content_layout = QHBoxLayout()
        content_layout.addWidget(self.content_label)
        content_layout.addWidget(self.content_edit)
        content_layout.addWidget(self.choose_content_button)

        bg_layout = QHBoxLayout()
        bg_layout.addWidget(self.bg_label)
        bg_layout.addWidget(self.bg_edit)
        bg_layout.addWidget(self.choose_bg_button)

        font_layout = QHBoxLayout()
        font_layout.addWidget(self.font_label)
        font_layout.addWidget(self.font_combobox)

        font_color_layout = QHBoxLayout()
        font_color_layout.addWidget(self.fontcolor_label)
        font_color_layout.addWidget(self.font_color_combobox)

        input_layout.addLayout(content_layout)
        input_layout.addLayout(bg_layout)
        input_layout.addLayout(font_layout)
        input_layout.addLayout(font_color_layout)

        button_layout.addWidget(self.generate_button)
        button_layout.addWidget(self.save_button)

        show_label_layout.addStretch(1)
        show_label_layout.addWidget(self.show_label)
        show_label_layout.addStretch(1)

        display_layout.addLayout(show_label_layout)

        main_layout.addLayout(input_layout)
        main_layout.addLayout(button_layout)
        main_layout.addLayout(display_layout)

        self.setLayout(main_layout)

        # 事件绑定
        self.choose_content_button.clicked.connect(self.open_content_filepath)
        self.choose_bg_button.clicked.connect(self.open_bg_filepath)
        self.generate_button.clicked.connect(self.generate_card)
        self.save_button.clicked.connect(self.save_card)
        self.generate_card()

    def generate_card(self):
        content_path = self.content_edit.text()
        bg_path = self.bg_edit.text()
        font_family = self.font_combobox.currentText()
        font_color = self.font_color_combobox.currentText()

        if not all(map(self.check_filepath, [content_path, bg_path])):
            self.card_image = None
            return

        contents = open(content_path, encoding='utf-8').read().split('\n')

        # 获取系统字体文件路径
        font_path = self.get_font_path(font_family)

        if font_path is None:
            QMessageBox.critical(self, "错误", "无法找到所选字体的文件路径")
            return

        font_card = ImageFont.truetype(font_path, self.font_size)
        image = Image.open(bg_path).convert('RGB')
        draw = ImageDraw.Draw(image)

        if contents:
            draw.text((180, 30), contents[0], font=font_card, fill=font_color)
            for idx, content in enumerate(contents[1:]):
                draw.text((220, 40 + (idx + 1) * 40), content, font=font_card, fill=font_color)
                draw.text((180, 40 + (idx + 2) * 40 + 10), contents[-1], font=font_card, fill=font_color)

        self.display_image(image)
        self.card_image = image

    def get_font_path(self, font_family):
        font_paths = {
            "宋体": "C:\\Windows\\Fonts\\simsun.ttc",
            "新罗马": "C:\\Windows\\Fonts\\times.ttf",
            "SimSun": "C:\\Windows\\Fonts\\simsun.ttc",
            "SimHei": "C:\\Windows\\Fonts\\simhei.ttf",
            "楷体": "C:\\Windows\\Fonts\\simkai.ttf",
            "仿宋": "C:\\Windows\\Fonts\\simfang.ttf",
            "微软雅黑": "C:\\Windows\\Fonts\\msyh.ttc",
            "Microsoft JhengHei": "C:\\Windows\\Fonts\\msjh.ttc",
            # 添加其他常用字体的路径
        }
        return font_paths.get(font_family, None)

    def open_content_filepath(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "请选取祝福卡内容文件", '.',
                                                  "Text Files (*.txt);;All Files (*)")
        if filepath:
            self.content_edit.setText(filepath)

    def open_bg_filepath(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "请选取祝福卡背景图片", '.',
                                                  "Image Files (*.png *.jpg *.bmp);;All Files (*)")
        if filepath:
            self.bg_edit.setText(filepath)

    def save_card(self):
        if not self.card_image:
            return
        filename, _ = QFileDialog.getSaveFileName(self, '保存', './birthday_card.jpg',
                                                  'JPEG Image (*.jpg);;All Files (*)')
        if filename:
            self.card_image.save(filename)

    def check_filepath(self, filepath):
        return os.path.isfile(filepath)

    def display_image(self, image):
        fp = io.BytesIO()
        image.save(fp, 'BMP')
        qtimg = QtGui.QImage()
        qtimg.loadFromData(fp.getvalue(), 'BMP')
        qtimg_pixmap = QtGui.QPixmap.fromImage(qtimg)
        self.show_label.setPixmap(qtimg_pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = BirthdayCardGUI()
    gui.show()
    sys.exit(app.exec_())
