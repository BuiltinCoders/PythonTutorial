# # 1. Variables

# variables are like the container that stores data in it

var1 = 'Nitesh '
var2 = 11
var3 = 17.7
var4 = True
var5 = 'Kumar'
var6 = '10'
var7 = '60'

# print(var3)
# print(var4)

# how to concatenate two or more sting ?
# we can use '+' arthimetic opertators like :-
# print(var1+var5)

# we can also performe arthimatic operations like :-
# print(var2+var3)
# print(10*var1)


# # 2. Data type

# there are four major data types in python :-
# 1. string
# 2. integer
# 3. floating
# 4. boolean

# to check data type of any value we use type function
# print(type(var1))
# print(type(var2))
# print(type(var3))
# print(type(var4))


# # 3. Type casting

# we can change data type of one value into another using type casting
# we have many functions in type casting like :-
#  int()
#  float()
#  str()
#  boolean()

# print(int(var6)+int(var7))

# # 4. Input function
# input function recevies data from the user only in the string format and store it into variable


# name = input('Enter your name\n')
# print('User Input:',name)



######################## QUIZE TIME #########################
num1 = input('Enter your first number:\n')
num2 = input('Enter your second number:\n')

print('Sum of both numbers is',int(num1)+int(num2))