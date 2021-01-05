import sys
from PyQt5.QtWidgets import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('adbrix postback url tester')
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('postback URL:'), 0, 0)
        grid.addWidget(QLabel('Author:'), 1, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)

        self.setWindowTitle('QGridLayout')
        self.setGeometry(600, 600, 500, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
