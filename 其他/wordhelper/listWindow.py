from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ListWindow(object):
    def setupUi(self, ListWindow):
        ListWindow.setObjectName("ListWindow")
        ListWindow.resize(800, 588)
        self.centralwidget = QtWidgets.QWidget(ListWindow)
        self.centralwidget.setObjectName("centralwidget")

        self._setup_layouts()
        self._setup_widgets()

        ListWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ListWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        ListWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ListWindow)
        self.statusbar.setObjectName("statusbar")
        ListWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ListWindow)
        QtCore.QMetaObject.connectSlotsByName(ListWindow)

    def _setup_layouts(self):
        self.horizontalLayoutWidget_3 = self._create_layout_widget(self.centralwidget, 20, 443, 761, 31)
        self.horizontalLayout_3 = self._create_hbox_layout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        self.groupBox = self._create_group_box(self.centralwidget, 20, 10, 761, 431)
        self.horizontalLayoutWidget = self._create_layout_widget(self.groupBox, 20, 20, 721, 31)
        self.horizontalLayout = self._create_hbox_layout(self.horizontalLayoutWidget)

        self.groupBox_2 = self._create_group_box(self.centralwidget, 20, 470, 761, 81)
        self.horizontalLayoutWidget_2 = self._create_layout_widget(self.groupBox_2, 20, 30, 721, 31)
        self.horizontalLayout_2 = self._create_hbox_layout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

    def _setup_widgets(self):
        self.checkBox = self._create_check_box(self.horizontalLayoutWidget_3, "checkBox", self.horizontalLayout_3)
        self.executeButton = self._create_push_button(self.horizontalLayoutWidget_3, "executeButton", self.horizontalLayout_3)

        self.label = self._create_label(self.horizontalLayoutWidget, "label", self.horizontalLayout)
        self.sourcepath = self._create_line_edit(self.horizontalLayoutWidget, "sourcepath", self.horizontalLayout)
        self.browseButton = self._create_tool_button(self.horizontalLayoutWidget, "browseButton", self.horizontalLayout)
        self.listword = self._create_list_widget(self.groupBox, 20, 70, 721, 341, "listword")

        self.label_2 = self._create_label(self.horizontalLayoutWidget_2, "label_2", self.horizontalLayout_2)
        self.listfile = self._create_label(self.horizontalLayoutWidget_2, "listfile", self.horizontalLayout_2)
        self.openButton = self._create_push_button(self.horizontalLayoutWidget_2, "openButton", self.horizontalLayout_2)

    def _create_layout_widget(self, parent, x, y, width, height):
        widget = QtWidgets.QWidget(parent)
        widget.setGeometry(QtCore.QRect(x, y, width, height))
        widget.setObjectName(f"horizontalLayoutWidget_{x}_{y}")
        return widget

    def _create_hbox_layout(self, widget):
        layout = QtWidgets.QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setObjectName(f"horizontalLayout_{widget.objectName()}")
        return layout

    def _create_group_box(self, parent, x, y, width, height):
        group_box = QtWidgets.QGroupBox(parent)
        group_box.setGeometry(QtCore.QRect(x, y, width, height))
        group_box.setObjectName(f"groupBox_{x}_{y}")
        return group_box

    def _create_check_box(self, parent, name, layout):
        check_box = QtWidgets.QCheckBox(parent)
        check_box.setObjectName(name)
        layout.addWidget(check_box)
        return check_box

    def _create_push_button(self, parent, name, layout):
        button = QtWidgets.QPushButton(parent)
        button.setObjectName(name)
        layout.addWidget(button)
        return button

    def _create_label(self, parent, name, layout):
        label = QtWidgets.QLabel(parent)
        label.setObjectName(name)
        layout.addWidget(label)
        return label

    def _create_line_edit(self, parent, name, layout):
        line_edit = QtWidgets.QLineEdit(parent)
        line_edit.setObjectName(name)
        layout.addWidget(line_edit)
        return line_edit

    def _create_tool_button(self, parent, name, layout):
        tool_button = QtWidgets.QToolButton(parent)
        tool_button.setObjectName(name)
        layout.addWidget(tool_button)
        return tool_button

    def _create_list_widget(self, parent, x, y, width, height, name):
        list_widget = QtWidgets.QListWidget(parent)
        list_widget.setGeometry(QtCore.QRect(x, y, width, height))
        list_widget.setObjectName(name)
        return list_widget

    def retranslateUi(self, ListWindow):
        _translate = QtCore.QCoreApplication.translate
        ListWindow.setWindowTitle(_translate("ListWindow", "提取总目录"))
        self.checkBox.setText(_translate("ListWindow", "包含页码"))
        self.executeButton.setText(_translate("ListWindow", "开始提取"))
        self.groupBox.setTitle(_translate("ListWindow", "源"))
        self.label.setText(_translate("ListWindow", "请选择Word文档所在目录："))
        self.browseButton.setText(_translate("ListWindow", "..."))
        self.groupBox_2.setTitle(_translate("ListWindow", "结果"))
        self.label_2.setText(_translate("ListWindow", "目录文件保存位置："))
        self.listfile.setText(_translate("ListWindow", "还未提取..."))
        self.openButton.setText(_translate("ListWindow", "打开文件"))
