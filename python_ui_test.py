import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGroupBox, QRadioButton, QPushButton, QGridLayout, QVBoxLayout,
                             QHBoxLayout, QLineEdit)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        grid = QGridLayout()
        grid.addWidget(self.createOption(), 0, 0)
        grid.addWidget(self.createURLEdit(), 1, 0)
        grid.addWidget(self.resultOfMacro(), 2, 0)

        self.setLayout(grid)

        self.setWindowTitle('adbrix postback URL tester')
        self.setBaseSize(600, 800)
        self.setGeometry(300, 300, 480, 320)
        self.show()

    # make options using radio button
    def createOption(self):
        groupbox = QGroupBox('Option')

        radio1 = QRadioButton('Attribution')
        radio2 = QRadioButton('Event')
        radio1.setChecked(True)

        hbox = QHBoxLayout()
        hbox.addWidget(radio1)
        hbox.addWidget(radio2)
        groupbox.setLayout(hbox)

        return groupbox

    # make a edit text for url
    def createURLEdit(self):
        groupbox = QGroupBox('put postback url')

        url = QLineEdit()
        url.setObjectName("url")
        check_btn = QPushButton("check")
        check_btn.setObjectName("checkButton")

        vbox = QVBoxLayout()
        vbox.addWidget(url)
        vbox.addWidget(check_btn)
        groupbox.setLayout(vbox)
        check_btn.clicked.connect()
        return groupbox

    def resultOfMacro(self):
        groupbox = QGroupBox('Macro Results')

        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)

        return groupbox

    def printURL(self):
        print(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
