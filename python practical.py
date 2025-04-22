Program 1: Calculate Areas of Geometric Figures
import math

def calculate_area():
    print("Choose shape: circle, rectangle, triangle")
    shape = input("Enter shape: ").lower()

    if shape == "circle":
        r = float(input("Enter radius: "))
        area = math.pi * r * r
    elif shape == "rectangle":
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        area = l * b
    elif shape == "triangle":
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        area = 0.5 * b * h
    else:
        return "Invalid shape"
    print(f"Area of {shape}: {area}")

calculate_area()
 
 Program 2: Gross Salary Calculation
 def gross_salary():
    bs = float(input("Enter Basic Salary: "))
    da = 0.7 * bs
    ta = 0.3 * bs
    hra = 0.1 * bs
    gross = bs + da + ta + hra
    print(f"Gross Salary: {gross}")

gross_salary()

Program 3: Arithmetic Operations
def arithmetic_ops():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Addition: {a + b}")
    print(f"Subtraction: {a - b}")
    print(f"Multiplication: {a * b}")
    print(f"Division: {a / b}")
    print(f"Modulus: {a % b}")

arithmetic_ops()

Program 4: Task List Manager
task_list=[
    ("task1","2025-02-06","high"),
    ("task2","2025-02-07","medium"),
    ("task3","2025-06-8","low"),
    
    ]
#displaying task
print("initail task list")
print(task_list)

#adding new task
new_task=("task 4","2025 -06-09","high")
task_list.append(new_task)

#displaying task
print(new_task)
print(task_list)

#removing task
task_list.remove(task_list[1])
#displaying task
print(task_list)
#updating task
task_list[1]=("task3","2025-06-08","high")
#displaying task
print(task_list)


#sorting task
task_list.sort()
#displaying task
print(task_list)

##displaying updated task
print("\nUpdated task list:")

#reversing list
task_list.reverse()
print("\nreversed list",task_list)

Program 5: Set Operations for Enrollments
CET = {"Alice", "Bob"}
JEE = {"Bob", "Charlie"}
NEET = {"Alice", "David"}

all_students = CET | JEE | NEET
common = CET & JEE & NEET
unique_CET = CET - JEE

print("All Students:", all_students)
print("Common in all:", common)
print("Unique to CET:", unique_CET)

Program 6: Dictionary of Student Records
def student_records():
    records = {}
    while True:
        print("\n1. Add/Update Record\n2. Display Records\n3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter student name: ")
            grade = input("Enter grade: ")
            attendance = input("Enter attendance: ")
            records[name] = {"Grade": grade, "Attendance": attendance}
        elif choice == 2:
            for name, info in records.items():
                print(f"{name}: Grade={info['Grade']}, Attendance={info['Attendance']}")
        elif choice == 3:
            break

student_records()

Program 7: Even or Odd Number Check
def check_even_odd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is Even.")
    else:
        print(f"{num} is Odd.")

check_even_odd()

Program 8: Factorial of a Number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")

Program 9: Prime Number Check Using Function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a Prime Number.")
else:
    print(f"{num} is Not a Prime Number.")
    
  Program 10: Simple Calculator Using Functions
    def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return x / y if y != 0 else "Cannot divide by zero"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Addition:", add(a, b))
print("Subtraction:", sub(a, b))
print("Multiplication:", mul(a, b))
print("Division:", div(a, b))

Program 11: Division with Exception Handling
def safe_division():
    try:
        a = float(input("Enter numerator: "))
        b = float(input("Enter denominator: "))
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except ValueError:
        print("Error: Invalid input!")

safe_division()

Program 12: Debugging with pdb
import pdb

def buggy_sum():
    pdb.set_trace()
    a = 5
    b = "10"  # This will cause error
    print(a + int(b))

buggy_sum()

Program 13: NumPy Arrays Creation and Manipulation
import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4]])
c = np.array([[[1], [2]], [[3], [4]]])

print("1D Array:", a)
print("2D Array:", b)
print("3D Array:", c)
print("Reshaped:", b.reshape(4, 1))
print("Slice:", a[1:])
print("Index:", b[1][0])

Program 14: Element-wise Array Operation
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Dot Product:", np.dot(a, b))
print("Cross Product:", np.cross(a, b))

Program 15: Array Statistics with NumPy
import numpy as np

data = np.array([1, 2, 3, 4, 5])
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Std Dev:", np.std(data))
print("Variance:", np.var(data))
print("Correlation Coefficients:\n", np.corrcoef(data, data))

Program 16: Validate Phone and Email Using Regex
import re

phone = input("Enter phone number: ")
email = input("Enter email: ")

phone_pattern = re.fullmatch(r"\d{10}", phone)
email_pattern = re.fullmatch(r"[\w.-]+@[\w.-]+\.\w+", email)

if phone_pattern:
    print("Valid phone number.")
else:
    print("Invalid phone number.")

if email_pattern:
    print("Valid email.")
else:
    print("Invalid email.")
    