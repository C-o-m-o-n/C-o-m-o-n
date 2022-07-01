import math
import random
import time

#shapes
#print("choose a shape: ")
#tri = print("triangle")
#rec = print("rectangle")
#crc = print("circle")
#squ = print("square")

print(
"""Welcome to area calculater.
	 I can calculate the areas 
	 of the following shapes"""
)
print("triangle")
print("rectangle")
print("circle")
print("square")
print(" ")
chosen = input("choose a shape: " )

#formulas
#rectangle = l*w
#square = l*w or l*l
#triangle = ((1/2)*(b*h))
#circle = int((3.14*(r**2))

#calculations
def calc():
    if chosen == "triangle":
        print("you chose a triangle")
        print(" ")
        h = float(input("Enter the height: "))
        b = float(input("enter the base: "))
        triangle = ((1/2)*(b*h))
        print(" ")
        print("calculating.........")
        print(" ")
        time.sleep(2)
        print(f"the area of your shape is: {triangle}cm²")
        
    elif chosen == "rectangle":
        print("you chose a rectangle")
        print(" ")
        l = float(input("Enter the length: "))
        w = float(input("Enter a width: "))
        rectangle = l*w
        print(" ")
        print("calculating.........")
        print(" ")
        time.sleep(2)
        print(f"the area of your shape is: {rectangle}cm²")
        
    elif chosen == "circle":
        print("you choce a circle")
        print(" ")
        r = float(input("Enter the radius: "))
        circle = float((3.14*(r**2)))
        print(" ")
        print("calculating.........")
        print(" ")
        time.sleep(2)
        print(f"the area of your shape is: {circle}cm²")
        
    elif chosen == "square":
        print("you choce a square")
        print(" ")
        l = float(input("Enter the length: "))
        w = float(input("Enter a width: "))
        square = l*w
        print(" ")
        print("calculating.........")
        print(" ")
        time.sleep(2)
        print(f"the area of your shape is: {square}cm²")
        
    else:
        print(
        	"""You did not enter a shape 
        	from the list or maybe it is 
        	a typo. Please try again"""
        	)
calc()