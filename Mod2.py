import math

# take user input
sideA = float(input("Enter the triangles first side: "))
sideB = float(input("Enter the triangles second side: "))
sideC = float(input("Enter the triangles third side: "))

#  calculate perimeter
i = (sideA + sideB + sideC) / 2

# calculate area
area = (i*(i-sideA)*(i-sideB)*(i-sideC)) ** 0.5

# print answer
print("The area of the triangle is: %0.2f" %area)