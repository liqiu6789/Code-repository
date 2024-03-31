from PyQt5.Qt import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLabel


class ButtonImage(QPushButton):
    def __init__(self, name_label, image_url):
        super().__init__()
        self.initUI(name_label, image_url)

    def initUI(self, name_label, image_url):
        self.resize(300, 300)
        # 使用内部布局
        self.layout = QVBoxLayout(self)
        # 设置标签居中
        alignment = Qt.AlignHCenter | Qt.AlignVCenter
        # 创建并设置名称标签
        self.name_label = QLabel(name_label)
        self.name_label.setAlignment(alignment)
        # 创建并设置图片标签
        self.image_label = QLabel()
        pixmap = QPixmap(image_url)
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(alignment)
        # 将标签添加到布局中
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.name_label)



