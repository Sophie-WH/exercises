l1 = input("Please give the length of the first rectangle: ")
w1 = input("Please give the width of the first rectangle: ")
l2 = input("Please give the length of the second rectangle: ")
w2 = input("Please give the width of the second rectangle: ")

if l1 * w1 > l2 * w2:
    print ("The area of rectangle one is greater.")
elif l1 * w1 == l2 * w2:
    print ("The areas are equal.")
else:
    print ("The area of rectangle of two is greater.")