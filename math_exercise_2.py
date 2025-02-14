# Exercise 2 (Find C on a right triangle)

import math

a = float(input("Enter side A in cm: "))
b = float(input("Enter side B in cm: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C is {c}cm")