# Here we declare that the Square class inherits from the Rectangle class
from lecture_5.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


if __name__ == '__main__':
    s = Square(10)
    print(s.area())
