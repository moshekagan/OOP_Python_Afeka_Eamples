class School:
    def __init__(self, name, students=[]):
        self.name = name
        self.students = students

    def __str__(self):
        msg = f"---- {self.name} ----"

        for student in self.students:
            msg += "\n"
            msg += str(student)

        return msg

    def __repr__(self):
        return str(self)
