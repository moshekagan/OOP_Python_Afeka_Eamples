"""
NumPy  basic
"""

import numpy as np

a = np.array([1, 2, 3])
print(a)


b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
print(b)

# Get Dimension
print(a.ndim)
print(b.ndim)

# Get Shape
print(a.shape)
print(b.shape)

# Get type
print(a.dtype)
print(b.dtype)

# Get Size
print(a.itemsize)
print(b.itemsize)

# Get Total size
print(a.nbytes)
print(b.nbytes)



