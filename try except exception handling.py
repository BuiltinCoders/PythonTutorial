# # try except blocks are to handle exceptional cases or errors

# without try except block
num1 = input("Enter your 1 number:\n")
num2 = input("Enter your 2 number:\n")
 
# print("The sum of both the numbers is", int(num1)+int(num2))
# # if we enter a non-numerical value this programe will show error and next codes will not run
# print("This programe is very important")


# using try except blocks

try:
    print("The sum of both the numbers is", int(num1)+int(num2))
except Exception as e:
    print(e)

# using try except exception handling we can handle the exception and the next codes can be run as usual
print("This programe is ver important")