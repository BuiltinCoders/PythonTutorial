# # tell method 
  # tell method tell the updated location of cursor

# f = open("intro3.txt")
# print(f.tell())
# print(f.readline())

# print(f.tell())
# print(f.readline())

# print(f.tell())
# print(f.readline())

# f.close()


# # seek method
  # seek method is used to adjust the location of cursor

f = open("intro3.txt")
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())

f.seek(15)
print(f.tell())
print(f.readline())

f.close()