# Challenge
# Print a list of words in random order. The programme should print all the words and not repeat any.

import random

random_list = []
WORDS = ["Smooth","Run","Little","Dady","Hunter","Pog","Art","Question"]
print("\n\nOriginal list of words:", WORDS)

while WORDS:
   word = random.choice(WORDS)
   random_list.append(word)
   WORDS.remove(word)

print("\n", random_list)
