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
    print()

    if choice == "0":
        print("Exited")

    elif choice == "1":
        print(pool, strength, health, wisdom, dexterity)