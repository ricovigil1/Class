# author: enrique vigil

# user input
number = int(input("Enter a number from the range 1 through 7 corresponding to the day of the week: "))

# conditional statements
if number == 1:
    print("Monday")
elif number == 2:
    print("Tuesday")
elif number == 3:
    print("Wednesday")
elif number == 4:
    print("Thursday")
elif number == 5:
    print("Friday")
elif number == 6:
    print("Saturday")
elif number == 7:
    print("Sunday")
else:
    print("Error - Incorrect input: please enter a number from 1 through 7.")
