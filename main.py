# Lesson 7 (Conditional Expression)

# conditional expression = A one-line shortcut for the if-else (ternary operators)
# Print or assign one of the values based on condition
# Formula = X if condition else Y

# Example

num1 = -5
num2 = 5
a = 6
b = 7
age = 13
temperature = 0
user_role = "guest"

# print("Positive" if num1 > 0 else "Negative")

# print("EVEN" if num2 % 2 == 0 else "ODD")

# max_num = a if a > b else b
# print(max_num)

# min_num = a if a < b else b
# print(min_num)

# status = "Adult" if age >= 18 else "Child"
# print(status)

# weather = "HOT" if temperature > 20 else "COLD"
# print(weather)

access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)