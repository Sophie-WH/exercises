# Programming Exercise 5-3
#
# Program to compute recommended insurance to carry on an item.
# This program accepts a replacement cost from a user,
# calculates a minimum recommended insurance to carry from a global constant,
# then passes these values to a function to be displayed

# Global constant for the percent of replacement cost to insure

replacement_percent = 0.7

# Define the main function
def main():
    # Define local float variables for replacement cost and minimum insurance
    replacement_cost = 0.0
    minimum_insurance = 0.0
    # Get the replacement cost from the user
    replacement_cost = float(input("Please enter the replacement cost: "))
    # Calculate the minimum insurance amount using the global constant
    minimum_insurance = replacement_percent * replacement_cost
    # Call the function to display the insurance details, 
    # passing the replacement cost and minimum insurance to the function
    insurance_details(replacement_cost, minimum_insurance)


# Define a function to display the insurance details
# This function accepts the replacement cost and minimum insurance as parameters,
# uses the global constant to calculate percent insured,
# and displays the insurance details.
def insurance_details(replacement_cost, minimum_insurance):
	# display the replacement cost, formatting the value to 2 decimal places
    print(str.format("\nReplacement Cost = {:.2f}", replacement_cost))
    # display the percent insured, formatting the value to 2 decimal places
    print(str.format("Percent insured = {:.1f}" + "%", replacement_percent * 100))
	# display the minimum insurance, formatting the value to 2 decimal places
    print(str.format("Minimum insurance = {:.2f}", minimum_insurance))


# Call the main function to start the program
main()
