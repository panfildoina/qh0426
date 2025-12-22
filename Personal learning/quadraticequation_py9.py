#Write a Python program to solve quadratic equation.
#a, b and c are real numbers and
#The solutions of this quadratic equation is given by:
#𝑎𝑥^2 + 𝑏𝑥 + 𝑐 = 0
#solution:(−𝑏 ± (𝑏 − 4𝑎𝑐 )^1/2)/(2𝑎)
import math
#Input coefficients
a = float(input("Enter coeffiecient a: "))
b = float(input("Enter coeffiecient b: "))
c = float(input("Enter coeffiecient c: "))

#calculate the discriminant
discriminant = b**2 -4*a*c

#check if discriminat is negative, positive or zero

if discriminant > 0:
    #Two real and distinct roots 
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Root 1: {root1}")
    print(f"Root 2 : {root2}")
elif discriminant == 0:
    #one real root (repeated)
    root = -b / (2*a)
    print(f"Root: {root}")
else:
    #complex roots
    real_part = -b /(2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} - {imaginary_part}i")