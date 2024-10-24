# TASK 1
def convert_temperature(temp, original_unit):
    if original_unit == 'C':
        # Convert Celsius to Fahrenheit and Kelvin
        fahrenheit = (temp * 9/5) + 32
        kelvin = temp + 273.15
        return fahrenheit, kelvin
    elif original_unit == 'F':
        # Convert Fahrenheit to Celsius and Kelvin
        celsius = (temp - 32) * 5/9
        kelvin = celsius + 273.15
        return celsius, kelvin
    elif original_unit == 'K':
        # Convert Kelvin to Celsius and Fahrenheit
        celsius = temp - 273.15
        fahrenheit = (celsius * 9/5) + 32
        return celsius, fahrenheit
    else:
        return "Invalid original unit. Please enter C, F, or K."

# Get user input
temp = float(input("Enter temperature value: "))
original_unit = input("Enter original unit (C, F, or K): ")

# Convert temperature
if original_unit in ['C', 'F', 'K']:
    converted_units = convert_temperature(temp, original_unit)
    if original_unit == 'C':
        print(f"{temp}°C is equal to {converted_units[0]}°F and {converted_units[1]}K")
    elif original_unit == 'F':
        print(f"{temp}°F is equal to {converted_units[0]}°C and {converted_units[1]}K")
    elif original_unit == 'K':
        print(f"{temp}K is equal to {converted_units[0]}°C and {converted_units[1]}°F")
else:
    print(convert_temperature(temp, original_unit))