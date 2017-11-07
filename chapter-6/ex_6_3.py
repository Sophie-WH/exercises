# Programming Exercise 6-3
#
# Program to open a file and display its contents with line numbers.
# This program prompts the user for a file name,
# reads the file until it ends
# then displays each line with its line number before closing the file.

# define the main function
def main():
    # Define local variables for line and filename (strings) and counter (int)
    line = " "
    filename = input("Please enter filename: ")
    x = 0
    
    # Prompt the user for a file name
    # Open the specified file for reading
    filename = open(filename, "r")
    # use a for loop to loop through all the lines
    while line != "":
        # increment the counter
        x += 1
        # print the current line number without carriage return
        line = filename.readline()
        print (str(x) + ": "),
        # Strip the '\n' from the end of the line
        # display the line (should be on same line as line number)
        print (line)

    # Close file

    filename.close()

# Call the main function to start the program
main()
