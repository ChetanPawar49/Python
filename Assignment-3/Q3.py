class Person:
    def __init__(self, name, age, person_id):
        self.name = name
        self.age = age
        self.person_id = person_id

    def __str__(self):
        return f"{self.name}, Age: {self.age}, ID: {self.person_id}"

class Student(Person):
    def __init__(self, name, age, person_id, grade):
        super().__init__(name, age, person_id)
        self.grade = grade
        self.enrolled_courses = []

    def enroll_in_course(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.enroll_student(self)
        else:
            print(f"{self.name} is already enrolled in {course.course_name}")

    def __str__(self):
        return f"Student: {super().__str__()}, Grade: {self.grade}"

class Teacher(Person):
    def __init__(self, name, age, person_id, subject):
        super().__init__(name, age, person_id)
        self.subject = subject
        self.assigned_courses = []

    def assign_course(self, course):
        if course not in self.assigned_courses:
            self.assigned_courses.append(course)
            course.assign_teacher(self)
        else:
            print(f"{self.name} is already assigned to {course.course_name}")

    def __str__(self):
        return f"Teacher: {super().__str__()}, Subject: {self.subject}"

class Course:
    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = []
        self.teacher = None

    def enroll_student(self, student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
        else:
            print(f"{student.name} is already enrolled in {self.course_name}")

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def get_students(self):
        return [str(student) for student in self.enrolled_students]

    def calculate_average_grade(self):
        if not self.enrolled_students:
            return None
        total_grade = sum(student.grade for student in self.enrolled_students)
        return total_grade / len(self.enrolled_students)

    def __str__(self):
        return f"Course: {self.course_name}, ID: {self.course_id}, Teacher: {self.teacher.name if self.teacher else 'None'}"

class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_course(self, course):
        self.courses.append(course)

    def enroll_student_in_course(self, student_id, course_id):
        student = self.find_student_by_id(student_id)
        course = self.find_course_by_id(course_id)
        if student and course:
            student.enroll_in_course(course)
        else:
            print("Student or course not found.")

    def assign_teacher_to_course(self, teacher_id, course_id):
        teacher = self.find_teacher_by_id(teacher_id)
        course = self.find_course_by_id(course_id)
        if teacher and course:
            teacher.assign_course(course)
        else:
            print("Teacher or course not found.")

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.person_id == student_id:
                return student
        return None

    def find_teacher_by_id(self, teacher_id):
        for teacher in self.teachers:
            if teacher.person_id == teacher_id:
                return teacher
        return None

    def find_course_by_id(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None

    def view_students_in_course(self, course_id):
        course = self.find_course_by_id(course_id)
        if course:
            students = course.get_students()
            return students if students else "No students enrolled."
        return "Course not found."

    def view_courses_for_student(self, student_id):
        student = self.find_student_by_id(student_id)
        if student:
            courses = [course.course_name for course in student.enrolled_courses]
            return courses if courses else "No courses enrolled."
        return "Student not found."

    def calculate_average_grade_for_course(self, course_id):
        course = self.find_course_by_id(course_id)
        if course:
            avg_grade = course.calculate_average_grade()
            return avg_grade if avg_grade is not None else "No students in the course."
        return "Course not found."


# Example Usage:
school = School()

# Add students
student1 = Student("Alice", 14, 1, 85)
student2 = Student("Bob", 15, 2, 90)
school.add_student(student1)
school.add_student(student2)

# Add teachers
teacher1 = Teacher("Mr. Smith", 40, 101, "Mathematics")
teacher2 = Teacher("Mrs. Johnson", 35, 102, "Science")
school.add_teacher(teacher1)
school.add_teacher(teacher2)

# Add courses
course1 = Course("Math 101", "M101")
course2 = Course("Science 101", "S101")
school.add_course(course1)
school.add_course(course2)

# Enroll students in courses
school.enroll_student_in_course(1, "M101")
school.enroll_student_in_course(2, "S101")

# Assign teachers to courses
school.assign_teacher_to_course(101, "M101")
school.assign_teacher_to_course(102, "S101")

# View students in a course
print(school.view_students_in_course("M101"))

# View courses for a student
print(school.view_courses_for_student(1))

# Calculate average grade for a course
print(f"Average grade for Math 101: {school.calculate_average_grade_for_course('M101')}")