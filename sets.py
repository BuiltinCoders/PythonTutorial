# sets are the collection of organized and unique data

s = set()
# print(type(s))

# we can also create set using list
ls = [1,2,5,7,8]
s_from_list = set([1,2,3,4,5])

# print(s_from_list)
# print(type(s_from_list))

# also
# print(set(ls))

# # Functions and methods of sets

# 1. add method
  # add method is used to data to set
s.add(1)
# print(s)

# as set is collection of unique data
s.add(2)
# print(s)

# 2. union method
  # union method is used to create set directly
# sl = s.union({1,2,3})
# print(sl)

# 3. intersection method
  # intersection method find out the common common values of two or more sets
sl = s.intersection({1,2,3})
# print(s, sl)

# 4. len function
  # len function is used to get the length of sets
# print(len(s))

# 5. min function
  # min function get the smallest value of set
# print(min(s))

# 6. max function
  # max function returns the largest value of set
# print(max(s))

# 7. isdisjoint method
  # isdisjoint method checks whelter the set is difference or join
sq = {4, 6}
# print(s.isdisjoint(sq))

# 8. remove method
  # remove method is used to remove data from set
s.remove(1)
print(s)