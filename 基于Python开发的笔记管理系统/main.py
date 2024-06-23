import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit,
                             QListWidget, QVBoxLayout, QWidget,
                             QPushButton, QLineEdit, QLabel, QHBoxLayout, QInputDialog, QMessageBox, QToolBar, QAction)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QDateTime


class Note:
    def __init__(self, title, content, tags, date):
        self.title = title
        self.content = content
        self.tags = tags
        self.date = date


class NoteApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.notes = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('基于Python开发的笔记管理系统')
        self.setGeometry(100, 100, 800, 600)

        # Widgets
        self.noteListLabel = QLabel('笔记列表:')
        self.noteList = QListWidget()
        self.noteContentLabel = QLabel('笔记内容:')
        self.noteContent = QTextEdit()
        self.titleInput = QLineEdit()
        self.tagInput = QLineEdit()

        # Buttons
        self.newBtn = QPushButton('新建')
        self.saveBtn = QPushButton('保存')
        self.deleteBtn = QPushButton('删除')
        self.filterBtn = QPushButton('按标签过滤')

        # Layouts
        layout = QVBoxLayout()
        hLayout = QHBoxLayout()
        hLayout.addWidget(QLabel('标题:'))
        hLayout.addWidget(self.titleInput)
        hLayout.addWidget(QLabel('标签:'))
        hLayout.addWidget(self.tagInput)

        btnLayout = QHBoxLayout()
        btnLayout.addWidget(self.newBtn)
        btnLayout.addWidget(self.saveBtn)
        btnLayout.addWidget(self.deleteBtn)
        btnLayout.addWidget(self.filterBtn)

        layout.addLayout(hLayout)
        layout.addWidget(self.noteListLabel)
        layout.addWidget(self.noteList)
        layout.addWidget(self.noteContentLabel)
        layout.addWidget(self.noteContent)
        layout.addLayout(btnLayout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Toolbar for rich text
        self.createToolbar()

        # Signals
        self.newBtn.clicked.connect(self.newNote)
        self.saveBtn.clicked.connect(self.saveNote)
        self.deleteBtn.clicked.connect(self.deleteNote)
        self.filterBtn.clicked.connect(self.filterNotes)
        self.noteList.itemClicked.connect(self.loadNote)

    def createToolbar(self):
        toolbar = QToolBar()

        boldAction = QAction('加粗', self)
        boldAction.triggered.connect(self.makeBold)
        toolbar.addAction(boldAction)

        italicAction = QAction('斜体', self)
        italicAction.triggered.connect(self.makeItalic)
        toolbar.addAction(italicAction)

        underlineAction = QAction('下划线', self)
        underlineAction.triggered.connect(self.makeUnderline)
        toolbar.addAction(underlineAction)

        self.addToolBar(toolbar)

    def makeBold(self):
        if self.noteContent.fontWeight() == QFont.Bold:
            self.noteContent.setFontWeight(QFont.Normal)
        else:
            self.noteContent.setFontWeight(QFont.Bold)

    def makeItalic(self):
        state = self.noteContent.fontItalic()
        self.noteContent.setFontItalic(not state)

    def makeUnderline(self):
        state = self.noteContent.fontUnderline()
        self.noteContent.setFontUnderline(not state)

    def newNote(self):
        self.titleInput.clear()
        self.tagInput.clear()
        self.noteContent.clear()
        self.noteList.clearSelection()

    def saveNote(self):
        title = self.titleInput.text()
        content = self.noteContent.toHtml()  # Save as HTML for rich text
        tags = self.tagInput.text().split(',')
        date = QDateTime.currentDateTime()

        if self.noteList.currentItem():
            current_note = self.notes[self.noteList.currentRow()]
            current_note.title = title
            current_note.content = content
            current_note.tags = tags
            current_note.date = date
        else:
            new_note = Note(title, content, tags, date)
            self.notes.append(new_note)
            self.noteList.addItem(title)

    def deleteNote(self):
        if self.noteList.currentItem():
            del self.notes[self.noteList.currentRow()]
            self.noteList.takeItem(self.noteList.currentRow())

    def loadNote(self, item):
        selected_note = self.notes[self.noteList.row(item)]
        self.titleInput.setText(selected_note.title)
        self.tagInput.setText(','.join(selected_note.tags))
        self.noteContent.setHtml(selected_note.content)  # Load as HTML for rich text

    def filterNotes(self):
        tag, ok = QInputDialog.getText(self, '按标签过滤', '输入标签:')
        if ok:
            self.noteList.clear()
            for note in self.notes:
                if tag in note.tags:
                    self.noteList.addItem(note.title)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NoteApp()
    ex.show()
    sys.exit(app.exec_())
