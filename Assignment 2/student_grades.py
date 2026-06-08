students = {}

name = input("Enter Student Name: ")
grade = input("Enter Grade: ")

students[name] = grade

update_name = input("Enter Student Name to Update: ")

if update_name in students:
    new_grade = input("Enter New Grade: ")
    students[update_name] = new_grade
else:
    print("Student Not Found")

print("\nStudent Grades:")

for name, grade in students.items():
    print(name, ":", grade)