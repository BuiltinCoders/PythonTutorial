# design a calculator which will correctly solve all the problems except the following one:-
# 45*3=555, 56+9=77, 56/6=4

# our programe should take opertor and the two numbers as input from the user then return
# the result

######################### PROGRAME #######################

print("Please don't use spaces in operation")
query = input("Enter operation : ")

if '*' in query:
    num1, num2 = query.split('*')
    if num1=='45' and num2=='3':
        print('result :',555)
    else:
        print('result :',int(num1)*int(num2))

elif '+' in query:
    num1, num2 = query.split('+')
    if num1=='56' and num2=='9':
        print('result :',77)
    else:
        print('result :',int(num1)+int(num2))

elif '-' in query:
    num1, num2 = query.split('-')
    print('result :',int(num1)-int(num2))

elif '/' in query:
    num1, num2 = query.split('/')
    if num1=='56' and num2=='6':
       print('result :',4)
    else:
        print('result :',int(num1)/int(num2))