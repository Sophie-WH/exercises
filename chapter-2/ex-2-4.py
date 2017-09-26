# Programming Exercise 2-4
#
# Program to compute a final price for five items with tax.
# This program will prompt a user for a set of five prices,
# sum them to a subtotal and calculate sales tax with tax rate stored in a constant,
# then display the results on the screen.

# Variables to hold the prices of five items, the subtotal, and the total.
# All should be initialized as floats.

Item1 = 0.0
Item2 = 0.0
Item3 = 0.0
Item4 = 0.0
Item5 = 0.0
subtotal = 0.0
total = 0.0
sales_tax = 0.0
printer = ""

# Constant for the sales tax rate.

tax_rate = 0.06

# Get the price of each item by prompting the user.
# You will need to convert each input to a float.

Item1 = float(input("Please give the price for item 1: "))
Item2 = float(input("Please give the price for item 2: "))
Item3 = float(input("Please give the price for item 3: "))
Item4 = float(input("Please give the price for item 4: "))
Item5 = float(input("Please give the price for item 5: "))

# Calculate the subtotal by adding up the item prices.

subtotal = Item1 + Item2 + Item3 + Item4 + Item5

# Calculate the sales tax by multiplying the subtotal by the tax rate.

sales_tax = subtotal * tax_rate

# Calculate the total by adding the subtotal and tax.

total = sales_tax + subtotal

# Print the values for the subtotal, tax and total.
# Label each value, and format them to display with two decimal places. 

printer = str.format("Subtotal = {:.2f}\n", subtotal)
printer += str.format("Sales Tax = {:.2f}\n", sales_tax)
printer += str.format("Total = {:.2f}\n", total)

print (printer)