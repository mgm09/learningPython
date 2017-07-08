# Geek translator
# Demonstrates using dictionaries

geek = {"404": "Clueless. From the web error message 404. Meaning page not found.",
        "Googling": "Searching the internet for background information on a person.",
        "Keyboard Plaque": "The collection of debris found in computer keyboards.",
        "Link Rot": "The collection of debris found in computer keyboards.",
        "Percussive Maintenance": "The act of striking an electronic device to make it work.",
        "Uninstalled": "Being fired. Especially popular during the dot-bomb era."}

choice = None
while choice != 0:
    print(
        """
        
        Geek translator
        
        0 - Quit
        1 - Look up a geek term
        2 - Add a geek term
        3 - Redefine a geek term
        4 - Delete a geek term
        """
    )

    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Good-bye")

    # get a definition
    elif choice == "1":
        term = input("What term do you want me to translate?: ")
        if term in geek:
            definition = geek[term]
            print("\n", term, "means", definition)
        else:
            print("\nSorry, I don't know", term)

    # add a term-definition pair
    elif choice == "2":
        term = input("What term do you want to add?: ")
        if term not in geek:
            definition = input("\nWhat's the definition?: ")
            geek[term] = definition
            print("\n", term, "has been added.")
        else:
            print("\nThat term already exists! Try redefining it.")

    # redefine an existing term
    elif choice == "3":
        term = input("What term do you want to redefine?: ")
        if term in geek:
            definition = input("What's the new definition?: ")
            geek[term] = definition
            print("\n", term, "has been redefined.")
        else:
            print("\nThat term doesn't exist! Try adding it")

    # delete a term-definition pair
    elif choice == "4":
        term = input("What term do you want me to delete?: ")
        if term in geek:
            del geek[term]
            print("\nOkay, I deleted", term)
        else:
            print("\nI can't do that!", term, "doesn't exist in the dictionary.")

    # some unknown choice
    else:
        print("\nSorry, but", choice, "isn't a valid choice.")

input("\n\Press enter to exit.")

