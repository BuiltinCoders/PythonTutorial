import random

# # Modules are the file that we use in our programe
 # There are two type of modules in python :
  # 1. builtin - present in our python packages
  # 2. external -  downloaded from external resouces

# 1. Builtin Modules
 # builtin modules are already present in our current python packages

# 2. External Modules
 # external modules are the modules which are to download from python community

# using builtin module 
# random module

# Some Methods of Random Module are:-

 # 1. randit method
random_number = random.randint(0, 5)
# print(random_number)

 # 2. random method
rand = random.random()     # Between 0 and 1
# print(rand)

rand2 = random.random()*100
# print(rand2)

 # 3. choice method
ls = ["Nitesh", "Rohan", "Harry"]
choice = random.choice(ls)
# print(choice)