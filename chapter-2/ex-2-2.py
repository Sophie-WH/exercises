# Programming Exercise 2-2
#
# Program to compute expected profit from sales.
# This program will prompt a user for a sales projection
# and use it to calculate expected profit from a predefined profit margin
# then display the result.

# Variables to hold the sales total and the profit
# initialize them as float values
sales_total = 0.0
profit = 0.0

# Get the amount of projected sales.
# be sure to convert the input to a float

sales_total = float(input("Please input the predicted sales amount: "))

# Calculate the projected profit using a 23% profit margin.

profit = sales_total + (sales_total * (23/100))

# Print the projected profit.
# be sure to format the output to two decimal places

print(profit, "%.2f")