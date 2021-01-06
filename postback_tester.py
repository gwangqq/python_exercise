import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import openpyxl

# connection UI file to Python file
# UI file and Python File must be in the same directory
form_class = uic.loadUiType("postback_test.ui")[0]


# compare partner's postback url with adbrix postback macro
def compareQueryStrings(url, sheet_num, start, end):
    # 1. extract query strings
    query_string = url[url.find("?") + 1:]
    print(query_string)

    # 2. spilt query using '&' or '=' and then put in a list
    a_list = query_string.split("&")

    # 3. make a list of query string values
    value_list = []
    i = 0
    while i < len(a_list):
        tmp = a_list[i]
        # print("a_list[%d] %s" % (i, tmp))
        value_list.append(tmp[tmp.find("=") + 1:])
        i = i + 1

    # 4. comparing every single query in a list with postback macros.
    # read excel file through oepnpyxl library
    wb = openpyxl.load_workbook("/Users/gwanggyupark/Documents/postback_macro.xlsx")
    ws = wb[sheet_num]
    cells = ws[start:end]

    macro_list = []
    for row in cells:
        # print(row)
        for cell in row:
            # print(cell.value)
            macro_list.append(cell.value)

    # 5. If query strings are all well set according to macros, return a success mesaage otherwise failed message
    # checking all the macros in url
    j = 0
    errorNum = 0
    while j < len(value_list):
        tmp = value_list[j]
        # print(tmp)
        if tmp in macro_list:
            print("valid macro")
            j = j + 1
        else:
            print("\'" + tmp + "\'" + " is invalid macro. Check this macro one more time.")
            j = j + 1
            errorNum = errorNum + 1
    return errorNum


# window class
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # signal to connect button and function
        self.checkButton.clicked.connect(self.checkButtonFunction)

    # when checkButton is clicked, this function works.
    def checkButtonFunction(self):
        testUrl = self.urlEdit.text().strip()
        print(self.urlEdit.text())

        # put different conditions when open excel file
        if self.radioButton1.isChecked():
            num = compareQueryStrings(testUrl, 'Sheet1', 'A1', 'A77')
            if num == 0:
                print("This postback is correct postback url.")
                self.resultLabel.setText("This postback is correct postback url.")
            else:
                print("%d invalid macro" % num)
                self.resultLabel.setText("%d errors is found." % num)
        else:
            num = compareQueryStrings(testUrl, 'Sheet2', 'A1', 'A240')
            if num == 0:
                print("This postback is correct postback url.")
                self.resultLabel.setText("This postback is correct postback url." % num)
            else:
                print("%d invalid macro" % num)
                self.resultLabel.setText("%d errors is found." % num)


# execute this file
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
