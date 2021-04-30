# # for loop is a type of loop in python which runs the code till the condition is true or till the end of data

# 1. for loop in List
list1 = ['tomato', 'onion', 'radish', 'potato', 'chilli']

# how to use 'for loop'

# for i in list1:              # 'i' stands for inisilization, we can use any name or character in place of 'i'
#     print(i)


# 2. for loop in Tuple
tuple1 = ('apple', 'orange', 'banana', 'pineapple', 'lichi')
# for fruit in tuple1:
#     print(fruit)


# 3. for loop on list inside list
list2 = [['tomato', 1], ['onion', 3], ['radish', 2.5], ['potato', 5], ['chilli', 0.7]]
# for veg in list2:
#     print(veg)

# we can also get the values in seperate variables
# for veg, quantity in list2:
#     print(f'vegetable: {veg} | quantity: {quantity}')

# 4. for loop in dictionay

# we can convet above data type into dictionary using dict function
dict1 = dict(list2)
# for d in dict1:
#     print(d)             # This will give all the keys of the dictionary

# to get both keys and values of the dictionary we use 'items method'
# for k in dict1.items():
#     print(k)

# we can also get the seperated values of dictionary
# for key, value in dict1.items():
#     print(f"key: {key} and value: {value}")

# 5. we can also for use for loop as :-
# for i in range(0, 11):    # in the stop argument we need to write incrimented value by 1
#     print(i)


################################ QUIZE TIME ###################################
print('\n')
print(" QUIZE TIME ".center(50, '*'))

ls = ['Nitesh', 17, 'Mohan', 15, 'Sohan', 45, 'harry', 25, 'Rohan', 5]

for item in ls:
    if (type(item)==int or type(item)==float) and item>=6:
        print(item)