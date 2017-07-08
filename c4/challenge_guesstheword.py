# Guess the word challenge game
# The computer chooses a random word and the player has to guess the word
# The player has 5 chances to guess letters in the word, then has to guess the word

import random

# create and empty variable to count the number of guesses made for letters in a word
word_count = 0

# create a selection of words to randomly choose
WORDS = ("python", "difficult", "elaine", "jumble", "easy", "saxaphone")

# pick one word from the sequence randomly
correct_word = random.choice(WORDS)

# start the game
print("""
               Welcome to the word guessing game!
        
        You get 5 chances to guess letters in the word.
        After that you must guess what you think the word is
        
                            Good luck!
        """
      )
print("\nThe word you have to guess has", len(correct_word), "letters.")

# get the player to guess possible letters in the word

while word_count < 5:
    letter = input("Guess a letter -----> ")
    if letter.lower() in correct_word.lower():
        print("Yes!")
    else:
        print("No")
    word = word_count + 1

answer = input("Now guess the word: ")

if answer.lower() == correct_word.lower():
    print("Yes! You guessed it right!")
else:
    print("Sorry thats not correct, the correct word is:", correct_word)
