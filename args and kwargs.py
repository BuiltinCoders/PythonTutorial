# # *args are you used to make parameter values limit infinite

# Normal function
def function_name_print(a, b, c, d):
    print(a, b, c, d)

# function_name_print("Nitesh", "Mohan", "Sohan", "Harry")

# Using *args

# def funargs(*args):
#     # print(type(args))
#     for items in args:
#         print(items)

name = ["Nitesh", "Mohan", "Sohan", "Harry"]
# funargs(*name)

# args convert data type into tuple
# we can also send normal value to function with *args
# we need to give normal arguments first and then *args              ------ Convention
# def funargs(pre_name, *args):      #if you def funargs(*args, per_name): ---- error
#     # print(type(args))
#     print(pre_name)
#     for items in args:
#         print(items)

# name = ["Nitesh", "Mohan", "Sohan", "Harry", "Coder"]
first_name = "Google"
# funargs(first_name, *name)


# # **kwargs

# **kwargs are used with dictionaries
# def funkwargs(**kwargs):
#     print(type(kwargs))
#     for key, value in kwargs.items():
#         print(f"{key} is a {value}")

# kw = {
#     "Karan":"Class teacher",
#     "Nitesh":"Monitor",
#     "Rohan":"Front bencher",
#     "Sohan":"Back bencher"
# }

# funkwargs(**kw)

# we can also use normal parameters with **kwargs also with *args
# we must give normal parameters before *args and **kwargs
# sequence of using normal parameters, *args and **kwargs
 # 1. Normal parameters
 # 2. *args
 # 3. **kwargs

def funkwargs(pre_name, *args, **kwargs):
    print(pre_name)

    for items in args:
        print(items)
    print("\nIntroducing **Kwargs")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

kw = {
    "Karan":"Class teacher",
    "Nitesh":"Monitor",
    "Rohan":"Front bencher",
    "Sohan":"Back bencher"
}

funkwargs(first_name, *name, **kw)