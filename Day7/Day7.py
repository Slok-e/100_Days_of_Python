import random
import os
from words import word_list
from art import stages, logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
guessed_letters = []

print(logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks representing the word lenght.
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    os.system("clear")

    #Check if letter already guessed.
    if guess in guessed_letters:
        print(f"You already guessed {guess},  try again.")
    else:
        guessed_letters.append(guess)
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You choice {guess}, is not in the word, you lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
        

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])