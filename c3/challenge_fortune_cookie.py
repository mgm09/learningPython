# Fortune cookie game
# The player will be provided with 5 different fortunes with one being chosen at random.

import random

print("Welcome, you are about to hear sacred fortunes of your future")

answer = ""
while not answer:
    answer = input("Are you ready, yes or no? ")

if answer == "yes":
    fortune = random.randint(1, 5)
    if fortune == 1:
        print("fortune 1 is given")
    elif fortune == 2:
        print("fortune 2 is given")
    elif fortune == 3:
        print("fortune 3 is given")
    elif fortune == 4:
        print("fortune 4 is given")
    elif fortune == 5:
        print("fortune 5 is given")
    else:
        print("looks like you do not have a future.....")
else:
    print("well what a shame, you will never know....")
