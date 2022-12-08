class A(Exception):
    pass


class B(A):
    pass


class C(B):
    pass


for cls in [A, B, C]:
    try:
        raise cls()
    except A:
        print("A")
    except B:
        print("B")
    except C:
        print("C")
