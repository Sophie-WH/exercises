from Table import print_two_header
# Programming Exercise 5-13
#
# Program to display a table of times and falling distances for a specific range in seconds.
# This program accepts no input,
# but uses a loop to pass a range of times in seconds to a function
# 	that returns the falling distance for that amount of time,
# and displays the results as a table.



# define the main function

def main():
    # define a local float variable to hold distance
    distance = 0.0
    time = 0
    # Set up results chart, printing time and falling distance separated by a tab
    # include a separator line made with a row of underscores
    # loop through a range of time values (in seconds)
    print_two_header("Time", "Distance")
    while time <= 5:
    # pass the time to a falling distance function and assign result to distance
        print(format(str(time), "4") + "\t\t" + str(falling_distance(time)))
	# print the time and distance formatted to two places, separated by a tab
        time += 1

# Define a function to calculate the falling distance for a time in seconds
# The function accepts a time in seconds as a parameter,
# computes the distance,
# and returns the distance it has fallen in that time
def falling_distance(time):
    return(time * 5.7)
	# compute the falling distance using a formula and the time
	
	# return the falling distance



# Call the main function to start the program

main()



