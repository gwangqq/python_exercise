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

# set value at each list
for row in cells_attribution:
    for cell in row:
        attribution_macro_list.append(cell.value)

for row in cells_attribution_description:
    for cell in row:
        attribution_macro_list_description.append(cell.value)

for row in cells_attribution_example:
    for cell in row:
        attribution_macro_list_example.append(cell.value)
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

# set value at each list
for row in cells_event:
    for cell in row:
        event_macro_list.append(cell.value)

for row in cells_event_description:
    for cell in row:
        event_macro_list_description.append(cell.value)

for row in cells_event_example:
    for cell in row:
        event_macro_list_example.append(cell.value)


# window class
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # add items in a list widget
        i = 0
        # default value
        while i < len(attribution_macro_list):
            print(attribution_macro_list[i])
            self.macroList.addItem(attribution_macro_list[i])
            i = i + 1

        self.radioButton.clicked.connect(self.checkRadio)
        self.radioButton_2.clicked.connect(self.checkRadio)
        self.macroList.clicked.connect(self.listClickFunction)

    # function when radio button is clicked
    def checkRadio(self):
        self.macroList.clear()
        print("either of radio buttons is clicked")
        if self.radioButton.isChecked:
            i = 0
            print("radioButton checked")
            while i < len(attribution_macro_list):
                self.macroList.addItem(attribution_macro_list[i])
                i = i + 1
        elif self.radioButton_2.isChecked:
            i = 0
            print("radioButton2 checked")
            while i < len(event_macro_list):
                self.macroList.addItem(event_macro_list[i])
                i = i + 1

    # function when a item on the list is clicked
    def listClickFunction(self):
        self.macroDescription.clear()
        index = self.macroList.currentRow()
        if self.radioButton.isChecked:
            description = attribution_macro_list_description[index]
            example = attribution_macro_list_example[index]
            self.macroDescription.append("%s \n\n%s" % (description, example))
        elif self.radioButton_2.isChecked:
            description = event_macro_list_description[index]
            example = event_macro_list_example[index]
            self.macroDescription.append("%s \n\n%s" % (description, example))


# execute this file
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
