# Author: Enrique Vigil
# Date: 10.31.26
# Assignment: Prog Assign_8 - Lists

def main():
    # creates an empty list to store the numbers
    numbers = []

    # asks the user to enter 20 numbers
    for count in range(20):
        number = float(input(f"Enter number {count + 1}: "))
        numbers.append(number)

    # calculates the lowest, highest, total, and average of the list
    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    # displays the results
    print("Lowest number:", lowest)
    print("Highest number:", highest)
    print("Total:", total)
    print("Average:", average)


# runs the program
main()
