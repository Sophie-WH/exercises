# Programming Exercise 4-5
#
# Program to compute total and average monthly rainfall over a span of years.
# This program gets a number of years from a user,
# then uses nested loops to prompt for rainfall for each month in each year
#	and calculate the total and the average monthly rainfall,
# then displays the number of months, total rainfall and average monthly rainfall

# Create float variables for total rainfall, monthly rainfall, average monthly rainfall

total_rainfall = 0.0
monthly_rainfall = 0.0
ave_rainfall = 0.0

# Create int variables for number of years and number of months.

years = 0
months = 0

# Get number of years from the user

years = int(input("Please give the amount of years: "))

# Nested loop logic to loop through the years and their months
#
# Outer for loop for the number of years

for x in range(1, years + 1):
	print("Year " + str(x) + ".")
	for y in range(1, 13):
		monthly_rainfall = input("Please give the amount of rainfall for month " + str(y) + ": ")
		total_rainfall += float(monthly_rainfall)
		y += 1
	ave_rainfall = total_rainfall / 12
	print("For year " + str(x) + " total amount of rainfall was " + str.format("{:.2f}", total_rainfall) + " and the average amount was " + str.format("{:.2f}", ave_rainfall) + ".")
	x += 1
	# Print the current year message

	# Inner loop for 12 months 

		# Get monthly rainfall for current month from the user
		
		# add monthly rainfall to total rainfall
		
		# increment number of months
		
			
# Calculate the average rainfall using total rainfall and number of months

# print the results on the screen, including details for total months, total rainfall,
#	and average monthly rainfall, formatting any floats to 2 decimal places.

