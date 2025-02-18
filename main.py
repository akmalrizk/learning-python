# Lesson 6 (Logical Operators)

# logical operators = used on conditional statements

# and = check two or more conditions if True
#  or = checks if at least one condition is True
# not = True if condition is False, and vice versa

# Example 1 (and)

temp = 40

# if temp > 0 and temp < 30:
#     print("The temperature is good")
# else:
#     print("The temperature is bad")

# Example 2 (or)

if temp <= 0 or temp >= 30:
    print("The temperature is bad")
else:
    print("The temperature is good")

# Example 3 (not)

sunny = True

if  not sunny:
    print("It is cloudy outside")
else:
    print("It is sunny outside")