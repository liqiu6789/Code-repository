from PyQt5 import (QtWidgets, QtGui)

import login_app
import home_app
import sys
import request_api


class MainWindow:
    def __init__(self):
        self.api = request_api.ApiRequest()
        self.homeWindow = None
        self.loginWindow = None
        self.admin_name = None
        self.login()

    # ########## 主页选项 >>
    def home_app(self):
        self.loginWindow.destroy()
        self.loginWindow = None
        self.homeWindow = home_app.Window(self.admin_name, self.api)
        self.homeWindow.logoutButton.clicked.connect(self.login)
        self.homeWindow.exitButton.clicked.connect(self.home_exit)

    def home_exit(self):
        if self.homeWindow:

            if QtWidgets.QMessageBox.information(
                    self.homeWindow,
                    "警告",
                    "确定要退出吗？",
                    QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Yes
            ) == QtWidgets.QMessageBox.Yes:

                sys.exit(0)
    # ########## 结束主页选项 <<

    # ########## 登录选项 >>
    def login(self):
        if self.homeWindow:

            if QtWidgets.QMessageBox.information(
                    self.homeWindow,
                    "警告",
                    "确定要注销吗？",
                    QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Yes
            ) == QtWidgets.QMessageBox.Yes:

                self.homeWindow.destroy()
                self.homeWindow = None

        if not self.homeWindow:
            self.loginWindow = login_app.Dialog()
            self.loginWindow.logButton.clicked.connect(self.login_click)
            self.loginWindow.backButton.clicked.connect(self.register)
            self.loginWindow.show()

    def register(self):
        self.loginWindow = login_app.Dialog('reg')
        self.loginWindow.logButton.clicked.connect(self.register_click)
        self.loginWindow.backButton.clicked.connect(self.login)
        self.loginWindow.show()

    def register_click(self):
        user = self.loginWindow.userLine.text().lower()
        password = self.loginWindow.passLine.text()
        c_password = self.loginWindow.confirmPassLine.text()
        if user and password and c_password:
            if password == c_password:
                data = {
                    "username": f"{user}",
                    "password": f"{password}",
                    "is_staff": True,
                    "is_active": True
                }
                url = 'http://127.0.0.1:8000/contact/v1/register/'
                request = self.api.register(data, url)
                if request is True:
                    QtWidgets.QMessageBox.information(self.loginWindow, "警告", '用户已添加。')
                    self.loginWindow.destroy()
                    self.loginWindow = None
                    return self.login()
                else:
                    txt = self.detail_request(request)
                    QtWidgets.QMessageBox.information(self.loginWindow, "警告", txt)

            else:
                QtWidgets.QMessageBox.information(
                    self.loginWindow,
                    "警告",
                    "密码不匹配，请重试"
                )
        else:
            QtWidgets.QMessageBox.information(self.loginWindow, "警告", "字段不能为空")

    def login_click(self):
        user = self.loginWindow.userLine.text().lower()
        password = self.loginWindow.passLine.text()
        if user and password:
            data = {
                "username": f"{user}",
                "password": f"{password}"
            }
            url = 'http://127.0.0.1:8000/contact/v1/token/'
            request = self.api.login(data=data, url=url)
            if request is True:
                self.admin_name = user
                self.home_app()
                # return True
            else:
                QtWidgets.QMessageBox.information(self.loginWindow, "警告", request['detail'])
        else:
            QtWidgets.QMessageBox.information(self.loginWindow, "警告", "字段不能为空")
    # ########## 结束登录选项 <<

    @staticmethod
    def detail_request(request: dict):
        txt = ''
        for i in request:
            txt += str(request[i][0]) + '\n'
        return txt


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    app.setStyle('QtCurve')
    app.setFont(QtGui.QFont("Noto Sans", 10))
    # ['Breeze', 'Oxygen', 'QtCurve', 'Windows', 'Fusion']
    sys.exit(app.exec_())
