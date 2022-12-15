def get_pos_number():
    num = int(input("insert a positive number: "))

    if num <= 0:
        raise ValueError(f"The number should be positive! ({num})")

    return num


try:
    user_num = get_pos_number()
    print(f"the number is {user_num}")
except ValueError:
    user_num = get_pos_number()
    print(f"the number is {user_num}")