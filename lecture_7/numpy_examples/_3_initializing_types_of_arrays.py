"""
Initializing different types of arrays
"""

import numpy as np

# All 0s matrix
a = np.zeros(5)
print(a)

a = np.zeros((2,3))
print(a)

# All 1s matrix
a = np.ones(3)
print(a)

a = np.ones((3, 5))
print(a)

# any other number
a = np.full((3, 5), 54)
print(a)

# any other full_like
arr = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
a = np.full_like(arr, 3)
print(a)

# random decimal numbers
a = np.random.rand(4, 2)
print(a)

# random Integer values
a = np.random.randint(7, size=(3, 3))
print(a)

# the identity matrix
a = np.identity(5)
print(a)

# Repeat an array
a = np.array([[1, 2, 3]])
r1 = np.repeat(a, 3, axis=0)
print(r1)
r2 = np.repeat(a, 3, axis=1)
print(r2)

# linspace - get X values with equal spaces between 2 numbers
print(np.linspace(10, 20))   # 50 (default) values between 10 to 20
print(np.linspace(10, 20, 10))  # 10 values between 10 to 20

'''
Lets create this array:
[
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 9, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
]
'''
print("Special matrix: ")

output = np.ones((5, 5))
print(output)

z = np.zeros((3, 3))
z[1, 1] = 9
print(z)

output[1:4, 1:4] = z
print(output)


# Be careful when copying arrays!!!!
a = np.array([1, 2, 3])
b = a
print(b)

b[0] = 100
print(b)
print(a)

# instead of copy array as above, use copy() method!
a = np.array([1, 2, 3])
b = a.copy()
print(b)

b[0] = 100
print(b)
print(a)
