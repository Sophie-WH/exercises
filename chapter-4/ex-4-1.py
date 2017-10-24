# Programming Exercise 4-1
#
# Program to total the values of five integers.
# This program the user for an integer five times,
# and totals them up,
# then displays the total entered on the screen.

# Initialize variables for bugs collected and total bugs.
# be sure to initialize them as integers

bugs_collected = 0
total_bugs = 0
x = 0;
# Get the number of bugs collected from the user
# use a for loop to get the number of bugs exactly five times, once for each day

while x <= 4:
    bugs_collected = (int)(input("Please enter the number of bugs found today: "))
    total_bugs += bugs_collected
    x += 1
    
print("You have collected " + str(total_bugs) + " bugs.")

	# input bugs collected on this day and convert it to an int

    
    # add bugs collected to total bugs


# Display the total number of bugs collected for all five days.
