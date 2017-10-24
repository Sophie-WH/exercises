# Programming Exercise 5-4
#
# Program to compute monthly and annual auto expenses.
# This program prompts a user for several auto monthly expense amounts,
# then passes them to a function to total the values, annualize them,
# and display the details and totals on the screen.



# define the main function
def main():
    loan = 0.0
    insurance = 0.0
    gas = 0.0
    oil = 0.0
    tires = 0.0
    maintenance = 0.0
    # Define local float variables for loan, insurance, gas, oil, tires and maintenance

    # Get the amount of the monthly loan payment from the user.
    loan = float(input("Please enter the monthly loan payment: "))

    # Get the amount of the monthly insurance from the user.
    insurance = float(input("Please enter the monthly insurance payment: "))

    # Get the amount of the monthly gas from the user.
    gas = float(input("Please enter the monthly gas payment: "))

    # Get the amount of the monthly oil from the user.
    oil = float(input("Please enter the monthly oil payment: "))

    # Get the amount for monthly tire wear from the users.
    tires = float(input("Please enter the monthly tire payment: "))

    # Get the amount for monthly maintenance from the user.
    maintenance = float(input("Please enter the monthly maintenance payment: "))
        
    # Call the function to summarize car expenses,
    # passing the loan, insurance, gas, oil, tires and maintenance as arguments.
    car_expenses(loan, insurance, gas, oil, tires, maintenance)


# Define a function to summarize car expenses,
# it accepts loan, insurance, gas, oil, tires, and maintenance as arguments,
# calculates a monthly total and an annual total,
# and displays these totals.
def car_expenses(loan, insurance, gas, oil, tires, maintenance):
    
    # Define local float variables for monthly total and annual total
    monthly_total = 0.0
    annual_total = 0.0
    # calculate the monthly total
    monthly_total = loan + insurance + gas + oil + tires + maintenance
    # calculate the annual total
    annual_total = monthly_total * 12

    # Print monthly and annual information, formatting float value to 2 decimal places.
    print(str.format("\nMonthly Total = {:.2f}", monthly_total))
    print(str.format("Annual Total = {:.2f}", annual_total))

# Call the main function to start the program

main()