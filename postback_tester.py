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

    # when checkButton is clicked, this function works.
    def checkButtonFunction(self):
        print(self.urlEdit.text())
        testUrl = self.urlEdit.text().strip()
        postbackType = self.
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
        ws = wb['Sheet1']

        print('------a list of valid postback macro-----')
        cells = ws['A1':'A77']

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
