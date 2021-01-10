import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
import openpyxl

# connection UI file to Python file. UI file and Python File must be in the same directory
form_class = uic.loadUiType("macro_list.ui")[0]

# -----------------------make two lists of postback macro-----------------------------
# "/Users/gwanggyupark/Documents/postback_macro.xlsx" -> file directory for Mac
wb = openpyxl.load_workbook("postback_macro.xlsx", data_only=True)

# make a list of attribution postback macro
ws_attribution = wb["Sheet3"]
# changeable count of attribution macro
count_attribution = 0
for row in ws_attribution:
    if not all([cell.value is None for cell in row]):
        count_attribution += 1
# cells
cells_attribution = ws_attribution['A1':'A%d' % count_attribution]
cells_attribution_description = ws_attribution['B1':'B%d' % count_attribution]
cells_attribution_example = ws_attribution['C1':'C%d' % count_attribution]

# list
attribution_macro_list = []
attribution_macro_list_description = []
attribution_macro_list_example = []
for row in cells_attribution:
    for cell in row:
        attribution_macro_list.append(cell.value)
# print(">>>>>>>>attribution macro list is made>>>>>>>>")
# print(attribution_macro_list)

# make a list of event postback macro
ws_event = wb["Sheet4"]
# changeable count of event macro
count_event = 0
for row in ws_event:
    if not all([cell.value is None for cell in row]):
        count_event += 1
# cells
cells_event = ws_event['A1':'A%d' % count_event]
cells_event_description = ws_event['B1':'B%d' % count_event]
cells_event_example = ws_event['C1':'C%d' % count_event]
# list
event_macro_list = []
event_macro_list_description = []
event_macro_list_example = []
for row in cells_event:
    for cell in row:
        event_macro_list.append(cell.value)


# window class
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # add items in a list widget
        i = 0

        while i < len(attribution_macro_list):
            print(attribution_macro_list[i])
            self.macroList.addItem(attribution_macro_list[i])
            i = i + 1


# execute this file
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
