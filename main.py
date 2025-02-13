# Lesson 2 (Typecasting)

# typecasting = the process of converting a value of one data type to another data type (string to integer, integer to float, float to boolean, etc)
# Explicit vs Implicit

# name = "Akmal Rizky Fauzan"
# age = 25
# gpa = 3.02
# student = False

# print(type(name)) --> to know the data type of the variable
# print(type(age))
# print(type(gpa))
# print(type(student))

# Explicit
# Integer to Float
# age = float(age)
# print(type(age))

# Float to Integer
# gpa = int(gpa)
# print(type(gpa))

# Boolean to String
# student = str(student)
# print(type(student))

# Integer to Boolean
# age = bool(age)
# print(age) 
# When print the age, it will be True because there are numbers but not ZERO
# If the number is ZERO, it will be False
# print(type(age))

# String to Boolean
# name = bool(name)
# print(name) 
# When print the name, it will be True because there are characters but not EMPTY
# If there an EMPTY string, it will be False
# print(type(name))

# Implicit
x = 2
y = 2.0

x = x/y

print(x)
# X will become a float because the math operation makes X (integer) turns to like Y (float) data type.