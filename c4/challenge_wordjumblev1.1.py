# Word jumble v1.1
# The counter picks a random word and "jumbles" it
# The player can ask for a hint if they wish
# The player has to guess the original word

import random

# Create an empty variable for counting the number of guesses
fail = 0

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

# Pick one word randomly from the sequence
word = random.choice(WORDS)
correct = word

# Create a jumbled version of the word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[0:position]

# Start the game
print("""
            Welcome to Word Jumble!
        
        Unscramble the letters to make a word.
      (Press the enter key at the prompt to quit.)
    """
       )

print("The jumble is:", jumble)

# Get the player to guess the word
guess = input("\nYour guess: ")
while guess != correct and guess != "" and fail < 4 or guess == "hint":
    if guess != "hint":
        print("Sorry that is not the correct answer. Try entering 'hint' for some help")
        fail = fail + 1
    guess = input("Your guess: ")
    if guess == "hint":
        print("hint", correct[len(correct)-3])
        continue

if guess == correct:
    print("Thats it, you guess correct!\n")
    print("Points: ", (5-(fail)))
elif fail <= 5:
    print("Sorry you guess wrong too many times")
    print("POINTS: 0")

print("Thanks for playing")
input("\nPress enter to exit")