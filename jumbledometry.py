import math
import circle
import rectangle


AREA_OF_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

def main():

    choice = 0
    while choice != QUIT_CHOICE:
        display_menu()
        choice = int(input("Enter your choice: "))
        handle_choice(choice)
        
def handle_area_of_circle():
    radius = float(input("Enter the circle's radius: "))
    print(str.format("The area is {:.2f}", circle.area(radius)))
    
def handle_circumference():
    radius = float(input("Enter the circle's radius: "))
    print(str.format("The area is {:.2f}", circle.circumference(radius)))

def area_of_rect():
    width = float(input("Enter the rectangle's width: "))
    length = input("Enter the rectangle's length: ")
    print(str.format("The area is {:.2f}", rectangle.area(width,length)))
    
def perimeter_of_rect():
    width = float(input("Enter the rectangle's width: "))
    length = float(input("Enter the rectangle's length: "))
    print(str.format("The perimeter is {:.2f}", rectangle.perimeter(width,length)))

def handle_choice(choice):
    choice = int(input("Enter your choice: "))
    if choice == AREA_OF_CIRCLE_CHOICE:
        handle_area_of_circle()
    elif choice == CIRCUMFERENCE_CHOICE:
        handle_circumference()
    elif choice == AREA_RECTANGLE_CHOICE:
        area_of_rect()
    elif choice == PERIMETER_RECTANGLE_CHOICE:
        perimeter_of_rect()
    elif choice == QUIT_CHOICE:
        print("Exiting the program...")
    else:
        print("Error: Invalid selection.")

def display_menu():
    print("\n MENU")
    print("1) Area of a circle")
    print("2) Circumference of a circle")
    print("3) Area of a rectangle")
    print("4) Perimeter of a rectangle")
    print("5) Quit")

main()