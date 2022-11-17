class Student:
    def __init__(self, name, s_id, courses=[]):
        self.name = name
        self.student_id = s_id
        self.courses = courses

    def describe_student_as_str(self):
        return f"{self.name} (#{self.student_id}) Learn: {self.courses}"

    def talk(self):
        print(f"Hi! my name is: {self.name}")

    def __str__(self):
        return f"{self.student_id}, {self.name}, {self.courses}"

    def __repr__(self):
        return str(self)
