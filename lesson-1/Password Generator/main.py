import random
# import string

# def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
#     characters = ""
#     if use_upper:
#         characters += string.ascii_uppercase
#     if use_lower:
#         characters += string.ascii_lowercase
#     if use_digits:
#         characters += string.digits
#     if use_symbols:
#         characters += string.punctuation
    
#     # Generate password by choosing random characters
#     password = "".join(random.choice(characters) for _ in range(length))
#     return password

# # User preferences
# length = int(input("Enter password length: "))
# use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
# use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
# use_digits = input("Include numbers? (y/n): ").lower() == 'y'
# use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

# # Generate and display the password
# password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
# print("Generated password:", password)



numbers = [1,2,3]
x = random.choices(numbers, k=2)
print(x)
import string
string.punctuation
print(random.choice(string.ascii_lowercase))




