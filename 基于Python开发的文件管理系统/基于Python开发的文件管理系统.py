import sys
import os
import shutil
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileSystemModel, QTreeView, QListView, QVBoxLayout, QWidget,
                             QToolBar, QLineEdit, QAction, QFileDialog, QLabel, QSplitter, QHBoxLayout, QMessageBox)
from PyQt5.QtCore import Qt, QDir, QSortFilterProxyModel, QModelIndex
from PyQt5.QtGui import QIcon, QPixmap


class FileManager(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('基于Python开发的文件管理系统')
        self.setGeometry(100, 100, 1000, 600)

        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())

        self.proxyModel = QSortFilterProxyModel()
        self.proxyModel.setSourceModel(self.model)
        self.proxyModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.proxyModel.setFilterKeyColumn(0)  # Apply filter to the file names

        self.treeView = QTreeView()
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(QDir.rootPath()))
        self.treeView.setColumnWidth(0, 250)
        self.treeView.setAlternatingRowColors(True)
        self.treeView.setSelectionMode(QTreeView.ExtendedSelection)

        self.listView = QListView()
        self.listView.setModel(self.proxyModel)
        self.listView.setRootIndex(self.proxyModel.mapFromSource(self.model.index(QDir.rootPath())))
        self.listView.setAlternatingRowColors(True)
        self.listView.setSelectionMode(QListView.ExtendedSelection)

        self.treeView.clicked.connect(self.onTreeViewClicked)
        self.listView.doubleClicked.connect(self.onListViewDoubleClicked)

        self.searchBar = QLineEdit()
        self.searchBar.setPlaceholderText('搜索文件...')
        self.searchBar.textChanged.connect(self.searchFiles)

        self.previewLabel = QLabel('文件预览')
        self.previewLabel.setAlignment(Qt.AlignCenter)
        self.previewLabel.setStyleSheet('background-color: white; border: 1px solid black;')
        self.previewLabel.setWordWrap(True)

        self.toolbar = self.addToolBar('Toolbar')
        self.createActions()

        mainLayout = QVBoxLayout()
        searchLayout = QHBoxLayout()
        searchLayout.addWidget(self.searchBar)
        mainLayout.addLayout(searchLayout)

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.treeView)
        splitter.addWidget(self.listView)
        splitter.addWidget(self.previewLabel)
        splitter.setSizes([200, 400, 400])
        mainLayout.addWidget(splitter)

        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)

    def createActions(self):
        copyAction = QAction('复制', self)
        copyAction.triggered.connect(self.copyFile)
        self.toolbar.addAction(copyAction)
        self.addAction(copyAction)

        moveAction = QAction('移动', self)
        moveAction.triggered.connect(self.moveFile)
        self.toolbar.addAction(moveAction)
        self.addAction(moveAction)

        deleteAction = QAction('删除', self)
        deleteAction.triggered.connect(self.deleteFile)
        self.toolbar.addAction(deleteAction)
        self.addAction(deleteAction)

        viewListAction = QAction('列表视图', self)
        viewListAction.triggered.connect(self.setListView)
        self.toolbar.addAction(viewListAction)
        self.addAction(viewListAction)

        viewIconAction = QAction('图标视图', self)
        viewIconAction.triggered.connect(self.setIconView)
        self.toolbar.addAction(viewIconAction)
        self.addAction(viewIconAction)

    def onTreeViewClicked(self, index):
        path = self.model.filePath(index)
        self.listView.setRootIndex(self.proxyModel.mapFromSource(self.model.index(path)))

    def onListViewDoubleClicked(self, index):
        path = self.model.filePath(self.proxyModel.mapToSource(index))
        if os.path.isfile(path):
            self.previewFile(path)

    def previewFile(self, path):
        if path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            pixmap = QPixmap(path)
            self.previewLabel.setPixmap(pixmap.scaled(self.previewLabel.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        elif path.lower().endswith(('.txt', '.py', '.log', '.md')):
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            self.previewLabel.setText(content)
        else:
            self.previewLabel.setText(f'预览: {path}')

    def searchFiles(self):
        searchText = self.searchBar.text()
        self.proxyModel.setFilterRegExp(searchText)
        self.updateListView()

    def updateListView(self):
        currentIndex = self.treeView.currentIndex()
        path = self.model.filePath(currentIndex)
        self.listView.setRootIndex(self.proxyModel.mapFromSource(self.model.index(path)))

    def copyFile(self):
        selectedIndexes = self.listView.selectedIndexes()
        if not selectedIndexes:
            return
        srcPath = self.model.filePath(self.proxyModel.mapToSource(selectedIndexes[0]))
        dstPath = QFileDialog.getExistingDirectory(self, '选择目标文件夹')
        if dstPath:
            shutil.copy(srcPath, dstPath)

    def moveFile(self):
        selectedIndexes = self.listView.selectedIndexes()
        if not selectedIndexes:
            return
        srcPath = self.model.filePath(self.proxyModel.mapToSource(selectedIndexes[0]))
        dstPath = QFileDialog.getExistingDirectory(self, '选择目标文件夹')
        if dstPath:
            shutil.move(srcPath, dstPath)

    def deleteFile(self):
        selectedIndexes = self.listView.selectedIndexes()
        if not selectedIndexes:
            return
        reply = QMessageBox.question(self, '确认删除', '确定要删除选中的文件吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            for index in selectedIndexes:
                path = self.model.filePath(self.proxyModel.mapToSource(index))
                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.remove(path)

    def setListView(self):
        self.listView.setViewMode(QListView.ListMode)

    def setIconView(self):
        self.listView.setViewMode(QListView.IconMode)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileManager()
    ex.show()
    sys.exit(app.exec_())
