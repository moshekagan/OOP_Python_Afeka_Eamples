class Weight:
    def __init__(self, kilos):
        self.kilos = kilos

    def __str__(self):
        return f"The weight is: {self.kilos}"

    def __add__(self, other):
        return Weight(self.kilos + other.kilos)

    def __sub__(self, other):
        return Weight(self.kilos - other.kilos)

    def __mul__(self, other):
        return Weight(self.kilos * other.kilos)

    def __truediv__(self, other):
        return Weight(self.kilos / other.kilos)


if __name__ == '__main__':
    w1 = Weight(3)
    w2 = Weight(4)

    add_w = w1 + w2
    sub_w = w1 - w2
    nul_w = w1 * w2
    div_w = w1 / w2

    print(add_w)    # The weight is: 7
    print(sub_w)    # The weight is: -1
    print(nul_w)    # The weight is: 12
    print(div_w)    # The weight is: 0.75
