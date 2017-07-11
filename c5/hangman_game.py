# Hangman game
#
# The classic game of hangman. The computer picks a random word and the player needs to guess the word right, by guessing
# one letter at a time. If the player can't guess the word in time, the little stick figure gets hanged.

# imports
import random

# contants

HANGMAN = (
    """
    - - - - -
    |       |
    |
    |
    |
    |
    |
    |
    |
    - - - - - - - -
    """,
    """
    - - - - -
    |       |
    |       0
    |
    |
    |
    |
    |
    |
    - - - - - - - -
    """,
    """
    - - - - -
    |       |
    |       0
    |      -+-
    |
    |
    |
    |
    |
    - - - - - - - -
    """,
    """
    - - - - -
    |       |
    |       0
    |     /-+-
    |
    |
    |
    |
    |
    - - - - - - - -
    """,
    """
    - - - - -
    |       |
    |       0
    |     /-+-/
    |
    |
    |
    |
    |
    - - - - - - - -
    """,
    """
    - - - - -
    |       |
    |       0
    |     /-+-/
    |       |
    |
    |
    |
    |
    - - - - - - - -
    """,
    """
    - - - - -
    |       |
    |       0
    |     /-+-/
    |       |
    |       |
    |
    |
    |
    - - - - - - - -
    """,
    """
    - - - - -
    |       |
    |       0
    |     /-+-/
    |       |
    |       |
    |     |
    |     |
    |
    - - - - - - - -
    """,
    """
    - - - - -
    |       |
    |       0
    |     /-+-/
    |       |
    |       |
    |     |   |
    |     |   |
    |
    - - - - - - - -
    """)

# Max amount of times user can be wrong
MAX_WRONG = len(HANGMAN) - 1

# Words that are used for game
WORDS = ("OVERUSED", "CLAM", "GUAM", "TAFFETA", "PYTHON")

# Initialize variables
word = random.choice(WORDS)  # the word to be guessed

so_far = "-" * len(word)  # one dash for each letter in word to be guessed

wrong = 0  # number of wrong guesses the player has made

used = []  # letters already guessed

print("Welcome to Hangman, good luck!")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nYou've used the following letters:\n", used)
    print("\nSo far, the word is: \n", so_far)

    guess = input("\n\nEnter your guess: ")
    guess = guess.upper()

    while guess is used:
        print("You've already guessed the letter", guess)
        guess = input("Enter your guess: ")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print("\nYes!", guess, "is in the word!")

        # create a new so_far to include guess
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new

    else:
        print("\nSorry,", guess, "isn't in the word.")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou've been hanged!")
else:
    print("\nYou guessed it!")

print("\nThe word was", word)

input("\n\nPress the enter key to exit.")