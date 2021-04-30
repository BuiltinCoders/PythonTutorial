# 1. How to write in a text file using write mode
 # write mode overwrite the whole data of the text file with the new data
# f = open('intro2.txt', "w")
# f.write("Hello, This is Nitesh Kumar")   # ------> write mode "w" overwrite the data of text file

# f.close()

# 2. How to write in a text file using append mode
 # append mode just add/append data with other data in the text file

# f = open("intro2.txt", "a")
# f.write("\nThis is from Nitesh Kumar")
# f.write("\nThat i am wrting text using append mode")

# f.close()

# 3. How to get length of data written by us using write or append mode into text file

# In append mode
# f = open("intro2.txt","a")
# a = f.write("I am getting len of data")
# print(a)

# In write mode
# f = open("intro2.txt","w")
# a = f.write("I am getting len of data")
# print(a)


# 4. Handle read and write both
 # we can use both read and write mode for perticular text file
f = open("intro2.txt", "r+")   # ------> "r+" stands for read and write mode
print(f.read())
print(f.write("\nusing 'r+' mode"))
print(f.read())

f.close()