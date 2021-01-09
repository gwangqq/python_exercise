import openpyxl

load_wb = openpyxl.load_workbook("postback_macro.xlsx", data_only=True)
# get a sheet
load_ws = load_wb['Sheet1']
count = 0
for row in load_ws:
    if not all([cell.value is None for cell in row]):
        count += 1
print(count)
get_cells = load_ws['A1':'A%d' % count]
for row in get_cells:
    for cell in row:
        print(cell.value)

# 셀 주소로 값 출력
print("\n" + load_ws['A1'].value)
