# # Global Variables
  # global variables are those variables which can be used in the whole programe.

# # Local Variables
  # local variables are those variables which can be used only in perticular function or perticular loop, etc.


# l = 10         # Global Variables - which can be used across the programe
# def func1(n):
#     # l = 5          # Local Variables - Which can used only in this function
#     m = 8
#     # print(l,m)
#     global l          # This syntax is used to convert local variable into global variable
#     l = l + 45
#     print(l)
#     print(n,"I have printed")


# func1("Nitesh Kumar")
# print(l)



# # Nested Funtion
  # nested function refers to create functions inside functions
# def nitesh():
#     x = 20
#     def rohan():
#         global x
#         x = 88
#     print("before calling rohan()", x)
#     rohan()
#     print("after calling rohan()", x)

# nitesh()
# print(x)



# Quick Quize
# what will be the value of x

x = 89
def nitesh():
    x = 20
    def rohan():
        global x
        x = 88
    print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)

nitesh()
print(x)   # result - "88", as in rohan function x = 88 is defined as the global variable  
