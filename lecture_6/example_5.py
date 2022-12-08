class A(Exception):
    pass


class B(A):
    pass


class C(B):
    pass


for cls in [A, B, C]:
    try:
        raise cls()
    except C:
        print("C")
    except B:
        print("B")
    except A:
        print("A")
