while True:
    try:
        apple = int(input("Enter the total value:\n"))
        mn = int(input("Enter the minimum value:\n"))
        mx = int(input("Enter the maximum value:\n"))

        if mn>mx:
            print("Your minimum value is greater than maximum value")

    except ValueError:
        print("Your given input must be integer")


    else:
        for i in range(mn, mx+1):
            if mn == mx:
                print("There is no range between mn and mx")
                for j in range(mn, mx+1):
                    if apple%j==0:
                        print(f"{j} is a factorial of {apple}")
                    else:
                        print(f"{j} is not a factorial of {apple}")
            
            else:
                if apple%i==0:
                    print(f"{i} is a factorial of {apple}")
                else:
                    print(f"{i} is not a factorial of {apple}")
        break