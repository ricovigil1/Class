# Author: Enrique Vigil
# Date: 09/26/26
# Assignment: Prog Assign_4 - Loops and Iteration program 2

# user inpit how many years of rainfall data will be entered
years = int(input("How many years of rainfall data? "))

# at least one year is needed to calculate an average
while years < 1:
    years = int(input("Please enter at least 1 year: "))

total_rainfall = 0.0
total_months = 0

# nested loops - the outer loop runs once for each year
for year in range(1, years + 1):
    # the inner loop runs once for each of the 12 months
    for month in range(1, 13):
        rainfall = float(input(
            f"Rainfall in inches for year {year}, month {month}: "
        ))
        total_rainfall += rainfall
        total_months += 1

# average rainfall per month calculation
average_rainfall = total_rainfall / total_months

# display the data results fr the rainfall period
print(f"Number of months: {total_months}")
print(f"Total rainfall: {total_rainfall:.2f} inches")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")
