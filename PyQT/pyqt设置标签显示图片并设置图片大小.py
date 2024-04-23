from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 创建一个 QVBoxLayout
        layout = QVBoxLayout()

        # 创建一个 QLabel
        label = QLabel(self)

        # 加载图片并缩放到 100x100 像素
        pixmap = QPixmap('1.png').scaled(800, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # 设置 QLabel 的 pixmap
        label.setPixmap(pixmap)

        # 将 QLabel 添加到布局中
        layout.addWidget(label)

        # 设置窗口的布局
        self.setLayout(layout)


if __name__ == '__main__':
    import sys
    from PyQt5.QtCore import Qt

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())