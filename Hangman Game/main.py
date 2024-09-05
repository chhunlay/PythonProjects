import random

from hangman_words import word_list
from hangman_arts import stages, logo
# from replit import clear
# use random
print(logo)

chosen_word = random.choice(word_list)
# print(chosen_word)
# create new variable to check 
end_of_game = False
lives = 6      
 
# generate blank letter for the words
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

# use while loop 
while not end_of_game:
    # guess the word
    guess = input("Gess a letter: ").lower()
    # clear()
    
    # lose condition
    if guess not in chosen_word:
        print("You guessed {guess}, that's not in the word. You lose a life.")
        lives -=1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            
    # join all the elements in the list and turn it into a string
    print(f"{' '}".join(display))
            
    # check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Currrent position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(display)

    # check if the word is gessed then break the loop
    if "_" not in display:
        end_of_game = True
        print("==> You win")
        
    print(stages[lives])
 
