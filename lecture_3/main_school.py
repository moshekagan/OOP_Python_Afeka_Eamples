import csv
from lecture_3.Student import Student
from lecture_3.School import School


def load_from_csv(students_csv_file):
    students = []

    with open(students_csv_file) as csvfile:
        reader = csv.reader(csvfile)

        next(reader)

        for row in reader:
            student_id = row[0]
            student_name = row[1]
            new_student = Student(student_id, student_name)
            students.append(new_student)

    return students


students = load_from_csv("students.csv")
school = School("Afeka", students)
print(school)
