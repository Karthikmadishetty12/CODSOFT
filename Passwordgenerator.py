import random
import string

print("Welcome to the Password Generator!")

# Ask user for the length of the password
length = int(input("Enter the desired length of your password: "))

# Define characters to use in the password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the password
password = ''.join(random.choice(characters) for _ in range(length))

# Display the password
print("Generated Password:", password)