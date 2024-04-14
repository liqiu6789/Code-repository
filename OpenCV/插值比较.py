import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import cv2

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QGridLayout, QHBoxLayout, QVBoxLayout, \
    QWidget, QPushButton
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import cv2


class ImageResizeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Resize with Interpolation')
        self.setGeometry(100, 100, 1200, 900)

        # 创建垂直布局
        vertical_layout = QVBoxLayout()

        # 创建按钮用于打开文件对话框
        self.open_button = QPushButton('Open Image', self)
        self.open_button.clicked.connect(self.loadImage)
        vertical_layout.addWidget(self.open_button)

        # 创建中心部件
        central_widget = QWidget()
        central_widget.setLayout(vertical_layout)
        self.setCentralWidget(central_widget)

    def loadImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "",
                                                   "All Files (*);;;PNG Files (*.png);;;JPG Files (*.jpg)",
                                                   options=options)
        if file_name:
            # 读取图片
            self.original_image = cv2.imread(file_name)
            # 将图片转换为Qt可以显示的格式
            qt_image = QImage(self.original_image.data, self.original_image.shape[1], self.original_image.shape[0],
                              QImage.Format_RGB888).rgbSwapped()
            self.original_pixmap = QPixmap.fromImage(qt_image)

            # 创建水平布局来放置所有图片
            horizontal_layout = QHBoxLayout()

            # 添加原图
            self.original_label = QLabel(self)
            self.original_label.setPixmap(self.original_pixmap)
            horizontal_layout.addWidget(self.original_label)

            # 创建2x2的网格布局来放置插值图片
            grid_layout = QGridLayout()
            self.interpolation_labels = {}
            interpolations = ['Nearest', 'Linear', 'Cubic', 'Lanczos']
            for i, interpolation in enumerate(interpolations):
                resized_image = self.resizeImage(interpolation)
                qt_resized_image = QImage(resized_image.data, resized_image.shape[1], resized_image.shape[0],
                                          QImage.Format_RGB888).rgbSwapped()
                resized_pixmap = QPixmap.fromImage(qt_resized_image)

                # 创建一个垂直布局，将图片和名字标签放入其中
                vertical_layout = QVBoxLayout()

                label = QLabel(self)
                label.setPixmap(resized_pixmap)
                vertical_layout.addWidget(label)

                name_label = QLabel(interpolation, self)
                #name_label.setAlignment(Qt.AlignVCenter)  # 设置名字标签垂直居中对齐
                vertical_layout.addWidget(name_label)
                vertical_layout.setAlignment(Qt.AlignCenter)
                # 将垂直布局添加到网格布局中
                grid_layout.addLayout(vertical_layout, i // 2, i % 2)

                self.interpolation_labels[interpolation] = (label, name_label)

                # 将网格布局放入一个QWidget中，以便可以添加到水平布局中
            grid_widget = QWidget()
            grid_widget.setLayout(grid_layout)
            horizontal_layout.addWidget(grid_widget)

            # 将水平布局添加到垂直布局中
            vertical_layout = self.centralWidget().layout()
            vertical_layout.addLayout(horizontal_layout)

    def resizeImage(self, interpolation):
        # 原始图片的尺寸
        original_height, original_width = self.original_image.shape[:2]
        new_size = (int(original_width * 2), int(original_height * 2))

        # 使用指定的插值方法进行缩放
        resized_image = cv2.resize(self.original_image, new_size,
                                   interpolation=cv2.INTER_CUBIC if interpolation == 'Cubic' else
                                   cv2.INTER_LANCZOS4 if interpolation == 'Lanczos' else
                                   getattr(cv2, f'INTER_{interpolation.upper()}'))
        return resized_image


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageResizeWindow()
    ex.show()
    sys.exit(app.exec_())