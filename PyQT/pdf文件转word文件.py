import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QFileDialog
from PyQt5.QtCore import Qt
import os
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from docx import Document
from PyPDF2 import PdfReader


class PdfToWordConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('开始转换')
        self.setGeometry(300, 300, 300, 200)

        self.pdf_line_edit = QLineEdit(self)
        self.pdf_line_edit.setReadOnly(True)

        self.open_pdf_button = QPushButton('选择pdf文件', self)
        self.open_pdf_button.clicked.connect(self.open_pdf_file)

        self.convert_button = QPushButton('开始转换', self)
        self.convert_button.clicked.connect(self.convert_pdf_to_word)

        layout = QVBoxLayout()
        layout.addWidget(self.open_pdf_button)
        layout.addWidget(self.pdf_line_edit)
        layout.addWidget(self.convert_button)
        self.setLayout(layout)

    def open_pdf_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "选择pdf文件", "",
                                                   "PDF Files (*.pdf)", options=options)
        if file_name:
            self.pdf_line_edit.setText(file_name)

    def convert_pdf_to_word(self):
        pdf_path = self.pdf_line_edit.text()
        if not pdf_path:
            print("Please select a PDF file first.")
            return

            # Extract text from PDF using PdfReader
        reader = PdfReader(pdf_path)
        text = ''
        for page in reader.pages:
            text += page.extract_text()

            # Create Word file with the same name in the same directory
        dir_path, file_name = os.path.split(pdf_path)
        word_path = os.path.join(dir_path, os.path.splitext(file_name)[0] + '.docx')
        document = Document()
        document.add_paragraph(text)
        document.save(word_path)
        QMessageBox.information(self, "转换完成",
                                "pdf文件成功转为word!",
                                QMessageBox.Ok, QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PdfToWordConverter()
    ex.show()
    sys.exit(app.exec_())