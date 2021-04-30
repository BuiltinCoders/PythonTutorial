ls = ["Tomato", "Onion", "Potato", "Ginger"]

# Using normal way
# i = 1
# for item in ls:
#     if i%2 != 0:
#         print(item)
#     i+=1

# using enumerate function
# enumerate function is used to get the index and value of the list
for index, item in enumerate(ls):
    if index%2==0:
        print(f"The index value of {item} is {index}")