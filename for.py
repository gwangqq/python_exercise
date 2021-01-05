# test_list = ['one', 'two', 'three', 'four']
# for i in test_list:
#     print(i)
#
# a = [(1,2), (3,4), (5,6)]
# for (first, last) in a:
#     print(first)
#     print(last)

marks = [90, 25, 67, 45, 80]
number = 0
# hot to use continue in for
for mark in marks:
    number = number + 1
    if mark < 60: continue
    print("Congratulation %d student. You passed the exam." % number)

# how to use function "for"
# for mark in marks:
#     number = number + 1
#     if mark >= 60:
#         print("number %d student passed the exam." % number)
#     else:
#         print("number %d student failed the exam." % number)

for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end=" ")
    print(' ')


def total(a, b):
    result = a + b
    return result


print(total(4, 6))
