class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.courses = []

    def enroll(self, course) -> None:
        self.courses.append(course)
        course.enroll_student(self)


class Course:
    def __init__(self, title: str, instructor: str):
        self.title = title
        self.instructor = instructor
        self.students = []

    def enroll_student(self, student) -> None:
        self.students.append(student)


student1 = Student(name="Alice", age=20)
student2 = Student(name="Bob", age=22)

course1 = Course(title="Introduction to Python", instructor="Dr. Smith")
course2 = Course(title="Data Structures", instructor="Prof. Johnson")

student1.enroll(course1)
student1.enroll(course2)
student2.enroll(course1)

print(f"{student1.name} is enrolled in courses: {[course.title for course in student1.courses]}")
print(f"{student2.name} is enrolled in courses: {[course.title for course in student2.courses]}")

print(f"\n{course1.title} has {len(course1.students)} students:")
for student in course1.students:
    print(f"- {student.name}")

print(f"\n{course2.title} has {len(course2.students)} students:")
for student in course2.students:
    print(f"- {student.name}")
