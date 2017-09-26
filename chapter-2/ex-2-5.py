# Programming Exercise 2-5
#
# Program to calculate distances traveled over time at a speed.
# This program uses no input.
# It will calculate the distance traveled for 6, 10 and 15 hours at a constant speed,
# then display all the results on the screen.

# Variables to hold the three distances.
# be sure to initialize these as floats.

slowest = float(6)
medium = float(10)
fast = float(15)

# Constant for the speed.

speed = 65


# Calculate the distance the car will travel in
# 6, 10, and 15 hours.

slowest *= speed
medium *= speed
fast *= speed

# Print the results for all calculations.

printer = str.format("{:.2f} miles in 6 hours at 65 mph.\n", slowest)
printer += str.format("{:.2f} miles in 10 hours at 65 mph.\n", medium)
printer += str.format("{:.2f} miles in 15 hours at 65 mph.\n", fast)

print (printer)




