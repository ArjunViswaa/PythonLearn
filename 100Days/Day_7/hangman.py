import random
import hangman_words
from hangman_art import stages, logo

print(logo)

chosen_word = random.choice(hangman_words.word_list)
# print(chosen_word)

placeholder = ""
for letter in chosen_word : 
    placeholder += "_"

print(placeholder)


game_over = False
correct_letters = []
lives = 6

while not game_over : 
    print(f"*********************** {lives} / 6 Lives left ***********************")
    guess_letter = input("Guess a letter : ").lower()
    display = ""

    if guess_letter in correct_letters : 
        print(f"You've already guessed {guess_letter}...")

    for letter in chosen_word : 
        if letter == guess_letter : 
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters : 
            display += letter
        else : 
            display += "_"

    print(display)

    if guess_letter not in chosen_word : 
        lives -= 1
        print(f"You guessed {guess_letter}, that's not in the word. You lose a life")
        if lives == 0 : 
            game_over = True
            print(f"*********************** YOU LOSE!!! The correct word is {chosen_word} ***********************")

    print(stages[lives])

    if "_" not in display : 
        game_over = True
        print(f"*********************** YOU WIN!!! The correct word is {chosen_word} ***********************")

# for letter in chosen_word : 
#     if letter == guess_letter : 
#         print("Right")
#     else : 
#         print("Wrong")