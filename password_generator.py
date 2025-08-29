import random
import string

def generate_password(length=12):
    # Characters to use: letters, digits, and special symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
# Ask user for desired password length
try:
    length = int(input("Enter the desired password length (default 12): ") or 12)
    print("Your secure password is:", generate_password(length))
except ValueError:
    print("Please enter a valid number.")
