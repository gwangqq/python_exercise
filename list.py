t1 = (1, 2, 'a', 'b')
t2 = ('c', 'd')
print(t1 + t2)
print(t1 * 3)
print(t1[0:2])

l1 = [3, 4, 'c', 'd']
print(l1)

l1[0] = 'z'

print(l1)

a = {"name" : "jake"}
print(a)
a["age"] = 29
print(a)
del a["age"]
print(a)

b = {1 : "a", 1 : "b"}
print(b)

test = {"a" : "gwanggyu", "b" : "jake", "c" : "gawnggyu park", "d" : "bakbakbak"}

test.clear()
print(test.keys())
print(test.values())
print(test.items())
# test.clear()
print(test)
print(test.get("e"))
print(test.get("e", "nothing"))
print("a" in test)
print("f" in test)

for k in test.keys():
    print(k)

for v in test.values():
    print(v)
for k,v in test.items():
    print("key is : " + k)
    print("value is : " + v)

#s1 = set([1, 2, 3])
s1 = {1,2,3}
print(type(s1))
print(s1)

l = [1,2,2,3,3,4,2,3,2,4]
print(l)
newList = list(set(l))
print(newList)

h = set("hello")
print(h)

s1 = set([1,2,3,4,5,6])
s1.add(7)
s2 = set([4,5,6,7,8,9])
print(s1 & s2)
# print(s1.intersection(s2))
print(s1 | s2)
# print(s1.union(s2))
print(s1 - s2)
print(s1.difference(s2))
print(s2.difference(s1))

