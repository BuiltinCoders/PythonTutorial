# if __name__== '__main__' runs the code in it only if the __name__== '__main__' or
# the code under the if __name__== '__main__' is run directly form the main file

def printhar(str):
    return f"This '{str}' is printed by printhar funtion"

def add(num1, num2):
    return num1 + num2 + 5

# print(printhar("Nitesh"))
# o = add(7, 3)
# print(o)

print(__name__)
# using if __name__== 'main'
if __name__== '__main__':
    print(printhar("Nitesh"))
    o = add(7, 3)
    print(o)