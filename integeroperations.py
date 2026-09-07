# integer operations
while True:
    num1 = input("Please enter the first two-digit integer, or Q/q to quit: ")

    if num1 == "Q" or num1 == "q":
        break

    num1 = int(num1)
    num2 = int(input("Then enter the second two-digit integer: "))

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = int(input("Please enter your choice (1-4): "))

    if choice == 1:
        answer = num1 + num2
        print("The sum of", num1, "and", num2, "is", answer,"!")
    elif choice == 2:
        answer = num1 - num2
        print("The difference of", num1, "and", num2, "is", answer,"!")
    elif choice == 3:
        answer = num1 * num2
        print("The product of", num1, "and", num2, "is", answer,"!")
    elif choice == 4:
        answer = num1 / num2
        print("The quotient of", num1, "and", num2, "is", answer,"!")
    else:
        print("Invalid operation.")