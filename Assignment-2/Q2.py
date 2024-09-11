# Sample student data
students_data = [
    {"student_name": "Chetan", "grades": {"Math": 95, "Science": 92, "English": 98}},
    {"student_name": "Aditi", "grades": {"Math": 95, "Science": 92, "English": 98}},
    {"student_name": "Ravi", "grades": {"Math": 72, "Science": 75, "English": 70}},
    {"student_name": "Sneha", "grades": {"Math": 89, "Science": 82, "English": 91}},
    {"student_name": "Ajay", "grades": {"Math": 65, "Science": 68, "English": 74}},
]

# Initialize variables to store insights
total_grades = {}
grade_counts = {}
student_averages = {}
grade_distribution = {}

# Process the student data
for student in students_data:
    student_name = student["student_name"]
    grades = student["grades"]
    
    # Calculate the average grade for the student
    total = sum(grades.values())
    count = len(grades)
    average = total / count
    student_averages[student_name] = average
    
    # Update total grades and grade counts by course
    for course, grade in grades.items():
        if course in total_grades:
            total_grades[course] += grade
            grade_counts[course] += 1
        else:
            total_grades[course] = grade
            grade_counts[course] = 1

        # Update grade distribution
        if grade >= 90:
            grade_distribution.setdefault('A', 0)
            grade_distribution['A'] += 1
        elif grade >= 80:
            grade_distribution.setdefault('B', 0)
            grade_distribution['B'] += 1
        elif grade >= 70:
            grade_distribution.setdefault('C', 0)
            grade_distribution['C'] += 1
        elif grade >= 60:
            grade_distribution.setdefault('D', 0)
            grade_distribution['D'] += 1
        else:
            grade_distribution.setdefault('F', 0)
            grade_distribution['F'] += 1

# Calculate average grade per course
average_grades_per_course = {course: total_grades[course] / grade_counts[course] for course in total_grades}

# Determine top-performing student(s)
top_average = max(student_averages.values())
top_students = [name for name, avg in student_averages.items() if avg == top_average]

# Display the insights
print("Average Grades per Course:")
for course, avg_grade in average_grades_per_course.items():
    print(f"  {course}: {avg_grade:.2f}")

print("\nTop-Performing Student(s):")
for student in top_students:
    print(f"  {student} with an average grade of {top_average:.2f}")

print("\nGrade Distribution:")
for grade, count in grade_distribution.items():
    print(f"  {grade}: {count}")
