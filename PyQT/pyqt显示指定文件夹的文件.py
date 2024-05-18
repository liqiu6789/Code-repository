import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QListView, QFileDialog,QWidget
from PyQt5.QtCore import QDir, QStringListModel
from PyQt5.QtCore import QDir, Qt


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建按钮
        self.button = QPushButton('选择目录', self)
        self.button.clicked.connect(self.selectDirectory)

        # 创建ListView来显示文件列表
        self.listView = QListView(self)
        self.model = QStringListModel()
        self.listView.setModel(self.model)

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.listView)

        # 将布局设置到中央窗口部件
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # 设置窗口标题和大小
        self.setWindowTitle('目录文件列表')
        self.setGeometry(300, 300, 300, 200)

    def selectDirectory(self):
        # 打开目录选择对话框
        directory = QFileDialog.getExistingDirectory(self, "选择目录")

        if directory:
            # 清除旧的文件列表
            self.model.setStringList([])

            # 使用QDir和QStringList遍历目录中的文件
            dir_obj = QDir(directory)
            file_list = dir_obj.entryList(['*'], QDir.Files | QDir.Dirs | QDir.NoDotAndDotDot)

            # 将文件列表转换为QStringList，并设置到模型中
            self.model.setStringList(list(file_list))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyMainWindow()
    ex.show()
    sys.exit(app.exec_())