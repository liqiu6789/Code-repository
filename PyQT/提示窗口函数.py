from PyQt5.QtWidgets import QMessageBox

def show_message_box(self, message):
    """
    显示一个带有指定消息的提示窗口。

    参数:
        message (str): 要在提示窗口中显示的消息文本。
    """
    # 创建一个QMessageBox对象
    msg_box = QMessageBox()
    # 设置消息框的类型为Information
    msg_box.setIcon(QMessageBox.Information)
    # 设置标题和消息文本
    msg_box.setWindowTitle('提示')
    msg_box.setText(message)

    # 显示消息框并等待用户响应
    msg_box.exec_()