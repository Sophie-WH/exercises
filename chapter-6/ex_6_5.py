# Programming Exercise 6-5
#
# Program to total the value of numbers in a text file.
# The program takes no user input, but requires a text file with numbers, one per line,
# which it opens, reads line by line, and totals the numbers in a variable,
# then displays the total on the screen.

# Define the main function.
def main():
    # Declare a local string variable for line and two floats for total and current number
    line = " "
    total = 0.0
    current_num = 0.0
    
    # Open numbers.txt file for reading
    filename = open("numbers.txt", "r")
    line = filename.readline()
    # iterate over the lines in the file
    while line != "":
        # get a number from the current line
        current_num = float(line)
        # add it to total
        total += current_num
        line = filename.readline()

    # Close file
    filename.close()
    # Display the total of the numbers in the file
    print("Total = ", total)


# Call the main function to start the program.
main()

