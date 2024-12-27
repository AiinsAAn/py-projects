# Temperature Converter
print("Welcome to the Temperature Converter!")

# Display conversion options
print("\nChoose the temperature scale you want to convert from:")
print("1. Celsius to Fahrenheit and Kelvin")
print("2. Fahrenheit to Celsius and Kelvin")
print("3. Kelvin to Celsius and Fahrenheit")

# Get the user's choice
choice = input("\nEnter your choice (1/2/3): ")

# Get the temperature to convert
temperature = float(input("\nEnter the temperature to convert: "))

# Perform the selected conversion
if choice == '1':
    # Celsius to Fahrenheit and Kelvin
    fahrenheit = (temperature * 9/5) + 32
    kelvin = temperature + 273.15
    print(f"{temperature} Celsius is equal to {fahrenheit} Fahrenheit and {kelvin} Kelvin.")
elif choice == '2':
    # Fahrenheit to Celsius and Kelvin
    celsius = (temperature - 32) * 5/9
    kelvin = celsius + 273.15
    print(f"{temperature} Fahrenheit is equal to {celsius} Celsius and {kelvin} Kelvin.")
elif choice == '3':
    # Kelvin to Celsius and Fahrenheit
    celsius = temperature - 273.15
    fahrenheit = (celsius * 9/5) + 32
    print(f"{temperature} Kelvin is equal to {celsius} Celsius and {fahrenheit} Fahrenheit.")
else:
    print("Invalid choice. Please select a number between 1 and 3.")
