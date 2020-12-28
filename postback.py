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

# 6. If query strings are all well set according to macros, return a success mesaage otherwise failed message

# 7. Need to detailed failure message to let a person know what is wrong in postback url.

