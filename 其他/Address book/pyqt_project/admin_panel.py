from PyQt5 import QtWidgets
import style


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 150, 400, 400)
        # ================ 布局 =======================
        self.mainLayout = QtWidgets.QVBoxLayout()
        # ================== 输入框 =================
        self.userLine = QtWidgets.QLineEdit()
        self.nameLine = QtWidgets.QLineEdit()
        self.familyLine = QtWidgets.QLineEdit()
        self.emailLine = QtWidgets.QLineEdit()
        self.activeChekBox = QtWidgets.QCheckBox("活跃")
        self.staffChekBox = QtWidgets.QCheckBox("员工状态")
        # ============= 按钮 ================
        self.updateButton = QtWidgets.QPushButton("更新")
        # ============= 数据库 ======================

        self.ui()

    def page_ui(self):
        group_box = QtWidgets.QGroupBox("管理员面板")
        group_box.setStyleSheet(style.add_contact_layout())

        v_form = QtWidgets.QFormLayout()
        h_box = QtWidgets.QHBoxLayout()
        v_box = QtWidgets.QVBoxLayout()

        v_form.setVerticalSpacing(20)
        v_form.addRow("用户名 :", self.userLine)
        v_form.addRow("姓名 :", self.nameLine)
        v_form.addRow("姓氏 :", self.familyLine)
        v_form.addRow("电子邮件 :", self.emailLine)
        v_form.addRow(self.activeChekBox)
        v_form.addRow(self.staffChekBox)

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
        self.mainLayout.addWidget(self.updateButton, 1)
        self.setLayout(self.mainLayout)
        self.show()

    def set_item(self, data: dict):
        data = data[0]
        self.userLine.setText(data['username'])
        self.nameLine.setText(data['first_name'])
        self.familyLine.setText(data['last_name'])
        self.emailLine.setText(data['email'])
        self.staffChekBox.setChecked(data['is_staff'])
        self.activeChekBox.setChecked(data['is_active'])

    def get_item(self):
        user_name = self.userLine.text()
        name = self.nameLine.text()
        family = self.familyLine.text()
        email = self.emailLine.text()
        staff = self.staffChekBox.isChecked()
        active = self.activeChekBox.isChecked()
        return {
            "username": f"{user_name}",
            "first_name": f"{name}",
            "last_name": f"{family}",
            "email": f"{email}",
            "is_staff": staff,
            "is_active": active
        }
