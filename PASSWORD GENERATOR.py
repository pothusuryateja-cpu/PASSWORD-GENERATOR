import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

try:
    length = int(input("Enter password length: "))
    if length <= 0:
        print("Please enter a positive number.")
    else:
        print("Generated Password:", generate_password(length))

except ValueError:
    print("Please enter a valid number.")
