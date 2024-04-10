import sys
import base64
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class ImageConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('图片转换工具')
        self.setGeometry(300, 300, 800, 600)

        # 创建控件
        self.openButton = QPushButton('打开图片', self)
        self.openButton.clicked.connect(self.openImage)

        self.imagePathEdit = QLineEdit(self)
        self.imagePathEdit.setReadOnly(True)

        self.convertButton = QPushButton('开始转换', self)
        self.convertButton.clicked.connect(self.convertImageToBase64)

        self.imageLabel = QLabel(self)
        self.imageLabel.setAlignment(Qt.AlignCenter)

        # 布局设置
        layout = QVBoxLayout()
        layout.addWidget(self.openButton)
        layout.addWidget(self.imagePathEdit)
        layout.addWidget(self.convertButton)
        layout.addWidget(self.imageLabel)

        self.setLayout(layout)

    def openImage(self):
        fileName, _ = QFileDialog.getOpenFileName(self, '打开图片', '', 'Image Files (*.png *.jpg *.bmp)')
        if fileName:
            self.imagePathEdit.setText(fileName)
            pixmap = QPixmap(fileName)
            self.imageLabel.setPixmap(pixmap.scaled(self.imageLabel.size(), Qt.KeepAspectRatio))

    def convertImageToBase64(self):
        imagePath = self.imagePathEdit.text()
        if imagePath:
            with open(imagePath, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

            txtPath = imagePath.rsplit('.', 1)[0] + '.txt'
            with open(txtPath, 'w') as txt_file:
                txt_file.write(encoded_string)

            print(f'图片已转换为Base64编码并保存到 {txtPath}')
        else:
            print('请先选择图片')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageConverter()
    ex.show()
    sys.exit(app.exec_())