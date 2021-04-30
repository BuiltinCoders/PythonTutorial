import random

# overview
instruction = {"s":"snake", "w":"water", "g":"gun"}
characters = ["s", "w", "g"]

print(" Snake Water Gun ".center(50, "*"))
print()
print("You have 10 chances to score greater than computer")
print()
print("Instruction:-")
for key, value in instruction.items():
    print(f"Press {key} for {value}")

# main function

computer_score = 0
player_score = 0
chances = 10

for i in range(10):
    computer_choice = random.choice(characters)
    try:
        print()
        user_choice = input("Select your character:\n").lower()
    except Exception as error:
        print("Some thing went wrong")
    
    if user_choice not in characters:
        print("Invalid input")
        continue
    
    elif user_choice==computer_choice:
        print("This is draw between you and computer")
    
    elif user_choice=="s" and computer_choice=="w":
        print("You win!")
        player_score+=1
    
    elif user_choice=="s" and computer_choice=="g":
        print("You loose!")
        computer_score+=1
    
    elif user_choice=="w" and computer_choice=="g":
        print("You win!")
        player_score+=1
    
    elif user_choice=="w" and computer_choice=="s":
        print("You loose!")
        computer_score+=1
    
    elif user_choice=="g" and computer_choice=="s":
        print("You win!")
        player_score+=1
    
    elif user_choice=="g" and computer_choice=="w":
        print("You loose!")
        computer_score+=1
    print(f"Computer choice: {computer_choice}")
    print(f"Player score: {player_score}  Computer score: {computer_score}")
    chances-=1
    print(f"Chances left: {chances}")

if player_score>computer_score:
    print("\nYou defeated the computer")
    print("Keep it up")
else:
    print("\nComputer defeated you")
    print("Try again")