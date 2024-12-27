# Simple Calculator for Beginners
print("Welcome to the Simple Calculator!")

# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Check for division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "undefined (cannot divide by zero)"

# Display the results
print("\nResults:")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
