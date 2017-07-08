# Guessing number game.
# The player has a limited number of tries to guess the correct number.

import random

print("\tWelcome to 'Guess my number'")
print("\tI am thinking of a number between 1 and 100.")
print("\tYou have 5 tries to guess the number I am thinking of")

# initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

while guess != the_number:
    if guess > the_number:
        print("Lower...")
    elif guess < the_number:
        print("Higher...")
    if tries == 5:
        print("too bad you ran out of tries! Better luck next time loser!")

    tries += 1
    guess = int(input("Take a guess: "))



# Congratulate the player
print("You guess it right! The number was", the_number)
print("And it only took you", tries,"tries.")

