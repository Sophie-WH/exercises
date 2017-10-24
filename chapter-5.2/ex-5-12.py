# Programming Exercise 5-12
#
# Program to find the greater of two integers.
# This program accepts two integers,
# passes them to a function that compares them,
# and displays which one is greater.

# define the main function
def main():

    # Define local variables to hold two integers
    int1 = 0
    int2 = 0

    # prompt the user for the first integer
    
    int1 = int(input("Please enter the first number: "))
    
    # prompt the user for the second integer
    
    int2 = int(input("Please enter the second number: "))

    # print the return value from calling a function to find the greater of two integers
    # the two integers are passed as arguments
    print(compare_numbers(int1, int2))
    
 
# Define a function to compare integer values.
# This function accepts two integer parameters,
# compares them,
# and returns the value of the greater.
def compare_numbers(int1, int2):
    
    if (int1 > int2):
        return (str(int1) + " is greater than " + str(int2))
    else:
        return (str(int2) + " is greater than " + str(int1))

	# if the first integer is greater, return the first integer

	# else, return the second integer



# Call the main function to start the program
main()



