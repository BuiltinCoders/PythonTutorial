def gettime():
    import datetime
    return datetime.datetime.now()

print("Instructions :-")

print("Press '0' = To select first option")
print("Press '1' = To select second option")
print("Press '2' = To select third option\n")

try:
    tp = int(input("What you want to do:\n0. retrieve data\n1. log data\n\n"))
    while tp<0 or tp>1:
        print("Option not found\n")
        tp = int(input("What you want to do:\n0. retrieve data\n1. log data\n\n"))
        continue
    
    profile = int(input("Which profile:\n0. Harry\n1. Rohan\n2. Hammad\n\n"))
    while profile<0 or profile>2:
        print("Option not found\n")
        profile = int(input("Which profile:\n0. Harry\n1. Rohan\n2. Hammad\n\n"))
        continue
    
    plane = int(input("What to you want to access:\n0. Diet\n1. Exercise\n\n"))
    while plane<0 or plane>1:
        print("Option not found\n")
        plane = int(input("What to you want to access:\n0. Diet\n1. Exercise\n\n"))
        continue

except Exception as e:
    print("Try to input correct details")

# # Harry

if profile<0 or profile>2:
    print("Option not found")

# read diet plane of harry
elif tp==0 and profile==0 and plane==0:
    print()
    print("Content:")
    with open("exercise5(harry d).txt", "r") as f:
        content = (f.read())
        print(content)

# log diet plane of harry
elif tp==1 and profile==0 and plane==0:
    diet = input("What you want to log:\n")
    print("Data loged")
    print("Date and Time:",gettime())
    with open("exercise5(harry d).txt", "a") as f:
        if len(diet)>80:
            f.write(f"Date and Time: {gettime()}\n")
            f.write(f"{diet[0:81]}\n")
            f.write(f"{diet[82:len(diet)]}\n\n")
        else:
            f.write(f"Date and Time: {gettime()}\n")
            f.write(f"{diet}\n\n")

# read exercise plane of harry
elif tp==0 and profile==0 and plane==1:
    print()
    print("Content:")
    with open("exercise5(harry e).txt", "r") as f:
        content = (f.read())
        print(content)

# log exercise plane of harry
elif tp==1 and profile==0 and plane==1:
    diet = input("What you want to log:\n")
    print("Data loged")
    print("Date and Time:",gettime())
    with open("exercise5(harry e).txt", "a") as f:
        if len(diet)>80:
            f.write(f"Date and Time: {gettime()}\n")
            f.write(f"{diet[0:81]}\n")
            f.write(f"{diet[82:len(diet)]}\n\n")
        else:
            f.write(f"Date and Time: {gettime()}\n")
            f.write(f"{diet}\n\n")

# # Rohan

# read diet plane of rohan
elif tp==0 and profile==1 and plane==0:
    print()
    print("Content:")
    with open("exercise5(rohan d).txt", "r") as f:
        content = (f.read())
        print(content)

# log diet plane of rohan
elif tp==1 and profile==1 and plane==0:
    diet = input("What you want to log:\n")
    print("Data loged")
    print("Date and Time:",gettime())
    with open("exercise5(rohan d).txt", "a") as f:
        if len(diet)>80:
            f.write(f"Date and Time: {gettime()}\n")
            f.write(f"{diet[0:81]}\n")
            f.write(f"{diet[82:len(diet)]}\n\n")
        else:
            f.write(f"Date and Time: {gettime()}\n")
            f.write(f"{diet}\n\n")

# read exercise plane of rohan
elif tp==0 and profile==1 and plane==1:
    print()
    print("Content:")
    with open("exercise5(rohan e).txt", "r") as f:
        content = (f.read())
        print(content)

# log exercise plane of rohan
elif tp==1 and profile==1 and plane==1:
    diet = input("What you want to log:\n")
    print("Data loged")
    print("Date and Time:",gettime())
    with open("exercise5(rohan e).txt", "a") as f:
        if len(diet)>80:
            f.write(f"Date and Time: {gettime()}\n")
            f.write(f"{diet[0:81]}\n")
            f.write(f"{diet[82:len(diet)]}\n\n")
        else:
            f.write(f"Date and Time: {gettime()}\n")
            f.write(f"{diet}\n\n")

# # Hammad

# read diet plane of hammad
elif tp==0 and profile==2 and plane==0:
    print()
    print("Content:")
    with open("exercise5(hammad d).txt", "r") as f:
        content = (f.read())
        print(content)

# log diet plane of hammad
elif tp==1 and profile==2 and plane==0:
    diet = input("What you want to log:\n")
    print("Data loged")
    print("Date and Time:",gettime())
    with open("exercise5(hammad d).txt", "a") as f:
        if len(diet)>80:
            f.write(f"Date and Time: {gettime()}\n")
            f.write(f"{diet[0:81]}\n")
            f.write(f"{diet[82:len(diet)]}\n\n")
        else:
            f.write(f"Date and Time: {gettime()}\n")
            f.write(f"{diet}\n\n")

# read exercise plane of rohan
elif tp==0 and profile==2 and plane==1:
    print()
    print("Content:")
    with open("exercise5(hammad e).txt", "r") as f:
        content = (f.read())
        print(content)

# log exercise plane of rohan
elif tp==1 and profile==2 and plane==1:
    diet = input("What you want to log:\n")
    print("Data loged")
    print("Date and Time:",gettime())
    with open("exercise5(hammad e).txt", "a") as f:
        if len(diet)>80:
            f.write(f"Date and Time: {gettime()}\n")
            f.write(f"{diet[0:81]}\n")
            f.write(f"{diet[82:len(diet)]}\n\n")
        else:
            f.write(f"Date and Time: {gettime()}\n")
            f.write(f"{diet}\n\n")
