# flip a coin 100 times and show how many times it lands on heads & tails.

import random

print("welcome to the coin flip. Lets see which is luckier heads or tails!")
input("Press enter to begin the coin toss.")

# initial values
count = 100
flip = 1
heads = "Heads"
tails = "Tails"
h = 1
t = 1

# flip the coin
while flip != count:
    coin = random.randint(1, 2)
    if coin == 1:
        print(heads)
        h += 1
    elif coin == 2:
        print(tails)
        t += 1

    flip += 1

# print the results
print("The coin was flipped", flip, "times!")
print("Head was flipped", h, "times!")
print("Tails was flipped", t, "times!")
