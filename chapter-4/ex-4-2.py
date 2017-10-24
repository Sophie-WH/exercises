# Programming Exercise 4-2
#
# Program to output table of calories burned for different times.
# This program takes no input.
# It uses a constant for calories burned per minute to calculate the calories burned for a range of different times,
# then displays a table with the results for each time. 

# Declare a constant for the calories burned per minute.

cal_per_min = 0

# Declare variables for calories burned and number of minutes.
# initialize calories burned as a float and minutes as an integer

cals_burned = 500.0
minutes = 8
x = 0

# print the table header using two tabs between Minutes and Calories Burned
# print a line under the header using underscores

print("Minutes:      Calories Burned:")
print("______________________________")

# Use a for loop to calculate and display a display a line for each value of minutes
# set up the loop using a range of comma-separated minutes values 

while x <= minutes:
    cal_per_min = cals_burned / minutes
    print(str(x) + "            " + str(cal_per_min * x))
    x += 1

    # calculate calories burned using the constant for calories burned per minute

    # display the minutes and calories burned using two tabs between the values

