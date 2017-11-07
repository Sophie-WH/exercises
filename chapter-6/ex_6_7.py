def main():
    
    num = 0
    is_a_number = False
    while is_a_number == False:
        try:
            num = int(input("Please enter a valid number: "))
            is_a_number = True
        except ValueError as e:
            print(e, "is not a number.")
            
    
main()