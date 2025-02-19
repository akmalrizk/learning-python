# Lesson 8 (Useful String Method)

# name = input("Enter your full name: ")
# phone_number = input("Enter your phone number: ")

# result = len(name) 
# len() --> to count the characters
# result = name.find("o")
# find() --> to find a character (first) within a string (name)
# result = name.rfind("o")
# rfind() --> to find a character (last) within a string (name)
# name = name.capitalize()
# capitalize() --> to capitalize the first letter of the string
# name = name.upper()
# upper() --> to upper case the string
# name = name.lower()
# lower() --> to lower case the string
# result = name.isdigit()
# isdigit() --> to see if there are ONLY numbers (boolean)
# result = name.isalpha()
# isdigit() --> to see if there are ONLY alphabet (boolean)
# result = phone_number.count("-")
# count() --> to count how many a character in a string
# phone_number = phone_number.replace("-", "")
# replace() --> to replace a character with a character within a string

# print(help(str))
# print the guide of all string method

# print(phone_number)

# Example

# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter your username: ")

if len(username) > 12:
    print("Your username can not be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can not contain space(s)")
elif username.isalpha():
    print("Your username can not contain number(s)")
else:
    print(f"Welcome {username}!")