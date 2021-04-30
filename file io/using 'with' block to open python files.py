# # "With" block
# 'with' block is a short hand technique used to open python files
# there is no need to run close method as 'with' block do this automatically

# 1. Normal Way
# f = open("intro3.txt", "rt")
# # print(f.readlines())
# print(f.readline())

# f.close()

# 2. using 'with' block
with open("intro3.txt", 'rt') as f:
    a = f.readlines()
    print(a)

f = open("intro3.txt")
a = f.readlines()
print(a)

f.close()