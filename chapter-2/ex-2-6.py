# Programming Exercise 2-6
#
# Program to calculate a total sale price using state and local sales tax.
# This program prompts a user for an amount of purchase,
# uses constants to calculate state, county and total sales tax, and a purchase total
# then displays the details of these calculations for the user.

# Variables for purchase amount, state tax, county tax, total tax and total sale
# all initialized as floats

amount = float(0.0)
state_tax = float(0.0)
county_tax = float(0.0)
total_tax = float(0.0)
total_sale = float(0.0)


# Constants for the state and county tax rates

state = float(input("\nWhat is the state tax of where you live?\n"))
county = float(input("\nWhat is the county tax of where you live?\n"))

# Get the amount of purchase from the user, casting it to a float.

amount = float(input("\nWhat is the subtotal of the purchase?\n"))

# Calculate the state sales tax.

state_tax = amount * state

# Calculate the county sales tax.

county_tax = amount * county

# Sum the total tax.

total_tax = state_tax + county_tax

# Calculate the total of the sale.

total_sale = amount + total_tax

# Print detailed information about the sale, formatting all values to two decimal places.

printer = ""

printer += str.format("\nState Tax = {:.2f}\n", state_tax)
printer += str.format("County Tax = {:.2f}\n", county_tax)
printer += str.format("Tax = {:.2f}\n", total_tax)
printer += str.format("Subtotal = {:.2f}\n", amount)
printer += str.format("Total = {:.2f}\n", total_sale)

print (printer)



