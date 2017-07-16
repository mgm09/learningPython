# Character building game
# This programme lets the user build skills for a character in an RPG

print(
    """
                *** The RPG character building tool ***
                
                    Add from a pool of points to four 
                    different skill sets for your hero.
""")

pool = 30           # pool of points
strength = 0        # skill set strength
health = 0          # skill set health
wisdom = 0          # skill set wisdom
dexterity = 0       # skill set dexterity
choice = None       # the menu choice

while choice != "0":

    print("""
            
            Choose an option:
            
            0 - exit
            1 - view skill points
            2 - remove skills points
            3 - Add skill points
    """)

    choice = int(input("Option: "))
    if choice == 0:
        print("Exited")

    # list all the different skills with points
    elif choice == 1:
        print(
            """
            Skills:
                
                Strength is {0}
                Health is {1}
                Wisdom is {2}
                Dexterity is {3}
                
                Pool is {4}
                """.format(strength, health, wisdom, dexterity, pool))

    elif choice == 2:
        print(
            """
            Choose skill to reduce:
                
                0. Exit
                1. Strength
                2. Health
                3. Wisdom
                4. Dexterity
        """)
        reduce_choice = int(input("Choice: "))
        if reduce_choice is "0":
            print("Exited")
        elif reduce_choice is 1 and strength > 0:
            reduce_value = int(input("Reduce skill Strength to: "))
            if reduce_value < strength and reduce_value >= 0:
                pool = pool + (strength - reduce_value)
                strength = reduce_value
            else:
                print("sorry you can not reduce any more points from Strength.")
        elif reduce_choice is 2 and health > 0:
            reduce_value = int(input("Reduce skill Health to: "))
            if reduce_value < health and reduce_value >= 0:
                pool = pool + (health - reduce_value)
                health = reduce_value
            else:
                print("Sorry you can not reduce any more points from Health.")
        elif reduce_choice is 3 and wisdom > 0:
            reduce_value = int(input("Reduce skill Wisdom to: "))
            if reduce_value < wisdom and reduce_value >= 0:
                pool = pool + (wisdom - reduce_value)
                wisdom = reduce_value
            else:
                print("Sorry you can not reduce any more points from Wisdom,")
        elif reduce_choice is 4 and dexterity > 0:
            reduce_value = int(input("Reduce skill Dexterity to: "))
            if reduce_value < dexterity and reduce_value >= 0:
                pool = pool + (dexterity - reduce_value)
                dexterity = reduce_value
            else:
                print("Sorry you can not reduce any more points from Dexterity.")

    elif choice == 3 and pool > 0:
        print(
            """
            Choose skill to increase:
            
                0. Exit
                1. Strength
                2. Health
                3. Wisdom
                4. Dexterity
        """)
        increase_choice = int(input("Choice: "))
        if increase_choice is "0":
            print("Exited")
        elif increase_choice is 1 and strength < 30:
            increase_value = int(input("Increase Strength to: "))
            if increase_value > strength and increase_choice <= 30:
                pool = pool - (increase_value - strength)
                strength = increase_value
            else:
                print("You can not increase Strength any further.")
        elif increase_choice is 2 and health < 30:
            increase_value = int(input("Increase Health to: "))
            if increase_value > health and increase_choice <= 30:
                pool = pool - (increase_value - health)
                health = increase_value
            else:
                print("You can not increase Health any further.")
        elif increase_choice is 3 and wisdom < 30:
            increase_value = int(input("Increase Wisdom to: "))
            if increase_value > wisdom and increase_choice <= 30:
                pool = pool - (increase_value - wisdom)
                wisdom = increase_value
            else:
                print("You can not increase Wisdom any further.")
        elif increase_choice is 4 and dexterity < 30:
            increase_value = int(input("Increase Dexterity to: "))
            if increase_value > dexterity and increase_value <= 30:
                pool = pool - (increase_value - dexterity)
                dexterity = increase_value
            else:
                print("You can not increase Dexterity any further.")

input("Press enter to exit programme.")