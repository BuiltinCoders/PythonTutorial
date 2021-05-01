# The equality operator(==) compares the values of both the operands and checks for value equality.
# 'is' operator checks whelther both the operands refers to the same object or not.

list1 = []
list2 = []
list3 = []
list3 = list1
print(list1 == list2)
print(list1 is list2)
print(list1 is list3)
list3 = list3 + list2
print(list1 is list3)