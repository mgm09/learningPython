# Mood computer
# Demonstrates the elis clause

import random

print("I sense your energy. Your true emotions are coming across my screen.")
print("You are....")

mood = random.randint(1, 3)

if mood == 1:
    # Happy
    print( \
        """
        :)
        """)
elif mood == 2:
    # Neutral
    print(\
        """
        :>|
        """)
elif mood == 3:
    # Sad
    print (\
        """
        : (
        """)
else:
    print("Illegal mood value! (You must be in a really bad mood!).")
    print("... today.")

input("\n\nPress enter to exit")