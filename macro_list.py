import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import openpyxl

# connection UI file to Python file. UI file and Python File must be in the same directory
form_class = uic.loadUiType("macro_list.ui")[0]

# -----------------------make lists of postback macro-----------------------------
# "/Users/gwanggyupark/Documents/postback_macro.xlsx" -> file directory for Mac
wb = openpyxl.load_workbook("postback_macro.xlsx", data_only=True)

# make a list of attribution postback macro
ws_attribution = wb["Sheet3"]
# changeable count of attribution macro
count_attribution = 0
for row in ws_attribution:
    if not all([cell.value is None for cell in row]):
        count_attribution += 1
# print(count_attribution)
# cells
cells_attribution = ws_attribution['A1':'A%d' % count_attribution]
cells_attribution_description = ws_attribution['B1':'B%d' % count_attribution]
cells_attribution_example = ws_attribution['C1':'C%d' % count_attribution]

# list
attribution_macro_list = []
attribution_macro_list_description = []
attribution_macro_list_example = []
# attribution dictionary
attribution_dict = {}
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
j = 0
while j < count_attribution:
    attribution_dict[attribution_macro_list[j]] = "{0}|{1}".format(attribution_macro_list_description[j],
                                                                   attribution_macro_list_example[j])
    j = j + 1
# print(attribution_dict)
# make a list of event postback macro
ws_event = wb["Sheet4"]
# changeable count of event macro
count_event = 0
for row in ws_event:
    if not all([cell.value is None for cell in row]):
        count_event += 1
# print(count_event)
# cells
cells_event = ws_event['A1':'A%d' % count_event]
cells_event_description = ws_event['B1':'B%d' % count_event]
cells_event_example = ws_event['C1':'C%d' % count_event]
# list
event_macro_list = []
event_macro_list_description = []
event_macro_list_example = []
# event dictionary
event_dict = {}
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
k = 0
while k < count_event:
    event_dict[event_macro_list[k]] = "{0}|{1}".format(event_macro_list_description[k],
                                                       event_macro_list_example[k])
    k = k + 1


# -------------------------------------------------------------------------
# window class
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # add items in a list widget
        i = 0
        # default value
        while i < len(attribution_macro_list):
            # print(attribution_macro_list[i])
            self.macroList.addItem(attribution_macro_list[i])
            i = i + 1
        # radio button
        self.radioButton.clicked.connect(self.checkRadio)
        self.radioButton2.clicked.connect(self.checkRadio)
        # when user click item on list
        self.macroList.itemClicked.connect(self.listClickFunction)
        # when search button is clicked -> find specific macro
        self.searchButton.clicked.connect(self.searchButtonFunction)
        # when user push return
        self.searchEdit.returnPressed.connect(self.searchButtonFunction)

    # function when radio button is clicked
    def checkRadio(self):
        self.macroList.clear()
        self.macroDescription.clear()
        i = 0
        if self.radioButton.isChecked():
            print("radioButton checked")
            while i < len(attribution_macro_list):
                self.macroList.addItem(attribution_macro_list[i])
                i = i + 1
        elif self.radioButton2.isChecked():
            print("radioButton2 checked")
            while i < len(event_macro_list):
                self.macroList.addItem(event_macro_list[i])
                i = i + 1

    # function when a item on the list is clicked
    def listClickFunction(self):
        self.macroDescription.clear()
        item = self.macroList.currentItem().text()
        # print(item)
        if self.radioButton.isChecked():
            # print("radioButton clicked : %d" + self.radioButton.isChecked())
            value = attribution_dict[item].split("|")
            self.macroDescription.append("{0}\n\n{1}".format(value[0], value[1]))
        elif self.radioButton2.isChecked():
            value = event_dict[item].split("|")
            self.macroDescription.append("{0}\n\n{1}".format(value[0], value[1]))

    # when user want to find specific macro on the list
    def searchButtonFunction(self):
        searched_macro = self.searchEdit.text()
        self.macroList.clear()
        self.macroDescription.clear()
        if self.radioButton.isChecked():
            i = 0
            while i < len(attribution_macro_list):
                if searched_macro in attribution_macro_list[i]:
                    self.macroList.addItem(attribution_macro_list[i])
                    # print(attribution_macro_list[i])
                i = i + 1
        elif self.radioButton2.isChecked():
            i = 0
            while i < len(event_macro_list):
                if searched_macro in event_macro_list[i]:
                    self.macroList.addItem(event_macro_list[i])
                    # print(event_macro_list[i])
                i = i + 1


# execute this file
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
