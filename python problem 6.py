#                                           Guess The Number

import random

a = int(input("Enter the value of a:\n"))
b = int(input("Enter the value of b:\n"))

# generating random number
random_int = random.randint(a, b)

trials = 1

for i in range(2):
    
    print('\n', end='')
    if i == 0:
        print("Player 1")
    else:
        print("Player 2")
    
    while True:
        user_guess = int(input(f"Please guess the number between {a} and {b}:\n"))

        if user_guess > random_int:
            print(f"Wrong, guess a smaller number again.")
            trials += 1

        elif user_guess < random_int:
            print(f'Wrong, guess a smaller number again.')
            trials += 1

        elif user_guess == random_int:
            print(f"Correct, you took {trials} to guess the number.")

            if i == 0:
                trial1 = trials
            else:
                trial2 = trials

            trials = 1
            break

print('\n', end='')
if trial1 < trial2:
    print(f"Player 1 wins!")
else:
    print(f"Player 2 wins!")
