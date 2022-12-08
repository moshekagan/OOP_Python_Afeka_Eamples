num = int(input("insert a positive number: "))

if num <= 0:
    raise ValueError(f"The number should be positive! ({num})")
