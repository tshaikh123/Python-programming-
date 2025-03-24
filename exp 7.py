student_records = {
    "Alice": {"grades": [85, 92, 78], "attendance": 95},
    "Bob": {"grades": [79, 83, 88], "attendance": 89},
    "Charlie": {"grades": [92, 88, 94], "attendance": 98}
}
# Adding a new student
student_records["David"] = {"grades": [90, 87, 93], "attendance": 96}
# Updating grades for Alice
if "Alice" in student_records:
   student_records["Alice"]["grades"] = [90, 85, 88]
else:
   print("Student Alice not found!")
# Updating attendance for Bob
if "Bob" in student_records:
    student_records["Bob"]["attendance"] = 91
else:
    print("Student Bob not found!")
# Display all student records
for name, details in student_records.items():
    print(f"Student: {name}")
    print(f"Grades: {details['grades']}")
    print(f"Attendance: {details['attendance']}")
    print("-" * 20)