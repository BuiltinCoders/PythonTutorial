# size of the list
size = int(input("Enter the size of the list:\n"))

calaries_list = []

# taking items of the list form the user
for x in range(size):
    item = int(input(f"Enter the {x+1} value:\n"))
    calaries_list.append(item)

print(f"Your list is {calaries_list}\n")

# coping calaries_list
reversed1 = calaries_list[:]
reversed2 = calaries_list[::-1]
reversed3 = calaries_list[:]

# 1. builtin method
reversed1.reverse()
print(f"first reversed of {calaries_list} is {reversed1}")


# 2. slicing
print(f"second reversed list of {calaries_list} is {calaries_list[::-1]}")


# 3. swaping first element with last element
for i in range(len(calaries_list)//2):
    reversed3[i], reversed3[len(calaries_list)-i -1] = reversed3[len(calaries_list)-i -1], reversed3[i]
print(f"Third reversed list is {calaries_list} is {reversed3}\n")


if reversed1==reversed2 and reversed2 == reversed3:
    print("All the result are same")