# # recursion is a situation when a function calls itself

# def print1(str1):
#     print1(str1)
#     print("This is "+ strl)

# print1("Nitesh Kumar")


# # Factorial

# 1. using iterative approach

num = int(input("Enter a number:\n"))

# def factorial_iterative(n):
#     factorial = 1
#     for i in range(n):
#         factorial = factorial * (i+1)
#     return factorial
# print(factorial_iterative(num))


# 2. using recursive approach

# def factorial_recursive(n):
#     if n==1:
#         return 1
#     else:
#         return n * factorial_recursive(n-1)

# print(factorial_recursive(num))



# # OUICK QUIZE

def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(num))
