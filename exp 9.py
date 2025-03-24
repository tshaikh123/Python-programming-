import math

def factorial(n):
    return math.factorial(n)
    
num = 5
print("Factorial of", num, "is", factorial(num))
# Input: An integer number
num = 6
# Initialize the factorial variable to 1
factorial_result = 1 
# Calculate the factorial using a for loop
for i in range(1, num + 1):
    factorial_result *= i
# Output: The factorial of the number
print(f"The factorial of {num} is {factorial_result}")