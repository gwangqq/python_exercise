# import pandas as pd

# df = pd.read_excel('/Users/gwanggyupark/Documents/postback macro.xlsx')

# print(df)

import openpyxl

wb = openpyxl.load_workbook("/Users/gwanggyupark/Documents/postback_macro.xlsx")
ws = wb['Sheet1']

print('------a list of valid postback macro-----')
cells = ws['A1':'A155']

macro_list = []
for row in cells:
    # print(row)
    for cell in row:
        print(cell.value)
        macro_list.append(cell.value)

print(macro_list)
