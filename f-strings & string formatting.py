import math

me = "Nitesh"
al = 7

# different  techniques of string formatting

# 1.
# a = "This is %s"%me
# print(a)

# 2.
# a = "This is %s %s"%(me, al)
# print(a)

# 3.
# a = "This is {0} {1}"
# b = a.format(me, al)
# print(b)

# 4. using f strings
# a = f"This is {me} {al}"
# print(a)

a = f"This is value of cos 2 {math.cos(2)}"
print(a)