# Trust fund buddy
# Demonstrates type conversation

print(
    """
            Trust Fund Buddy

    Totals your monthly spending so that your trust fund doesn't run out (and your forced to get a real job).

    Please enter the requested, monthly costs. Since you're rich, ignore pennies and use only dollar amounts.

    """
)


car = int(input("Lambo tune-ups: "))
rent = int(input("Manhatten apartment: "))
jet = int(input("Private jet rent: "))
gifts = int(input("Gifts: "))
food = int(input("Dinning out: "))
staff = int(input("Staff (butlers, chef, driver, assistant): "))
guru = int(input("Personal guru and coach: "))
games = int(input("Computer games: "))

total = car + rent + jet + gifts + food + staff + guru + games

print("\nGrand Total:", total)

input("\n\nPress the enter key to exit")