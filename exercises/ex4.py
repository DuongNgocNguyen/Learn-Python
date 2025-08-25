"""
Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""
import math

r = float(input("Enter the radius of the circle: "))
# Cách 1:
area1 = math.pi * r * r
print("Area =", area1)

# Cách 2:
area2 = math.pi * r**2
print("Area =", area2)

# Cách 3:
area3 = math.pi * math.pow(r, 2)
print("Area =", area3)