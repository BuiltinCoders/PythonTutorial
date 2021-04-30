import sys
print(sys.path)

# importing file 2 ....
# from file2 import a     # ----> Bad practice
# print(a)

# also

import file2     # ---> Good practice
print(file2.a)
file2.printjoke("This is you")
