# Student Grade Calculator, comments were added for expalantion and clarity with notes in due process to help each info plate out

# Lists and Tuples
subjects = ["Filipino", "Science", "English", "ICT", "Math", "PE"]
units = (3, 3, 3, 3, 3, 3)  # Tuple containing units per subject

# Student Info
student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")
course = input("Enter course: ")

# Get grades for each subject
grades = []
print("\nEnter grades for each subject:")
for subject in subjects:
    while True:
        try:
            grade = float(input(f"{subject}: "))
            if 0 <= grade <= 100:
                grades.append(grade)
                break
            else:
                print("Please enter a grade between 0 and 100")
        except ValueError:
            print("Please enter a valid number")

#general weighted average calculation
total_weighted_grade = 0
total_units = sum(units)

for i in range(len(subjects)):
    total_weighted_grade += grades[i] * units[i]

gwa = total_weighted_grade / total_units

#display results here
print("\n=== Student Information ===")
print(f"Name: {student_name}")
print(f"Student ID: {student_id}")
print(f"Course: {course}")

print("\n=== Grade Summary ===")
for i in range(len(subjects)):
    print(f"{subjects[i]}: {grades[i]:.2f} ({units[i]} units)")

print("\n=== General Weighted Average ===")
print(f"GWA: {gwa:.2f}")