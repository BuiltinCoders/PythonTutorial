# comprehension is a technique of python like lambda exprehension. This technique is used to compress code
# for same type of code


# some signs that specify the type
# list = []
# dictionary = {key:value}
# set = {}
# generator = ()


# simple techinque
# ls = []

# for i in range(100):
    # if i%3==0:
#       ls.append(i)
# print(ls)

# using comprehension

# list comprehension
# ls = [i for i in range(100) if i%3==0]
# print(ls)

# dictionary comprehension
# dict1 = {i:f"Item{i}" for i in range(10) if i%2==0}
# dict2 = {value:key for key,value in dict1.items()}
# print(dict1)
# print(dict2)

# set comprehension
# set1 = {item for item in ['item1', 'item2', 'item3', 'item2', 'item1']}
# print(set1)
# print(type(set1))

# generator comprehension
gen1 = (i for i in range(100) if i%2==0)
# print(gen1)
print(type(gen1))
for gen in gen1:
    print(gen1.__next__(), end=(' '))