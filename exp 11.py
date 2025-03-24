def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b
    
# Display menu
print("Select Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# User input
choice = input("Enter choice (1/2/3/4): ")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the operation
    if choice == '1':
        print(f"Result: {num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {num1} × {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {num1} ÷ {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input! Please select a valid option.")
except ValueError:
    print("Invalid input! Please enter numeric values.")