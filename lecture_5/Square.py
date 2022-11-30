# Here we declare that the Square class inherits from the Rectangle class
from lecture_5.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

