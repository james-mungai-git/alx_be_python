# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Conversion functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User interaction
try:
    temp = float(input("Enter the temperature to convert: "))
    scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if scale == "C":
        print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
    elif scale == "F":
        print(f"{temp}°F is {convert_to_celsius(temp)}°C")
    else:
        raise ValueError("Invalid scale. Please enter 'C' or 'F'.")

except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")
