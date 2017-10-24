from Table import print_three_header
# Programming Exercise 5-15
#
# Program to find the average of five scores and output the scores and average with letter grade equivalents.
# This program prompts a user for five numerical scores,
# calculates their average, and assigns letter grades to each,
# and outputs the list and average as a table on the screen.

# define the main function
def main():
    # define local variables for average and five scores
    average = 0.0
    score_list = [0.0, 0.0, 0.0, 0.0, 0.0]
    # Get five scores from the user

    for x in range(0, 5):
        score_list[x] = float(input("Please enter score " + str(x + 1) + ": "))
    # find the average by passing the scores to a function that returns the average

    # display grade and average information in tabular form
    # as score, numeric grade, letter grade, separated by tabs
    print_three_header("Score", "Numeric Grade", "Letter Grade")
    # display a line of underscores under this header
    
    # print data for all five scores, using the score,
    # with the result of a function to determine letter grade
    for x in range(0, 5):
        print(str(x + 1) + "\t\t" + str(score_list[x]) + "\t\t\t" + letter_grade(score_list[x]))
    # display a line of underscores under this table of data

    # display the average and the letter grade for the average



# Define a function to return the average of 5 grades.
# This function accepts five values as parameters,
# computes the average,
# and returns the average.
def average(list_of_scores):
    # define a local float variable to hold the average
    ave = 0.0
    while x <= 4:
        ave += list_of_scores[x]
        x += 1
    ave /= (x + 1)
    # return the average
    return ave


# Define a function to return a numeric grade from a number.
# This function accepts a grade as a parameter,
# Uses logical tests to assign it a letter grade,
# and returns the letter grade.
def letter_grade(score):
    # if score is 90 or more, return A
    if score > 90:
        return "A"
    # 80 or more, return B
    elif score > 80:
        return "B"
    # 70 or more, return C
    elif score > 70:
        return "C"
    # 60 or more, return D
    elif score > 60:
        return "D"
    # anything else, return F
    else:
        return "F"

# Call the main function to start the program
main()

