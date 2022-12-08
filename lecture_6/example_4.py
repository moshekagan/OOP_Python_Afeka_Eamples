class InvalidYearError(Exception):
    pass


year = int(input("insert a year: "))
if not 1970 <= year <= 2023:
    raise InvalidYearError(f"{year} is not a valid year!")
