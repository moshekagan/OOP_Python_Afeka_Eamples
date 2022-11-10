class Car:
    def __init__(self, licence, model, year):
        self.licence_plate = licence
        self.model = model
        self.year = year
        self.speed = 0

    def drive(self, speed):
        self.speed = speed

    def show_speed(self):
        print(f"{self.model} - {self.speed}")

    def __str__(self):
        return f"{self.model}, {self.licence_plate}"

    def __repr__(self):
        return str(self)


c1 = Car(1234, "nissan", 2020)
c2 = Car(3333, "ferrai", 2022)

c1.show_speed()
c2.show_speed()

c1.drive(50)
c2.drive(100)

c1.show_speed()
c2.show_speed()

print(c1)

cars = [c1, c2]
print(cars)
