# Word jumble
#
# The computer picks a random word then "jumbles" it
# The player has to guess the original word

import random

# Create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

# Pick one word randomly from the sequence
word = random.choice(WORDS)
correct = word

# Create a jumbled version of the word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[0:position] + word[(position + 1):]

# Start the game
print(
    """
            Welcome to Word Jumble!
        
        Unscramble the letters to make a word.
      (Press the enter key at the prompt to quit.)
    """
)
print("The jumble is:", jumble)

# Get the players guess
guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    guess = input("Your guess: ")

if guess == correct:
    print("That's it! You guess it!\n")

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")