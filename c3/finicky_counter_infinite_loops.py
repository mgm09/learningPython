# Finicky counter
# Demonstrates the break and continue statements

counter = 0

while True:
    counter += 1
    # end loop if count greater than 10
    if counter > 10:
        break
    # skip 5
    if counter == 5:
        continue
    print(counter)

input("\n\nPress enter to exit.")