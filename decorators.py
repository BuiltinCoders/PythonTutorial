# # # Decorators are used to enhance the function's ability

# # def function1():
# #     print("Hello World")

# # func2 = function1
# # del function1
# # func2()

# # # Function callng function as an argument
# # def funcret(num):
# #     if num==0:
# #         return print
# #     if num==1:
# #         return sum
        
# # a = funcret(0)
# # print(a)

# # a = funcret(1)
# # print(a)

# # also

# # def executor(func):
# #     func("This is func")

# # executor(print)


# # # decorator concept

# # doing threw normal way
# # def dec1(func1):
# #     def nowexe():
# #         print("Executing Now")
# #         func1()
# #         print("Executed")
# #     return nowexe

# # def who_is_nitesh():
# #     print("Nitesh is a good boy")

# # who_is_nitesh = dec1(who_is_nitesh)
# # who_is_nitesh()

# # using decorators
# def dec1(func1):
#     def nowexe():
#         print("Executing Now")
#         func1()
#         print("Executed")
#     return nowexe

# @dec1
# def who_is_nitesh():
#     print("Nitesh is a good boy")


# who_is_nitesh()


############################## Seperator ################################
def decorator_function(any_function):
    def wrapper():
        print("This awesome function")
        any_function()
        print("ended")
    return wrapper

@decorator_function
def func1():
    print("This is func1")

def func2():
    print("This is func2")

func1()
func2()