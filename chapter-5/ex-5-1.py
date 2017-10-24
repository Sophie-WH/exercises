# Programming Exercise 5-1
#
# Program to convert kilometers to miles.
# This program accepts a distance in kilometers from the user,
# passes it to a function, which calculates its value in miles
# and displays the result for the user.


# Global constant for the ratio of kilometers to miles

kil_to_miles = 0.621371

# define the main function

def get_kilometers():
    # Define a local float variable to hold the distance in kilometers
    kilometers = 0.0
    # Get distance in kilometers from the user
    kilometers = float(input("Please enter the number of kilometers: "))
    # pass the distance in kilometers to a function to convert to miles
    convert_kilometers(kilometers)


# define the function to convert to miles
# the function takes kilometers as an argument
# calculates the equivalent number of miles
# and prints the result
def convert_kilometers(kilos):
    # Define a local float variable for miles
    miles = 0.0
	# use the global conversion constant to compute miles    
    miles = kilos * kil_to_miles
    # print the results, formatting float values to 2 decimal places
    print(str.format("Total Miles = {:.2f}\n", miles))


# Call the main function to start the program
get_kilometers()
