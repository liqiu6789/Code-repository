from PyQt5 import QtWidgets
import style


class Window(QtWidgets.QWidget):
    def __init__(self, page: str):
        super().__init__()
        self.page = page

        self.setGeometry(150, 150, 400, 400)
        # ================ 布局 =======================
        self.mainLayout = QtWidgets.QVBoxLayout()
        # ================== 输入框 =================
        self.nameLine = QtWidgets.QLineEdit()
        self.familyLine = QtWidgets.QLineEdit()
        self.emailLine = QtWidgets.QLineEdit()
        self.phoneLine = QtWidgets.QLineEdit()
        # ============= 按钮 ================
        if self.page == 'add':
            self.addButton = QtWidgets.QPushButton("添加")
        elif self.page == 'edit':
            self.addButton = QtWidgets.QPushButton("编辑")
        # ============= 数据库 ======================

        self.ui()

    def page_ui(self):
        group_box = QtWidgets.QGroupBox("联系人面板")
        group_box.setStyleSheet(style.add_contact_layout())

        v_form = QtWidgets.QFormLayout()
        h_box = QtWidgets.QHBoxLayout()
        v_box = QtWidgets.QVBoxLayout()

        v_form.setVerticalSpacing(20)
        v_form.addRow("姓名 :", self.nameLine)
        v_form.addRow("姓氏 :", self.familyLine)
        v_form.addRow("电子邮件 :", self.emailLine)
        v_form.addRow("电话 :", self.phoneLine)

        h_box.addLayout(QtWidgets.QVBoxLayout(), 2)
        h_box.addLayout(v_form, 3)
        h_box.addLayout(QtWidgets.QVBoxLayout(), 2)

        v_box.addLayout(QtWidgets.QHBoxLayout(), 1)
        v_box.addLayout(h_box, 3)
        v_box.addLayout(QtWidgets.QHBoxLayout(), 1)

        group_box.setLayout(v_box)

        return group_box

    def ui(self):
        self.mainLayout.addWidget(self.page_ui(), 7)
        self.mainLayout.addWidget(self.addButton, 1)
        self.setLayout(self.mainLayout)
        self.show()
