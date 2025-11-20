import math

# Ask the user for a number
num = float(input("Enter a number: "))

# Using math module functions
square_root = math.sqrt(num)
power = math.pow(num, 2)         # num raised to the power 2
sine_value = math.sin(num)       # sine of the number
cosine_value = math.cos(num)     # cosine of the number

# Printing results
print("Square root of", num, "is:", square_root)
print(num, "raised to power 2 is:", power)
print("Sine of", num, "is:", sine_value)
print("Cosine of", num, "is:", cosine_value)
