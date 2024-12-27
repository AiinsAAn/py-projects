# Unit Converter: Length Conversion
print("Welcome to the Length Unit Converter!")

# Display conversion options
print("\nChoose the units to convert:")
print("1. Kilometers to Meters")
print("2. Kilometers to Centimeters")
print("3. Meters to Kilometers")
print("4. Meters to Centimeters")
print("5. Centimeters to Kilometers")
print("6. Centimeters to Meters")

# Get the user's choice
choice = input("\nEnter your choice (1-6): ")

# Get the length to convert
quantity = float(input("\nEnter the quantity to convert: "))

# Perform the selected conversion
if choice == '1':
    meters = quantity * 1000
    print(f"{quantity} kilometers is equal to {meters} meters.")
elif choice == '2':
    cm = quantity * 100000
    print(f"{quantity} kilometers is equal to {cm} centimeters.")
elif choice == '3':
    km = quantity / 1000
    print(f"{quantity} meters is equal to {km} kilometers.")
elif choice == '4':
    cm = quantity * 100
    print(f"{quantity} meters is equal to {cm} centimeters.")
elif choice == '5':
    km = quantity / 100000
    print(f"{quantity} centimeters is equal to {km} kilometers.")
elif choice == '6':
    meters = quantity / 100
    print(f"{quantity} centimeters is equal to {meters} meters.")
else:
    print("Invalid choice. Please select a number between 1 and 6.")
