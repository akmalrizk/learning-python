# Lesson 9 (String Indexing)

# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"

# print(credit_number[0]) --> the first digit (0)
# print(credit_number[:4]) --> the first 4 digits
# print(credit_number[5:9]) --> the second 4 digits
# print(credit_number[5:]) --> print everything except the first 4 digits
# print(credit_number[-1]) --> the last digits (-1)
# print(credit_number[::2]) --> print every 2 characters

# Exercise 1 (get the last 4 digits)

# last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")

# Exercise 2 (credit number backwards)

credit_number = credit_number[::-1]
print(credit_number)