try:
    num = int(input("insert a number: "))
    print(10 / num)
except ValueError:
    print("You were asked to enter a number :( ")
    num = 1
except ZeroDivisionError:
    print("Houston we have problem! The number can't be zero :(")
    num = 1
finally:
    print(f"The number is {num}")
