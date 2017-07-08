# Print a message from the user backwards
# The user provides the computer with a message, and it prints it backwards to the user

message = str(input("Enter your message here: "))

print("\nThe message is backwards: ")

for letter_nr in range(len(message), 0, -1):
    print(message[letter_nr-1])

input("\nPress enter to exit")
