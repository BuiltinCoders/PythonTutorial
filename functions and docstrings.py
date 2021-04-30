# # A function is a block of code which only runs when it called. we can pass data, known as
# parameters, into a function. A function can return data as a result


# # There are two type of functions in python:-
# 1. Builtin function                 ------------   pre-defined function
# 2. User defined function            ------------   defined or made by user

# 1. Builtin function
# sum is a builtin function used to add numerical values of tuple, list, etc.

# a = 4
# b = 3
# c = sum((a, b))    # bultin function
# print(c)


# 2. User defined function

#  how to create a function in python
# def function():
#     print("You are running function 1.")

# function()
# print(function())      # -------------- returns a value with none because this doesn't returns a value


# function taking parameters
# def function(a, b):
#     print("You are running function 1.", a+b)

# function(4, 3)
# print(function(6, 9)) # ----------------- returns a value with none


# function returning value
# def average(a, b):
#     av = (a+b)/2
#     return av

# print(average(7, 5))



# # Docstrings
  # docstrings are the strings literals that appears right after the definition of a function,
  # method, class, or module

def average(a, b):
    """This function gives average of two numbers
    This function can only take two parameters"""
    av = (a+b)/2
    return av

print(average.__doc__)   # ---> This statement("function_name.__doc__") is used to get the docstring of that function
print(help(len))     # ---> help function is also used to see docstrings of function