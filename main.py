print("Let's calculate the cost of your pizza")
LABOUR = 0.75
RENT = 1
MATERIALS = 0.5
Diameter = int(input("How big do you want the diameter to be in inches? "))
Subtotal = LABOUR + RENT + MATERIALS * Diameter
print("The cost of the pizza with the diamater of " + str(Diameter ) + "is " + str(Subtotal))