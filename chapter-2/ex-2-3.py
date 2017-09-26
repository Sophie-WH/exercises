# Programming Exercise 2-3
#
# Program to convert area in square feet to acres.
# This program will prompt a user for the size of a tract in square feet,
# then use a constant ratio value to calculate it value in acres
# and display the result to the user.

# Variables to hold the size of the tract and number of acres.
# be sure to initialize these as floats

tract = 0
acres = 0

# Constant for the number of square feet in an acre.

sFeetInAcres = 43560

# Get the square feet in the tract from the user.
# you will need to convert this input to a float

tract = float(input("How many square feet? "))

# Calculate the number of acres.

acres = tract / sFeetInAcres

# Print the number of acres.
# remember to format the acres to two decimal places

printer = str.format("{:.2f} Acres", acres)
print (printer)