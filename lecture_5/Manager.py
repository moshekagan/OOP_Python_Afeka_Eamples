from lecture_5.Employee import Employee


class Manager(Employee):

    def __init__(self, first_name, last, pay, employees=None):
        super().__init__(first_name, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_all_employees(self):
        for emp in self.employees:
            print('-->', emp.fullname())
