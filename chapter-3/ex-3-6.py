month = 0
day = 0
year = 0

message = ""

month = (int)(input("Please enter the month: "))
day = (int)(input("Please enter the day: "))
year = (int)(input("Please enter the year: "))

if month > 12:
    message = "Invalid month."
elif day > 31:
    message = "Invalid day."
elif year < 0 or year > 99:
    message = "Invalid year."
else:
    message = str(month) + "/" + str(day) + "/" + str(year)
    if day * month == year:
        message += " is a magical date."
    else:
        message += " is not a magical date."

print (message)
    
