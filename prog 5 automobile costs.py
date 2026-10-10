# Author: Enrique Vigil
# Date: 10.10.26
# Assignment: Prog Assign_5 - Functions

# calculation for total monthly vehicle cost
def calculate_monthly_cost(loan, insurance, gas, oil, tires, maintenance):
    return loan + insurance + gas + oil + tires + maintenance


# calculation for the annual cost 
def calculate_annual_cost(monthly_cost):
    return monthly_cost * 12


def main():
    # requests the user for each monthly expense
    loan = float(input("Please enter your monthly loan payment: $"))
    insurance = float(input("Please enter your monthly insurance cost: $"))
    gas = float(input("Please enter your monthly gas cost: $"))
    oil = float(input("Please enter your monthly oil cost: $"))
    tires = float(input("Please enter your monthly tire cost: $"))
    maintenance = float(input("Please enter your monthly maintenance cost: $"))

    # calls the functions to calculate the total costs
    monthly_total = calculate_monthly_cost(
        loan, insurance, gas, oil, tires, maintenance
    )
    annual_total = calculate_annual_cost(monthly_total)

    # displays the totals with two decimal places
    print(f"\nTotal monthly vehicle cost: ${monthly_total:,.2f}")
    print(f"Total annual vehicle cost: ${annual_total:,.2f}")


# starta the program
main()
