# The counting machine
# A tool that will count for the user, from any starting number to ending number.

number = 0


print("Lets help you count!")
start = int(input("\nEnter the number you want to start with: "))
finish = int(input("Now enter the number you want to end on: "))
increase = int(input("Finally enter the amount you wish to count by: "))

print("\n\nCounting for you now:")
for number in range(start, finish+1, increase):
    print(number)

input("\n\nThank you for counting. Press the enter key to exit.")
