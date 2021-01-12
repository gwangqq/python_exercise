import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import openpyxl

# connection UI file to Python file. UI file and Python File must be in the same directory
form_class = uic.loadUiType("macro_list.ui")[0]

# -----------------------make lists of postback macro-----------------------------
# "/Users/gwanggyupark/Documents/postback_macro.xlsx" -> file directory for Mac
wb_macro = openpyxl.load_workbook("postback_macro.xlsx", data_only=True)

# make a list of attribution postback macro
ws_attribution_macro = wb_macro["Sheet3"]
# changeable count of attribution macro
count_attribution_macro = 0
for row in ws_attribution_macro:
    if not all([cell.value is None for cell in row]):
        count_attribution_macro += 1
# print(count_attribution)
# cells
cells_attribution_macro = ws_attribution_macro['A1':'A%d' % count_attribution_macro]
cells_attribution_description_macro = ws_attribution_macro['B1':'B%d' % count_attribution_macro]
cells_attribution_example_macro = ws_attribution_macro['C1':'C%d' % count_attribution_macro]

# list
attribution_macro_list_macro = []
attribution_macro_list_description_macro = []
attribution_macro_list_example_macro = []
# attribution dictionary
attribution_dict = {}
# set value at each list
for row in cells_attribution_macro:
    for cell in row:
        attribution_macro_list_macro.append(cell.value)

for row in cells_attribution_description_macro:
    for cell in row:
        attribution_macro_list_description_macro.append(cell.value)

for row in cells_attribution_example_macro:
    for cell in row:
        attribution_macro_list_example_macro.append(cell.value)
# print(">>>>>>>>attribution macro list is made>>>>>>>>")
# print(attribution_macro_list)
j = 0
while j < count_attribution_macro:
    attribution_dict[attribution_macro_list_macro[j]] = "{0}|{1}".format(attribution_macro_list_description_macro[j],
                                                                         attribution_macro_list_example_macro[j])
    j = j + 1
# print(attribution_dict)
# make a list of event postback macro
ws_event_macro = wb_macro["Sheet4"]
# changeable count of event macro
count_event_macro = 0
for row in ws_event_macro:
    if not all([cell.value is None for cell in row]):
        count_event_macro += 1
# print(count_event)
# cells
cells_event_macro = ws_event_macro['A1':'A%d' % count_event_macro]
cells_event_description_macro = ws_event_macro['B1':'B%d' % count_event_macro]
cells_event_example_macro = ws_event_macro['C1':'C%d' % count_event_macro]
# list
event_macro_list_macro = []
event_macro_list_description_macro = []
event_macro_list_example_macro = []
# event dictionary
event_dict = {}
# set value at each list
for row in cells_event_macro:
    for cell in row:
        event_macro_list_macro.append(cell.value)

for row in cells_event_description_macro:
    for cell in row:
        event_macro_list_description_macro.append(cell.value)

for row in cells_event_example_macro:
    for cell in row:
        event_macro_list_example_macro.append(cell.value)
k = 0
while k < count_event_macro:
    event_dict[event_macro_list_macro[k]] = "{0}|{1}".format(event_macro_list_description_macro[k],
                                                             event_macro_list_example_macro[k])
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
        while i < len(attribution_macro_list_macro):
            # print(attribution_macro_list[i])
            self.macroList.addItem(attribution_macro_list_macro[i])
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
            while i < len(attribution_macro_list_macro):
                self.macroList.addItem(attribution_macro_list_macro[i])
                i = i + 1
        elif self.radioButton2.isChecked():
            print("radioButton2 checked")
            while i < len(event_macro_list_macro):
                self.macroList.addItem(event_macro_list_macro[i])
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
            while i < len(attribution_macro_list_macro):
                if searched_macro in attribution_macro_list_macro[i]:
                    self.macroList.addItem(attribution_macro_list_macro[i])
                    # print(attribution_macro_list[i])
                i = i + 1
        elif self.radioButton2.isChecked():
            i = 0
            while i < len(event_macro_list_macro):
                if searched_macro in event_macro_list_macro[i]:
                    self.macroList.addItem(event_macro_list_macro[i])
                    # print(event_macro_list[i])
                i = i + 1


# execute this file
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
