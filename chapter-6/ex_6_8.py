def main():
    
    min = 1
    max = 18
    num = 0
    
    is_in_range = False
    
    while is_in_range == False:
        try:
            num = input("Please enter a file between " + str(min) + " and " + str(max) + ": ")
            realnum = int(num)
            if realnum > min and realnum < max:
                print("Thank you, your number is", num + ", and is in the correct range.")
                is_in_range = True
            else:
                print("This number is not in the correct range.")
        except ValueError:
            print(num, "is not a number.")
            
main()