# a = input("what is your name?\n")
# b = input("how much do you earn?\n")

# if int(b)==0:
#     raise ZeroDivisionError("b is not excepted to zero")
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")
# print(f"Hello {a}")

c = input("What is your name?\n")

try:
    print(a)
except Exception as e:
    if c == "harry":
        raise ValueError("Harry is not allowed")
    print('variable not found')