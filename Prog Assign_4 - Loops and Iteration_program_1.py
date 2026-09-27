# Author: Enrique Vigil
# Date: 09/26/26
# Assignment: Prog Assign_4 - Loops and Iteration program 1

# starting at zero point
total_bugs = 0

# number of bugs collected on each of the five days
for day in range(1, 6):
    bugs = int(input(f"How many bugs were collected on day {day}? "))
    total_bugs += bugs

# display the total after all five days
print(f"Total bugs collected over five days: {total_bugs}")
