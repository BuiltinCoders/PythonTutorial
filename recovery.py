import os

os.chdir("E:/NITESH/Study/sample")
items = os.listdir()
# print(items)
for files in items:
    new_name = files.lower()
    os.rename(files, new_name)