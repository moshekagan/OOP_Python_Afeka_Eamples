class Student:
    def __init__(self, name, s_id, courses):
        self.name = name
        self.student_id = s_id
        self.courses = courses

    def describe_student_as_str(self):
        return f"{self.name} (#{self.student_id}) Learn: {self.courses}"

    def talk(self):
        print(f"Hi! my name is: {self.name}")


# Create single student
student_1 = Student("Arik", 1234, ["Python", "Math", "Economy"])
student_1.talk()

# Create multiple student
student_data = [
    ["Lior", 1111, ["Python", "Math", "Economy"]],
    ["Liad", 222, ["Python"]],
    ["Limor", 222, ["Math", "Physics"]]
]

students = []
for s in student_data:
    new_student = Student(s[0], s[1], s[2])
    students.append(new_student)
    new_student.talk()
