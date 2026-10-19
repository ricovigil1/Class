# Author: Enrique Vigil
# Date: 10.18.26
# Assignment: Prog Assign_6 - Modules & Libraries

# Paint Job Estimator
# Every 112 square feet requires 1 gallon of paint and 8 hours of labor. Labor costs $35 per hour

SQUARE_FEET_PER_GALLON = 112
HOURS_PER_GALLON = 8
LABOR_RATE = 35.00


def main():
    # Get the wall area and paint price from the user
    square_feet = float(input("Please enter the square feet to be painted: "))
    price_per_gallon = float(input("Please enter the paint price per gallon: $"))

    # Calculates the paint and labor 
    gallons_required = square_feet / SQUARE_FEET_PER_GALLON
    labor_hours = gallons_required * HOURS_PER_GALLON

    # Calculates the costs
    paint_cost = gallons_required * price_per_gallon
    labor_charges = labor_hours * LABOR_RATE
    total_cost = paint_cost + labor_charges

    # Displays the results
    print("\nPaint Job Estimate")
    print("------------------------------")
    print(f"Gallons of paint required: {gallons_required:,.2f}")
    print(f"Hours of labor required:   {labor_hours:,.2f}")
    print(f"Cost of paint:             ${paint_cost:,.2f}")
    print(f"Labor charges:             ${labor_charges:,.2f}")
    print(f"Total cost:                ${total_cost:,.2f}")


# Run the program
if __name__ == "__main__":
    main()
