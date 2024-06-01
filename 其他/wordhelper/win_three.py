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
        self.horizontalLayout_3 = self._create_hbox_layout(self.centralwidget, 20, 443, 761, 31)
        self.groupBox = self._create_group_box(self.centralwidget, 20, 10, 761, 431)
        self.horizontalLayout = self._create_hbox_layout(self.groupBox, 20, 20, 721, 31)
        self.groupBox_2 = self._create_group_box(self.centralwidget, 20, 470, 761, 81)
        self.horizontalLayout_2 = self._create_hbox_layout(self.groupBox_2, 20, 30, 721, 31)

    def _setup_widgets(self):
        self.checkBox = self._create_check_box(self.horizontalLayout_3, "checkBox")
        self.executeButton = self._create_push_button(self.horizontalLayout_3, "executeButton")
        self.label = self._create_label(self.horizontalLayout, "label")
        self.sourcepath = self._create_line_edit(self.horizontalLayout, "sourcepath")
        self.browseButton = self._create_tool_button(self.horizontalLayout, "browseButton")
        self.listword = self._create_list_widget(self.groupBox, 20, 70, 721, 341, "listword")
        self.label_2 = self._create_label(self.horizontalLayout_2, "label_2")
        self.listfile = self._create_label(self.horizontalLayout_2, "listfile")
        self.openButton = self._create_push_button(self.horizontalLayout_2, "openButton")

    def _create_hbox_layout(self, parent, x, y, width, height):
        widget = QtWidgets.QWidget(parent)
        widget.setGeometry(QtCore.QRect(x, y, width, height))
        layout = QtWidgets.QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        return layout

    def _create_group_box(self, parent, x, y, width, height):
        group_box = QtWidgets.QGroupBox(parent)
        group_box.setGeometry(QtCore.QRect(x, y, width, height))
        return group_box

    def _create_check_box(self, layout, name):
        check_box = QtWidgets.QCheckBox(layout.parentWidget())
        check_box.setObjectName(name)
        layout.addWidget(check_box)
        return check_box

    def _create_push_button(self, layout, name):
        button = QtWidgets.QPushButton(layout.parentWidget())
        button.setObjectName(name)
        layout.addWidget(button)
        return button

    def _create_label(self, layout, name):
        label = QtWidgets.QLabel(layout.parentWidget())
        label.setObjectName(name)
        layout.addWidget(label)
        return label

    def _create_line_edit(self, layout, name):
        line_edit = QtWidgets.QLineEdit(layout.parentWidget())
        line_edit.setObjectName(name)
        layout.addWidget(line_edit)
        return line_edit

    def _create_tool_button(self, layout, name):
        tool_button = QtWidgets.QToolButton(layout.parentWidget())
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

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 572)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


class Ui_PageWindow(object):
    def setupUi(self, PageWindow):
        PageWindow.setObjectName("PageWindow")
        PageWindow.resize(792, 676)
        self.centralwidget = QtWidgets.QWidget(PageWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = self._create_group_box(self.centralwidget, 20, 10, 761, 281, "groupBox")
        self.horizontalLayout = self._create_hbox_layout(self.groupBox, 20, 20, 721, 31)
        self._setup_source_widgets()
        self.groupBox_2 = self._create_group_box(self.centralwidget, 20, 320, 761, 321, "groupBox_2")
        self._setup_result_table()
        self.horizontalLayout_2 = self._create_hbox_layout(self.groupBox_2, 20, 280, 721, 31)
        self._setup_result_widgets()
        PageWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PageWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 23))
        self.menubar.setObjectName("menubar")
        PageWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PageWindow)
        self.statusbar.setObjectName("statusbar")
        PageWindow.setStatusBar(self.statusbar)
        self.retranslateUi(PageWindow)
        QtCore.QMetaObject.connectSlotsByName(PageWindow)

    def _setup_source_widgets(self):
        self.label = self._create_label(self.horizontalLayout, "label")
        self.sourcepath = self._create_line_edit(self.horizontalLayout, "sourcepath")
        self.browseButton = self._create_tool_button(self.horizontalLayout, "browseButton")
        self.listword = QtWidgets.QListWidget(self.groupBox)
        self.listword.setGeometry(QtCore.QRect(20, 70, 721, 192))
        self.listword.setObjectName("listword")

    def _setup_result_table(self):
        self.pagetable = QtWidgets.QTableWidget(self.groupBox_2)
        self.pagetable.setGeometry(QtCore.QRect(20, 30, 721, 241))
        self.pagetable.setRowCount(1)
        self.pagetable.setColumnCount(2)
        self.pagetable.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("文件名"))
        self.pagetable.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("页码"))
        self.pagetable.horizontalHeader().setDefaultSectionSize(101)
        self.pagetable.setItem(0, 0, QtWidgets.QTableWidgetItem())
        self.pagetable.setItem(0, 1, QtWidgets.QTableWidgetItem())

    def _setup_result_widgets(self):
        self.label_2 = self._create_label(self.horizontalLayout_2, "label_2")
        self.totalpage = QtWidgets.QLabel(self.horizontalLayout_2.parentWidget())
        self.totalpage.setObjectName("totalpage")
        self.horizontalLayout_2.addWidget(self.totalpage)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.executeButton = QtWidgets.QPushButton(self.horizontalLayout_2.parentWidget())
        self.executeButton.setObjectName("executeButton")
        self.horizontalLayout_2.addWidget(self.executeButton)

    def _create_hbox_layout(self, parent, x, y, width, height):
        widget = QtWidgets.QWidget(parent)
        widget.setGeometry(QtCore.QRect(x, y, width, height))
        layout = QtWidgets.QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        return layout

    def _create_group_box(self, parent, x, y, width, height, name):
        group_box = QtWidgets.QGroupBox(parent)
        group_box.setGeometry(QtCore.QRect(x, y, width, height))
        group_box.setObjectName(name)
        return group_box

    def _create_label(self, layout, name):
        label = QtWidgets.QLabel(layout.parentWidget())
        label.setObjectName(name)
        layout.addWidget(label)
        return label

    def _create_line_edit(self, layout, name):
        line_edit = QtWidgets.QLineEdit(layout.parentWidget())
        line_edit.setObjectName(name)
        layout.addWidget(line_edit)
        return line_edit

    def _create_tool_button(self, layout, name):
        tool_button = QtWidgets.QToolButton(layout.parentWidget())
        tool_button.setObjectName(name)
        layout.addWidget(tool_button)
        return tool_button

    def retranslateUi(self, PageWindow):
        _translate = QtCore.QCoreApplication.translate
        PageWindow.setWindowTitle(_translate("PageWindow", "统计Word文档页码"))
        self.groupBox.setTitle(_translate("PageWindow", "源"))
        self.label.setText(_translate("PageWindow", "请选择Word文档所在目录："))
        self.browseButton.setText(_translate("PageWindow", "..."))
        self.groupBox_2.setTitle(_translate("PageWindow", "结果"))
        self.label_2.setText(_translate("PageWindow", "合计页码："))
        self.totalpage.setText(_translate("PageWindow", "未统计"))
        self.executeButton.setText(_translate("PageWindow", "开始统计"))
