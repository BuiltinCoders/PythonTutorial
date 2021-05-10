#                                       The Next Palindrome
while True:
    try:
        t = int(input("Enter the number of test cases:\n"))
        break
    except ValueError:
        print("Only integer values are allowed")

for x in range(t):
    try:
        n = int(input("Enter the Number:\n"))
    
    except ValueError:
        print("Only integer values allowed")
    
    else:
        i = n+1
        while i>n:
            i_str = str(i)
            if i_str==i_str[::-1]:
                print(f"Next palindrome for {n} is {i}\n")
                break
            else:
                i+=1
    