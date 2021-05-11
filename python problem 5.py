#                Palindromify The List

try:
    size = int(input("Enter the size of the list:\n"))

    l = []

    for i in range(size):
        value = int(input(f"Enter the {i} value of the list:\n"))
        l.append(value)

# handling exception
except ValueError:
    print("Only integer values are allowed")

else:
    pl = []

    for j in l:
        if j > 10:
            p = j+1
            while p > j:
                # checking whelter the p is palindrom or not
                if str(p) == str(p)[::-1]:
                    pl.append(p)
                    break
                else:
                    p += 1
        else:
            pl.append(j)

    print(f"Palindromified list is {pl}")
