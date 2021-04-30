# # break statement is used to stop the loop and exit the loop

# i=1
# while True:
#     if i==31:
#         break
#     print(i, end=" ")
#     i+=1

# # continue statement is used to skip the left code if condition is true

# i=0
# while True:
#     i+=1
#     if i<31:
#         continue
#     if i==51:
#         break
#     print(i, end=' ')



############################ QUIZE TIME #############################
print('\n')
print(' QUIZE TIME '.center(50, '*'))

while True:
    number = int(input('Enter the number : \n'))
    if number<=100:
        print("Try number greater than this")
        continue
    else:
        print('Congratulation! you have have entered anumber greater than 100 ')
        break