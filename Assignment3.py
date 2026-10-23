# Smart Temperature Converter & Take input from the user in celsius and Print it's equivalent in Fahrenheit and Kelvin 
# Use Explicit Type Conversion and Arithmetic Operators
# formula for conversion:
# Fahrenheit = (Celsius * 9/5) + 32
# Kelvin = Celsius + 273.15

Celsius = float(input("Enter Your Temperature in Celsius: "))

Fahrenheit = (Celsius * 9/5) + 32
print("Temperature in Fahrenheit: ", Fahrenheit)
print("Temperature in Celsius data type is:", type(Celsius))


Kelvin = Celsius + 273.15
print("Temperature in Kelvin: ", Kelvin)
print("Temperature in Kelvin data type is:", type(Kelvin))


# Converted Values in string format
Fahrenheit_str = str(Fahrenheit)
print("Temperature in Fahrenheit (String Format): ", Fahrenheit_str)

Kelvin_str = str(Kelvin)
print("Temperature in Kelvin (String Format): ", Kelvin_str)