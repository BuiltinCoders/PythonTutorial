# short hand if else notation is a technique used to make if else statement short
# but it reduces the readibilty of the code
# it should be used in suitable condition

a = int(input("Enter A value :\n"))
b = int(input("Enter B value :\n"))

# 1. normal if else statement
# if a>b:
#     print("A is greater than B")
# else:
#     print("B is greater than A")

# 2. using short hand if else notation
if a>b :print("A is greater than B")
# print("A is greater than B") if a>b else print("B is greater than A")