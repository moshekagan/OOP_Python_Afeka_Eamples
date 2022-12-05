from lecture_5.Employee import Employee


class Developer(Employee):
    RAISE_AMT = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def __str__(self):
        return f"{super().__str__()} is a developer"


if __name__ == '__main__':
    e = Employee("Avi", "Choen", 50000)
    print(e.pay)
    e.apply_raise()
    print(f"{e.first} after {e.pay}")
    print()

    d = Developer("Yossi", "Levi", 50000, "Python")
    print(d.pay)
    d.apply_raise()
    print(f"{d.first} after {d.pay}")