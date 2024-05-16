import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QListView, QFileDialog, QWidget
from PyQt5.QtCore import QDir, QStringListModel, QModelIndex, Qt


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

        # 当列表项被点击时触发事件
        self.listView.clicked.connect(self.on_listView_clicked)

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

        # 成员变量，用于存储最后选择的目录
        self.last_directory = ''

    def selectDirectory(self):
        # 打开目录选择对话框
        directory = QFileDialog.getExistingDirectory(self, "选择目录")

        if directory:
            # 清除旧的文件列表
            self.model.setStringList([])

            # 使用QDir和QStringList遍历目录中的文件
            dir_obj = QDir(directory)
            # 过滤出文件和目录（不包括.和..），但我们可以进一步过滤只显示图片文件
            file_filter = QDir.Files | QDir.Dirs | QDir.NoDotAndDotDot
            file_list = dir_obj.entryList(['*.png', '*.jpg', '*.jpeg', '*.bmp', '*.gif'], file_filter)

            # 将文件列表转换为QStringList，并设置到模型中
            self.model.setStringList(file_list)

            # 存储最后选择的目录
            self.last_directory = directory

    def on_listView_clicked(self, index):
        # 检查点击的项是否是一个文件（而不是目录）
        if not index.isValid():
            return

            # 获取当前点击的文件的名称
        file_name = self.model.stringList()[index.row()]

        # 假设你已经选择了包含图片文件的目录，构建文件的完整路径
        file_path = os.path.join(self.last_directory, file_name)

        # 检查文件是否存在，并且是一个文件（而不是目录）
        if os.path.isfile(file_path):
            # 使用 os.startfile 在 Windows 上预览图片
            os.startfile(file_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyMainWindow()
    ex.show()
    sys.exit(app.exec_())