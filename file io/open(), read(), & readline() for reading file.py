# # open function
 # open function is used to open perticular file for editing
 # closing file is a good practice after opening file


# 1. How to read text file using read mode "r"
# f = open("intro.txt")      # ----->  as a default there is "r" as a default mode
# f = open("intro.txt", "r")   # ------> no change in output 
# content = f.read()
# print(content)

# f.close()

# 2. How to read text file in binary mode "b"
# f = open("intro.txt", "rb")     # ------->  here "rb" stands for read binary mode
# content = f.read()
# print(content)

# f.close()

# 3. How to read text file using read text"rt" mode
# f = open("intro.txt", "rt")       # ------> here "rt" stands for read text binary mode
# content = f.read()
# print(content)

# f.close()

# 4. How to read limited data of text file
# f = open("intro.txt", "rt")
# content = f.read(5)     # ------> we have write "5" in read method to read only first 5 characters of text file
# print(content)

# f.close()

# 5. What if we print perticular characters of text file and do it again
# f = open("intro.txt", "rt")
# content = f.read(5)     # ------> we have write "5" in read method to read only first 5 characters of text file
# print(content)
# content = f.read(5)
# print(content)
# f.close()
# while reading first data the cursor set at the end of the character and when we retry to read
# the file again it reads data from the end of character so we get the next characters of data

# 6. What if we try to read the greater characters than the length of text file
# f = open("intro.txt", "rt")
# content = f.read(15432)  # ------> numerical value sets the limit of the characters of data
# print("1.", content)
# content = f.read(5543)
# print("2.", content)
# f.close()
# while reading greater characters than the length of text file it ignore's the command

# 7. How to read text file line by line
# f = open("intro.txt")

# for line in f:
#     print(line, end="")

# f.close()

# 7. Readline method
 # readline method is used to read data line by line and get the next line on demand
# f = open('intro.txt', 'r')
# content = f.readline()
# print(content)
# content = f.readline()
# print(content)
# f.close()

# 8. Readlines method
 # readlines method is used to get all the data of text file in a list form
# f = open("intro.txt")
# content = f.readlines()
# print(content)

# f.close()

# 9. How to read text files of other folder than cwd
f = open(r"E:\NITESH\Collection of Games\Freedom Fighter\Readme.txt")
content = f.read()
print(content)

f.close()