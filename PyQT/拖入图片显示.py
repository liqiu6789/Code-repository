import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QDragEnterEvent, QDropEvent
from PyQt5.QtCore import Qt, QFile, QIODevice
from PyQt5.QtCore import QMimeData


class ImageDropWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建布局
        layout = QVBoxLayout()

        # 创建QLabel用于显示图片
        self.label = QLabel(self)
        layout.addWidget(self.label)

        # 设置窗口布局
        self.setLayout(layout)

        # 设置窗口标题和大小
        self.setWindowTitle('Image Dropper')
        self.setGeometry(300, 300, 600, 400)

        # 允许窗口接受拖拽
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QDragEnterEvent):
        # 检查拖拽的数据中是否包含文件
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                if url.scheme() == 'file':
                    event.acceptProposedAction()
                    return
        event.ignore()

    def dropEvent(self, event: QDropEvent):
        # 获取拖拽的文件URL
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                if url.scheme() == 'file':
                    # 从URL获取文件路径
                    file_path = url.toLocalFile()
                    # 加载图片
                    self.loadImage(file_path)
                    # 接收操作
                    event.acceptProposedAction()
                    return
        event.ignore()

    def loadImage(self, file_path):
        # 加载图片并显示
        pixmap = QPixmap(file_path)
        self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.KeepAspectRatio))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageDropWidget()
    ex.show()
    sys.exit(app.exec_())