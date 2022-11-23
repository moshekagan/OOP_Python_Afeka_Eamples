def gcd(numerator, denominator):
    while numerator != denominator:
        if numerator > denominator:
            numerator = numerator - denominator
        else:
            denominator = denominator - numerator
    return numerator


if __name__ == '__main__':
    print(gcd(4, 2))
    print(gcd(9, 3))
    print(gcd(5, 2))
    print(gcd(14, 2))
    print(gcd(1, 2))
