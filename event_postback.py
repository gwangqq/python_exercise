# hot to make postback url chekcing program
# 1. get postback url as string
# 2. get query strings from url
# 3. spilt query using '&' and then put in a list
# 4. make a list of query string values
# 5. comparering every single query in a list with postback macros.
# 6. If query strings are all well set according to macros, return a success mesaage otherwise failed message
# 7. Need to detailed failure message to let a person know what is wrong in postback url.

# 1. get postback url as string
postback_url = input("postback url: ").strip()
print("registered url: " + postback_url)

# 2. get query strings from url
# print(postback_url.find("?"))
query_string = postback_url[postback_url.find("?")+1:]
print(query_string)

# 3. spilt query using '&' or '=' and then put in a list
a_list = query_string.split("&")


# 4. make a list of query string values
value_list = []
i = 0
while i < len(a_list):
    tmp = a_list[i]
    print("a_list[i]" + tmp)
    value_list.append(tmp[tmp.find("=")+1:])
    i = i + 1
print("value_list : ")
print(value_list)

# 5. comparering every single query in a list with postback macros.
import openpyxl 
# read excel file through oepnpyxl library
wb = openpyxl.load_workbook("/Users/gwanggyupark/Documents/postback_macro.xlsx")
ws = wb['Sheet1']

print('------a list of valid postback macro-----')
cells = ws['A1':'A73']

macro_list = []
for row in cells:
    # print(row)
    for cell in row:
        # print(cell.value)
        macro_list.append(cell.value)


# 6. If query strings are all well set according to macros, return a success mesaage otherwise failed message
# chekcing all the macro in url
        # if value_list.value in macro_list:
        #     print("valid")
        # else:
        #     print("invalid")
j = 0
while j < len(value_list):
    tmp = value_list[j]
    # print(tmp)
    if tmp in macro_list:
        print("valid macro")
        j = j + 1
    else:
        print(tmp + "is invalid macro. Check this macro one more time")
        j = j + 1

# 7. Need to detailed failure message to let a person know what is wrong in postback url.

