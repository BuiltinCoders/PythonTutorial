# # List
# list are the collection of mutiple data of different datatype
# list are mutable

grocery = ['harpic', 'vim bar', 'deodrant', 'bhindi', 51]
numbers = [5,6,3,8,2]
# print(grocery)

# to print perticular character of list we can define the character's postion in the list
# print(grocery[2])
# print(grocery[5])               ------- list index out of range error

# to replace perticular character of list
# grocery[0] = 'cleaner'
# print(grocery[0])

# list slicing
# print(numbers[1:3:1])
# print(numbers[:])
# print(numbers[0:])
# print(numbers[:5])
# print(numbers[::-1])
# print(numbers[::-2])


# # List functions & methods

# 1. sort method
  # sort method is used to sort data in asscending order
  # sort method actualy sort the real data

# numbers.sort()
# print(numbers)

# 2. reverse method
  # reverse method is used to reverse the order of data
  # it also reverse the actual real data

# numbers.reverse()
# print(numbers)

# 3. len function
  # len function is used to get the length of data
# print(len(numbers))

# 4. max function
  # max function is used to get the largest value of data
# print(max(numbers))

# 5. min function
  # min function is used to get the lowest value of data
# print(min(numbers))

# 6. append method
  # append method is one of the way used to add new data to list
  # it added the new data into the real data
# numbers.append(73)
# print(numbers)

# 7. insert method
  # to add new data to perticular position in the list we use insert method
  # it also added the new data in the real data
# numbers.insert(1, 7)
# print(numbers)

# 8. extend method
  # extend method is used to add two or more list
# grocery.extend(numbers)
# print(grocery)

# 9. remove method
  # remove data is used to remove data from list
# numbers.remove(6)
# print(numbers)

# 10. pop method
  # pop method deletes the last value of list
# numbers.pop()
# print(numbers)

# 11. delete method
  # delete method is used to delete perticular data from list
# del numbers[2]
# print(numbers)

# # Binary
  # binary is used to swap the value between two variables

# normal
a = 7
b = 3

# temp = a
# a = b
# b = temp

# print(a,b)

# using binary
# a, b = b, a
# print(a,b)

# count method
# print(numbers.count(1))

# sorted method
# print(sorted(numbers))

# clear method
# numbers.clear()
# print(numbers)

# copy method
# number_copy = numbers.copy()
# print(number_copy)