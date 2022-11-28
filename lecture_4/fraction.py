from lecture_4.gcd import gcd


class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:    #undefined fraction
            self.num = 0
            self.denom = 0
        else:
            dv = gcd(abs(numerator), abs(denominator))
            self.num = numerator // dv
            self.denom = denominator // dv
            if self.denom < 0:
                self.denom = abs(self.denom)
                self.num = -1 * self.num

    def __str__(self):
        if self.denom == 0:
            return 'Undefined Fraction'
        else:
            return f'{self.num}/{self.denom}'

    def __repr__(self):
        if self.denom == 0:
            return 'Undefined Fraction denominator is 0'
        else:
            return f'the numerator is {self.num} and the denominator is {self.denom}'

    def __eq__(self, other):
        return self.num == other.num and self.denom == other.denom

    def __add__(self, other):
        new_num = self.num * other.denom + other.num * self.denom
        new_denom = self.denom * other.denom

        return Fraction(new_num, new_denom)

    def __sub__(self, other):
        new_num = self.num * other.denom - other.num * self.denom
        new_denom = self.denom * other.denom

        return Fraction(new_num, new_denom)

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.denom * other.denom)

    def __truediv__(self, other):
        return self * Fraction(other.denom, other.num)

    def __float__(self):
        return self.num / self.denom


if __name__ == '__main__':
    print("--- Fraction str ---")
    a = Fraction(4, 2)
    print(a)
    b = Fraction(3, 4)
    print(b)
    c = Fraction(1, 2)
    print(c)
    d = Fraction(0, 0)
    print(d)
    print()

    print("--- eq ---")
    print(a == b)
    print(a == Fraction(6, 3))
    print()

    print("--- add ---")
    print(c + b)
    print("--- sub ---")
    print(c - b)
    print("--- mul ---")
    print(c * b)
    print("--- truediv ---")
    print(c / b)
    print("--- float ---")
    print(float(b))
    print(float(Fraction(4, 2)))
    print(float(c / b))
