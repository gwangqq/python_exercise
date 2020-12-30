list = ["a", "b", "c", "d"]

list2 = ["c", "d", "e", "f"]

i = 0
print(len(list))
while i < len(list):
    tmp = list[i]
    print(tmp)
    if tmp in list2:
        print("okay")
        i = i + 1
        
    else:
        print("not okay")
        i = i + 1
        