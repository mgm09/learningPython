# High Scores 2.0
# Demonstrates nested sequences

scores = []

choice = None
while choice != "0":
    print(
        """
        High Scores 2.0
        
        0 - Quit
        1 - List scores
        2 - Add a score
        """
    )

    choice = input("Choice: ")
    print()

    # Exit
    if choice == "0":
        print("Good-bye")

    # Display high-score table
    elif choice == "1":
        print("High Scores\n")
        print("NAME\tSCORE")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)

    # Add a score
    elif choice == "2":
        name = input("What is the player's name?: ")
        score = int(input("What score did the player get?: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]     # Keep only top 5 scores

    # Some unknown choice
    else:
        print("Sorry. But", choice, "isn't a valid choice.")

input("\n\nPress the enter key to exit.")
