import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import openpyxl

# connection UI file to Python file. UI file and Python File must be in the same directory
form_class = uic.loadUiType("postback_test.ui")[0]

# -----------------------make two lists of postback macro-----------------------------
# "/Users/gwanggyupark/Documents/postback_macro.xlsx" -> file directory for Mac
wb = openpyxl.load_workbook("/Users/gwanggyupark/Documents/postback_macro.xlsx")

# make a list of attribution postback macro
ws_attribution = wb["Sheet1"]
cells_attribution = ws_attribution['A1':'A77']
attribution_macro_list = []
for row in cells_attribution:
    for cell in row:
        attribution_macro_list.append(cell.value)
# print(">>>>>>>>attribution macro list is made>>>>>>>>")
# print(attribution_macro_list)

# make a list of event postback macro
ws_event = wb["Sheet2"]
cells_event = ws_event['A1':'A240']
event_macro_list = []
for row in cells_event:
    for cell in row:
        event_macro_list.append(cell.value)

# print(">>>>>>>>event macro list is made>>>>>>>>")
# print(event_macro_list)

# ---------------------------------------------------------------------------------
# text color
green = "<font color=\"Green\">"
pink = "<font color=\"Red\">"
end = "</font>"


# split query strings by '&'
def splitQueryString(query_strings):
    split_query_strings = query_strings.split("&")
    return split_query_strings


# window class
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # signal to connect button and function
        self.checkButton.clicked.connect(self.checkButtonFunction)

    # when checkButton is clicked, this function works.
    def checkButtonFunction(self):
        # clear detailTextEdit
        self.detailTextEdit.clear()
        test_url = self.urlEdit.text().strip()

        # set domain on label in the middle of window
        domain = test_url[:test_url.find("?")]
        self.domain.setText(domain)

        # split query strings from postback url
        query_string = test_url[test_url.find("?") + 1:]
        print(">>>>>>>>>> check button is clicked")
        # print(self.urlEdit.text())

        # radio buttons for options(attribution, event)
        if self.radioButton1.isChecked():
            # compare attribution macro list with query strings
            split_query_strings = splitQueryString(query_string)
            print(">>>>>>>>>radioButton1.isChecked()")
            print(split_query_strings)
            print(len(split_query_strings))
            i = 0
            while i < len(split_query_strings):
                value = split_query_strings[i][split_query_strings[i].find("=") + 1:]
                print(">>>>>>>>radioButton1")
                print(value)
                if value in attribution_macro_list:
                    print(split_query_strings[i])
                    self.detailTextEdit.append(green + split_query_strings[i] + end)
                else:
                    self.detailTextEdit.append(pink + split_query_strings[i] + end)
                i = i + 1
                print(i)
        else:
            # compare attribution macro list with query strings
            split_query_strings = splitQueryString(query_string)
            print(">>>>>>>>>radioButton2.isChecked()")
            print(split_query_strings)
            i = 0
            while i < len(split_query_strings):
                value = split_query_strings[i][split_query_strings[i].find("=") + 1:]
                print(">>>>>>>>radioButton2")
                print(value)
                if value in event_macro_list:
                    self.detailTextEdit.append(green + split_query_strings[i] + end)
                else:
                    self.detailTextEdit.append(pink + split_query_strings[i] + end)
                i = i + 1
                print(i)


# execute this file
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
