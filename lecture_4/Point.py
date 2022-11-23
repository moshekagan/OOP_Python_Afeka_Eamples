class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y-other)**2) ** 0.5
    # 
    def distance_from_the_origin(self):
        return self.distance(Point())

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


if __name__ == '__main__':
    p1 = Point(-1, -1)
    p2 = Point(1, 1)

    print(p1 == p2)     # False
    print(p2 == Point(1, 1))    # True

