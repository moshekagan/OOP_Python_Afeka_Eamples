import numpy as np
import matplotlib.pyplot as plt


# NumPy’s array class is called ndarray
# What is an array
a = np.array([1, 2, 3, 4, 5, 6])
print(a)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(a[0])
print(a[1, 3])
print(a[0, :])
print(a[:, 2])

b = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(b[0, 1:6:2])
b[1, 5] = 20
b[:, 2] = [100, 200]

# Attributes of an array

print(f'the shape of a is {a.shape}')  # Tuple of array dimensions.
print(f'the type of a is {type(a)}')
print(f'the type of a elements is {a.dtype}')
print(f'the size of a is {a.size}')  # Number of elements in the array.
print(f'number of dimensions of a is {a.ndim}')  # Number of array dimensions.
print(f'{a.data}')  # Python buffer object pointing to the start of the array's data.

# initializing arrays

a = np.zeros((3, 4))
print(a)
a = np.zeros((3, 4), dtype='int32')
print(a)
a = np.ones((2, 5))
print(a)
x = np.ones(2, dtype=np.int64)
print(x)
a = np.full((2, 2), 99)
print(a)
a = np.identity(5)
print(a)

# To create sequences of numbers, NumPy provides the arange function
# which is analogous to the Python built-in range, but returns an array.
a = np.arange(4)
print(a)
a = np.arange(2, 9, 2)
print(a)
a = np.arange(0, 2, 0.3)
print(a)
# linspace receives as an argument the number of elements that we want, instead of the step
a = np.linspace(0, 10, 5)
print(a)

a = np.linspace(0, 2, 9)  # 9 numbers from 0 to 2
print(a)
x = np.linspace(0, 2 * np.pi, 100)  # useful to evaluate function at lots of points
f = np.sin(x)

# Arrays manipulation - reshape,flatten,transpose

b = np.arange(12).reshape(4, 3)
print(b)

c = np.arange(24).reshape(2, 3, 4)  # 3d array
print(c)

print(np.arange(10000))
print(np.arange(10000).reshape(100, 100))

y = np.array([[2, 3], [4, 5], [6, 7]])
print(y.flatten())  # order='C' is the default ('C' - flatten in row major)
print(y.flatten(order='F'))  # 'F' - flatten in column major

a = np.arange(6).reshape((2, 3))
print(a)
b = np.transpose(a)
print(b)

# numpy random

x = np.random.randint(100, size=(5))
print(x)

x = np.random.randint(100, size=(3, 5))
print(x)

x = np.random.rand(5)
print(x)

x = np.random.rand(3, 5, 2)
print(x)

x = np.random.uniform(2, 10, size=(2, 3))
print(x)

x = np.random.choice(np.arange(50)+1)
print(x)

x = np.random.choice([3, 5, 7, 9], size=(3, 5))
print(x)

# visual representation
# histogram
a = np.random.randint(30, size=(50))
plt.hist(a, bins=[0, 5, 10, 15, 20, 25, 30])
plt.title('histogram')
plt.show()

# graph of sin(x)
x = np.arange(0, 2 * np.pi, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()

# numpy basic operations
a = np.array([20, 30, 40, 50])
print(a)
b = np.arange(4)
print(b)
c = a - b  # elementwise substraction
print(c)
print(a + 2)
print(b ** 2)

a = np.arange(12).reshape(4, 3)
b = np.array([10, 20, 30])
print(a + b)
print(np.add(a, b))

print(a * b)
print(np.multiply(a, b))

print(a / b)
print(np.divide(a, b))

l1 = [10, 20, 30]
l2 = [100, 200, 300]
# print(l2 - l1)  # Error unsupported operand type(s) for -
print(np.subtract(l2, l1))

a = np.arange(20).reshape(4, 5)
print(a)
print(10 * np.sin(a))
print(a < 5)

# In a 2-dimensional NumPy array, the axes are the directions along the rows and columns.

b = np.arange(12).reshape(3, 4)
print(b)
print(b.sum())
print(b.sum(axis=0))
print(b.sum(axis=1))

print(b.min())
print(b.min(axis=0))
print(b.min(axis=1))  # same for max()

# indexing and slicing
# The syntax of Python NumPy slicing is [start : stop : step]
a = np.arange(10) ** 3
print(a)
print(a[2])
print(a[2:5])

a[:6:2] = 1000
# equivalent to a[0:6:2] = 1000;
# from start to position 6, exclusive, set every 2nd element to 1000
print(a)

print(a[::-1])  # reversed a

# 2D arrays slicing
a = np.arange(18).reshape(6, 3)
print(a)

print(a[3, 2])
print(a[3:5, 1:3])
print(a[:, 1:3])

# 3D arrays slicing
a = np.arange(18).reshape(2, 3, 3)
print(a[1, -1, 2])
print(a[1, -1])

print(a[1])
print(a[1, :, :])
print(a[1, ...])  # same as print(a[1,:,:])

# Iterating over array
a = np.arange(18).reshape(6, 3)

for x in a:
    print(type(x))
    print(x)

for x in a:
    for y in x:
        print(type(y))
        print(y)

# using np.nditer()
a = np.arange(18).reshape(6, 3)
for x in np.nditer(a):
    print(type(x))
    print(x)

# joining arrays

# concatenate
a = np.arange(10).reshape(2, 5)
b = np.arange(10, 20).reshape(2, 5)
print(f"a = \n{a}")
print(f"b = \n{b}")
c = np.concatenate((a, b))
print(f"c = \n{c}")
d = np.concatenate((a, b), axis=1)
print(f"d = \n{d}")

# vstack,hstack

v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

v = np.vstack([v1, v2])
print(v)
h = np.hstack([v1, v2])
print(h)
