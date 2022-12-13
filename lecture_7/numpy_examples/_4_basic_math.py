"""
Basic Mathematics
"""

import numpy as np

a = np.array([1, 2, 3, 4])
print(a)

print(a + 2)
print(a - 2)
print(a * 2)
print(a / 2)
print(a ** 2)

a += 3
print(a)

b = np.array([1, 0, 1, 0])
print(a + b)

# Take the sin / cos
print(np.sin(a))
print(np.cos(a))

# Aggregate function
a = np.array([2, 4, 6, 8])
print(a.max())
print(a.min())
print(a.std())
print(a.mean())
