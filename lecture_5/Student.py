from lecture_5.Person import Person


class Student(Person):
    def __init__(self, fname, lname, graduation_year, courses):
        super().__init__(fname, lname)
        self.graduation_year = graduation_year
        self.courses = courses

    def calculate_avg(self):
        sum_grades = 0
        for c in self.courses:
            sum_grades += c[1]

        return sum_grades / len(self.courses)

    def print_name(self):
        print(f"my name is {self.first_name}, {self.last_name} the avg: {self.calculate_avg()}")


if __name__ == '__main__':
    s = Student("John", "Doe", 2025, [("Math", 90), ("Python", 95)])
    s.print_name()

    p = Person("Avi", "Doe")
    p.print_name()

