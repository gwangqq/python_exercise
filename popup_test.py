from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QGridLayout, QWidget, QLabel


class NewWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(NewWindow, self).__init__(parent)
        self.label = QLabel('New Window!')
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.layout = QGridLayout(centralWidget)
        self.layout.addWidget(self.label)


class MyWindow(QtWidgets.QMainWindow, QPushButton):
    def __init__(self):
        super(MyWindow, self).__init__()
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.setWindowTitle("ASSET")
        self.Button = QPushButton('Action', self)
        self.Button.clicked.connect(self.Action)
        self.layout = QGridLayout(centralWidget)
        self.layout.addWidget(self.Button)
        self.new_window = NewWindow(self)

    def Action(self):
        self.new_window.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
