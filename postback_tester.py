import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import openpyxl

# connection UI file to Python file
# UI file and Python File must be in the same directory
form_class = uic.loadUiType("postback_test.ui")[0]


# class
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # signal to connect button and function
        self.checkButton.clicked.connect(self.checkButtonFunction)
        self.radioButton1.clicekd.connect(self.chosenRadioButton)
        self.radioButton2.clicekd.connect(self.chosenRadioButton)


    # when checkButton is clicked, this function works.
    def checkButtonFunction(self):
        print(self.urlEdit.text())
        testUrl = self.urlEdit.text().strip()

        # 1. extract query strings
        query_string = testUrl[testUrl.find("?") + 1:]
        print(query_string)

        # 2. spilt query using '&' or '=' and then put in a list
        a_list = query_string.split("&")

        # 3. make a list of query string values
        value_list = []
        i = 0
        while i < len(a_list):
            tmp = a_list[i]
            print("a_list[i]" + tmp)
            value_list.append(tmp[tmp.find("=") + 1:])
            i = i + 1

        # 4. comparing every single query in a list with postback macros.

        # read excel file through oepnpyxl library
        wb = openpyxl.load_workbook("/Users/gwanggyupark/Documents/postback_macro.xlsx")
        if self.radioButton1:
            ws = wb['Sheet1']
            cells = ws['A1':'A77']
        elif self.radioButton2:
            ws = wb['Sheet2']
            cells = ws['A1':'A240']
        print('------a list of valid postback macro-----')

        macro_list = []
        for row in cells:
            # print(row)
            for cell in row:
                # print(cell.value)
                macro_list.append(cell.value)

        # 5. If query strings are all well set according to macros, return a success mesaage otherwise failed message
        # chekcing all the macro in url
        j = 0
        errorNum = 0
        while j < len(value_list):
            tmp = value_list[j]
            # print(tmp)
            if tmp in macro_list:
                print("valid macro")
                j = j + 1
            else:
                print("\'" + tmp + "\'" + " is invalid macro. Check this macro one more time")
                j = j + 1
                errorNum = errorNum + 1

    def chosenRadioButton(self):

        print("A") if a > b else print("=") if a == b else print("B")
        if self.radioButton1.isChecked():
            print("GroupBox_rad1 Chekced")
        elif self.radioButton2.isChecked():
            print("GroupBox_rad2 Checked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
