from random import randint
import art

""" Draft:
1. Choose a random number between 1 and 100
2. Funtion to set difficulty
3. Let the user guess a number
4. Funtion to check users' guess against actual answer
5. Track the number of turns and reduce by 1 if they get it wrong.
6. Repeat the guessing funcionality if they get it wrong.
"""

print("Welcome to the number guessing game")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy': 
        return 10
    elif level == 'hard':
        return 5
    else:
        print("Invalid choice. Setting difficulty to 'easy' by default.")
        return 10

def check_guess(guess, answer):
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        print(f"You got it! The answer was {answer}.")

def game():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    
    answer = randint(1, 100)
    turns = set_difficulty()
    guess = None
    
    while guess != answer and turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        
        check_guess(guess, answer)
        turns -= 1
        
        if guess != answer and turns > 0:
            print("Guess again.")
        elif guess != answer and turns == 0:
            print("You've run out of guesses, you lose.")
            print(f"The correct answer was {answer}.")

game() 