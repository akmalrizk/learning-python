# Email Slicer Program

email = input("Enter your email: ")

# index = email.index("@")

# username = email[:index]
# domain = email[index + 1:]

# Shorter Method

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print(f"Your username is {username} and your domain is {domain}")