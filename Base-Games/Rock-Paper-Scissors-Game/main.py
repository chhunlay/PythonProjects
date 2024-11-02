import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______) 
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

while True:
    user_input = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")

    if user_input.isdigit():
        user_choice = int(user_input)

        if 0 <= user_choice <= 2:
            break
        else:
            print("Invalid input. Please enter a number between 0 and 2.")
    else:
        print("Invalid input. Please enter a valid number.")

print("\nYour choice:")
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("\nComputer's choice:")
print(game_images[computer_choice])

print("\nResult:")
if user_choice == computer_choice:
    print("It's a draw")
elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose")

####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end