# Function to calculate factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Calling the function with a sample number
number = 5
result = factorial(number)

# Printing the result
print("Factorial of", number, "is:", result)
