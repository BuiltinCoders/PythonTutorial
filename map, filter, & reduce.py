# # 1. Map
  # map applies a function to all the items in an input list
  # map gives a object value

# numbers = ["1", "51", "73"]
# # numbers = list(map(int, numbers))

# # normal way
# for num in range(len(numbers)):
#     numbers[num] = int(numbers[num])

# # using map
# print(numbers)
# # numbers = ["1", "51", "73"]
# # numbers = list(map(int, numbers)
# # print(type(numbers[2]))
# print(numbers[1]+5)

# using lambda with map
# num = [1, 4, 3, 46, 62, 3, 4, 2, 345, 3]
# sq = list(map((lambda x: x*x), num))
# print(sq)

# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a

# func = [square, cube]

# for i in range(6):
#     val = list(map(lambda x:x(i), func))
#     print(val)


# # 2. Filter
  # filter gives a list if the function gives true value
  # filter gives a filter object value so, we need to convert the data into list datatype
  # or other suitable datatypes

# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# def is_greater_5(num):
#     return  num>5

# gr_than_5 = list(filter(is_greater_5, ls))
# print(gr_than_5)



# # 3. Reduce
  # reduce applies a rolling computation to sequence pair of elements
  # reduce is library of functools module

from functools import reduce
ls = [1,2,3,4,5]
total = reduce(lambda x,y: x+y, ls)
print(total)