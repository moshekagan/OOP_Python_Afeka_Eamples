
# cube class(subclass of Square)


class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length


if __name__ == '__main__':
    cube = Cube(3)
    print(cube.surface_area())

    print(cube.volume())
