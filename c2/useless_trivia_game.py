# Useless trivia
#
# Gets personal information from the user and then
# prints true but useless information about him or her

name = input ("Hi, what is your name? ")

age = int(input("How old are you? "))

weight = int(input("Okay, just one last question. How many kg do you weigh? "))

# Printing lower case and upper case
print("\nIf poet ee cumings were to email you, he'd address you as", name.lower())
print("But if ee were mad, he'd call you", name.upper())

# Printing name 5 times
called = name * 5
print("\nIf a small child were trying to get your attention",)
print("your name would become:")
print(called)

# Calculating seconds
seconds = age * 365 * 24 * 60 * 60
print ("\nYou're over", seconds, "seconds old.")

# Calculating moon_weight and sun_weight

moon_weight = weight / 6
print ("\nDid you know that on the moon you would weigh only", moon_weight, "kg")

sun_weight = weight * 27.1
print("\nOn the sun, you'd weigh", sun_weight," kg (but, ah.... not for long!).")

input("\n\nPress enter to exit.")