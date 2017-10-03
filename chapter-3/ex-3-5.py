min = 100
max = 12000
multiplier = 9.81

mass = 0.0
weight = 0.0

mass = input("Please give the mass of the object in kilograms: ")

weight = mass * multiplier

if weight < min:
   print(str.format("Weight = {:.2f}\n", weight))
   print("The weight is smaller than the minimum.")
elif weight < max:
   print(str.format("Weight = {:.2f}\n", weight))
   print("The weight is bigger than the maximum.")