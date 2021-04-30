mystr = "virtual world"
decimal = 's.s.f.a.e'
digits = "12345"

# # String slicing

# 1. start argument
   # staring index of string
# print(mystr[0:])
# 2. stop argument
   # ending index of string
# print(mystr[:7])
# 3. step argument
   # skipping index of string
# print(mystr[::2])

# string slicing refers to print perticular part of string
# print(mystr[0:7])

# if we left stop argument undefined it will be set to end of string
# print(mystr[0:])

# if we left start argument undefined it will be set to '0' means starting of the string
# print(mystr[:7])

# if we left both arguments undefined it will print the whole string
# print(mystr[:])

# if left step index undefined it will set to default 1
# print(mystr[::])

# negative arguments
# print(mystr[-5:-3])

# to reverse the order of string
# print(mystr[::-1])
# print(mystr[::-2])

# len function is used to find the length of string
# print(len(mystr)


# # Other Functions and Method

# 1. type function
  # type function is used to get data type of any data
# print(type(mystr))

# 2. isalnum method
  # isalnum function is used to check whelter the data is integer or not or whelter the data is alpha or not
# print(mystr.isalnum())

# 3. isalpha method
  # isalpha method is used to check whelther the data is alpha or not
# print(mystr.isalpha())

# 4. endswith method
  # endswith method is used to check whelther the data is ending with perticular syndex
# print(mystr.endswith('ld'))

# 5. count method
  # count method is used to count perticular character of a string
# print(mystr.count('r'))

# 6. capitalize method
  # capitalize method is used to make first letter capital
# print(mystr.capitalize())

# 7. find method
  # find method is used to find perticular character in a string
# print(mystr.find('world'))

# 8. lower method
  # lower method is used to write the whole string in small letters
# print(mystr.lower())

# 9. upper method
  # upper method is used to write the whole string in capital letters
# print(mystr.upper())

# 10. replace method
  # replace method is used to replace perticular character or word with another character or word
# print(mystr.replace("world", "environment"))

# 11. casefold method
  # casefold method converts string into lower case
# print(mystr.casefold())

# 12. centre method
  # centre method returns a centered string
# print(mystr.center(17, "*"))

# 13. encode method
  # encode method returns an encoded version of the string
# print(mystr.encode())

# 14. expandtabs method
  # expandtabs method sets the tab size of the string
# print(mystr.expandtabs(100))

# 15. format method
  # format method formats specified values in a string
# print(mystr.format())

# 17. format_map method
  # format_map method formats specified values in a string
# print(mystr.format_map())

# 18. isdecimal method
  # isdecimal method returns true if all characters in the string are decimal
# print(mystr.isdecimal())
# print(decimal.isdecimal())

# 19. isidentifier method
  # isidentifier method returns true if the string is an identifier
# print(mystr.isidentifier())

# 20 islower method
  # islower method returns true if all characters in the string are lower case
# print(mystr.islower())