# task3_student_marks.py

# Step 1: Create a dictionary of student marks
student_marks = {
    "Anil": 85,
    "Riya": 92,
    "John": 78,
    "Priya": 88,
    "Karan": 90
}

# Step 2: Ask user to enter a student's name
name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display marks or show error message
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"Student named '{name}' not found in the record.")
