import sys

from PyQt5.Qt import pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMenu, QAction


class CustomMessageBox(QWidget):
    signal_def = pyqtSignal(str)  # 定义自定义信号，传递一个str参数，也可以是其他类型

    def __init__(self):
        super().__init__()
        self.setWindowTitle("名字修改")
        self.resize(240, 130)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setPlaceholderText('输入内容')
        self.lineEdit.setGeometry(20, 10, 200, 30)
        self.button = QPushButton('确定', self)
        self.button.move(20, 50)
        self.button.clicked.connect(self.enter_name)
        self.quit = QPushButton('取消', self)
        self.quit.move(145, 50)
        self.quit.clicked.connect(self.quit_win)

    def enter_name(self):
        text = self.lineEdit.text()
        self.signal_def.emit(str(text))
        self.close()

    def quit_win(self):
        self.close()


class FolderFileUi(QWidget):
    def __init__(self):
        super().__init__()
        # file_type：1代表文件夹，0代表文件
        self.resize(300, 200)
        self.folds_name_label = QLabel("测试标签", self)
        self.folds_name_label.move(100, 30)

    def contextMenuEvent(self, evt) -> None:
        menu = QMenu(parent=self)
        rename = QAction('重命名')
        rename.triggered.connect(self.rename_fun)
        del_btn = QAction('删除')
        del_btn.triggered.connect(self.del_fun)
        menu.addAction(rename)
        menu.addAction(del_btn)
        menu.exec(evt.globalPos())

    def rename_fun(self):
        # 实例化子窗口
        self.w = CustomMessageBox()
        self.w.show()
        # 绑定自定义信号到deal_emit_dir_slot函数，deal_emit_dir_slot函数用于接收信号后的操作
        self.w.signal_def.connect(self.deal_emit_dir_slot)

    def deal_emit_dir_slot(self, text):
        # 把标签名更新为子窗口传递过来的text
        self.folds_name_label.setText(text)
        self.folds_name_label.update()
        self.folds_name_label.adjustSize()

    def del_fun(self):
        self.folds_image_label.deleteLater()
        self.folds_name_label.deleteLater()
        self.deleteLater()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = FolderFileUi()
    demo.show()
    sys.exit(app.exec_())

