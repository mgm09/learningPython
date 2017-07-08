# Guessing number game
#
# The computer picks a random number between 1 and 100
# The play tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

import random

print("\tWelcome to 'Guess my number'")
print("\nI'm thinking of a number between 1 and 100.")
print("Try and guess it in as few attempts as possible.")

# set initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# guessing loop
while guess != the_number:
    if guess > the_number:
        print("lower...")
    else:
        print("Higher...")

    guess = int(input("Take a guess: "))
    tries += 1

# congratulate the player

print("You guessed it! The number was", the_number)
print("And it only took you", tries, "tries!")

input("\n\nPress enter to exit.")