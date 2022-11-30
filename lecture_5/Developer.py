from lecture_5.Employee import Employee


class Developer(Employee):
    RAISE_AMT = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def __str__(self):
        return f"{super().__str__()} is a developer"

