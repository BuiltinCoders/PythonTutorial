# # Type of operators in python

# 1. Arithmetic Operators
# 2. Assignment Operators
# 3. Comparison Operators
# 4. Logical Operators
# 5. Identity Operators
# 6. Membership Operators
# 7. Bitwise Operators

# 1. Assignment Operators
  # assignment operators are used to do numeric caculation
  # examples of assignment operators are :- +, -, *, **, /, //, %
    # add operator "+" = gives addition of numbers
    # subtraction operator "-" = gives substraction of numbers
    # multiplication operator "*" = gives multiplied value of numbers
    # exponent operator "**" = gives exponential value
    # divide operator "/" = gives divided value
    # divide operator "//" = gives divided value in integer
    # modulus operator "%" = gives reminder of the dividion operation

# print("5+6 =",5+6)
# print("5-6 =",5-6)
# print("5*6 =",5*6)
# print("5**3 =",5**3)
# print("5/6 =",5/6)
# print("5//6 =",5//6)
# print("5%6 =",5%6)


# 2. Assignment Operators
  # assignment operators are used to assign values to variables
  # example of assignment operators are :-  =, +=, -=, *=, /=, %=, //=, **=
   # equals to assignment operator "=" = assign values to variables
   # "+=" assignment operator = example:-  x+=5("+=" stands for "x = x+5")
   # "-=" assignment operator = example:-  x-=5("-=" stands for "x = x-5")
   # "*=" assignment operator = example:-  x*=5("*=" stands for "x = x*5")
   # "/=" assignment operator = example:-  x/=5("/=" stands for "x = x/5")
   # "%=" assignment operator = example:-  x%=5("%=" stands for "x = x%5")
   # "//=" assignment operator = example:-  x//=5("//=" stands for "x = x//5")
   # "**=" assignment operator = example:-  x**=5("**=" stands for "x = x**5")

# x = 5
# print(x)

# x+=6
# print(x)

# x-=6
# print(x)

# x*=6
# print(x)

# x/=6
# print(x)

# x%=6
# print(x)

# x//=6
# print(x)

# x**=6
# print(x)


# 3. Comparison Operators
  # comparision operators are used to compare between two numbers
  # examples of comparison operators are:-  ==, >, <, >=, <=, !=
   # "==" = equals to
   # ">" = greater than
   # "<" = smaller than
   # ">=" = greater than equals to
   # "<=" = smaller than equals to

# a = 5
# b = 10

# print(a==b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)
# print(a!=b)


# 4. Logical Operators
  # logical operators are those operators used to create condition
  # examples of logical operators are:-  and, or, not
   # "and" logical operator = True if both the operands are true
   # "or" logical operator = True if either of the operands is true
   # "not" logical operator = True if operands is false

# x = 5
# y = 6

# print((x==y) and (x<y))
# print((x==y) or (x<y))
# print(not(x==y))


# 5. Identity Operators
  # identity operators are used to check if the two values(or variables) are located on the same part of
  # the memory. Two variables that are equal does not imply that they are identical
  # examples of identity operator are:-  is, is not
   # "is" identity operator = True if the operands are identical(refer to the same object)
   # "is not" identity operator = True if the operands are not identical(do not refer to the same object)

# a = 5
# b = 10
# c = a

# print(a is b)
# print(a is c)
# print(a is not b)


# 6. Membership Operators
  # membership operators are used to test whelther a value or variable is found in a sequence(string, list, tuple,
  # set and dictionary)
  # example of membership operators are:-   "in" and "not in"
   # "in" membership operators = True if value/variable is found in the sequence
   # "not in" membership operators = True if value/variable is not found in the sequence

# ls = [1, 2, 3, 4, 5]

# print(5 in ls)
# print(100 in ls)
# print(100 not in ls)


# 7. Bitwise Operators
  # bitwise operators act on operands as if they were strings of binary digits. They operate bit by bit
  # examples of bitwise operators are :-   "&", "|", etc.
   #  "&" bitwise AND
   #  "|" bitwise OR

x = 10
y = 4

print(x & y)
print(x|y)