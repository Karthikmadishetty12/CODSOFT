num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Get operation from the user
choice = input("Enter your choice (+, -, *, /): ")

# Perform the operation
if choice == "+":
    result = num1 + num2
    print("Result:", result)
elif choice == "-":
    result = num1 - num2
    print("Result:", result)
elif choice == "*":
    result = num1 * num2
    print("Result:", result)
elif choice == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid operation selected!")
