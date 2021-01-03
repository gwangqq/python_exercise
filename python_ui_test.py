import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # set width and height of window 
        self.setGeometry(300, 300, 400, 400)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()