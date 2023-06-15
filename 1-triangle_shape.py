num_asterisks = int(input("Enter a number: "))

for i in range(num_asterisks, 0, -2):

    for j in range(i):

        print("*", end=" ")

    print()

