age = input("Please enter your age in years: ")

if age <= 1:
    print("This age is classified as an infant.")
elif age > 1 and age < 13:
    print("This age is classified as a child.")
elif age >= 13 and age < 20:
    print("This age is classified as a teenager.")
else:
    print("This age is classified as an adult.")