######################## GUESS THE NUMBER ##########################

# # Concept:-
  # 1. Take input from the user.
  # 2. Sujest whelter the number is greater or smaller than the preset number.
  # 3. If the user guess is wrong ask user again.
  # 4. The user have only 10 chances.
  # 5. If user guess the number under his/her 10 chances declare him/her winner

print('\n')
print(" Guess The Number ".center(50, '*'))

print("You Have 10 Chances To Win This Game")
guess = int(input("Enter a number: "))

chances = 9
or_num = 18
game_over = True

while game_over:
    if guess<or_num:
        print('Try again! Guess greater number than this')
        print('\n')
        print("You Have",chances,"Chances Left")
        guess = int(input("Enter a number again: "))
        if chances>1:
            chances-=1
        else:
            print("You loose this game")
            break
    elif guess>or_num:
        print("Try again! Guess smaller number than this")
        print('\n')
        print("You Have",chances,"Chances Left")
        guess = int(input("Enter a number again: "))
        if chances>0:
            chances-=1
        else:
            print("Sorry! You loose this game")
            break
    elif guess==or_num:
        print("Congratulation\'s You have won this game by",chances,"chances")
        break