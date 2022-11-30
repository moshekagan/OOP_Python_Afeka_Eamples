class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def print_name(self):
        print(f"{self.first_name}, {self.last_name}")

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


if __name__ == '__main__':
    # Use the Person class to create an object, and then execute the print_name method:

    x = Person("John", "Doe")
    x.print_name()  # John, Doe
