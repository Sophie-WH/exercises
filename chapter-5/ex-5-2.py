# Programming Exercise 5-2
#
# Program to calculate final purchase details.
# This program takes a purchase amount from a user,
# then calculates state tax, county tax and total tax,
# 	and passes them to a function to be totaled
# and displayed



# Global constants for the state and county tax rates

state_tax = 0.06
county_tax = 0.02

# define the main function

def main():
    
    # Define local float variables for purchase, state tax and county tax
    tax_state_calc = 0.0
    tax_county_calc = 0.0
    purchase = 0.0
    # Get the purchase amount from the user
    purchase = float(input("Please enter your total purchase: "))
    # Calculate the state tax using the global constant for state tax rate
    tax_state_calc = purchase * state_tax
    # Calculate the county tax using the global constant for county tax rate
    tax_county_calc = purchase * county_tax
    # Call the sale details function, passing the purchase, state tax and county tax
    sales_details(purchase, tax_state_calc, tax_county_calc)


# define a function to display purchase details
# this function accepts purchase, stateTax, and countyTax as arguments,
# calculates the total tax and sale total,
# then displays the purchase details

def sales_details(purchase, tax_state_calc, tax_county_calc):
    # Define local float variables for total tax and sale total
    total_tax = 0.0
    sale_total = 0.0
	# Calculate the total tax
    total_tax = tax_state_calc + tax_county_calc
	# Calculate the total sale
    sale_total = total_tax + purchase
    # Display the purchase details, including purchase, state tax, county tax,
    #	total tax, and sale total, each on a line.  Format floats to 2 decimal places.
    print(str.format("\nPurchase = {:.2f}", purchase))
    print(str.format("State Tax = {:.2f}", tax_state_calc))
    print(str.format("County Tax = {:.2f}", tax_county_calc))
    print(str.format("Total Tax = {:.2f}", total_tax))
    print(str.format("Sales Total = {:.2f}", sale_total))


# Call the main function to start the program.
main()