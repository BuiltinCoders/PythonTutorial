# dictionary is the collection of data in key - value pair

d1 = {}
# print(type(d1))

# d2 = {"Nitesh":"curry", "Rohan":"rice", "Jade":"meggi"}
# print(d2)

# we can also print perticular value of dictionary using key
# print(d2["Nitesh"])

# # List indside list
d2 = {"Nitesh":"curry", "Rohan":"rice", "Jade":{"breakfast":"chapati", "lunch":"snacks", "dinner":"rice with pulses"}}
# print(d2)
# print(d2["Jade"])

# how to access data of dictionary inside dictionary
# print(d2["Jade"]["lunch"])

# how to add data to dictionary
d2["jake"] = "bowled vegetables"
# print(d2)

d2["maya"] = "pizza"
# print(d2)

# how to delete data from dictionary
# print(d2)
# del d2["maya"]
# print(d2)


# # Functions of dictionary

# 1. copy method
  # copy method is used to make copy of dictionary
  # copy method makes another copy of data which is not linked to original data
# d3 = d2.copy()

# del d2["jake"]
# print(d3)
# print(d2)

# 2. get method
  # get method is used to get the value of key from dictionary
# print(d2.get("maya"))

# 3. update method
  # update method is a way used to add data to dictionary
# d2.update({"bro":"carrot"})
# print(d2)

# 4. keys method
  # keys method is used to get all the keys of dictionary
# print(d2.keys())

# 5. items method
  # items method is used to get key-value pair of dictionary
print(d2.items())