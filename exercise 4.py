rows = int(input("How many rows:\n"))
tp = int(input("Type 'o' or '1'"))

bl = bool(tp)

if bl == True:
    for i in range(1, rows+1):
        for j in range(1, i+1):
            print("*", end="")
        print()               
elif bl == False:
    for i in range(rows, 0, -1):
        for j in range(1, i+1):
            print("*", end="")
        print()