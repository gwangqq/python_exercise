import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # layout
        layout = QVBoxLayout()
        layout.addWidget(QPushButton('Search'))
        layout.addWidget(QPushButton('Bottom'))

        # button
        self.btn = QPushButton("check", self)
        self.btn.move(20, 20)

        # statusbar
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.statusbar.showMessage("adbrix postback url tester")

        # set width and height of window
        self.setGeometry(300, 300, 400, 400)

        # edit_text for partner url
        self.line_edit = QLineEdit(" ", self)
        self.line_edit.move(10, 20)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
