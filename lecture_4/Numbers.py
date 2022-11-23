class Numbers:
    def __init__(self, nums):
        self.numbs = nums

    def __int__(self):
        return int(sum(self.numbs))

    def __float__(self):
        return float(sum(self.numbs))


if __name__ == '__main__':
    numbers = Numbers([1, 2, 5.6, 7.23])

    print(int(numbers))  # 15
    print(float(numbers))  # 15.83
